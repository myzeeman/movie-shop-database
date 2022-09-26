import easygui as gui
import main
import change_movie


def password():

    '''user is required to enter a password to access the database'''

    password = 'admin'

    while True:

        message = 'Please enter the password to access the program'
        user_password = gui.passwordbox(message)

        if password == user_password:
            break
        
        else:
            message = 'Password incorrect, try again or exit'
            choices = ['Try again', 'Exit']
            response = gui.buttonbox(message, choices = choices)

            if response == 'Exit' or response == None:
                exit()
            
if __name__ == '__main__':
    password()
  