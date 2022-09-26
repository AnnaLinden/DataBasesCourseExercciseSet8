#8.2
'''Write a program that asks the user to enter the area code (for example FI) and prints out the airports
located in that country ordered by airport type. For example, Finland has 65 small airports,
15 helicopter airports and so on.'''
#select name, type from airport where iso_country = "Fi" order by type asc, name asc;

#? how to print input not in one line

import mysql.connector

def get_airports (area_code):
    sql = "select name, type from airport where iso_country = '"+ area_code + "' order by type asc, name asc;"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    print(response)

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "test",
    password = "test",
    autocommit = True
)

area_code = input("To fetch the list of airports, enter the area code: ")
get_airports(area_code)