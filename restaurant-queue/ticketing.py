import sqlite3
from sqlite3 import Error
from sqlite3 import Connection, Cursor, Row

class Ticketing:
    
    def __init__(self, database="ticketing.db") -> None:
        # self.__database = database
        self.__connect = self.__create_connection(database)

    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __create_connection(self, database):
        try:
            self.__connect = sqlite3.connect(database, isolation_level=None, check_same_thread=False)
            self.__connect.row_factory = self.__dict_factory
            # connect.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))

            return self.__connect
        except Error as e:
            print(e)

    def get_all_ticketing(self, page=0, order="DESC"):
        limit =""
        order_by = ""

        if order in ["ASC", "DESC"]: 
            order_by = f"ORDER BY id {order}"
            
        if page > 0:
            limit = f"LIMIT {page}"
            
        sql = """
            SELECT * FROM ticketing {} {}
        """

        self.__connect.cursor()
        result = self.__connect.execute(sql.format(order_by, limit)).fetchall()
        return result
    
    def get_ticketing_by_id(self, id):
        sql = """
            SELECT * FROM ticketing WEHRER id = ? LIMIT 1
        """

        self.__connect.cursor()
        result = self.__connect.execute(sql, [id, ]).fetchall()
        return result

    def get_ticketing_by_member(self, member, ready=0):
        sql = """
            SELECT * FROM ticketing WHERE total_of_member = ? AND ready = ? ORDER BY id ASC LIMIT 1
        """

        self.__connect.cursor()
        result = self.__connect.execute(sql, [member, ready]).fetchall()
        return result

    def add_ticketing(self, member):
        sql = """
            INSERT INTO ticketing (total_of_member) VALUES (?)
        """

        self.__connect.cursor()
        return self.__connect.execute(sql, [member, ]).lastrowid

    def update_state(self, member):
        sql = """
            UPDATE ticketing
            SET ready = 1 
            WHERE total_of_member = ? ORDER BY id ASC LIMIT 1
        """
        self.__connect.cursor()
        self.__connect.execute(sql, member)

    def get_ticketing_by_state(self, member=1, ready=1):
        sql = """
            SELECT id FROM ticketing WHERE total_of_member = ? AND ready = ? LIMIT 1
        """
        self.__connect.cursor()
        result = self.__connect.execute(sql, [member, ready]).fetchall()
        return result