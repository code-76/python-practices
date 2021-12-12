import sqlite3, config
from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor, Row

class Database(object):

    def create_connection(self):
        try:
            connect = sqlite3.connect(config.SQLALCHEMY_DATABASE, isolation_level=None, check_same_thread=False)
            connect.row_factory = self.__dict_factory
            return connect
        except Error as e:
            print(e)

    def __dict_factory(self, cursor: Cursor, row: Row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __create_ticketing_table(self, connect: Connection):
        # timestamp DATE DEFAULT (datetime('now','localtime'))
        connect.execute(
            """
                CREATE TABLE IF NOT EXISTS ticketing (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    number integer NOT NULL DEFAULT 1,
                    total_of_member integer NOT NULL DEFAULT 1,
                    ready integer NOT NULL DEFAULT 0,
                    code text NOT NULL DEFAULT 'A',
                    queue_code text NOT NULL
                );
            """
        )

    def __create_ticketing_types_table(self, connect: Connection):
        # code text CHECK(type IN ('A','B','C')) NOT NULL DEFAULT 'A',
        # SUBSTRING(MD5(RAND())
        connect.execute(
            """
                CREATE TABLE IF NOT EXISTS ticketing_types (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    code text NOT NULL DEFAULT 'A',
                    number integer NOT NULL DEFAULT 0,
                    member integer NOT NULL DEFAULT 1
                );
            """
        )

    def __insert_ticketing_type(self, connect: Connection, code, number = 0):
        connect.execute(
            """
                INSERT INTO ticketing_types (code, member) VALUES (?, ?)
            """
        , [code, number])

    def init(self):
        connect = self.create_connection()
        self.__create_ticketing_table(connect)
        self.__create_ticketing_types_table(connect)
        self.__insert_ticketing_type(connect, "A", 1)
        self.__insert_ticketing_type(connect, "B", 2)
        self.__insert_ticketing_type(connect, "C", 3)
        self.__insert_ticketing_type(connect, "D", 4)
        self.__insert_ticketing_type(connect, "E", 5)
        self.__insert_ticketing_type(connect, "F", 6)
        self.__insert_ticketing_type(connect, "G", 7)
        self.__insert_ticketing_type(connect, "H", 8)
        self.__insert_ticketing_type(connect, "I", 9)
        self.__insert_ticketing_type(connect, "J", 10)
        connect.commit()
        connect.close()