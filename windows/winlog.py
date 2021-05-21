import time
import tkinter as tk
from tkinter import ttk

class WinLog(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Log'

        self.__create_widgets()
        self.__display_widgets()

        for i in range(10):
            self.update_log(i)

    def __create_widgets(self):
        self.__log = tk.Text(self, height=3)
        scr = ttk.Scrollbar(self, orient='vertical', command=self.__log.yview)
        self.__log['yscrollcommand'] = scr.set
    
    def __display_widgets(self):
        self.__log.pack(expand=True, fill=tk.BOTH)

    def update_log(self, message):
        self.__log['state'] = tk.NORMAL
        timestamp = time.strftime('[%F %T]')
        self.__log.insert('end', f'{timestamp} {message}\n')
        self.__log.see('end')
        self.__log['state'] = tk.DISABLED
