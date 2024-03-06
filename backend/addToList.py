# Port: 5005
# Routes: /updateListing/<id> (PUT), /deleteListing/<id> (DELETE)
# Dataclass: listings
# -----------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------
# [PUT] Updates a listing
# - Update entry with specified id from the "listings" collection. Follows listings dataclass requirements.
# - Duplicate listing check: If a listing with the same name exists, reject the request
# - Possible return codes: 200 (Updated), 410 (Duplicate Detected), 420 (Invalid ID), 440 (Not Found), 450 (Error during update)
@app.route("/addToTried/", methods=['PUT'])
def addToTried():
    
    addedListing = request.get_json()
    date = addedListing["date"]
    listingID = addedListing["listingID"]
    userID = ObjectId(addedListing["userID"])

   
    try:
        result = db.users.update_one(
            {"_id": userID},
            # {"$set": data.asdict(updatedBottle)}
            {"$push": {"drinkLists.Drinks I Have Tried.listItems": [
                date,
                listingID
            ]}})

        
        return jsonify(
            {
                "code": 200,
                "data": listingID,
                "message": "Listing was added into the list."
            }
        ), 200
    
    except Exception as e:
        
        return jsonify(
            {
                "code": 440,
                "data": listingID,
                "message": "Listing was not added into the list"
            }
        ), 440
    


# # -----------------------------------------------------------------------------------------
# # [DELETE] Deletes a listing
# # - Delete entry with specified id from the "listings" collection
# # - Possible return codes: 201 (Deleted), 400 (Listing doesn't exist), 500 (Error during deletion)
@app.route("/addToWant/", methods=['PUT'])
def addToWant():
    
    addedListing = request.get_json()
    
    date = addedListing["date"]
    listingID = addedListing["listingID"]
    userID = ObjectId(addedListing["userID"])

   
    try:
        result = db.users.update_one(
            {"_id": userID},
            # {"$set": data.asdict(updatedBottle)}
            {"$push": {"drinkLists.Drinks I Want To Try.listItems": [
                date,
                listingID
            ]}})

        
        return jsonify(
            {
                "code": 200,
                "data": listingID,
                "message": "Listing was added into the list."
            }
        ), 200
    
    except Exception as e:
        
        return jsonify(
            {
                "code": 440,
                "data": listingID,
                "message": "Listing was not added into the list"
            }
        ), 440

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port = 5005)