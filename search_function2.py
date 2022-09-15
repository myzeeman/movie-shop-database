import easygui as gui
import sqlite3

def search_movies():

    '''Asks user to search for a movie and displays result'''

    #connecting to database
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    #gathering all movie data from database
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()

    #asking user to search for a movie
    message = ('Please enter a movie name to search for \n'+
              'or click cancel to exit')
    search = gui.enterbox(message)

    #gathers all names from list of movies, makes list for easy searching:
    names = [i[0] for i in movies]
    
    #if user clicks cancel than exits back to menu
    if not(search == None):
        if search in names:
            print(movies[names.index(search)])

        else:
            print('Movie not found')

if __name__ == '__main__':
    search_movies()