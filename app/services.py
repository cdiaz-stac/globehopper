#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

def db_open_connection():
    conn.myconn._open_connection()
    global mycursor 
    mycursor = conn.myconn.cursor() 

def db_close_connection():
    mycursor.close()
    conn.myconn.close() 

#Create a country record
def create_country(data):
    #open connection
    db_open_connection()

    country_id = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = ("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)")
    values = (country_id, name, population, continent)
    mycursor.execute(mysql, values)

    #Close connection
    db_close_connection()

#Update a country record by its ID
def update_country(country_id, data):
    #open connection
    db_open_connection()


    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "UPDATE Country SET Name = %s, Population = %s, Continent = %s WHERE CountryId = %s"
    values = (name, population, continent, country_id)
    mycursor.execute(mysql, values)

    #Close connection
    db_close_connection()

#Delete a country record by its ID
def delete_country(country_id):
    #open connection
    db_open_connection()

    #Execute the SQL
    mysql = "DELETE FROM Country WHERE CountryId = %s"
    value = (country_id,)
    mycursor.execute(mysql, value)

    #Close connection
    db_close_connection()

#Read all records from country table using SQL
def all_countries():
    #open connection
    db_open_connection()

    #Execute the SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #Close connection
    db_close_connection()

    return results

############################################# CITY ########################################
#Create a city record
def createcityservice(data):
    #Open connection
    db_open_connection()

    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    first = data['FirstLandmark']
    second = data['SecondLandmark']
    third = data['ThirdLandmark']

    #Execute the SQL
    mysql = "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (cityid, name, countryid, capital, first, second, third)
    mycursor.execute(mysql, values)

    #Close connection
    db_close_connection() 
    


#Gets all records from city table using SQL
def allcitiesservice():
    #Open connection
    db_open_connection()

    #Execute the SQL
    mycursor.execute("SELECT * FROM city")
    results = mycursor.fetchall()

    #Close connection
    db_close_connection() 
    
    return results


#Update a city record
def updatecityservice(city_id, data):
    #Open connection
    db_open_connection() 

    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    first = data['FirstLandmark']
    second = data['SecondLandmark']
    third = data['ThirdLandmark']

    #Execute the SQL
    mysql = "UPDATE City SET Name = %s, CountryId= %s, Capital= %s, FirstLandmark= %s, SecondLandmark= %s, ThirdLandmark= %s WHERE cityId = %s"
    values = (name, countryid, capital, first, second, third, city_id)
    mycursor.execute(mysql, values)

    #Close connection
    db_close_connection()


#Delete a city record
def deletecityservice(city_id):
    #Open connection
    db_open_connection()

    #Execute the SQL
    mysql = "DELETE FROM City WHERE CityId = %s"
    values = [(city_id)]
    mycursor.execute(mysql, values)
    print(city_id)
    #Close connection
    db_close_connection()