from system.system_info import SystemInfo
from linux.directories import Directories
from info.zerodaycode import ZeroDayCode
from info.show_options import categories

class PySystem:

    current_OS = getattr(SystemInfo, 'current_OS')

    def __init__(self, *args, **kwargs):
        print(self._greet())
        print(self._choose_category_warning())

    def __str__(self):
        return f'{ZeroDayCode.app_name}, version: {ZeroDayCode.PySystem_version}'
    
    def _greet(self):
        return f'\nHello. Welcome to \'{self.__str__()}\'. A command line tool for manage your GNU/Linux system.\n'
    
    def _choose_category_warning(self) -> str:
        print('Choose one of the availiable categories:\n')
        for idx, category in categories.items():
            print(f'''      [{idx}] : {categories[idx]}''')
        return ''

    def perform_action(self, category, action=1):
        '''This methods works as a fake switch implementation (Python does not
        have switch statement) in order to choose a class (based on what action users wants to get INFO) 
        and asign it to an instance.
        Every class will have a method called 'SHOW INFO' and this will be dynamically
        selected with the fake switch.
        This aproach saves memory and optimizes the OOP aproach, which is usually slow as opossite of the procedural
        way. Fake switch (just a dict) is much faster than make several if/else checks, and just ONE
        class is allocated on memory when an action is required.
        '''
        if PySystem.current_OS == 'Linux':
            linux_switcher = {
                0 : self.__str__(),
                # 1 : list_files(),
                2 : Directories(action)
            }
            selection = linux_switcher.get(category, lambda: 0)
            return selection.show_info()
            # return linux_switcher.get(category, lambda: 0), PySystem.current_OS
        
        # Future implementation on WINDOWS as windows_switcher
