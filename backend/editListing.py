# Port: 5002
# Routes: /updateListing/<id> (PUT), /deleteListing/<id> (DELETE)
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
@app.route("/updateListing/<id>", methods=['POST'])
def updateListing(id):
    listing_id=ObjectId(id)
    updatedListing = request.get_json()
    
    # Duplicate listing check: Reject if listing with the same bottle name already exists in the database
    updatedListingName = updatedListing["listingName"]
    existingBottle = db.listings.find_one({"listingName": updatedListingName})
    if(existingBottle != None):
        if(existingBottle["_id"] != listing_id):
            return jsonify(
                {   
                    "code": 410,
                    "data": {
                        "listingName": updatedListingName
                    },
                    "message": "Bottle already exists."
                }
            ), 410
    
    # Update the listing entry with the specified id
    updatedBottle = data.listings(**updatedListing)
    print(updatedBottle)
    try:
        result = db.listings.update_one(
            {"_id": listing_id},
            {"$set": data.asdict(updatedBottle)}
        )

        if result.matched_count > 0:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "_id": id
                    },
                    "message": "Listing updated successfully."
                }
            ), 200
        else:
            return jsonify(
                {
                    "code": 440,
                    "data": {
                        "_id":  id
                    },
                    "message": "Listing was not updated"
                }
            ), 440
        
    # If Id is invalid
    except InvalidId:
        return jsonify(
            {
                "code": 420,
                "data": {
                    "_id": id
                },
                "message": "Invalid listing ID."
            }
        ), 420
    
    # If listing does not work
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 450,
                "data": {
                    "_id": id
                },
                "message": "An error occurred updating the listing."
            }
        ), 450

# -----------------------------------------------------------------------------------------
# [DELETE] Deletes a listing
# - Delete entry with specified id from the "listings" collection
# - Possible return codes: 201 (Deleted), 400 (Listing doesn't exist), 500 (Error during deletion)
@app.route("/deleteListing/<id>", methods=['DELETE'])
def deleteListing(id):
        
    # Find the listing entry with the specified id
    existingListing = db.listings.find_one({"_id": ObjectId(id)})
    if(existingListing == None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Listing doesn't exist."
            }
        ), 400


    # Delete the listing entry with the specified id
    try: 
        result = db.listings.delete_one({"_id": ObjectId(id)})

        return jsonify(
            {   
                "code": 201,
                "message": "Listing deleted successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred deleting listing!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port = 5002)