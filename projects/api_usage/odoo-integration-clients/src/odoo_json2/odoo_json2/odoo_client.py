__author__ = 'Joan A. Pinol  (japinol)'

import getpass

from collections import namedtuple
from .simple_json2 import Json2Client, Json2Connection

ServerConfig = namedtuple(
    "ServerConfig",
    "host dbname api_key port proxy_url ssl "
    "timeout timeout_connect"
    )


class OdooClient:
    def __init__(
            self, host, dbname, api_key=None,
            port=None, proxy_url=None, ssl=None,
            timeout=None, timeout_connect=None
        ):
        self._server_data = self._get_server_data(
            host, dbname, api_key, port, proxy_url, ssl,
            timeout, timeout_connect)
        self.client = self._get_client()

    def _get_client(self):
        return Json2Client(self._get_connection())

    def _get_connection(self):
        return Json2Connection(self._server_data)

    def _get_server_data(
            self, host, dbname, api_key,
            port, proxy_url, ssl, timeout, timeout_connect
        ):
        if port is None:
            raise ValueError("port must be specified")

        if api_key is None:
            api_key = getpass.getpass("API Key token: ")

        return ServerConfig(
            host, dbname, api_key, port, proxy_url, ssl,
            timeout, timeout_connect)
