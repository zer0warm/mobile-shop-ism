from view.view import ViewBase

class WinMainscreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def create_widgets(self):
        pass

    def display_widgets(self):
        pass

class ViewMainscreen(ViewBase):
    def __init__(self, master):
        super().__init__(master)
        self.create_mainscreen_window()
        self.display_mainscreen_window()
        self._display_default_windows()

    def create_mainscreen_window(self):
        self._window = WinMainscreen(self)
        self._window['width'] = 400
        self._window.create_widgets()

    def display_mainscreen_window(self):
        self._window.display_widgets()
        self._window.pack(side='left')
