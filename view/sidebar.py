import tkinter as tk
import sys

from controller.add import add_menu_handler
from controller.edit import edit_menu_handler
from controller.show import show_menu_handler
from controller.delete import delete_menu_handler

class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.__entries = []

    def create_widgets(self, menu):
        for entry, handler in menu:
            btn = tk.Button(self, text=entry, width=20, command=handler)
            self.__entries.append(btn)

    def display_widgets(self):
        for entry in self.__entries:
            if entry['text'] == 'Quit':
                entry.pack(anchor='s', fill=tk.X)
            else:
                entry.pack(fill=tk.X)
