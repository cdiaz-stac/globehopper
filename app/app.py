# Starting point of our WebApp - main
# pip install Flask

from flask import Flask, request, jsonify
import country
from flask_wtf.csrf import CSRFProtect  # pip install flask_wtf

# Using Flask framework
app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Add this line to set a secret key
csrf = CSRFProtect()
csrf.init_app(app)


# Delete - DELETE API
@app.route('/countries/<int:country_id>', methods=['DELETE'])
def delete_country(country_id):
    result = country.deleteCountry(country_id)
    if result:
        return jsonify({"message": "Country deleted successfully"}), 200
    else:
        return jsonify({"message": "Country not found"}), 404


# Update - PUT API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    data = request.json
    result = country.update_country1(country_id, data)
    if result:
        return jsonify({"message": "Country updated successfully"}), 200
    else:
        return jsonify({"message": "Country not found"}), 404


# Create - POST API
@app.route('/countries', methods=['POST'])
def create_country1():
    data = request.json
    return country.create_country(data)


# Read API
@app.get('/countries')
def get_all_countries():
    return country.get_countries()


# Execute on the terminal
if __name__ == '__main__':
    app.run()
