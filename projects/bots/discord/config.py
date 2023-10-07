import os
from pathlib import Path

DISCORD_API_KEY_FOLDER = os.path.join(str(Path.home()), '.api_keys', 'discord_api_keys')
DISCORD_API_TOKEN = os.path.join(DISCORD_API_KEY_FOLDER, 'discord_access_token.key')
DISCORD_CHANNEL_GENERAL = os.path.join(DISCORD_API_KEY_FOLDER, 'discord_channel_general.id')
