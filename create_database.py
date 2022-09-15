import sqlite3

conn = sqlite3.connect('movies.db') #connects to db which creates it

c = conn.cursor()

#creates table for movies with conditions needed
c.execute('''CREATE TABLE movies(name TEXT NOT NULL, 
                                 year INT CHECK(year > 1887 AND year < 2023),
                                 rating TEXT NOT NULL,
                                 length INT CHECK(length > 1 AND length < 1000),
                                 genre TEXT NOT NULL)''')

#list of movies with their data:
movies =   [['Ghostbusters',2016,'PG',116,'Comedy'],
            ['The Legend of Tarzan',2016,'PG',109,'Action'],
            ['Jason Bourne',2016,'PG',123,'Action'],
            ['The Nice Guys',2016,'R',116,'Crime'],
            ['The Secret Life of Pets',2016,'G',91,'Animation'],
            ['Star Trek Beyond',2016,'PG',120,'Action'],
            ['Batman v Superman',2016,'PG',151,'Action'],
            ['Finding Dory',2016,'G',103,'Animation'],
            ['Zootopia',2016,'G',108,'Animation'],
            ['The BFG',2016,'PG',90,'Fantasy'],
            ['A Monster Calls',2016,'PG',108,'Fantasy'],
            ['Independence Day: Resurgence',2016,'PG',120,'Action'],
            ['The Green Room',2016,'R',94,'Crime'],
            ['Doctor Strange',2016,'PG',130,'Fantasy'],
            ['The Jungle Book',2016,'PG',105,'Fantasy'],
            ['Alice Through the Looking Glass',2016,'PG',118,'Fantasy'],
            ['Imperium',2016,'R',109,'Crime'],
            ['The Infiltrator',2016,'R',127,'Crime'],
            ['Mad Max: Fury Road',2015,'R',120,'Action'],
            ['Spectre',2015,'PG',145,'Action'],
            ['Jurassic World',2015,'PG',100,'Action'],
            ['The Intern',2015,'PG',121,'Comedy'],
            ['Ted 2',2015,'R',121,'Comedy'],
            ['Trainwreck',2015,'R',122,'Comedy'],
            ['Inside Out',2015,'G',94,'Animation'],
            ['The Good Dinosaur',2015,'G',101,'Animation'],
            ['Divergent',2014,'PG',121,'Action'],
            ['The Max Runner',2014,'PG',115,'Action'],
            ['Birdman',2014,'R',119,'Comedy'],
            ['Guardians of the Galaxy',2014,'PG',121,'Fantasy'],
            ['The Lego Movie',2014,'PG',100,'Animation'],
            ['Big Hero 6',2014,'PG',108,'Animation'],
            ['The Drop',2014,'R',106,'Crime']]

#inserts each movie into database:
for i in movies:
    c.execute('''INSERT INTO movies VALUES(?,?,?,?,?)''', i)

#prints movies database to show that movies have been entered correctly:
c.execute('''SELECT rowid, * FROM movies''')
details = c.fetchall()
[print(i)for i in details]

#commits all changes to database so they are saved when program is closed.
conn.commit()