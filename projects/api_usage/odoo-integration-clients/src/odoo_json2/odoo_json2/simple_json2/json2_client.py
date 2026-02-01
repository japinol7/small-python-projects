from __future__ import annotations

__author__ = 'Joan A. Pinol  (japinol)'

from typing import Any, TypeAlias, Optional, Union

import requests

from .exceptions import OdooJson2Error
from .config import CLIENT_NAME
from ..tools.logger.logger import log
from ..version.version import VERSION

JSON: TypeAlias = dict[str, Any]

DEFAULT_LIMIT = 50


class Json2Client:
    """Represents a json-2 client."""

    def __init__(self, connection, context=None):
        self._connection = connection
        self._server = connection.server
        self._uid = connection.uid
        self._context = context or {}

    @property
    def context(self):
        """Returns the global context dict."""
        return self._context

    @context.setter
    def context(self, value):
        """Replaces the global context entirely."""
        if value is None:
            self._context = {}
        elif isinstance(value, dict):
            self._context = value
        else:
            raise TypeError("Context must be a dict or None.")

    def update_context(self, **kwargs):
        """Updates one or more context keys without replacing the whole dict."""
        self._context.update(kwargs)

    # ---------------------------
    # Response handling helper
    # ---------------------------
    def _handle_response(self, response: requests.Response) -> JSON:
        """Handle HTTP response and raise appropriate exceptions based on status code."""
        match response.status_code:
            case 200:
                return response.json()
            case 400:
                raise OdooJson2Error(f"Bad request: {response.text}")
            case 401:
                raise OdooJson2Error(f"Unauthorized: {response.text}")
            case 403:
                raise OdooJson2Error(f"Forbidden: {response.text}")
            case 404:
                raise OdooJson2Error(f"Not found: {response.text}")
            case code if code >= 500:
                raise OdooJson2Error(f"Server error {code}: {response.text}")
            case _:
                raise OdooJson2Error(
                    f"Unexpected response {response.status_code}: {response.text}")

    # ---------------------------
    # Core call
    # ---------------------------
    def call(self, model: str, method: str, **params: Any) -> JSON:
        """Call any Odoo model.method."""
        if self._context:
            local_context = params.get("context", {})
            params["context"] = {**self._context, **local_context}

        url = f"{self._connection._url_root}{model}/{method}"
        response = self._connection._client.post(
            url, json=params, timeout=self._connection._client.timeout)
        return self._handle_response(response)

    # -------------------------
    # Service Calls
    # -------------------------
    def get_db_list(self):
        """Gets the available databases."""
        url = f"{self._connection._url_root_web}database/list"
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {},
            "id": None,
            }

        jsonrpc_client = requests.Session()
        jsonrpc_client.headers.update({
            "Content-Type": "application/json-rpc; charset=utf-8",
            "User-Agent": f"odoo-json2/{VERSION} (requests/{requests.__version__})",
            })
        jsonrpc_client.proxies = self._connection.proxies
        timeout = (self._connection.timeout_connect, self._connection.timeout)

        response = jsonrpc_client.post(url, json=payload, timeout=timeout)
        return response.json()["result"]

    def get_server_version(self) -> str:
        """Gets the server version."""
        version_data = self.get_server_version_data()
        return version_data['version'] if isinstance(version_data, dict) else ''

    def get_server_version_data(self):
        """Gets the server version data."""
        url = f"{self._connection._url_root_web}version"
        jsonrpc_client = requests.Session()
        jsonrpc_client.headers.update({
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": f"odoo-json2/{VERSION} (requests/{requests.__version__})",
            })
        jsonrpc_client.proxies = self._connection.proxies
        timeout = (self._connection.timeout_connect, self._connection.timeout)

        response = jsonrpc_client.get(url, timeout=timeout)
        return self._handle_response(response)

    # ---------------------------
    # CRUD methods
    # ---------------------------
    def create(self, model: str, vals: Union[dict, list[dict]], **kwargs: Any
        ) -> JSON:
        """Creates a document object with the specified values."""
        return self.call(model, "create", vals_list=vals, **kwargs)

    def read(self, model: str, ids: list, fields: Optional[list] = None, **kwargs: Any
        ) -> JSON:
        """Gets the values of the document object for the specified ids."""
        return self.call(model, "read", ids=ids, fields=fields, **kwargs)

    def read_group(
            self, model: str, domain: list, fields: Optional[list] = None,
            group_by: Optional[list] = None, **kwargs: Any
        ) -> JSON:
        """Returns a list of dictionaries with the aggregate results
        grouped by the `group_by` field.
        """
        return self.call(
            model, "read_group", domain=domain,
            groupby=group_by, fields=fields, **kwargs)

    def search(
            self, model: str, domain: list, limit=DEFAULT_LIMIT, **kwargs: Any
        ) -> JSON:
        """Gets the ids of the document object that match the specified domain."""
        res = self.call(
            model, "search", domain=domain, limit=limit, **kwargs)

        if limit and limit != 1 and len(res) == limit:
            log.info(f"{CLIENT_NAME}: Search result truncated to {limit} records. "
                        "Use limit=0 to retrieve all results.")

        return res

    def search_count(self, model: str, domain: list, **kwargs: Any) -> JSON:
        """Returns the number of ids for the document object that match the
        specified domain.
        """
        return self.call(model, "search_count", domain=domain, **kwargs)

    def search_read(
            self, model: str, domain: list, fields: Optional[list] = None,
            limit=DEFAULT_LIMIT, **kwargs: Any
        ) -> JSON:
        """Combines the search and read operations in one call.
        Returns a list of dictionaries with the required fields for each object
        that matches the specified domain.
        """
        res = self.call(
            model, "search_read", domain=domain, fields=fields,
            limit=limit, **kwargs)

        if limit and limit != 1 and len(res) == limit:
            log.info(f"{CLIENT_NAME}: Search result truncated to {limit} records. "
                        "Use limit=0 to retrieve all results.")

        return res

    def write(self, model: str, ids: list, vals: dict, **kwargs: Any
        ) -> JSON:
        """Updates the document objects for the specified ids with the specified
        values.
        """
        return self.call(model, "write", ids=ids, vals=vals, **kwargs)

    def unlink(self, model: str, ids: list, **kwargs: Any) -> JSON:
        """Deletes the document objects that match the specified ids."""
        return self.call(model, "unlink", ids=ids, **kwargs)
