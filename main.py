import tkinter as tk
from tkinter import ttk

from view.view import ViewBase

if __name__ == '__main__':
    root = tk.Tk()

    root.title("wg's phone-shop-ism")
    root.geometry('1200x1000')

    ViewBase(root).pack()

    root.mainloop()
