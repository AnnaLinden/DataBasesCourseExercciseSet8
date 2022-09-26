'''Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and location (town)
from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.'''
# EFHK = helsinki
import mysql.connector

#select airport.name, country.name from airport,country
# where airport.iso_country = country.iso_country and airport.ident = "EFHK";

def get_airport_and_city (icao):
    sql = "select airport.name, country.name from airport,country"
    sql += " where airport.iso_country = country.iso_country and airport.ident = '" + icao + "'";
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

icao = input("Enter ICAO airport code: ")
get_airport_and_city (icao.title())