import subprocess

from info.show_options import directories_options

class Directories:
    
    def __init__(self, action, path='$HOME', *args, **kwargs):
        self.action = action
        self.path = path
        self.args = []
        self.set_args()

    def __str__(self) -> str:
        return 'directories'

    @staticmethod
    def show_directories_options():
        print(f'''-> Now select one of the availiable options to work with {Directories.__str__(Directories)}\n''')
        for idx, category in directories_options.items():
            print(f'''      [{idx}] : {directories_options[idx]}''')
        return ''

    def set_args(self) -> list:
        action_switcher = {
            1 : ['ls'],
            2 : ['ls', '-a'],
            3 : ['ls', '-lth'], #long format, human readable
            4 : ['ls', '-lta'], #long format, hidden files
        }

        self.args = [command for command in action_switcher.get(self.action)]
        if self.path != '':
            self.args.append(self.path)
        print(f'self.args -> {self.args}')
        return self.args

    def show_info(self):
        return subprocess.Popen(self.args)
