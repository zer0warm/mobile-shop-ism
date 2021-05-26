import tkinter as tk

from models.database import Database

class WinStatus(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Store status'

        self.__create_widgets()
        self.__display_widgets()
        self.__make_queries_map()

    def __create_widgets(self):
        self.__widgets = []
        for stat, query, index in self.__make_queries_map():
            Database.execute(query)
            value = Database.get_result()[index]
            self.__widgets.append((tk.Label(self, text=f'{stat}:', font='Helvetica 14 bold'), tk.Label(self, text=f'{value}')))

    def __make_queries_map(self):
        return [
            ('Current number of selling phones', 'select sum(qty) from phones;', 0),
            ('Brand with the largest number of variations',
             'select count(distinct name) as val, brand from phones group by brand order by val desc;', 1),
            ('Price range', 'select printf("%d - %d", min(price), max(price)) from phones;', 0),
            ('Most expensive phone', 'select max(price), name from phones;', 1),
            ('Cheapest phone', 'select min(price), name from phones;', 1),
        ]

    def __display_widgets(self):
        for i in range(len(self.__widgets)):
            stat, info = self.__widgets[i]
            stat.grid(row=i, column=0, sticky='w')
            info.grid(row=i, column=1, sticky='w')
