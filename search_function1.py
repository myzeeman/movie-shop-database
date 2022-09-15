import sqlite3
import easygui as gui

def search_movies():
    '''Asks user to search for a movie and displays result'''

    #connecting to database
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    #asks for useer to search for a movie
    message = ('Please enter a movie name to search for \n'+
              'or click cancel to exit')
    search = gui.enterbox(message)

    #if input is a string and is longer than 0 characters then checks for movie in db
    if (type(search) == str) and (len(search) > 0):
        c.execute('''SELECT * FROM movies WHERE name = ?''', [search])
        movie = c.fetchall()

        if len(movie) > 0:
            print(movie)

        else:
            print('Movie not found')
    #else then exits back to menu

if __name__ == '__main__':
    search_movies()