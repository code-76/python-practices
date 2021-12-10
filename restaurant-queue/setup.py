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
            id integer PRIMARY KEY AUTOINCREMENT,
            total_of_member integer NOT NULL DEFAULT 1,
            ready integer NOT NULL DEFAULT 0
        );
    """
    connect.execute(sql)

def create_ticketing_types_table(connect: Connection):
    sql = """
        CREATE TABLE IF NOT EXISTS ticketing_types (
            id integer PRIMARY KEY AUTOINCREMENT,
            type text CHECK(type IN ('A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')) NOT NULL DEFAULT 'A',
            number integer NOT NULL DEFAULT 1
        );
    """
    connect.execute(sql)

def insert_ticketing_type(connect: Connection, type, number = 0):
    sql = """
        INSERT INTO ticketing_types (type, number) VALUES (?, ?)
    """
    connect.execute(sql, [type, number])

def main():
    database = 'ticketing.db'
    connect = create_connection(database)
    create_ticketing_table(connect)
    create_ticketing_types_table(connect)
    insert_ticketing_type(connect, "A")
    insert_ticketing_type(connect, "B")
    insert_ticketing_type(connect, "C")
    insert_ticketing_type(connect, "E")
    insert_ticketing_type(connect, "F")
    insert_ticketing_type(connect, "G")
    insert_ticketing_type(connect, "H")
    insert_ticketing_type(connect, "I")
    insert_ticketing_type(connect, "J")
    print("Connection established!")

if __name__ == '__main__':
    main()
