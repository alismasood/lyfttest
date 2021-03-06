###################################################################################################
#
# Program name: Lyfttest
# Author:       Ali Masood
# Date:         1/29/2018
# Description:  A small web application created for Lyft's software engineer apprenticeship
#               application.
#
#               The following code was written with heavy help from the following tutorials:
#
#               1. The official Flask Tutorial by Armin Ronacher
#                   http://flask.pocoo.org/docs/0.12/tutorial/`
#
#               2. Implementing a RESTful Web API with Python & Flask by Luis Rei
#                   http://blog.luisrei.com/
#
#               3. Flask: Parsing JSON data
#                   https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/   
#
###################################################################################################

# Imports
import os
from flask import Flask, request, json, jsonify

# Flask app initialization
app = Flask(__name__) # create application instance
app.config.from_object(__name__) # load config from this file

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('LYFTTEST_SETTINGS',silent=True)

# Routes
@app.route('/')
def introduction():
    return 'Hello! This is Ali Masood\'s small web app built for the Lyft software apprenticeship!'

@app.route('/test', methods=['POST'])
def test():
    
    # Check request type
    if request.headers['Content-Type'] != 'application/json':
        return "415 Unsupported Media Type"
    
    # Check json object content
    jsoncontent = request.json
    if "x" not in jsoncontent or "y" not in jsoncontent:
        return "Error: x or y parameter were not found in the passed JSON object."
    
    # Check x and y parameter types
    x = jsoncontent["x"]
    y = jsoncontent["y"]
    if type(x) is not int or type(y) is not int:
        return "Error: x and y parameters passed in the JSON object must be of type int." 
    
    # All checks passed: return sum
    else:
        return jsonify({"sum":x+y})

    
if __name__ == '__main__':
    app.run()
