import os
from pathlib import Path

GITHUB_API_BASE_URI = "https://api.github.com"
GITHUB_API_VERSION = '2022-11-28'
GITHUB_API_KEY_FOLDER = os.path.join(str(Path.home()), '.api_keys', 'github_api_keys')
GITHUB_API_TOKEN = os.path.join(GITHUB_API_KEY_FOLDER, 'github_read_access_token.key')
GITHUB_API_PER_PAGE = 50
GITHUB_API_PER_PAGE_MAX = 100
