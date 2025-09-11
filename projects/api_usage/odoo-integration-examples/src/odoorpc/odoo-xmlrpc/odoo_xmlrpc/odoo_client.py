__author__ = 'Joan A. Pinol  (japinol)'

import getpass

from collections import namedtuple
from .simple_xmlrpc import XmlRpcClient, XmlRpcConnection

ServerConfig = namedtuple(
    "ServerConfig", "host dbname username password port proxy_url"
    )


class OdooClient:
    def __init__(
            self, host, dbname, username,
            password=None, port=None, proxy_url=None
        ):
        self._server_data = self._get_server_data(
            host, dbname, username, password, port, proxy_url
            )
        self.client = self._get_client()

    def _get_client(self):
        return XmlRpcClient(self._get_connection())

    def _get_connection(self):
        return XmlRpcConnection(self._server_data)

    def _get_server_data(self, host, dbname, username, password, port, proxy_url):
        if port is None:
            raise ValueError("port must be specified")

        if password is None:
            password = getpass.getpass("Password/API Key token: ")

        return ServerConfig(host, dbname, username, password, port, proxy_url)
