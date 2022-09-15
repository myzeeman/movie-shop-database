import sqlite3

conn = sqlite3.connect('movies.db') #connects to db which creates it

c = conn.cursor()

#creates table for movies with conditions needed
c.execute('''CREATE TABLE movies(name TEXT NOT NULL, 
                                 year INT CHECK(year > 1887 AND year < 2023),
                                 rating TEXT NOT NULL,
                                 length INT CHECK(length > 1 AND length < 1000),
                                 genre TEXT NOT NULL)''')
