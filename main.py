import tkinter as tk
from tkinter import ttk

import view.sidebar as sb
import view.winlog as log

if __name__ == '__main__':
    root = tk.Tk()

    root.title("which group?'s phone-shop-ism")
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0')

    logbar = log.WinLog(root)
    logbar.grid(row=10, column=1, columnspan=5)

    sidebar = sb.Sidebar(root)
    sidebar.create_widgets()
    sidebar.display_widgets()
    sidebar.grid(row=0, column=0, rowspan=10, sticky='nsew')
    
    root.mainloop()
