from tabulate import *
import easygui as gui
import sqlite3 as sql


def print_table():

    '''prints all movies as a table'''

    conn = sql.connect('movies.db')
    c = conn.cursor()
    c.execute('''SELECT rowid, * FROM movies''')
    movie_details = c.fetchall()
    
    feilds = ['#', 'Name', 'Release year', 'Rating', 'Length', 'Genre']
    movie_details.insert(0, feilds)

    if len(movie_details) > 1:

        format = 'fancy_grid'
        table = tabulate(movie_details, tablefmt = format)
        print(table)
    
    else:
        print('there are no movies to display')


if '__main__' == __name__:
    print_table()   