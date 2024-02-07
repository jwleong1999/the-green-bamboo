# Marked for deletion: route has been moved to editListing.py

import bson
import json
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.local import LocalProxy

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

import data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

def parse_json(data):
    return json.loads(json_util.dumps(data))

#[POST]
# require bottle name, producer ID, bottler, country of origin, drink type, ABV, official description, photo
# optional drink category, age, source link, review link
@app.route("/createReview", methods= ['POST'])
def createReviews():
    rawBottle = request.get_json()
    rawBottleName = rawBottle["listingName"]


    # existingBottle = db.Listings.find_one({"Expression Name": rawBottleName})
    existingBottle = db.listings.find_one({"listingName": rawBottleName})

    # Check whether bottle with the same name exists in the database
    if(existingBottle != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "Bottle already exists."
            }
        ), 400
    
    
    newBottle = data.listings(**rawBottle)

    try:
        insertResult = db.listings.insert_one(data.asdict(newBottle))

        return jsonify( 
            {   
                "code": 201,
                "data": rawBottleName
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "An error occurred creating the listing."
            }
        ), 500
    

if __name__ == "__main__":
    app.run(debug=True, port = 5001)