#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

#Create a country record
def create_country(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    country_id = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = ("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)")
    values = (country_id, name, population, continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Update a country record by its ID
def update_country(country_id, data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()


    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "UPDATE Country SET Name = %s, Population = %s, Continent = %s WHERE CountryId = %s"
    values = (name, population, continent, country_id)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Delete a country record by its ID
def delete_country(country_id):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = "DELETE FROM Country WHERE CountryId = %s"
    value = (country_id,)
    mycursor.execute(mysql, value)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Read all records from country table using SQL
def all_countries():
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results