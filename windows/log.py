import time
import tkinter as tk
from tkinter import ttk

class WinLog(tk.LabelFrame):
    __log = None

    def __init__(self, master):
        super().__init__(master)

        self.__create_widgets()
        self.__display_widgets()

    def __create_widgets(self):
        WinLog.__log = tk.Text(self, height=5)
        scr = ttk.Scrollbar(self, orient='vertical', command=WinLog.__log.yview)
        WinLog.__log['yscrollcommand'] = scr.set
    
    def __display_widgets(self):
        WinLog.__log.pack(expand=True, fill=tk.BOTH)

    @staticmethod
    def update_log(message):
        WinLog.__log['state'] = tk.NORMAL
        timestamp = time.strftime('[%F %T]')
        WinLog.__log.insert('end', f'{timestamp} {message}\n')
        WinLog.__log.see('end')
        WinLog.__log['state'] = tk.DISABLED

    #@staticmethod
    #def update_log_tkinter(*args):
    #    WinLog.__log['state'] = tk.NORMAL
    #    timestamp = time.strftime('[%F %T]')
    #    WinLog.__log.insert('end', f'{timestamp} Error {dir(args[1])}\n')
    #    WinLog.__log.see('end')
    #    WinLog.__log['state'] = tk.DISABLED
