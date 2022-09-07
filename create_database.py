import sqlite3

conn = sqlite3.connect('movies.db')

c = conn.cursor()

c.execute('''CREATE TABLE movies(name TEXT,
                                 year INT,
                                 length INT,
                                 rating TEXT,
                                 genre TEXT)''')