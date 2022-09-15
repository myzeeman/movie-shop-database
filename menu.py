import easygui as gui
from veiw_table import *
from delete_movie import *
from search_function1 import *

def menu():

    '''menu function for user to choose what to do to the database'''

    #constant variables for gui button box:
    options = ['Print Table', 'New Movie', 'Change Movie',
    'Delete Movie', 'Search Movies', 'Exit']
    msg = 'Please choose an option'
    title = 'Menu'
    #gui button box for main menu gui:
    user_input = gui.buttonbox(msg, title, options)
    #print(user_input) print statement for testing

    #runs chosen function:
    if user_input == options[0]:
        print_table()

    elif user_input == options[1]:
        new_movie()

    elif user_input == options[2]:
        change_movie()

    elif user_input == options[3]:
        delete_movie()

    elif user_input == options[4]:
        search_movies()

    elif user_input == options[5]:
        exit()
    
    menu()


if __name__ == '__main__':
    menu()