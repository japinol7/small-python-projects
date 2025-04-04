__author__ = 'Joan A. Pinol  (japinol)'

from collections import namedtuple
from .xmlrpc_jap import XmlRpcClient, XmlRpcConnection

ServerConfig = namedtuple("ServerConfig", "host dbname username password port")


class OdooClient:
    def __init__(self, host, dbname, username, password, port):
        self.server_data = self._get_server_data(
            host, dbname, username, password, port
            )
        self.client = self._get_client()

    def _get_client(self):
        return XmlRpcClient(self._get_connection())

    def _get_connection(self):
        return XmlRpcConnection(self.server_data)

    def _get_server_data(self, host, dbname, username, password, port):
        return ServerConfig(host, dbname, username, password, port)
