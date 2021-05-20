import tkinter as tk

from view.sidebar import Sidebar
from view.winlog import WinLog

from controller.add import add_menu_handler
from controller.edit import edit_menu_handler
from controller.show import show_menu_handler
from controller.delete import delete_menu_handler

class ViewBase(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._root = master
        self._non_sidebar = tk.Frame(master).pack(fill=tk.X, side='left')

    def _display_default_windows(self):
        sidebar = Sidebar(self)
        sidebar.create_widgets([
            ('Add', add_menu_handler),
            ('Edit', edit_menu_handler),
            ('Show', show_menu_handler),
            ('Delete', delete_menu_handler)])
        sidebar.display_widgets()
        sidebar.pack(anchor='w', expand=True, fill=tk.X, side='left')

        WinLog(self._non_sidebar).pack()
