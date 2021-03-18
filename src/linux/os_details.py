from system.system_info import SystemInfo

from info.show_options import OS_info_options

class OperatingSystemInfo(SystemInfo):
    
    def __init__(self, action, *args, **kwargs):
        self.action = action

    @staticmethod
    def show_OS_info_options():
        print(f'''-> Now select one of the availiable options to work with {OperatingSystemInfo.__str__(OperatingSystemInfo)}\n''')
        for idx, category in OS_info_options.items():
            print(f'''      [{idx}] : {OS_info_options[idx]}''')
        return ''

    def show_info(self) -> ():
        if self.action == 1:
            return self.get_os_base_details()
        elif self.action == 2:
            return self.get_architecture_linkage()
    
    def get_os_base_details(self) -> str:
        print(f'''
        OS: {super().OS}, {super().OS_architecture}
        Release: {super().OS_release}
        Version: {super().OS_version}
        ''')
        return ''
    
    def get_architecture_linkage(self) -> str:
        print(f'''
        Architecture: {super().OS_arch_linkage[0]}
        Linkage: {super().OS_arch_linkage[1]}
        ''')
        return ''