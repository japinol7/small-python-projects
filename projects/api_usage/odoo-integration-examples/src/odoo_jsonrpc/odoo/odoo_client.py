__author__ = 'Joan A. Pinol  (japinol)'

import getpass

from collections import namedtuple
from .simple_jsonrpc import JsonRpcClient, JsonRpcConnection

ServerConfig = namedtuple(
    "ServerConfig", "host dbname username password port proxy_url"
    )


class OdooClient:
    def __init__(self, host, dbname, username, password, port, proxy_url):
        self._server_data = self._get_server_data(
            host, dbname, username, password, port, proxy_url
            )
        self.client = self._get_client()

    def _get_client(self):
        return JsonRpcClient(self._get_connection())

    def _get_connection(self):
        return JsonRpcConnection(self._server_data)

    def _get_server_data(self, host, dbname, username, password, port, proxy_url):
        if password is None:
            password = getpass.getpass("Password/API Key token: ")

        return ServerConfig(host, dbname, username, password, port, proxy_url)
