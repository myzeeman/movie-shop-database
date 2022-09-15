from tabulate import *
import easygui as gui
import sqlite3 as sql


def print_table():

    '''Shows all movies in a table '''

    #connects to database so that all data can be gathered:
    conn = sql.connect('movies.db')
    c = conn.cursor()
    c.execute('''SELECT rowid, * FROM movies''')
    movie_details = c.fetchall()
    
    #list keys for top of table:
    feilds = ['#', 'Name', 'Release year', 'Rating', 'Length', 'Genre']

    #puts feilds list at front of list
    movie_details.insert(0, feilds)

    #If statement is true if there is one or more movie:
    if len(movie_details) > 1:

        format = 'fancy_grid'
        table = tabulate(movie_details, tablefmt = format)
        gui.textbox(table)
    
    else:
        gui.msgbox('there are no movies to display')

#if statement for testing
if '__main__' == __name__:
    print_table()   