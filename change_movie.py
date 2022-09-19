import sqlite3
import easygui as gui

def change_movie():

    '''Allows user to edit movies by choosing what perameter to change'''

    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute('''SELECT name FROM movies''')
    names = c.fetchall()
    names = [i[0] for i in names]

    message = 'What movie would you like to change'
    movie_choice = gui.choicebox(message, choices = names)
    
    c.execute('''SELECT * FROM movies WHERE name = ?''', [movie_choice])
    movie = c.fetchall()
    movie = movie[0]
    movie = [i for i in movie]
    
    categorys = ['Name', 'Release year', 'Rating', 'Length', 'Genre']
    message = 'Please choose one or more perameter to change'
    user_choice = gui.multchoicebox(message, choices = categorys)

    for category in user_choice:
        if category == 'Name':
            #Name entering with error checking
            message = 'Please input the name of the movie'
            name_change = False
            while not(name_change):
                name = gui.enterbox(message)

                if name == None or len(name) < 1:
                    message = 'Please re input the name of the movie'

                else:
                    movie[0] = name
                    name_change = True

        elif category == 'Release year':

            #Entering age of movie with easy guis integer box error checking
            message = 'Please input the year the movie was made'
            year_change = False
            while not(year_change):
                default = 2022
                lowerbound = 1887
                upperbound = 2023
                age = gui.integerbox(
                    message, default = default, lowerbound = lowerbound, upperbound = upperbound
                                    )
        
                if len(str(age)) > 0 and not(age == None):
                    movie[1] = age
                    year_change = True

        elif category == 'Rating':
            #entering age rating, with error checking
            message = 'Please choose the rating of the movie'
            rating_change = False
            while not(rating_change):
                choices = ['G', 'PG', 'R']
                rating = gui.choicebox(message, choices = choices)
                if rating in choices:
                    movie[2] = rating
                    rating_change = True

        elif category == 'Length':
            #entering length of movie with integerbox error checking
            length_change = False
            while not(length_change):
                message = 'Please choose a length of the movie'
                lowerbound = 1
                upperbound = 1000
                default = 100
                length = gui.integerbox(
                    message, default = default, lowerbound = lowerbound, upperbound = upperbound
                                    )
                
                if len(str(length)) > 0:
                    movie[3] = length
                    length_change = True

        elif category == 'Genre':
            #easy gui choicebox for choosing genre of movie
            message = 'Please input the genre of the movie'
            choices = ['Action', 'Fantasy', 'Comedy', 'Crime', 'Animation',
            'Documentary', 'Superhero', 'Romance', 'Horror', 'Thriller',
            'Drama', 'Western', 'Sci-Fi', 'Gangster', 'History']
            genre_change = False
            while not(genre_change):
                genre = gui.choicebox(message, choices = choices)

                if genre == None or len(genre) < 1:
                    message = 'Please re input the name of the movie'

                else:
                    movie[4] = genre
                    genre_change = True
    else:
        movie.append(movie_choice)
        c.execute('''UPDATE movies
                     Set name = ?,
                     year = ?,
                     rating = ?,
                     length = ?,
                     genre = ?
                     WHERE name = ?''', movie)
        conn.commit()


if __name__ == '__main__':
    change_movie()