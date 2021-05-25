import time

from system.py_system import PySystem

from info.show_options import categories
from info.show_options import OS_info_options
from info.show_options import directories_options
from info.show_options import processes_options

from linux.os_details import OperatingSystemInfo

from linux.directories import Directories
from linux.processes import Processes


if __name__ == '__main__':

    task = PySystem()

    def chose_category() -> int:
        '''get the category to work with'''
        
        valid_category = lambda x : x if x > 0 and x <= len(categories) else False

        while True:
            category = input('\n-> Enter a number to select a category: ')
            try:
                category = int(category)

                if not valid_category(category):
                    print('-> Error: Number not allowed. ')
                else:
                    break

            except PySystem.InvalidCategory:
                print('Select a valid option to continue')
        
        return category

    def chose_option(category) -> int:
        '''Get an action of the desired category'''

        if category == 1:
            options = OS_info_options
        elif category == 2:
            options = directories_options
        elif category == 3:
            options = processes_options

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
        '''Shows the availiable options on a category'''
        if category == 1:
            OperatingSystemInfo.show_OS_info_options()
        elif category == 2:
            Directories.show_directories_options()
        elif category == 3:
            Processes.show_processes_availiable_options()
        return category
    
    # MAIN
    def main(past_category=0, same_category=False):
        '''
        Entry point of the program. Execute calls to perform the given actions
        provided by the user. With the input parameters, we can handle the flow to
        let the user choose next action. This runtime is controlled by the while loop 
        at the botton of this main.py file.
        '''

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
        
    #Initiate the program execution and save values destructuring the returned tuple
    # Primary flow control works as a do - while loop.
    current_category, current_option = main()
    time.sleep(0.1)

    while True:
        if current_category == 3:
            break
        else:
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

        
    
