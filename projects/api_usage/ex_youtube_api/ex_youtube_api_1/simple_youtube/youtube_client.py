__author__ = 'Joan A. Pinol  (japinol)'

from collections import deque
from dataclasses import dataclass
from time import sleep

from simple_youtube.config import (
    YOUTUBE_API_MAX_RESULTS,
    FILTER_OUT_KEYWORDS,
    YOUTUBE_API_MAX_EMPTY_POLLS,
    )
from simple_youtube.exceptions import YoutubeApiError
from simple_youtube.youtube_connector import YoutubeConnector
from simple_youtube.youtube_response import YoutubeResponse
from tools.logger.logger import log


@dataclass
class YoutubeChatMessage:
    msg_id: str
    author: str
    message: str
    raw: dict


class YoutubeClient:
    def __init__(
            self, api_key, filter_keywords=None, filter_out_keywords=None
        ):
        self.connector = YoutubeConnector(api_key)
        self.response = YoutubeResponse()
        self.live_chat_id = None
        self.next_page_token = None
        self.retry_count = 0

        # bounded memory for duplicates
        self.seen_message_ids = deque(maxlen=5000)

        if filter_keywords:
            self.filter_keywords = [k.lower() for k in filter_keywords]
        else:
            self.filter_keywords = []

        if filter_out_keywords:
            self.filter_out_keywords = filter_out_keywords
            self.filter_out_keywords.extend(FILTER_OUT_KEYWORDS)
            self.filter_out_keywords = [k.lower() for k in self.filter_out_keywords]
        else:
            self.filter_out_keywords = [k.lower() for k in FILTER_OUT_KEYWORDS]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def close(self):
        self.connector.close()

    def get_resource_info(self, resource_name, path, params):
        self.response.clear()
        self.response.resource_name = resource_name

        raw_response = self.connector.get(path, params)
        self.response.set_state(raw_response)
        self.retry_count = 0

        return self.response

    def get_live_chat_id(self, video_id):
        params = {
            "part": "liveStreamingDetails",
            "id": video_id,
            }

        response = self.get_resource_info("videos", "videos", params)

        items = response.json.get("items", [])
        if not items:
            raise YoutubeApiError("Video not found")

        details = items[0].get("liveStreamingDetails", {})
        self.live_chat_id = details.get("activeLiveChatId")

        if not self.live_chat_id:
            raise YoutubeApiError("No active live chat found")

        return self.live_chat_id

    def get_live_chat_messages(self):
        if not self.live_chat_id:
            raise YoutubeApiError("live_chat_id not initialized")

        params = {
            "liveChatId": self.live_chat_id,
            "part": "snippet,authorDetails",
            "maxResults": YOUTUBE_API_MAX_RESULTS,
            }

        if self.next_page_token:
            params["pageToken"] = self.next_page_token

        response = self.get_resource_info(
            "liveChatMessages", "liveChat/messages", params)
        self.next_page_token = response.next_page_token

        return response

    def _filter_message_default(self, message):
        message = message.lower()
        return all([
            not self.filter_keywords or any(k in message for k in self.filter_keywords),
            all(k not in message for k in self.filter_out_keywords),
            ])

    def iter_live_chat_messages(
            self,
            *,
            filter_func=None,
            max_messages=None,
            max_empty_polls=YOUTUBE_API_MAX_EMPTY_POLLS,
        ):
        count = 0
        empty_polls = 0

        if filter_func is None:
            filter_func = self._filter_message_default

        while True:
            if max_messages is not None and count >= max_messages:
                log.debug("Max messages reached. Stopping iterator.")
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
                        raw=item)

                    # Count only real yielded messages
                    count += 1
                    yielded_this_cycle += 1

                    if max_messages is not None and count >= max_messages:
                        log.debug(
                            f"Max messages reached: {max_messages}. Stopping iterator.")
                        return

                if yielded_this_cycle == 0:
                    empty_polls += 1
                else:
                    empty_polls = 0

                # Stop if stream is 'dead'
                if empty_polls >= max_empty_polls:
                    log.debug("No new messages for a while. Stopping iterator.")
                    return

                sleep(response.polling_interval)

            except KeyboardInterrupt:
                log.debug("Interrupted by user")
                break

            except Exception as e:
                self.retry_count += 1
                wait = min(2 ** self.retry_count, 60)

                log.error(f"Error: {e} | retrying in {wait}s")
                sleep(wait)
