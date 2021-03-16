from py_system import PySystem

from info.show_options import categories

if __name__ == '__main__':

    task = PySystem()

    while True:
        chose_category = input('-> Please, enter a number: \n     ')
        try:
            chose_category = int(chose_category)
            break
        except:
            print('Select a valid option to continue')

        finally:
            print(f'You selected -> {categories[chose_category]}')

    task.perform_action(chose_category)
    

