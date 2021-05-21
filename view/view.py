import tkinter as tk

from view.sidebar import Sidebar
from view.winlog import WinLog

class ViewBase(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._root = master
        self._non_sidebar = tk.Frame(master).pack(fill=tk.X, side='left')

    def set_handlers(self, handlers):
        pass


    def _display_default_windows(self):
        sidebar = Sidebar(self)
        sidebar.create_widgets([
            ('Add', add_menu_handler),
            ('Edit', edit_menu_handler),
            ('Show', show_menu_handler),
            ('Delete', delete_menu_handler),
            ('Quit', self._root.destroy)])
        sidebar.display_widgets()
        sidebar.pack(anchor='w', expand=True, fill=tk.X, side='left')

        WinLog(self._non_sidebar).pack()
