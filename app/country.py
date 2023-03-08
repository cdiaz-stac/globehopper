#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#function to get all countries and return as a JSON object
def getCountries():
    results = services.allCountries()
    return jsonify(results)