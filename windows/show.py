import tkinter as tk
import tkinter.ttk as ttk

from models.mobilephone import Mobilephone
from models.database import Database

class WinShow(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'List of mobile phones'

        self.create_widgets()
        self.display_widgets()

    def create_widgets(self):
        headings = ('id', 'brand', 'name', 'color', 'storage', 'price', 'qty')
        self.__tree = ttk.Treeview(self, columns=headings, show='headings')

        for h in headings:
            if h != 'name':
                self.__tree.column(h, width=75)
            self.__tree.column(h, anchor='center')
            self.__tree.heading(h, text=h.upper())

        Database.execute('SELECT * FROM Phones')
        for row in Database.get_result(all_=True):
            self.__tree.insert('', 'end', values=row)

    def display_widgets(self):
        self.__tree.pack(expand=True, fill='both', side='top')

    def get_user_input(self):
        data = {}
        for label, textentry in self.__widgets:
            data[label['text']] = textentry
        return data
