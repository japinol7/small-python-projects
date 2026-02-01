from __future__ import annotations

__author__ = 'Joan A. Pinol  (japinol)'

from typing import Any, TypeAlias

import requests

from .config import (
    CLIENT_NAME,
    PORTS_TO_ACTIVATE_SSL,
    TIMEOUT_DEFAULT_SEC,
    TIMEOUT_CONNECT_DEFAULT_SEC,
    )
from ..tools.logger.logger import log
from ..version.version import VERSION

JSON: TypeAlias = dict[str, Any]


class Json2Connection:
    """Represents a json-2 connection."""

    def __init__(self, server):
        self.server = server
        self._url_root = None
        self._url_root_web = None
        self.uid = None
        self.ssl = self._is_ssl(server)
        self.timeout = server.timeout or TIMEOUT_DEFAULT_SEC
        self.timeout_connect = server.timeout_connect or TIMEOUT_CONNECT_DEFAULT_SEC
        self.proxy_url = server.proxy_url or None
        self._connect()

    @staticmethod
    def _is_ssl(server) -> bool:
        """Allows overriding SSL port-based default using an explicit flag
        in the server config.
        """
        if server.ssl is None:
            return server.port in PORTS_TO_ACTIVATE_SSL

        return True if server.ssl is True else False

    def _setup_urls(self):
        """Constructs the root URLs for the connection."""
        protocol = "https" if self.ssl else "http"
        base_url = f"{protocol}://{self.server.host}:{self.server.port}"
        self._url_root = f"{base_url}/json/2/"
        self._url_root_web = f"{base_url}/web/"

    @property
    def proxies(self) -> dict[str, str]:
        """Returns the proxies dictionary."""
        return {
            'http': self.proxy_url, 'https': self.proxy_url
            } if self.proxy_url else {}

    def _connect(self):
        log.info(f"{CLIENT_NAME}: Connecting to "
                 f"{self.server.host} ({self.server.dbname})")

        headers = {
            "Authorization": f"Bearer {self.server.api_key}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": f"odoo-json2/{VERSION} (requests/{requests.__version__})",
            }
        if self.server.dbname:
            headers["X-Odoo-Database"] = self.server.dbname

        self._client = requests.Session()
        self._client.headers.update(headers)
        self._client.proxies = self.proxies
        self._client.timeout = (self.timeout_connect, self.timeout)
        self._setup_urls()
