import sqlite3
import easygui as gui

def delete_movie():

    '''Asks user what movie to delete and removies it from database'''

    #connects to database and selects all movies:
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('SELECT * FROM movies')

    #puts all movies in a list
    movies = c.fetchall()

    #List comprehension to put all movie names in a list
    movie_names = [i[0] for i in movies]
    
    #is none so that program will exit if user does not choose an option or less than 2 movies
    movie_choice = None

    #gui choicebox cannot display less than two items
    if len(movie_names) > 1:
        #choice box for user to choose movie to delete:
        message = '''Please choose an item to delete or click 'cancel' to exit'''
        title = 'Delete menu'
        movie_choice = gui.choicebox(msg = message, title = title, choices = movie_names)
    
    #error message for less than two movies error
    else:
        message = (f'There are {len(movie_names)} and there is a minimum of 2 \n' +
                    'program will exit back to menu')
        gui.msgbox(message)

    #if user doesnt choose a movie then function exits back to menu
    if not(movie_choice == None):
        c.execute('''DELETE FROM movies WHERE name = ?''', [movie_choice])
        conn.commit()

#for testing purposes:
if '__main__' == __name__:
    delete_movie()