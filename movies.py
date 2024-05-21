#Import database from sqlite3
import sqlite3 
#cotants and variables
DATABASE = 'movies.db'

#functions of the code
with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = "SELECT * from movies;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print them nicely

    print(f"{'Movie':<40} {'Publish Year':<40} {'Genre':<40} {'Production Company':<30} {'Movie Length':<10} {'Production Budget':<15} {'Oscars Won':<5}")
for movie in results:
    print(f"{movie[0]:<40} {movie[1]:<40} {movie[2]:<40} {movie[3]:<40} {movie[4]:<10} {movie[5]:<15} {movie[6]:<5}")


#close db
db.close()