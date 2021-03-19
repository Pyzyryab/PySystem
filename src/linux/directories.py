import subprocess

from info.show_options import directories_options

class Directories:
    
    def __init__(self, action, path='', *args, **kwargs):
        self.current_user_path = kwargs['current_user_path']
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
        '''Given the action parameter -> type(action) == int
        returns a list where list[0] is the command and list[1:] are 
        the flags and options
        '''
        action_switcher = {
            0 : ['echo', 'PySystem is amazing!'],
            1 : ['ls'],
            2 : ['ls', '-a'],
            3 : ['ls', '-lth'], #long format, human readable
            4 : ['ls', '-lta'], #long format, hidden files
        }

        self.args = [command for command in action_switcher.get(self.action, action_switcher.get(0))]
        
        if self.path != '':
            self.args.append(self.path)
        else:
            self.args.append(self.current_user_path)
        
        return self.args

    def show_info(self):
        return subprocess.Popen(self.args)