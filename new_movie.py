import easygui as gui
import sqlite3
import datetime


def new_movie():

    '''allows user to add a new movie to database'''
    #connecting to database so that new movie can be saved
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    #list of all data for new movie
    movie = []

    #Name entering with error checking
    message = 'Please input the name of the movie'
    while len(movie) < 1:
        name = gui.enterbox(message)

        if name == None or len(name) < 1:
            message = 'Please re input the name of the movie'

        else:
            movie.append(name)

    #Entering age of movie with easy guis integer box error checking
    message = 'Please input the year the movie was made'
    while len(movie) < 2:
        default = 2022
        lowerbound = 1887
        upperbound = 2023
        age = gui.integerbox(
            message, default = default, lowerbound = lowerbound, upperbound = upperbound
                            )
        
        if len(str(age)) > 0:
            movie.append(age)

    #entering age rating, with error checking
    message = 'Please choose the rating of the movie'
    while len(movie) < 3:
        choices = ['G', 'PG', 'R']
        rating = gui.choicebox(message, choices = choices)
        if rating in choices:
            movie.append(rating)

        else:
            message = 'Please re choose the rating of the movie'

    #entering length of movie with integerbox error checking
    while len(movie) < 4:
        message = 'Please choose a length of the movie'
        lowerbound = 1
        upperbound = 1000
        default = 100
        length = gui.integerbox(
            message, default = default, lowerbound = lowerbound, upperbound = upperbound
                               )
        
        if len(str(length)) > 0:
            movie.append(length)
    
    #easy gui choicebox for choosing genre of movie
    message = 'Please input the genre of the movie'
    choices = ['Action', 'Fantasy', 'Comedy', 'Crime', 'Animation',
    'Documentary', 'Superhero', 'Romance', 'Horror', 'Thriller',
    'Drama', 'Western', 'Sci-Fi', 'Gangster', 'History']
    while len(movie) < 5:
        genre = gui.choicebox(message, choices = choices)

        if genre == None or len(genre) < 1:
            message = 'Please re input the name of the movie'

        else:
            movie.append(genre)

    if len(movie) == 5:
        c.execute('''INSERT INTO movies VALUES(?,?,?,?,?)''', movie)
    
    conn.commit()


if __name__ == '__main__':
    new_movie()