import sqlite3
from sqlite3 import Error

from tools.logger.logger import log


class SqliteConnection:

    def __init__(self, db_file):
        self.db_file = db_file

    def create(self):
        log.info(f"Connect to database: {self.db_file}")
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            log.error(e)

        return conn
