# pip install python-bsonjs
# pip install Flask
# pip install Flask Flask-PyMongo
# pip install pymongo

import bson
import json
from bson import json_util
from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

#This is to parse BSON data from Mongo so that we can parse it as JSON
#possibility to put this into a separate python file so that each flask function can just import that instead of having this chunk of code
def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route("/getItems")
def hello_world():

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

app.run(debug=True)