__author__ = 'Joan A. Pinol  (japinol)'

from .config import CLIENT_NAME
from ..tools.logger.logger import log

DEFAULT_LIMIT = 50


class XmlRpcClient:
    """Represents a xml-rpc client."""

    def __init__(self, connection, context=None):
        self._connection = connection.models
        self._common = connection.common
        self._db = getattr(connection, 'db', None)
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

    # -------------------------
    # Helpers
    # -------------------------
    def _call_kw(
            self, model, method, args=None, kwargs=None, context=None
        ):
        """Generic helper for execute_kw with merged context."""
        merged_ctx = {**self._context, **(context or {})}
        final_kwargs = kwargs.copy() if kwargs else {}
        final_kwargs['context'] = merged_ctx

        return self._connection.execute_kw(
            self._server.dbname,
            self._uid,
            self._server.password,
            model,
            method,
            args or [],
            final_kwargs,
            )

    # -------------------------
    # Service Calls
    # -------------------------
    def get_db_list(self):
        """Gets the available databases."""
        if not self._db:
            raise RuntimeError(
                "DB proxy is not available in the XML-RPC connection.")

        return self._db.list()

    def get_server_version(self):
        """Gets the server version."""
        return self._common.version()['server_version']

    def get_server_version_data(self):
        """Gets the server version data."""
        return self._common.version()

    def call_service(self, service_obj_name, method, kwargs=None):
        """Calls a given method on a given service object name with
        the specified kwargs. Service name examples: common, db.
        """
        service_obj_name = (service_obj_name or '').lower()
        if service_obj_name == 'common':
            proxy = self._common
        elif service_obj_name == 'db':
            if not self._db:
                raise RuntimeError(
                    "DB proxy is not available in the XML-RPC connection.")
            proxy = self._db
        else:
            raise ValueError(
                f"Unknown service name: {service_obj_name}")

        func = getattr(proxy, method)
        if kwargs is None:
            return func()
        return func(**kwargs)

    def call_common(self, method, kwargs=None):
        """Calls a given method on the common service
        with the specified kwargs.
        """
        func = getattr(self._common, method)
        if kwargs is None:
            return func()
        return func(**kwargs)

    def call_db(self, method, kwargs=None):
        """Calls a given method on the db service
        with the specified kwargs.
        """
        if not self._db:
            raise RuntimeError(
                "DB proxy is not available in the XML-RPC connection.")

        func = getattr(self._db, method)
        if kwargs is None:
            return func()

        return func(**kwargs)

    # -------------------------
    # Model Calls
    # -------------------------
    def call(
            self, model, method, ids, args=None, kwargs=None, context=None
        ):
        """Calls a recordset-level method (api.multi / api.onchange-style)."""
        ids = ids or []
        full_args = [ids] + (args or [])

        return self._call_kw(
            model, method, full_args, kwargs, context,
            )

    def call_on_model(
            self, model, method, args=None, kwargs=None, context=None
        ):
        """Calls an @api.model method (no recordset)."""
        return self._call_kw(
            model, method, args, kwargs, context,
            )

    # -------------------------
    # CRUD API
    # -------------------------
    def create(
            self, model, vals, context=None, **kwargs
        ):
        """Creates a document object with the specified values."""
        return self._call_kw(
            model, 'create',
            [vals], kwargs, context,
            )

    def read(
            self, model, ids, fields, context=None, **kwargs
        ):
        """Gets the values of the document object for the specified ids."""
        return self._call_kw(
            model, 'read',
            [ids, fields], kwargs, context,
            )

    def read_group(
            self, model, domain, fields, group_by,
            context=None, **kwargs
        ):
        """Returns a list of dictionaries with the aggregate results
        grouped by the `group_by` field.
        """
        kw = {'fields': fields, 'groupby': group_by, **kwargs}
        return self._call_kw(
            model, 'read_group',
            [domain], kw, context,
            )

    def search(
            self, model, domain, order=None,
            limit=DEFAULT_LIMIT, context=None, **kwargs
        ):
        """Gets the ids of the document object that match the specified domain."""
        kw = {'order': order, 'limit': limit, **kwargs}
        res = self._call_kw(
            model, 'search',
            [domain], kw, context,
            )

        if limit and limit != 1 and len(res) == limit:
            log.info(f"{CLIENT_NAME}: Search result truncated to {limit} records. "
                "Use limit=0 to retrieve all results.")

        return res

    def search_count(
            self, model, domain, context=None, **kwargs
        ):
        """Returns the number of ids for the document object that match the
        specified domain.
        """
        return self._call_kw(
            model, 'search_count',
            [domain], kwargs, context,
            )

    def search_read(
            self, model, domain, fields, order=None,
            limit=DEFAULT_LIMIT, context=None, **kwargs
        ):
        """Combines the search and read operations in one call.
        Returns a list of dictionaries with the required fields for each object
        that matches the specified domain.
        """
        kw = {'fields': fields, 'order': order, 'limit': limit, **kwargs}
        res = self._call_kw(
            model, 'search_read',
            [domain], kw, context,
            )

        if limit and limit != 1 and len(res) == limit:
            log.info(f"{CLIENT_NAME}: Search result truncated to {limit} records. "
                        "Use limit=0 to retrieve all results.")

        return res

    def write(
            self, model, ids, vals, context=None, **kwargs
        ):
        """Updates the document objects for the specified ids with the specified
        values.
        """
        return self._call_kw(
            model, 'write',
            [ids, vals], kwargs, context,
            )

    def unlink(
            self, model, ids, context=None, **kwargs
        ):
        """Deletes the document objects that match the specified ids."""
        return self._call_kw(
            model, 'unlink',
            [ids], kwargs, context,
            )
