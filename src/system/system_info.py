import platform
import subprocess

from os.path import expanduser

class SystemInfo:
    '''Base class to gathering info and "encapsulate it", and provide it to 
    any another class as an static way to access it.
    '''

    OS = platform.system()
    OS_release = platform.release()
    OS_version = platform.version()
    OS_architecture = platform.architecture()[0]
    OS_arch_linkage = platform.architecture()
    
    linux_user_home_directory = expanduser("~")