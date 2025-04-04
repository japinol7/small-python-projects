__author__ = 'Joan A. Pinol  (japinol)'

from xmlrpc import client as xmlrpclib

from .exceptions import UserError
from ..tools.logger.logger import log


class XmlRpcConnection:
    """Represents a xml-rpc connection."""

    def __init__(self, server):
        self.server = server
        self.common = None
        self.uid = None
        self._connect()

    def _connect(self):
        log.info(f'Connecting to {self.server.host} ({self.server.dbname}) '
                 f'as {self.server.username}')

        root = 'http://%s:%d/xmlrpc/' % (self.server.host, self.server.port)
        self.uid = (xmlrpclib.ServerProxy(root + 'common').login(
            self.server.dbname, self.server.username, self.server.password)
            )

        if not self.uid:
            raise UserError("Wrong username or password!")

        self.common = xmlrpclib.ServerProxy(root + 'object', allow_none=True)
