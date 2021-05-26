import tkinter as tk

from models.mobilephone import Mobilephone

class WinAdd(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Add new mobile phone'
        self.__create_widgets()
        self.__display_widgets()

    def __create_widgets(self):
        self.__widgets = [
            (tk.Label(self, text='Brand'), tk.Entry(self)),
            (tk.Label(self, text='Name'), tk.Entry(self)),
            (tk.Label(self, text='Storage'), tk.Entry(self)),
            (tk.Label(self, text='Color'), tk.Entry(self)),
            (tk.Label(self, text='Price'), tk.Entry(self)),
            (tk.Label(self, text='Quantity'), tk.Entry(self))
        ]
        self.__add_button = tk.Button(
                self,
                text='Add',
                command=self.__add_button_handler)
        self.__clear_button = tk.Button(
                self,
                text='Clear',
                command=self.__clear_button_handler)

    def __display_widgets(self):
        for i in range(len(self.__widgets)):
            label, textentry = self.__widgets[i]
            label.grid(row=i, column=0)
            textentry.grid(row=i, column=1, columnspan=5)
        self.__add_button.grid(row=i+1, column=4, sticky='nsew')
        self.__clear_button.grid(row=i+1, column=5, sticky='nsew')

    def __get_user_input(self):
        data = {}
        for label, textentry in self.__widgets:
            data[label['text']] = textentry
        return data

    def __add_button_handler(self):
        data = self.__get_user_input()

        brand = data['Brand'].get()
        name = data['Name'].get()
        storage = data['Storage'].get()
        color = data['Color'].get()
        price = data['Price'].get()
        quantity = data['Quantity'].get()

        new_phone = Mobilephone(brand, name, storage, color, float(price), quantity)
        new_phone.speak()
        new_phone.export_info()

    def __clear_button_handler(self):
        data = self.__get_user_input()
        for textentry in data.values():
            textentry.delete(0, 'end')
