#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify

#Using Flask framework
app = Flask(__name__)


#Execute on the terminal
if __name__ == 'main':
    app.run()