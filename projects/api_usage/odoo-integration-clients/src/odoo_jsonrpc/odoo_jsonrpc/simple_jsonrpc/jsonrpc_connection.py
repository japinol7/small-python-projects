__author__ = 'Joan A. Pinol  (japinol)'

import json
import random
import urllib.request

from .config import (
    CLIENT_NAME,
    PORTS_TO_ACTIVATE_SSL,
    TIMEOUT_DEFAULT_SEC,
    )
from .exceptions import OdooJsonRpcError
from ..tools.logger.logger import log
from ..version.version import VERSION


class JsonRpcConnection:
    """Represents a json-rpc connection."""

    def __init__(self, server):
        self.server = server
        self._url_root = None
        self.uid = None
        self.ssl = self._is_ssl(server)
        self.timeout = server.timeout or TIMEOUT_DEFAULT_SEC
        self._is_proxy_set = False
        self._connect()

    @staticmethod
    def _is_ssl(server):
        """Allows overriding SSL port-based default using an explicit flag
        in the server config.
        """
        if server.ssl is None:
            return True if server.port in PORTS_TO_ACTIVATE_SSL else False

        return True if server.ssl is True else False

    def call(self, service, method, *args):
        return self._json_rpc(
            'call', {
                'service': service, 'method': method, 'args': args,
                },
            )

    def execute(self, *args):
        return self._json_rpc(
            'call', {
                'service': 'object', 'method': 'execute', 'args': args,
                },
            )

    def execute_kw(self, *args):
        return self._json_rpc(
            'call', {
                'service': 'object', 'method': 'execute_kw', 'args': args,
                },
            )

    def _json_rpc(self, method, params):
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': random.randint(0, 1000000000),
            }

        req = urllib.request.Request(
            url=self._url_root,
            data=json.dumps(data).encode(),
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": f"odoo-jsonrpc/{VERSION}",
                },
            )

        reply = json.loads(urllib.request.urlopen(
            req, timeout=self.timeout).read().decode('UTF-8'))

        if reply.get('error'):
            raise Exception(reply['error'])

        return reply.get('result')

    def _set_proxy(self):
        log.debug(f"{CLIENT_NAME}: Setting proxy to: {self.server.proxy_url}")
        proxy_support = urllib.request.ProxyHandler(
            {'http': '%s' % self.server.proxy_url,
             'https': '%s' % self.server.proxy_url,
             })
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        self._is_proxy_set = True

    def _connect(self):
        log.info(f"{CLIENT_NAME}: Connecting to "
                 f"{self.server.host} ({self.server.dbname}) "
                 f"as {self.server.username}")

        if not self._is_proxy_set and self.server.proxy_url:
            self._set_proxy()

        protocol = "https" if self.ssl else "http"
        self._url_root = f"{protocol}://{self.server.host}:{self.server.port}/jsonrpc/"

        self.uid = self.call(
            'common', 'login',
            self.server.dbname, self.server.username, self.server.password)

        if not self.uid:
            raise OdooJsonRpcError("Wrong username or password!")
