import tkinter as tk
from tkinter import ttk

from windows.sidebar import Sidebar
from windows.log import WinLog
from windows.base import WinBase
from windows.manager import WinManager

from models.mobilephone import Mobilephone
from models.database import Database

if __name__ == '__main__':
    root = tk.Tk()

    root.title("which group?'s phone-shop-ism")
    root.geometry(f'900x{root.winfo_screenheight()}+100+0')

    sidebar_frame = tk.LabelFrame(root, width=300, height=900, bd=10)
    functional_frame = tk.LabelFrame(root, width=880, height=600, bd=10, background='green')
    log_frame = tk.LabelFrame(root, width=880, height=300, bd=10)

    logbar = WinLog(log_frame)
    logbar.pack(expand=True, fill='both')

    sidebar = Sidebar(sidebar_frame)
    sidebar.create_widgets()
    sidebar.display_widgets()
    sidebar.pack(expand=True, fill='both')

    WinManager.set_master(functional_frame)
    WinManager.set_root(root)

    sidebar_frame.pack(expand=True, fill='both', side='left')
    functional_frame.pack(expand=True, fill='both', side='top')
    functional_frame.pack_propagate(0)
    log_frame.pack(expand=True, fill='both', side='bottom')

    Database.init('sample.db')

    root.mainloop()
