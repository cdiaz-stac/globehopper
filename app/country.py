#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to get all countries and return as a JSON object
#Create a country record
def createcountryview(data):
    services.createcountryservice(data)
    return jsonify({'message' : 'Data inserted successfully'})

#Get all countries
def getallcountriesview():
    results = services.allcountriesservice()

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


#Update a country record
def updatecountryview(country_id, data):
    services.updatecountryservice(country_id, data)
    return jsonify({'message' : 'Data updated successfully'})


#Delete a country record
def deletecountryview(country_id):
    services.deletecountryservice(country_id)
    return jsonify({'message' : 'Data deleted successfully'})