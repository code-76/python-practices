import sqlite3, json
from sqlite3 import Error
from sqlite3 import Connection, Cursor, Row

class Ticketing:
    
    def __init__(self, database="ticketing.db") -> None:
        self.__database = database

    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __create_connection(self):
        try:
            connect = sqlite3.connect(self.__database, isolation_level=None, check_same_thread=False)
            connect.row_factory = self.__dict_factory
            # connect.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))

            return connect
        except Error as e:
            print(e)
    
    def get(self, number):
        connect = self.__create_connection()
        sql = """
            INSERT INTO ticketing (total_of_member) VALUES (?)
        """
        connect.execute(sql, [number, ])
        return connect.cursor().lastrowid

    def update_state(self, number):
        connect = self.__create_connection()
        sql = """
            UPDATE ticketing
            SET ready = 1 where total_of_member = ?
            ORDER BY id ASC LIMI 1
        """
        connect.execute(sql, number)