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

    # Request user home path
    user_home_directory = expanduser("~")
    if OS == 'Windows':
        user_home_directory += user_home_directory + '\\Desktop'
    

    # Python details
    python_detected = False

    def _retrive_python_info(self):
        '''
        Returns a tuple with all availiable info about if Python is found
        on the OS currently running
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
    
    # Java details
    java_detected = False

    def _retrive_java_info(self):
        '''
        The call from java_ver() returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).
        '''
        java_info = platform.java_ver()

        if java_info[0] != '':

            SystemInfo.java_detected = True

            return (
            java_info[0], #java_release
            java_info[1], #java_vendor
            java_info[2][0], #java_vm_name
            java_info[2][1], #java_vm_release
            java_info[2][2], #java_vm_vendor
            )
        
        # else:
        #     return ''

    @classmethod
    def java_info(cls):  
        '''
        Formatted version of retrieved data with _retrieve_python_info
        '''
        if not SystemInfo.java_detected:
            print(f'No JAVA instalation detected on your operating system')
        else:
            java_release, java_vendor, java_vm_name, java_vm_release, java_vm_vendor = SystemInfo._retrive_java_info(SystemInfo) #should pass cls reference on self parameter

            checked_java_values = [value if value != '' else 'No info availiable' for value in SystemInfo._java_info(SystemInfo)]
            java_names = [
            'Java release', 'Java vendor', 'Java VM name', 
            'Java VM release', 'Java VM vendor',
            ]
            
            for idx, element in enumerate(java_names):
                print(f'''      {java_names[idx]}: {java_names[idx]}''')