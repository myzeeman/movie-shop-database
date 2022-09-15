import sqlite3
import easygui as gui

def delete():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()
    movie_names = [i[0] for i in movies]
    print(movie_names)

if '__main__' == __name__:
    delete()