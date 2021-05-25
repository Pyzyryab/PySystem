from system.system_info import SystemInfo

from linux.directories import Directories
from linux.os_details import OperatingSystemInfo
from linux.processes import Processes

from info.zerodaycode import ZeroDayCode
from info.show_options import categories

class PySystem:

    current_OS = getattr(SystemInfo, 'OS')
    current_user_path = getattr(SystemInfo, 'user_home_directory')

    class InvalidCategory:
        '''Base exception for invalid user input on prompt'''
        pass

    def __init__(self, *args, **kwargs):
        print(self._greet())

    def __str__(self):
        return f'{ZeroDayCode.app_name}, version: {ZeroDayCode.PySystem_version}'
    
    def _greet(self):
        return f'\nHello. Welcome to \'{self.__str__()}\'. A command line tool for manage your GNU/Linux system.\n'
    
    def _choose_category_warning(self) -> str:
        print('Message: Choose one of the availiable categories:\n')
        for idx, category in categories.items():
            print(f'''      [{idx}] : {categories[idx]}''')
        return ''

    def perform_action(self, category, action):
        '''This methods works as a fake switch implementation (Python does not
        have switch statement) in order to choose a class (based on what action users wants to get INFO) 
        and asign it to an instance.
        Every class will have a method called 'SHOW INFO' and this will be dynamically
        selected with the fake switch.
        This aproach allocates all clases on memory on the very first time, optimizing the OOP aproach, which is usually slow as opossite of the procedural
        way. Fake switch (just a dict) is much faster than make several if/else checks, and now every time an action in required
        everything is ready at-a-moment-call.
        '''

        if PySystem.current_OS == 'Linux':
            linux_switcher = {
                0 : self.__str__(),
                1 : OperatingSystemInfo(action),
                2 : Directories(action, 
                    current_user_path=PySystem.current_user_path),
                3 : Processes(),
            }
            selection = linux_switcher.get(category, 0)
            print(f'Selection is: {selection}, category is: {category}, action is: {action}, len linx sw is: {len(linux_switcher)}')
            return selection.show_info()

        elif PySystem.current_OS == 'Windows':
            windows_switcher = {
                0 : self.__str__(),
                1 : OperatingSystemInfo(action),
                2 : Directories(action, 
                    current_user_path=PySystem.current_user_path),
                # 3 : ''
            }
            selection = windows_switcher.get(category, lambda action : 0 if len(windows_switcher) > action else action)
            return selection.show_info()

