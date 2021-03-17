from system.py_system import PySystem

from info.show_options import categories

from linux.directories import Directories

if __name__ == '__main__':

    task = PySystem()

    while True:
        chose_category = input('-> Enter a number to select a category: ')
        try:
            chose_category = int(chose_category)
            break
        except:
            print('Select a valid option to continue')

    print(f'\nYou selected -> {categories[chose_category]}')

    # Block to handle what category instanciate
    if chose_category == 2:
        Directories.show_directories_options()
    
    print(f'\nYou selected -> {categories[chose_category]}')

    # Block to get an action of the desired category
    while True:
        chose_option = input('-> Enter a number to select an option: ')
        try:
            chose_option = int(chose_option)
        except:
            print('Select a valid option to continue')

    # Finally, we use our instance to get the result
    task.perform_action(chose_category, chose_option)
    

