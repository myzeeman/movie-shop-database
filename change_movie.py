import sqlite3
import easygui as gui

def change_movie():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('''SELECT name FROM movies''')
    names = c.fetchall()
    names = [i[0] for i in names]
    print(names)


if __name__ == '__main__':
    change_movie()