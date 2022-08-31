import easygui as gui

def menu():
    options = ['Show Table', 'Print Table', 'New Movie', 'Change Movie',
    'Delete Movie', 'Search Movies', 'Exit']
    msg = 'Please choose an option'
    title = 'Menu'
    user_input = gui.buttonbox(msg, title, options)



if __name__ == '__main__':
    menu()