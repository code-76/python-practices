import sqlite3, json
from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor, Row

def dict_factory(cursor: Cursor, row: Row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_connection(database):
    try:
        connect = sqlite3.connect(database, isolation_level=None, check_same_thread=False)
        connect.row_factory = dict_factory
        # connect.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))

        return connect
    except Error as e:
        print(e)

def create_ticketing_table(connect: Connection):
    sql = """
        CREATE TABLE IF NOT EXISTS ticketing (
            id integer PRIMARY KEY,
            total_of_member integer NOT NULL Default 1,
            ready integer NOT NULL Default 0
        );
    """
    connect.execute(sql)

def main():
    database = 'ticketing.db'
    connect = create_connection(database)
    create_ticketing_table(connect)
    print("Connection established!")

if __name__ == '__main__':
    main()
