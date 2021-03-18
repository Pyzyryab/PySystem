import time

from system.py_system import PySystem

from info.show_options import categories

from linux.directories import Directories
from linux.os_details import OperatingSystemInfo

if __name__ == '__main__':

    task = PySystem()

    def chose_category() -> int:
        while True:
            category = input('\n-> Enter a number to select a category: ')
            try:
                category = int(category)
                break
            except:
                print('Select a valid option to continue')
        return category

    # Block to get an action of the desired category
    def chose_option() -> int:
        while True:
            option = input('\n-> Enter a number to select an option: ')
            try:
                option = int(option)
                break
            except:
                print('Select a valid option to continue')
        return option
    
    def main(past_category=0, same_category=False):
        if same_category:
            if past_category == 1:
                OperatingSystemInfo.show_OS_info_options()
            elif past_category == 2:
                Directories.show_directories_options()
            option = chose_option()

            task.perform_action(past_category, option)
            return (past_category, option)
            
        else:
            task._choose_category_warning()
            category = chose_category()
            print(f'\nYou selected -> {categories[category]}')
        
        # Block to handle what category instanciate
            if category == 1:
                OperatingSystemInfo.show_OS_info_options()
            elif category == 2:
                Directories.show_directories_options()
            
            option = chose_option()

            task.perform_action(category, option)
            return (category, option)
        
    #Initiate the program execution and save return values destructuring the returned tuple
    current_category, current_option = main()

    while True:
        again = input('Do you want to perform another action? Y/n: ')
        
        if again == 'Y' or again == 'y':
            change_category = input('In this category, or want to go back and choose category again? Y/n: ')
            if change_category == 'Y' or change_category == 'y':
                print(f'Current category on CHANGE CAT == Y -> {current_category} ')
                current_category, current_option = main(past_category=current_category, same_category=True)
            elif change_category == 'N' or change_category == 'n':
                print(f'Current category on CHANGE CAT == N -> {current_category} ')
                current_category, current_option = main(same_category=False)
            else:
                print('Please, select a valid option to continue')

        elif again == 'N' or again == 'n':
            break
        else:
            print('Please, select a valid option to continue')

        
    

