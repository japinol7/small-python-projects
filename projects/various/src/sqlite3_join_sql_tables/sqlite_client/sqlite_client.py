from sqlite3 import Error

from tools.logger.logger import log


class SqliteClient:

    def __init__(self, connection):
        self.connection = connection

    def sql_execute(self, sql_query):
        log.info(f"Execute query: \n{sql_query}")
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query)
        except Error as e:
            log.error(e)

    def is_table_already_created(self, table_name):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name = ? "
            "; ",
            (table_name, )
            )
        return data.fetchall() and True or False
