__author__ = 'Joan A. Pinol  (japinol)'

from xmlrpc import client as xmlrpclib

from .config import PORTS_TO_ACTIVATE_SSL
from .exceptions import UserError
from ..tools.logger.logger import log


class XmlRpcConnection:
    """Represents a xml-rpc connection."""

    def __init__(self, server):
        self.server = server
        self.common = None
        self.models = None
        self.uid = None
        self.ssl = True if server.port in PORTS_TO_ACTIVATE_SSL else False
        self._connect()

    def _connect(self):
        log.info(f'Connecting to {self.server.host} ({self.server.dbname}) '
                 f'as {self.server.username}')

        if self.ssl:
            root = 'https://%s:%d/xmlrpc/2/' % (self.server.host, self.server.port)
        else:
            root = 'http://%s:%d/xmlrpc/2/' % (self.server.host, self.server.port)

        self.uid = (xmlrpclib.ServerProxy(root + 'common').login(
            self.server.dbname, self.server.username, self.server.password)
            )

        if not self.uid:
            raise UserError("Wrong username or password!")

        # Set endpoints
        self.common = xmlrpclib.ServerProxy(root + 'common', allow_none=True)
        self.models = xmlrpclib.ServerProxy(root + 'object', allow_none=True)
