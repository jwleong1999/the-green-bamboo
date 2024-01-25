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

# [POST] Request for listing creation
# require bottle name, bottler, drink type, website/source link, producer (id OR name), brand relationship, review status, user ID, photo
# optional country of origin, drink category, ABV, age, review link
@app.route("/requestListing", methods= ['POST'])
def requestListing():
    rawRequest = request.get_json()
    rawRequestName = rawRequest["listingName"]

    # Check if bottle with the same name already exists in the database
    existingBottle = db.Listing.find_one({"listingName": rawRequestName}) # Update table name if necessary
    if (existingBottle != None):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "listingName": rawRequestName
                },
                "message": "Bottle already exists."
            }
        ), 400
    
    # Insert new request into database
    newRequest = data.requestListings(**rawRequest)
    try:
        insertResult = db.requestListings.insert_one(data.asdict(newRequest))

        return jsonify(
            {
                "code": 201,
                "data": rawRequestName
            }
        ), 201
    
    except Exception as e:
        print(str(e))

        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawRequestName
                },
                "message": "An error occurred while submitting the request."
            }
        ), 500

# [POST] Request for listing modification
# require proposed edits, brand relationship, original listing ID, user ID, review status
# optional source link, duplicate link
@app.route("/requestEdits", methods= ['POST'])
def requestEdits():
    rawRequest = request.get_json()
    rawListingID = rawRequest["listingID"]

    # Check if edit request is linked to a listing that exists in the database
    # existingListing = db.Listing.find_one({"_id": rawListingID}) # Update table name if necessary

    existingListing = True # Temporary placeholder, as the above code is not working. TODO: Fix this
    if (existingListing == None):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "listingID": rawListingID
                },
                "message": "Linked listing is not valid!"
            }
        ), 400
    
    # Insert new edit request into database
    newRequest = data.requestEdits(**rawRequest)
    try:
        insertResult = db.requestEdits.insert_one(data.asdict(newRequest))

        return jsonify(
            {
                "code": 201,
                "data": rawListingID
            }
        ), 201
    
    except Exception as e:
        print(str(e))

        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawListingID
                },
                "message": "An error occurred while submitting the request."
            }
        ), 500

if __name__ == "__main__":
    app.run(debug=True, port = 5002)