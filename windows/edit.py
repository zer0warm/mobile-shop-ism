import tkinter as tk
import tkinter.ttk as ttk

from models.database import Database
from models.mobilephone import Mobilephone
from windows.log import WinLog

class WinEdit(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Edit mobile phone details'

        self.__create_treeview()
        self.__display_treeview()

    def __create_treeview(self):
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

    def __select_handler(self, event):
        self.__values = self.__tree.item(self.__tree.selection()[0], 'values')
        WinLog.update_log(f'Current event: {event}')
        WinLog.update_log(f'Current values: {self.__values}')
        self.__tree.destroy()
        self.__create_edit_window(self.__values[1:])
        self.__display_edit_window()

    def __display_treeview(self):
        self.__tree.pack(expand=True, fill='both', side='top')

    def __create_edit_window(self, args):
        self.__widgets = []
        fields = ['Brand', 'Name', 'Color', 'Storage', 'Price', 'Quantity']
        for i in range(len(fields)):
            label = tk.Label(self, text=fields[i])
            entry = tk.Entry(self)
            entry.insert(0, args[i])
            self.__widgets.append((label, entry))

        self.__update_button = tk.Button(
                self,
                text='Update',
                command=self.__update_button_handler)
        self.__clear_button = tk.Button(
                self,
                text='Clear',
                command=self.__clear_button_handler)

    def __display_edit_window(self):
        for i in range(len(self.__widgets)):
            label, textentry = self.__widgets[i]
            label.grid(row=i, column=0)
            textentry.grid(row=i, column=1, columnspan=5)
        self.__update_button.grid(row=i+1, column=4)
        self.__clear_button.grid(row=i+1, column=5)

    def __destroy_edit_window(self):
        for label, textentry in self.__widgets:
            label.destroy()
            textentry.destroy()
        self.__update_button.destroy()
        self.__clear_button.destroy()

    def __get_user_input(self):
        data = {}
        for label, textentry in self.__widgets:
            data[label['text']] = textentry
        return data

    def __update_button_handler(self):
        data = self.__get_user_input()

        brand = data['Brand'].get()
        name = data['Name'].get()
        storage = data['Storage'].get()
        color = data['Color'].get()
        price = data['Price'].get()
        quantity = data['Quantity'].get()
        id_ = self.__values[0]

        new_phone = Mobilephone(brand, name, storage, color, float(price), quantity, id_)
        new_phone.update_info()
        new_phone.speak()

        self.__destroy_edit_window()
        self.__create_treeview()
        self.__display_treeview()

    def __clear_button_handler(self):
        temp = list(self.__values[1:])
        data = self.__get_user_input()
        for textentry in data.values():
            textentry.delete(0, 'end')
            textentry.insert(0, temp.pop(0))
