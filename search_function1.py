import sqlite3
import easygui as gui
import tabulate

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
            keys = ['Name:', 'Year:', 'Rating:', 'Length:', 'Genre:']
            format = 'fancy_grid'
            movie = [keys, movie[0]]
            table = tabulate.tabulate(movie, tablefmt = format)
            gui.msgbox(table)


        #    gui.msgbox(f'''
        #    Name   : {movie[0][0]}
        #    Year   : {movie[0][1]}
        #    Rating : {movie[0][2]}
        #    Length : {movie[0][3]}
        #    Genre  : {movie[0][4]}
        #    ''')

        else:
            print('Movie not found')
    #else then exits back to menu

if __name__ == '__main__':
    search_movies()