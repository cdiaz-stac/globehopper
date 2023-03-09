#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify
import country, city

#Using Flask framework for web app
app = Flask(__name__)

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