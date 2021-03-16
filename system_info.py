import platform

class SystemInfo:

    current_OS = platform.system()
    current_OS_release = platform.release()
    current_OS_version = platform.version()