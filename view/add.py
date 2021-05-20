import tkinter as tk

from view.view import ViewBase
from controller.add import add_button_handler, cancel_button_handler

class WinAdd(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__widgets = []
    
    def create_widgets(self, fields):
        for entry in fields:
            self.__widgets.append((tk.Label(self, text=entry), tk.Entry(self)))
        self.__add_button = tk.Button(text='Add', command=add_button_handler)
        self.__cancel_button = tk.Button(text='Cancel', command=cancel_button_handler)

    def display_widgets(self):
        for i in range(len(self.__widgets)):
            label, textentry = self.__widgets[i]
            label.grid(row=i, column=0)
            textentry.grid(row=i, column=1)

class ViewAdd(ViewBase):
    def __init__(self, master):
        super().__init__(master)
        self._create_add_window()
        self._display_add_window()
        self._display_default_windows()
    
    def _create_add_window(self):
        self._window = WinAdd(self)
        self._window.create_widgets(
                ['Brand', 'Name', 'Storage', 'Color', 'Price', 'Quantity'])

    def _display_add_window(self):
        self._window.display_widgets()
        self._window.pack(anchor='n')
