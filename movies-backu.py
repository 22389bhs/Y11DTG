#Import database from sqlite3
import sqlite3 
#cotants and variables
DATABASE = 'movies.db'

#functions of the code
def print_all_movie():
    '''Print all the movies nicely'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Production Company':<30} {'Movie Length':<15} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[3]:<30} {movie[4]:<15} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


#functions of the code
def print_all_movie_by_name():
    '''Print all the movies sorted by their name'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY movie_name;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Production Company':<30} {'Movie Length':<15} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[3]:<30} {movie[4]:<15} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


    #functions of the code

    
def print_all_movie_by_publish_year():
    '''Print all the movies sorted by their publish year'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY publish_year;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Publish Year':<30} {'Movie':<30} {'Genre':<30} {'Production Company':<30} {'Movie Length':<15} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[1]:<30} {movie[0]:<30} {movie[2]:<30} {movie[3]:<30} {movie[4]:<15} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


def print_all_movie_by_movie_genre():
    '''Print all movies sorted out by movie genre'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY movie_genre;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Genre':<30} {'Movie':<30} {'Publish Year':<30} {'Production Company':<30} {'Movie Length':<15} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[2]:<30} {movie[0]:<30} {movie[1]:<30} {movie[3]:<30} {movie[4]:<15} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


def print_all_movie_by_production_company():
    '''Print all the movies by their production company'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY production_company;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Production Company':<30} {'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Movie Length':<15} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[3]:<30} {movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[4]:<15} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


def print_all_movie_by_movie_length():
    '''Print all the movies sorted by their length'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY movie_length DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Movie Length':<15} {'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Production Company':<30} {'Production Budget':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[4]:<15} {movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[3]:<30} {movie[5]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


def print_all_movie_by_production_budget():
    '''Print all the movies by their production budget'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY production_budget DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Production Budget':<20} {'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Production Company':<30} {'Movie Length':<20} {'Oscars Won':<5}")
    for movie in results:
        print(f"{movie[5]:<20} {movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[3]:<30} {movie[4]:<20} {movie[6]:<5}")
        #loop ends here

    #close db
    db.close()


def print_all_movie_by_oscars_won():
    '''Print all the movies sorted by the ammount of oscars its won'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from movies ORDER BY oscars_won DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results then
        #print them nicely


        print(f"{'Oscars Won':<15} {'Movie':<30} {'Publish Year':<30} {'Genre':<30} {'Production Company':<30} {'Movie Length':<15} {'Production Budget':<25}")
    for movie in results:
        print(f"{movie[6]:<15} {movie[0]:<30} {movie[1]:<30} {movie[2]:<30} {movie[3]:<30} {movie[4]:<15} {movie[5]:<25}")
        #loop ends here

    #close db
    db.close()


#main code
while True:
    user_input = input("""
    What would you like to do.
    1. Print all movies
    2. Print all movies name
    3. Print all movies by publish year
    4. Print all movies by the movie genre
    5. Print all movies by the production company
    6. Print all movies by movie length
    7. Print all movies by production budget
    8. Print all movies by ammount of oscars won
    9. Exit
    """)
    if user_input == "1":
        print_all_movie()
    elif user_input == "2":
       print_all_movie_by_name()
    elif user_input == "3":
       print_all_movie_by_publish_year()
    elif user_input == "4":
       print_all_movie_by_movie_genre()
    elif user_input == "5":
       print_all_movie_by_production_company()
    elif user_input == "6":
       print_all_movie_by_movie_length()
    elif user_input == "7":
       print_all_movie_by_production_budget()
    elif user_input == "8":
       print_all_movie_by_oscars_won()
    elif user_input == "9":
       break
    else:
       print('That was not an option\n')

