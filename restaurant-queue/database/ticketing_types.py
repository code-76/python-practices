from database import Database

class TicketingTypes:
    
    def __init__(self) -> None:
        database = Database()
        self.__connect = database.create_connection()

    def update_type(self, id, code, member):
        self.__connect.cursor()
        self.__connect.execute(""""
            UPDATE SET code = ?, SET member = ? 
            FROM ticketing_types 
            WHERE id = ?
        """, [code, member, id])

    def add_type(self, code, member):
        self.__connect.cursor()
        self.__connect.execute("""
            INSERT INTO ticketing_types (code, member) VALUES (?, ?)
        """, [code, member])