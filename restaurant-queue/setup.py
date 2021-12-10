import sqlite3, json
from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor, Row

class Setup():
    def dict_factory(self, cursor: Cursor, row: Row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def create_connection(self, database):
        try:
            connect = sqlite3.connect(database, isolation_level=None, check_same_thread=False)
            connect.row_factory = self.dict_factory
            # connect.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))

            return connect
        except Error as e:
            print(e)

    def create_ticketing_table(self, connect: Connection):
        sql = """
            CREATE TABLE IF NOT EXISTS ticketing (
                id integer PRIMARY KEY AUTOINCREMENT,
                total_of_member integer NOT NULL DEFAULT 1,
                ready integer NOT NULL DEFAULT 0
            );
        """
        connect.execute(sql)

    def create_ticketing_types_table(self, connect: Connection):
        sql = """
            CREATE TABLE IF NOT EXISTS ticketing_types (
                id integer PRIMARY KEY AUTOINCREMENT,
                type text CHECK(type IN ('A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')) NOT NULL DEFAULT 'A',
                number integer NOT NULL DEFAULT 1
            );
        """
        connect.execute(sql)

    def insert_ticketing_type(self, connect: Connection, type, number = 0):
        sql = """
            INSERT INTO ticketing_types (type, number) VALUES (?, ?)
        """
        connect.execute(sql, [type, number])

    def init(self):
        database = 'ticketing.db'
        connect = self.create_connection(database)
        self.create_ticketing_table(connect)
        self.create_ticketing_types_table(connect)
        self.insert_ticketing_type(connect, "A")
        self.insert_ticketing_type(connect, "B")
        self.insert_ticketing_type(connect, "C")
        self.insert_ticketing_type(connect, "E")
        self.insert_ticketing_type(connect, "F")
        self.insert_ticketing_type(connect, "G")
        self.insert_ticketing_type(connect, "H")
        self.insert_ticketing_type(connect, "I")
        self.insert_ticketing_type(connect, "J")
        return "Connection established!"