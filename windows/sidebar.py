import tkinter as tk

from models.database import Database
from windows.manager import WinManager
from windows.log import WinLog

def handler(master, winstr):
    def callback():
        WinLog.update_log(f'<{winstr}> button pressed.')
        if winstr == 'populate':
            Database.execute(scripting=True, scriptfile='sample.sql')
            WinLog.update_log('Database: Populated data using <sample.sql>')
        else:
            WinManager.create_window(winstr)
    return callback

def quit_handler():
    Database.close()
    WinManager.destroy_everything()

class Sidebar(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__master = master

    def create_widgets(self):
        self.__entries = [
            tk.Button(self, command=handler(self.__master, 'add'), text='ADD'),
            tk.Button(self, command=handler(self.__master, 'edit'), text='EDIT'),
            tk.Button(self, command=handler(self.__master, 'show'), text='SHOW'),
            tk.Button(self, command=handler(self.__master, 'delete'), text='DELETE'),
            tk.Button(self, command=handler(self.__master, 'populate'), text='IMPORT'),
            tk.Button(self, command=quit_handler, text='QUIT')
        ]

    def display_widgets(self):
        for i in range(len(self.__entries)):
            self.__entries[i].pack(expand=True, fill='both')
