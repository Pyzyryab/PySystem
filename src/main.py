import time

from system.py_system import PySystem

from info.show_options import categories
from info.show_options import OS_info_options
from info.show_options import directories_options

from linux.directories import Directories
from linux.os_details import OperatingSystemInfo

if __name__ == '__main__':

    task = PySystem()

    def chose_category() -> int:
        valid_category = lambda x : x if x > 0 and x <= len(categories) else False

        while True:
            category = input('\n-> Enter a number to select a category: ')
            try:
                category = int(category)

                if not valid_category(category):
                    print('-> Error: Number not allowed. ')
                else:
                    break

            except:
                print('Select a valid option to continue')
        
        return category

    # Block to get an action of the desired category
    def chose_option(category) -> int:
        if category == 1:
            options = OS_info_options
        elif category == 2:
            options = directories_options

        valid_option = lambda x : x if x > 0 and x <= len(options) else False

        while True:
            option = input('\n-> Enter a number to select an option: ')
            try:
                option = int(option)

                if not valid_option(option):
                    print('-> Error: Number not allowed. ')
                else:
                    break

            except:
                print('Select a valid option to continue')
        
        return option

    def choose_cls_info(category):
        if category == 1:
            OperatingSystemInfo.show_OS_info_options()
        elif category == 2:
            Directories.show_directories_options()

        return category
    
    def main(past_category=0, same_category=False):
        if same_category:
            print('\n')
            choose_cls_info(past_category)
            option = chose_option(past_category)

            task.perform_action(past_category, option)
            return (past_category, option)
            
        else:
            task._choose_category_warning()
            category = chose_category()
            print(f'\nYou selected -> {categories[category]}')
        
            choose_cls_info(category)
            option = chose_option(category)

            task.perform_action(category, option)
            return (category, option)
        
    #Initiate the program execution and save return values destructuring the returned tuple
    current_category, current_option = main()
    time.sleep(0.1)

    while True:
        again = input('\nDo you want to perform another action? Y/n: ')
        
        if again == 'Y' or again == 'y':
            change_category = input('In this category(Y), or choose category again(N)? Y/n: ')
            if change_category == 'Y' or change_category == 'y':              
                current_category, current_option = main(past_category=current_category, same_category=True)
                time.sleep(0.1)
            elif change_category == 'N' or change_category == 'n':
                current_category, current_option = main(same_category=False)
                time.sleep(0.1)
            else:
                print('Please, select a valid option to continue')

        elif again == 'N' or again == 'n':
            break
        else:
            print('Please, select a valid option to continue')

        
    
