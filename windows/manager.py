from windows.base import WinBase
from windows.add import WinAdd
from windows.show import WinShow
from windows.edit import WinEdit
from windows.delete import WinDelete
from windows.status import WinStatus
from windows.log import WinLog

class WinManager:
    __active = None
    __root = None
    __master = None
    __window_maps = {'add': WinAdd, 'show': WinShow,
                     'edit': WinEdit, 'delete': WinDelete,
                     'status': WinStatus}

    @staticmethod
    def set_root(root):
        WinManager.__root = root

    @staticmethod
    def set_master(master):
        WinManager.__master = master

    @staticmethod
    def create_window(winstr):
        newwin = WinManager.__window_maps[winstr](WinManager.__master)
        WinManager.switch_window(newwin)
        WinLog.update_log(f'Switched to window <{winstr}>.')

    @staticmethod
    def switch_window(dest):
        if WinManager.__active:
            WinManager.__active.destroy()
        WinManager.__active = dest
        WinManager.__active.pack(expand=True, fill='both', side='top')

    @staticmethod
    def destroy_everything():
        WinManager.__root.destroy()
