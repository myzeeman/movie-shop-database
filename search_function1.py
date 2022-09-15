import sqlite3
import easygui as gui

def search_movies():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()


    message = 'Please enter a movie name to search for'
    search = gui.enterbox(message)

    if (type(search) == str) and (len(search) > 0):
        c.execute('''SELECT * FROM movies WHERE name = ?''', [search])
        movie = c.fetchall()
        print(movie)

if __name__ == '__main__':
    search_movies()