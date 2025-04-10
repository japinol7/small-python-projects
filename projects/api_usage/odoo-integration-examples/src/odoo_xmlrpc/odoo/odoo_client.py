__author__ = 'Joan A. Pinol  (japinol)'

import getpass

from collections import namedtuple
from .simple_xmlrpc import XmlRpcClient, XmlRpcConnection

ServerConfig = namedtuple("ServerConfig", "host dbname username password port")


class OdooClient:
    def __init__(self, host, dbname, username, password, port):
        self._server_data = self._get_server_data(
            host, dbname, username, password, port
            )
        self.client = self._get_client()

    def _get_client(self):
        return XmlRpcClient(self._get_connection())

    def _get_connection(self):
        return XmlRpcConnection(self._server_data)

    def _get_server_data(self, host, dbname, username, password, port):
        if password is None:
            password = getpass.getpass("Password/API Key token: ")

        return ServerConfig(host, dbname, username, password, port)
