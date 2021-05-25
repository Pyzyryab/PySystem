import subprocess
import time

from system.system_info import SystemInfo

from info.show_options import processes_options

class Processes:
    '''Show info about the processes status currently running in the OS'''

    def __init__(self):
        pass

    @staticmethod
    def show_processes_availiable_options():
        print(f'''-> Now select one of the availiable options:\n''')
        for idx, category in processes_options.items():
            print(f'''      [{idx}] : {processes_options[idx]}''')
        return ''

    @classmethod
    def show_info(cls):
        subprocess.Popen('clear')
        Processes.show_warning_and_use_top()

    @classmethod
    def show_warning_and_use_top(cls):
        subprocess.Popen(['echo', '-e', '\n'])
        subprocess.Popen(['echo', 'After showing the information, you can leave the program pressing the \'Enter\' key...'])
        time.sleep(3)
        subprocess.Popen(['top', '-n', '1'])