
import hashlib
from sqlite3.dbapi2 import Connection
from common.db import Database
from datetime import datetime

class Ticketing:
    
    def __init__(self) -> None:
        self.__database = Database()
    
    def acquire_ticketing(self, member: int):
        connect = self.__database.create_connection()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S").encode('utf-8')
        queue_code = hashlib.md5(current_time)

        new_ticketing = self.__get_ticketing(connect, member)
        new_ticketing['queue_code'] = queue_code.hexdigest()
        print(new_ticketing)
        connect.execute("""
            INSERT INTO ticketing (code, number, queue_code, total_of_member) VALUES (?, ?, ?, ?)
        """, [new_ticketing['code'], new_ticketing['number'], new_ticketing['queue_code'], member])

        connect.commit()
        connect.close()
        return new_ticketing


    def __get_ticketing(self, connect: Connection, member):
        connect.cursor()
        connect.execute("""
            UPDATE ticketing_types SET number = number + 1 WHERE member = ? LIMIT 1
        """, [member, ])

        data = connect.execute("""
            SELECT * FROM ticketing_types WHERE member = ?
        """, [member, ]).fetchmany(1)

        print(data)

        result =  {
            "code" : "A",
            "number" : 1
        }
        
        if len(data) > 0:
            result = {
                "code" : data[0]['code'],
                "number" : data[0]['number'],
                "create_at" : data[0]['created_at']
            }
            
        return result

    def queue_data(self, queue_code):
        connect = self.__database.create_connection()
        connect.cursor()
        current = None
        
        data = connect.execute("""
            SELECT * FROM ticketing
            WHERE queue_code = ? 
            LIMIT 1
        """, [queue_code,]).fetchmany(1)

        if len(data) == 1:
            current = connect.execute("""
                SELECT * FROM ticketing
                WHERE ready = 1 AND queue_code != ? AND code = ?
                ORDER BY created_at ASC LIMIT 1
            """, [queue_code, data[0]['code']]).fetchmany(1)

        connect.commit()
        connect.close()

        print(current)
        print(data)

        if not data:
            return None
        else:
            if not current:
                return {
                    "ready" : data[0]["ready"]
                }
            else:
                return {
                    "current" : {
                        "code" : current[0]['code'],
                        "number" : current[0]['number'],
                        "created_at" : current[0]['created_at']
                    },
                    "ready" : data[0]["ready"]
                }

    def queue_update(self, member):
        connect = self.__database.create_connection()
        connect.cursor()

        connect.execute("""
            UPDATE ticketing SET ready = 2 
            WHERE ready = 1 AND total_of_member = ? 
            LIMIT 1
        """, [member, ])

        connect.execute("""
            UPDATE ticketing SET ready = 1 
            WHERE ready = 0 AND total_of_member = ? 
            ORDER BY id ASC LIMIT 1
        """, [member,])

        data = connect.execute("""
            SELECT * FROM ticketing WHERE ready = 0 AND total_of_member = ? 
            ORDER BY id ASC LIMIT 1
        """, [member,]).fetchmany(1)

        if not data:
            connect.execute("""
                UPDATE ticketing_types SET number = 0 WHERE member = ? LIMIT 1
            """, [member,])

        connect.commit()
        connect.close()

        if len(data) > 0:
            return {
                "code" : data[0]['code'],
                "number" : data[0]['number']
            }
            
        return None