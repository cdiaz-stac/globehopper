#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Create a country
def create_country1(data):
    services.create_country(data)
    return jsonify({'message' : 'Data inserted successfully'})

#function to get all countries and return as a JSON object\
def get_countries():
    results = services.all_countries()
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

#Update an existing country
def update_country(country_id, data):
    country = services.get_country(country_id)
    if not country:
        return jsonify({'message': 'Country does not exist'})
    services.update_country(country_id, data)
    return jsonify({'message': 'Country updated successfully'})

#Delete an existing country
def delete_country(country_id):
    country = services.get_country(country_id)
    if not country:
        return jsonify({'message': 'Country does not exist'})
    services.delete_country(country_id)
    return jsonify({'message': 'Country deleted successfully'})