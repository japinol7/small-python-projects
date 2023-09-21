import os
from pathlib import Path

TMDB_API_BASE_URI = "https://api.themoviedb.org"
TMDB_API_VERSION = 3
TMDB_API_KEY_FOLDER = os.path.join(str(Path.home()), '.api_keys', 'tmdb_api_keys')
TMDB_API_TOKEN = os.path.join(TMDB_API_KEY_FOLDER, 'tmdb_read_access_token.key')
