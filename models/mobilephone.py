from models.database import Database
from windows.log import WinLog

class Mobilephone:
    def __init__(self, brand, name, storage, color, price, qty, id_=None):
        self.__id = id_
        self.__brand = brand
        self.__name = name
        self.__storage = storage
        self.__color = color
        self.__price = price
        self.__quantity = qty

    def speak(self):
        WinLog.update_log(f'Model: {self.__dict__}')

    def export_info(self):
        query = '''insert into phones (brand, name, storage, color, price, qty)
                   values (?, ?, ?, ?, ?, ?);'''
        variables = (self.__brand, self.__name, self.__storage,
                     self.__color, self.__price, self.__quantity)
        Database.execute(query, variables)
        WinLog.update_log('Database: Export query executed.')

    def update_info(self):
        query = '''update phones
                   set (brand, name, storage, color, price, qty) = (?, ?, ?, ?, ?, ?)
                   where id = ?;'''
        variables = (self.__brand, self.__name, self.__storage,
                     self.__color, self.__price, self.__quantity, self.__id)
        Database.execute(query, variables);
        WinLog.update_log('Database: Update query executed.')

    @staticmethod
    def import_info(db_obj):
        query = ''
        variables = ()
        db_obj.execute(query, variable)
