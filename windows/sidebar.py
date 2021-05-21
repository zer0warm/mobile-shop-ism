import tkinter as tk

from windows.add import WinAdd

def add_handler(root):
    def callback():
        window = WinAdd(root)
        window.grid(row=0, column=1, rowspan=10)
    return callback

def quit_handler(root):
    def callback():
        root.destroy()
    return callback

class Sidebar(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__master = master
        self['text'] = 'Menu'

    def create_widgets(self):
        self.__entries = [
            tk.Button(self, width=20, command=add_handler(self.__master), text='Add'),
            tk.Button(self, width=20, command=add_handler(self.__master), text='Edit'),
            tk.Button(self, width=20, command=add_handler(self.__master), text='Show'),
            tk.Button(self, width=20, command=add_handler(self.__master), text='Delete'),
            tk.Button(self, width=20, command=quit_handler(self.__master), text='Quit')
        ]

    def display_widgets(self):
        for i in range(len(self.__entries)):
            self.__entries[i].grid(row=i, column=0)
