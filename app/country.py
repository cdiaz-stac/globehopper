#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#function to get all countries and return as a JSON object
#Create a country
def createCountry(data):
    services.createCountry(data)
    return jsonify({'message' : 'Data inserted successfully'})



def getCountries():
    results = services.allCountries()
    
    data = []
    #Converted a list to dict
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name" : row[1],
            "Population" : row[2],
            "Continent" : row[3]
        })
    return jsonify(data)