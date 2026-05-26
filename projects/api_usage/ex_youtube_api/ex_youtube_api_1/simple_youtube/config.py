__author__ = 'Joan A. Pinol  (japinol)'

import os
from pathlib import Path

YOUTUBE_API_BASE_URI = "https://www.googleapis.com/youtube/v3"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_KEY_FOLDER = os.path.join(
    str(Path.home()),
    ".api_keys",
    "youtube_secrets",
    )
YOUTUBE_API_KEY = os.path.join(
    YOUTUBE_API_KEY_FOLDER,
    "youtube_secrets_api_key.key",
    ).strip()
YOUTUBE_API_POLL_INTERVAL = 5
YOUTUBE_API_MAX_RESULTS = 75  # Recommended max: 75
YOUTUBE_API_REQUEST_TIMEOUT = 15
YOUTUBE_API_MAX_RETRIES = 5

# Stop polling iterator after this max value
YOUTUBE_API_MAX_EMPTY_POLLS = 2

FILTER_OUT_KEYWORDS = [
    # 'bitcoin',
    # 'giveaway',
    # 'scam',
    'http://',
    'https://',
    ]
