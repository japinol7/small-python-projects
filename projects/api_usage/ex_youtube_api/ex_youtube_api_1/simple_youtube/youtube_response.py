__author__ = 'Joan A. Pinol  (japinol)'

from simple_youtube.config import YOUTUBE_API_POLL_INTERVAL
from simple_youtube.exceptions import YoutubeApiError


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
            raise YoutubeApiError(
                f"Invalid JSON response: {response.text[:300]}")

        items = self.json.get("items", [])
        self.items_len = len(items)

        self.next_page_token = self.json.get("nextPageToken")

        polling_ms = self.json.get(
            "pollingIntervalMillis",
            YOUTUBE_API_POLL_INTERVAL * 1000)
        self.polling_interval = polling_ms / 1000
