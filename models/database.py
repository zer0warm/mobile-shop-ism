import sqlite3

class Database:
    __connection = None
    __cursor = None

    @staticmethod
    def init(filename):
        Database.__connection = sqlite3.connect(filename)
        Database.__cursor = Database.__connection.cursor()

    @staticmethod
    def execute(query, variables=()):
        Database.__cursor.execute(query, variables)
        Database.__connection.commit()

    @staticmethod
    def get_result(all_=False):
        if all_:
            return Database.__cursor.fetchall()
        return Database.__cursor.fetchone()

    @staticmethod
    def close():
        Database.__connection.close()
