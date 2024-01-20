# pip install python-bsonjs
# pip install Flask
# pip install Flask Flask-PyMongo
# pip install pymongo
# pip install flask-cors

import bson
import json
from bson import json_util
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.local import LocalProxy

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)
CORS(app)  # Allow all requests
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

#This is to parse BSON data from Mongo so that we can parse it as JSON
#possibility to put this into a separate python file so that each flask function can just import that instead of having this chunk of code
def parse_json(data):
    return json.loads(json_util.dumps(data))

# [GET] Countries
@app.route("/getCountries")
def getCountries():

    #this step finds all the items in the collection, specifying Countries
    data = db.Countries.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allCountries = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allCountries.append(doc)
    return allCountries

# [GET] Listings
@app.route("/getListings")
def getListings():

    #this step finds all the items in the collection, specifying Listings
    data = db.Listings.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allListings = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allListings.append(doc)
    return allListings

# [GET] Producers
@app.route("/getProducers")
def getProducers():

    #this step finds all the items in the collection, specifying Producers
    data = db.Producers.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allProducers = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allProducers.append(doc)
    return allProducers

# [GET] Reviews
@app.route("/getReviews")
def getReviews():

    #this step finds all the items in the collection, specifying Reviews
    data = db.Reviews.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allReviews = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allReviews.append(doc)
    return allReviews

# [GET] Users
@app.route("/getUsers")
def getUsers():

    #this step finds all the items in the collection, specifying Users
    data = db.Users.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allUsers = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allUsers.append(doc)
    return allUsers

# [GET] Venues
@app.route("/getVenues")
def getVenues():

    #this step finds all the items in the collection, specifying Venues
    data = db.Venues.find({})

    #have to use data.clone so that cursor is not used up
    print(len(list(data.clone())))

    allVenues = []
    
    #parse bson as json
    dataEncode = parse_json(data)
    for doc in dataEncode:
        # print(doc)
        allVenues.append(doc)
    return allVenues

if __name__ == "__main__":
    app.run(debug=True, port = 5000)