__author__ = 'Joan A. Pinol  (japinol)'

from xmlrpc import client as xmlrpclib
import http.client

from .config import PORTS_TO_ACTIVATE_SSL
from .exceptions import UserError
from ..tools.logger.logger import log


class ProxiedHTTPSTransport(xmlrpclib.SafeTransport):
    def __init__(self, use_datetime=False, context=None):
        super().__init__(use_datetime=use_datetime, context=context)
        self.proxy_host = None
        self.proxy_port = None
        self.proxy_headers = {}

    def set_proxy(self, host, port=None, headers=None):
        """Configure the HTTP proxy used for HTTPS tunneling."""
        self.proxy_host = host
        self.proxy_port = port
        self.proxy_headers = headers.copy() if headers else {}

    def make_connection(self, host):
        """Build an HTTPSConnection to the proxy and tunnel to the target host."""
        if not self.proxy_host or not self.proxy_port:
            raise RuntimeError("Proxy not configured. Call set_proxy(host, port, headers) first.")

        # Create HTTPS connection to the proxy and set the connect tunnel to the target
        connection = http.client.HTTPSConnection(self.proxy_host, self.proxy_port, context=self.context)
        connection.set_tunnel(host, port=None, headers=self.proxy_headers)
        self._connection = host, connection
        return connection


class XmlRpcConnection:
    """Represents a xml-rpc connection."""

    def __init__(self, server):
        self.server = server
        self.common = None
        self.models = None
        self.uid = None
        self.ssl = True if server.port in PORTS_TO_ACTIVATE_SSL else False
        self._is_proxy_set = False
        self._connect()

    def _set_proxy(self):
        log.debug(f"Setting proxy to: {self.server.proxy_url}")
        if '//' in self.server.proxy_url:
            _, proxy_url = self.server.proxy_url.split('//')
        else:
            proxy_url = self.server.proxy_url
        proxy_host, proxy_port = proxy_url.split(':')

        transport = None
        if proxy_host and proxy_port:
            transport = ProxiedHTTPSTransport()
            transport.set_proxy(host=proxy_host, port=proxy_port)
            self._is_proxy_set = True
        return transport

    def _connect(self):
        log.info(f'Connecting to {self.server.host} ({self.server.dbname}) '
                 f'as {self.server.username}')

        transport = None
        if self.server.proxy_url and not self.ssl:
            log.warning(
                "Proxy configuration ignored. Feature not implemented "
                "for xml-rpc over HTTP. Only implemented for HTTPS.")
        elif self.server.proxy_url and self.ssl:
            transport = self._set_proxy()

        if self.ssl:
            root = 'https://%s:%d/xmlrpc/2/' % (self.server.host, self.server.port)
        else:
            root = 'http://%s:%d/xmlrpc/2/' % (self.server.host, self.server.port)

        self.uid = (xmlrpclib.ServerProxy(root + 'common', transport=transport).login(
            self.server.dbname, self.server.username, self.server.password)
            )

        if not self.uid:
            raise UserError("Wrong username or password!")

        # Set endpoints
        self.common = xmlrpclib.ServerProxy(
            root + 'common', allow_none=True, transport=transport)
        self.models = xmlrpclib.ServerProxy(
            root + 'object', allow_none=True, transport=transport)
