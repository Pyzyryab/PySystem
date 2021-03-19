import platform
import subprocess

from os.path import expanduser

class SystemInfo:
    '''Base class to gathering info and "encapsulate it", and provide it to 
    any another class as a static way to access it.
    '''
    OS = platform.system()
    OS_release = platform.release()
    OS_version = platform.version()
    OS_architecture = platform.architecture()[0]
    OS_arch_linkage = platform.architecture()[1]

    # libc type and version
    libc_type = platform.libc_ver()[0]
    libc_version = platform.libc_ver()[1]

    # Request user linux home path
    linux_user_home_directory = expanduser("~")

    # Python details
    python_detected = False

    def _retrive_python_info(self):
        '''
        Returns a tuple with all availiable info about if Python is found
        on the OS that makes the question
        '''
        if platform.python_version() != '':

            SystemInfo.python_detected = True

            return (
            platform.python_version(),
            platform.python_implementation(),
            platform.python_revision(),
            platform.python_build()[0],
            platform.python_build()[1],
            platform.python_compiler()
            )
    
    @classmethod
    def python_info(cls):  
        '''
        Formatted version of retrieved data with _retrieve_python_info
        '''
        py_version, py_impl, py_rev, py_build, py_build_date, py_compiler = SystemInfo._retrive_python_info(SystemInfo) #should pass cls reference on self parameter

        checked_py_values = [value if value != '' else 'No info availiable' for value in SystemInfo._retrive_python_info(SystemInfo)]
        py_names = [
        'Python version', 'Python implementation', 'Python revision', 
        'Python build branch', 'Python build date', 'Python compiler'
        ]

        if not SystemInfo.python_detected:
            print(f'''
            No Python instalation detected on your operating system
            ''')
        else:
            for idx, element in enumerate(py_names):
                print(f'''      {py_names[idx]}: {checked_py_values[idx]}''')
    