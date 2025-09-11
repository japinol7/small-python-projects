__author__ = 'Joan A. Pinol  (japinol)'

DEFAULT_LIMIT = 50


class JsonRpcClient:
    """Represents a json-rpc client."""

    def __init__(self, connection):
        self._connection = connection
        self._server = connection.server
        self._uid = connection.uid

    def get_server_version(self):
        """Gets the server version."""
        return self._connection.call('common', 'version')['server_version']

    def call(self, model_obj_name, method, values):
        """Calls a given method on a given model object name
        with the specified values.
        """
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            method, values,
            )

    def call_kw_on_instances(self, model_obj_name, method, ids, values):
        """Calls a given method on given model object instances
        with the specified values.
        This call uses execute_kw.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            method, ids, values,
            )

    def call_on_instances(self, model_obj_name, method, ids, values):
        """Calls a given method on given model object instances
        with the specified values.
        """
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            method, ids, values,
            )

    def create(self, model_obj_name, values):
        """Creates a document object with the specified values."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'create', values,
            )

    def read(self, model_obj_name, ids, fields):
        """Gets the values of the document object for the specified ids."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'read', ids, fields,
            )

    def search(self, model_obj_name, domain, order=None, limit=DEFAULT_LIMIT):
        """Gets the ids of the document object that match the specified domain."""
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search', domain,
            {'order': order, 'limit': limit},
            )

    def search_count(self, model_obj_name, domain):
        """Returns the number of ids for the document object that match the
        specified domain.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search_count', domain,
            )

    def search_read(
            self, model_obj_name, domain, fields, order=None, limit=DEFAULT_LIMIT
        ):
        """Combines the search and read operations in one call.
        Returns a list of dictionaries with the required fields for each object
        that matches the specified domain.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search_read', domain,
            {'fields': fields, 'order': order, 'limit': limit},
            )

    def write(self, model_obj_name, ids, values):
        """Updates the document objects for the specified ids with the specified
        values.
        """
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'write', ids, values,
            )

    def unlink(self, model_obj_name, ids):
        """Deletes the document objects that match the specified ids."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'unlink', ids,
            )
