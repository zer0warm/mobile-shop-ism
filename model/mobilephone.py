from model.database import Database

class Mobilephone:
    __id = 0

    def __init__(self, brand, name, storage, color, price, qty):
        self.__id = Mobilephone.__id
        self.__brand = brand
        self.__name = name
        self.__storage = storage
        self.__color = color
        self.__price = price
        self.__quantity = qty
        Mobilephone.__id += 1

    def speak(self):
        return self.__dict__

    def export_info(self):
        query = '''insert into phones (brand, name, storage, color, price, qty)
                   values (?, ?, ?, ?, ?, ?);'''
        variables = (self.__brand, self.__name, self.__storage,
                     self.__color, self.__price, self.__quantity)
        Database.execute(query, variables)

    @staticmethod
    def import_info(db_obj):
        query = ''
        variables = ()
        db_obj.execute(query, variable)
