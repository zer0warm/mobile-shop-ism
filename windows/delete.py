import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

from windows.log import WinLog
from models.mobilephone import Mobilephone
from models.database import Database

class WinDelete(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Delete mobile phones'

        self.__create_widgets()
        self.__display_widgets()

    def __create_widgets(self):
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

        self.__tree.bind('<<TreeviewSelect>>', self.__select_handler)

    def __display_widgets(self):
        self.__tree.pack(expand=True, fill='both', side='top')

    def __select_handler(self, event):
        self.__values = self.__tree.item(self.__tree.selection()[0], 'values')
        WinLog.update_log(f'Current event: {event}')
        WinLog.update_log(f'Current values: {self.__values}')
        yes = self.__create_delete_message()
        if yes:
            self.__delete_mobilephone()
            self.__tree.destroy()
            self.__create_widgets()
            self.__display_widgets()

    def __create_delete_message(self):
        return messagebox.askyesno(
                title='Delete mobilephone entry',
                message=f'Are you sure to delete this entry: {self.__values}')

    def __delete_mobilephone(self):
        brand, name, storage, color, price, qty = self.__values[1:]
        id_ = self.__values[0]

        phone = Mobilephone(brand, name, storage, color, float(price), qty, id_)
        phone.delete_info()
        phone.speak()
