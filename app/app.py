# Starting point of our WebApp - main
# pip install Flask

from flask import Flask, request, jsonify
import country
from flask_wtf.csrf import CSRFProtect  # pip install flask_wtf

# Using Flask framework
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)


# Delete - DELETE API
@app.route('/countries/<int:country_id>', methods=['DELETE'])
def deleteCountry(country_id):
    result = country.deleteCountry(country_id)
    if result:
        return jsonify({"message": "Country deleted successfully"}), 200
    else:
        return jsonify({"message": "Country not found"}), 404


# Update - PUT API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def updateCountry(country_id):
    data = request.json
    result = country.updateCountry1(country_id, data)
    if result:
        return jsonify({"message": "Country updated successfully"}), 200
    else:
        return jsonify({"message": "Country not found"}), 404


# Create - POST API
@app.route('/countries', methods=['POST'])
def createCountry():
    data = request.json
    return country.createCountry(data)


# Read API
@app.get('/countries')
def getAllCountries():
    return country.getCountries()


# Execute on the terminal
if __name__ == '__main__':
    app.run()