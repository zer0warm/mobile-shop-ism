import tkinter as tk

from model.mobilephone import Mobilephone

def add_button_handler(data):
    def callback():
        brand = data['Brand'].get()
        name = data['Name'].get()
        storage = data['Storage'].get()
        color = data['Color'].get()
        price = data['Price'].get()
        quantity = data['Quantity'].get()
        new_phone = Mobilephone(brand, name, storage, color, price)
        print(new_phone.speak())
    return callback

def clear_button_handler(data):
    def callback():
        for textentry in data.values():
            textentry.delete(0, 'end')
    return callback

class WinAdd(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Add new mobile phone'
        self.create_widgets()
        self.display_widgets()

    def create_widgets(self):
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
                command=add_button_handler(self.get_user_input()))
        self.__clear_button = tk.Button(
                self,
                text='Clear',
                command=clear_button_handler(self.get_user_input()))

    def display_widgets(self):
        for i in range(len(self.__widgets)):
            label, textentry = self.__widgets[i]
            label.grid(row=i, column=0)
            textentry.grid(row=i, column=1, columnspan=5)
        self.__add_button.grid(row=i+1, column=4)
        self.__clear_button.grid(row=i+1, column=5)

    def get_user_input(self):
        data = {}
        for label, textentry in self.__widgets:
            data[label['text']] = textentry
        return data
