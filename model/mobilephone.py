class Mobilephone:
    __id = 0

    def __init__(self, brand, name, storage, color, price):
        self.__id = Mobilephone.__id
        self.__brand = brand
        self.__name = name
        self.__storage = storage
        self.__color = color
        self.__price = price
        Mobilephone.__id += 1

    def export_info(self, db_obj):
        query = ''
        variables = ()
        db_obj.execute(query, variables)

    @staticmethod
    def import_info(db_obj):
        query = ''
        variables = ()
        db_obj.execute(query, variable)
