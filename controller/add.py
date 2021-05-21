class CtrlAdd:
    def __init__(self, view_object=None):
        self.__view_object = view_object

    def render(self):
        self.__view_object.pack()

    def add_button_handler(self):
        data = self.__view_object.get_window().get_user_input()
        print(data)
        # validation -> add details to Mobilephone -> interact with database

    def clear_button_handler(self):
        pass
