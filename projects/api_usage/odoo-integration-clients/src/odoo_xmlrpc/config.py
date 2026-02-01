"""Example test_server_access_config."""
import os
from pathlib import Path

from utils import read_file_as_string

# Warning: This configuration is for demonstration purposes only.
# DO NOT store secrets in this file.
# Instead, use a secrets management service.

ODOO_SECRETS_KEY_FOLDER_NAME = os.path.join(
    str(Path.home()), '.api_keys', 'odoo_secrets')
ODOO_SECRETS_TOKEN_FILE_NAME = os.path.join(
    ODOO_SECRETS_KEY_FOLDER_NAME, 'odoo_secrets_access_token.key')
ODOO_PROXY_URL_FILE_NAME = os.path.join(
    ODOO_SECRETS_KEY_FOLDER_NAME, 'odoo_proxy_url.txt')

TEST_SERVER_ACCESS_CONFIG = {
    'host': 'localhost',
    'dbname': 'odoo',
    'username': 'admin',
    'password': read_file_as_string(
        ODOO_SECRETS_TOKEN_FILE_NAME).strip() or 'odoo',
    'port': 8069,
    'timeout': 14,
    'ssl': False,
    'proxy_url': read_file_as_string(
        ODOO_PROXY_URL_FILE_NAME).strip() or None,
    }
