import os
from pathlib import Path

YOUTUBE_API_BASE_URI = "https://www.googleapis.com/youtube/v3"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_KEY_FOLDER = os.path.join(
    str(Path.home()),
    ".api_keys",
    "youtube_api_keys",
    )
YOUTUBE_API_KEY = os.path.join(
    YOUTUBE_API_KEY_FOLDER,
    "youtube_api_key.key",
    ).strip()
YOUTUBE_API_POLL_INTERVAL = 5
YOUTUBE_API_MAX_RESULTS = 50    # Recommended max: 200
YOUTUBE_API_REQUEST_TIMEOUT = 15
YOUTUBE_API_MAX_RETRIES = 5

YOUTUBE_API_MAX_EMPTY_POLLS = 3   # Stop polling iterator after this max value

FILTER_OUT_KEYWORDS = [
    # 'bitcoin',
    # 'giveaway',
    # 'scam',
    'http://',
    'https://',
    ]
