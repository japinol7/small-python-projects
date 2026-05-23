from collections import deque
from dataclasses import dataclass
from time import sleep, perf_counter

import requests

from config import (
    YOUTUBE_API_BASE_URI,
    YOUTUBE_API_POLL_INTERVAL,
    YOUTUBE_API_REQUEST_TIMEOUT,
    YOUTUBE_API_MAX_RESULTS,
    FILTER_OUT_KEYWORDS,
    YOUTUBE_API_MAX_EMPTY_POLLS,
    )
from tools.logger.logger import log


class YoutubeError(Exception):
    pass


@dataclass
class YoutubeChatMessage:
    msg_id: str
    author: str
    message: str
    raw: dict


class YoutubeResponse:
    def __init__(self):
        self.json = None
        self.text = None
        self.status_code = None
        self.resource_name = None

        self.items_len = 0
        self.next_page_token = None
        self.polling_interval = YOUTUBE_API_POLL_INTERVAL

    def clear(self):
        self.__init__()

    def set_state(self, response):
        self.text = response.text
        self.status_code = response.status_code

        try:
            self.json = response.json()
        except ValueError:
            raise YoutubeError(
                f"Invalid JSON response: {response.text[:300]}")

        items = self.json.get("items", [])
        self.items_len = len(items)

        self.next_page_token = self.json.get("nextPageToken")

        polling_ms = self.json.get(
            "pollingIntervalMillis",
            YOUTUBE_API_POLL_INTERVAL * 1000)

        self.polling_interval = polling_ms / 1000


class YoutubeClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_uri = YOUTUBE_API_BASE_URI

        self.url = None
        self.params = None

        self.live_chat_id = None
        self.next_page_token = None

        self.response = YoutubeResponse()

        # bounded memory for duplicates
        self.seen_message_ids = deque(maxlen=5000)

        self.retry_count = 0

        self._init()

    def _init(self):
        if not self.api_key:
            raise YoutubeError("YouTube API key missing")

        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "youtube-chat-client/1.0",
            })

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def close(self):
        self.session.close()

    def _sanitize_params(self):
        if not self.params:
            return {}

        safe = dict(self.params)
        if "key" in safe:
            safe["key"] = "***REDACTED***"
        return safe

    def _log_request(self):
        log.info(
            f"GET {self.url} params={self._sanitize_params()}")

    def _get_response(self):
        start = perf_counter()

        response = self.session.get(
            self.url,
            params=self.params,
            timeout=YOUTUBE_API_REQUEST_TIMEOUT)

        elapsed = perf_counter() - start

        if response.status_code != 200:
            raise YoutubeError(
                f"Youtube API error {response.status_code}: "
                f"{response.text[:300]}")

        log.info(f"Request OK ({elapsed:.2f}s)")

        self.response.set_state(response)
        self.retry_count = 0

        return self.response

    def get_resource_info(self, resource_name):
        self.response.clear()
        self.response.resource_name = resource_name

        self._log_request()
        return self._get_response()

    def get_live_chat_id(self, video_id):
        self.url = f"{self.base_uri}/videos"

        self.params = {
            "part": "liveStreamingDetails",
            "id": video_id,
            "key": self.api_key,
            }

        response = self.get_resource_info("videos")

        items = response.json.get("items", [])
        if not items:
            raise YoutubeError("Video not found")

        details = items[0].get("liveStreamingDetails", {})
        self.live_chat_id = details.get("activeLiveChatId")

        if not self.live_chat_id:
            raise YoutubeError("No active live chat found")

        return self.live_chat_id

    def get_live_chat_messages(self):
        if not self.live_chat_id:
            raise YoutubeError("live_chat_id not initialized")

        self.url = f"{self.base_uri}/liveChat/messages"

        self.params = {
            "liveChatId": self.live_chat_id,
            "part": "snippet,authorDetails",
            "key": self.api_key,
            "maxResults": YOUTUBE_API_MAX_RESULTS,
            }

        if self.next_page_token:
            self.params["pageToken"] = self.next_page_token

        response = self.get_resource_info("liveChatMessages")
        self.next_page_token = response.next_page_token

        return response

    def iter_live_chat_messages(
            self,
            *,
            filter_func=None,
            max_messages=None,
            max_empty_polls=YOUTUBE_API_MAX_EMPTY_POLLS,
        ):
        count = 0
        empty_polls = 0

        while True:
            if max_messages is not None and count >= max_messages:
                log.info("Max messages reached. Stopping iterator.")
                return

            try:
                response = self.get_live_chat_messages()
                items = response.json.get("items", [])
                yielded_this_cycle = 0

                for item in items:
                    msg_id = item.get("id")

                    if msg_id and msg_id in self.seen_message_ids:
                        continue

                    if msg_id:
                        self.seen_message_ids.append(msg_id)

                    author = item["authorDetails"]["displayName"]
                    snippet = item.get("snippet", {})
                    message = snippet.get("displayMessage", "")

                    if filter_func and not filter_func(message):
                        continue

                    yield YoutubeChatMessage(
                        msg_id=msg_id,
                        author=author,
                        message=message,
                        raw=item,
                        )

                    # Count only real yielded messages
                    count += 1
                    yielded_this_cycle += 1

                    if max_messages is not None and count >= max_messages:
                        log.info(
                            f"Max messages reached: {max_messages}. Stopping iterator.")
                        return

                if yielded_this_cycle == 0:
                    empty_polls += 1
                else:
                    empty_polls = 0

                # Stop if stream is 'dead'
                if empty_polls >= max_empty_polls:
                    log.info("No new messages for a while. Stopping iterator.")
                    return

                sleep(response.polling_interval)

            except KeyboardInterrupt:
                log.info("Interrupted by user")
                break

            except Exception as e:
                self.retry_count += 1
                wait = min(2 ** self.retry_count, 60)

                log.error(f"Error: {e} | retrying in {wait}s")
                sleep(wait)


def example_of_usage(video_id, filter_keywords, *, max_messages=None):
    from config import YOUTUBE_API_KEY
    from tools.logger import logger
    from tools.utils import utils

    logger.add_stdout_handler(
        logger_format=logger.LOGGER_FORMAT_NO_DATE)
    logger.add_file_handler(
        multiple_log_files=False,
        logger_format=logger.LOGGER_FORMAT_NO_DATE)

    filter_keywords = [k.lower() for k in filter_keywords]
    out_keywords = [k.lower() for k in FILTER_OUT_KEYWORDS]

    def filter_message(message):
        message = message.lower()

        return all([
            not filter_keywords or any(k in message for k in filter_keywords),
            all(k not in message for k in out_keywords),
            ])

    with YoutubeClient(
        api_key=utils.read_file_as_string(YOUTUBE_API_KEY)
    ) as client:
        client.get_live_chat_id(video_id)

        count = 1
        for item in client.iter_live_chat_messages(
            filter_func=filter_message,
            max_messages=max_messages,
            ):
            log.info(
                f"{count:4} "
                f"{item.author[:24]:24} "
                f"{item.message[:180]}")
            count += 1

        log.info("EOF")


def main():
    video_id = "VIDEO_ID"
    filter_keywords = []

    example_of_usage(
        video_id, filter_keywords,
        max_messages=120)


if __name__ == "__main__":
    main()
