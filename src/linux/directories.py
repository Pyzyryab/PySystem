import subprocess
class Directories:
    
    def __init__(self, action, path='/', *args, **kwargs):
        self.action = action
        self.path = path
        self.args = []
        self.set_args()

    def __str__(self):
        pass

    @classmethod
    def show_directories_options(cls):
        print('''
        [1] : List current directory files
        ''')
        return ''

    def set_args(self):
        action_switcher = {
            1 : ['ls', '-l'],
            2 : ['ls', '-la'],
        }

        self.args = [command for command in action_switcher.get(self.action)]
        if self.path != '':
            self.args.append(self.path)
        print(f'self.args -> {self.args}')
        return self.args

    def show_info(self):
        return subprocess.Popen(self.args)

# subprocess.call('ls')
# my_output = subprocess.run(['ls', '-l'], shell = True)
# subprocess.Popen(args)

# print(my_output)