#Define all functions related to city APIs

from flask import Flask, request, jsonify
import services

#Function to get all cities and return as a JSON object
#Create a city record
def createcityview(data):
    services.createcityservice(data)
    return jsonify({'message' : 'Data inserted successfully'})

def getallcitiesview(country_id=None):
    results = services.allcitiesservice()

    data = []
    #Converted a list to dict
    for row in results:
        city_data = {
            "CityId" : row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark" : row[4],
            "SecondLandmark" : row[5],
            "ThirdLandmark" : row[6]
        }
        # Filter by country id if provided
        if country_id is None or city_data["CountryId"] == country_id:
            data.append(city_data)

    return jsonify(data)



#Update a city record
def updatecityview(city_id, data):
    services.updatecityservice(city_id, data)
    return jsonify({'message' : 'Data updated successfully'})


#Delete a city record
def deletecityview(city_id):
    services.deletecityservice(city_id)
    return jsonify({'message' : 'Data deleted successfully'})