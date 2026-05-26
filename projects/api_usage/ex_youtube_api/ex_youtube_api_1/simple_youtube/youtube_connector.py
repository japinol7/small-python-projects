__author__ = 'Joan A. Pinol  (japinol)'

from time import perf_counter

import requests

from simple_youtube.config import (
    YOUTUBE_API_BASE_URI,
    YOUTUBE_API_REQUEST_TIMEOUT,
    )
from simple_youtube.exceptions import YoutubeApiError
from tools.logger.logger import log


class YoutubeConnector:
    def __init__(self, api_key):
        if not api_key:
            raise YoutubeApiError("YouTube API key missing")

        self.api_key = api_key
        self.base_uri = YOUTUBE_API_BASE_URI
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "youtube-chat-client/1.0",
            })

    def close(self):
        self.session.close()

    def _sanitize_params(self, params):
        if not params:
            return {}

        safe_params = dict(params)
        if "key" in safe_params:
            safe_params["key"] = "***REDACTED***"

        return safe_params

    def get(self, path, params=None):
        url = f"{self.base_uri}/{path}"
        params = params or {}
        if "key" not in params:
            params["key"] = self.api_key

        log.debug(f"GET {url} params={self._sanitize_params(params)}")

        time_start = perf_counter()
        response = self.session.get(
            url,
            params=params,
            timeout=YOUTUBE_API_REQUEST_TIMEOUT)
        time_elapsed = perf_counter() - time_start

        if response.status_code != 200:
            raise YoutubeApiError(
                f"Youtube API error {response.status_code}: "
                f"{response.text[:300]}")

        log.debug(f"Request OK ({time_elapsed:.2f}s)")
        return response
