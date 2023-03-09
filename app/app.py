#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify #g
import country, city #os
from flask_wtf.csrf import CSRFProtect, generate_csrf
#Using Flask framework for web app
app = Flask(__name__)
#app.secret_key = 'your-secret-key-here'

#with app.app_context():
 #   with app.test_request_context():
  #      csrf_token = generate_csrf()
   #     g.csrf_token = csrf_token
    #    print(csrf_token)

#csrf = CSRFProtect()
#csrf.init_app(app) # Compliant

##########################################  COUNTRY   ###################################################
#Create - POST api
@app.post('/countries')
def createcountryapi():
    data = request.json
    return country.createcountryview(data)

#Read - GET api
@app.get('/countries')
def getallcountriesapi():
    return country.getallcountriesview()

#Update - PUT api
@app.put('/countries/<int:country_id>')  #Query string parameter
def updatecountryapi(country_id):
    data = request.json
    return country.updatecountryview(country_id, data)

#Delete - DELETE api
@app.delete('/countries/<int:country_id>')  #Query string parameter
def deletecountryapi(country_id):
    return country.deletecountryview(country_id)


##########################################  CITY   ###################################################
#Create - POST api
@app.post('/cities')
def createcityapi():
    data = request.json
    return city.createcityview(data)

#Read - GET api
@app.get('/cities')
def getallcitiesapi():
    return city.getallcitiesview()

#Update - PUT api
@app.put('/cities/<int:city_id>')  #Query string parameter
def updatecityapi(city_id):
    data = request.json
    return city.updatecityview(city_id, data)

#Delete - DELETE api
@app.delete('/cities/<int:city_id>')  #Query string parameter
def deletecityapi(city_id):
    return city.deletecityview(city_id)





#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)