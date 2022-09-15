import sqlite3
import easygui as gui

def delete():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()
    movie_names = [i[0] for i in movies]

    message = '''Please choose an item to delete or click 'cancel' to exit'''
    title = 'Delete menu'
    movie_choice = gui.choicebox(msg = message, title = title, choices = movie_names)
    print(movie_choice)

if '__main__' == __name__:
    delete()