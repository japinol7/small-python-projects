__author__ = 'Joan A. Pinol  (japinol)'

import json
import random
import urllib.request

from .config import PORTS_TO_ACTIVATE_SSL
from .exceptions import UserError
from ..tools.logger.logger import log


class JsonRpcConnection:
    """Represents a json-rpc connection."""

    def __init__(self, server):
        self.server = server
        self._url_root = None
        self.uid = None
        self.ssl = True if server.port in PORTS_TO_ACTIVATE_SSL else False
        self._connect()

    def call(self, service, method, *args):
        return self._json_rpc(
            'call',
            {'service': service, 'method': method, 'args': args},
            )

    def execute(self, *args):
        return self._json_rpc(
            'call',
            {'service': 'object', 'method': 'execute', 'args': args},
            )

    def execute_kw(self, *args):
        return self._json_rpc(
            'call',
            {'service': 'object', 'method': 'execute_kw', 'args': args},
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
                "Content-Type": "application/json",
                },
            )

        reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))

        if reply.get('error'):
            raise Exception(reply['error'])

        return reply['result']

    def _connect(self):
        log.info(f'Connecting to {self.server.host} ({self.server.dbname}) '
                 f'as {self.server.username}')

        if self.ssl:
            self._url_root = "https://%s:%s/jsonrpc/" % (self.server.host, self.server.port)
        else:
            self._url_root = "http://%s:%s/jsonrpc/" % (self.server.host, self.server.port)

        self.uid = self.call(
            'common', 'login',
            self.server.dbname, self.server.username, self.server.password)

        if not self.uid:
            raise UserError("Wrong username or password!")
