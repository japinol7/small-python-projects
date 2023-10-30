from tools.logger import logger
from tools.logger.logger import log
from sqlite_connecttion.sqlite_connecttion import SqliteConnection
from sqlite_client.sqlite_client import SqliteClient

APP_NAME = 'sqlite3_join_sql_tables'


def create_and_fill_table_book_stores(conn):
    if SqliteClient(conn).is_table_already_created('book_stores'):
        return

    log.info("Create and fill table: book_stores")
    SqliteClient(conn).sql_execute(
        "CREATE TABLE IF NOT EXISTS book_stores ( "
        "    id integer PRIMARY KEY, "
        "    book_store_name text NOT NULL, "
        "    city text NOT NULL "
        ");"
        )
    conn.commit()

    book_stores_vals = (
        (1, "book_store_01", "New York"),
        (2, "book_store_02", "Chicago"),
        (3, "book_store_03", "Seattle"),
        (4, "book_store_04", "Nashville"),
        (5, "book_store_05", "San Francisco"),
        (6, "book_store_06", "Seattle"),
        (7, "book_store_07", "New York"),
        (8, "book_store_08", "Seattle"),
        (9, "book_store_09", "San Francisco"),
        (10, "book_store_10", "Seattle"),
        (11, "book_store_11", "Nashville"),
        (12, "book_store_12", "Chicago"),
        (13, "book_store_13", "Boston"),
        (14, "book_store_14", "Seattle"),
        )

    sql = "INSERT INTO book_stores(id, book_store_name, city) "\
          "    VALUES(?, ?, ?) " \
          ";"
    cursor = conn.cursor()
    for book_store_vals in book_stores_vals:
        cursor.execute(sql, book_store_vals)
    conn.commit()


def create_and_fill_table_users(conn):
    if SqliteClient(conn).is_table_already_created('users'):
        return

    log.info("Create and fill table: users")
    SqliteClient(conn).sql_execute(
        "CREATE TABLE IF NOT EXISTS users ( "
        "    id integer PRIMARY KEY, "
        "    username text NOT NULL, "
        "    city text NOT NULL "
        ");"
        )
    conn.commit()

    users_vals = (
        (1, "user_01", "Boston"),
        (2, "user_02", "San Francisco"),
        (3, "user_03", "Chicago"),
        (4, "user_04", "Nashville"),
        (5, "user_05", "Seattle"),
        (6, "user_06", "Seattle"),
        (7, "user_07", "Nashville"),
        (8, "user_08", "Seattle"),
        (9, "user_09", "San Francisco"),
        (10, "user_10", "New York"),
        (11, "user_11", "Boston"),
        (12, "user_12", "Chicago"),
        (13, "user_13", "Boston"),
        (14, "user_14", "New York"),
        (15, "user_15", "Dallas"),
        (16, "user_16", "San Francisco"),
        (17, "user_17", "Chicago"),
        (18, "user_18", "Paris"),
        (19, "user_19", "Nashville"),
        (20, "user_20", "Boston"),
        (21, "user_21", "Seattle"),
        (22, "user_22", "Denver"),
        )

    sql = "INSERT INTO users(id, username, city) "\
          "    VALUES(?, ?, ?) " \
          ";"
    cursor = conn.cursor()
    for user_vals in users_vals:
        cursor.execute(sql, user_vals)
    conn.commit()


def join_users_and_book_stores(cursor, city, order="asc"):
    log.info(f"Execute query join_users_and_book_stores with city: {city}, order: {order}")
    res = cursor.execute(
        "SELECT users.username, book_stores.book_store_name FROM users "
        "LEFT JOIN book_stores ON users.city = book_stores.city "
        "WHERE users.city = :city "
        f"ORDER BY users.username {order}, book_stores.book_store_name {order} "
        ";",
        {'city': city}
        )
    data = res.fetchall()
    return data


def main():
    log.info(f'Start App {APP_NAME}')
    conn = SqliteConnection(r'db\book_store.db').create()
    create_and_fill_table_book_stores(conn)
    create_and_fill_table_users(conn)

    cursor = conn.cursor()
    data = join_users_and_book_stores(cursor, city='Seattle', order='desc')

    for item in data:
        print(item)

    log.info('End App')


if __name__ == '__main__':
    logger.add_stdout_handler()
    main()
