import sqlite3

class Database:
    def __init__(self, filename):
        self.__connection = sqlite3.connect(filename)

    def prepare(self):
        self.__cursor = self.__connection.cursor()

    def execute(self, query, variables):
        self.__cursor.execute(query, variables)

    def get_result(self, all_=False):
        if all_:
            return self.fetchall()
        return self.fetchone()

    def close(self):
        self.__connection.commit()
        self.__connection.close()
