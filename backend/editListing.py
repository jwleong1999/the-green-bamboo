# Flask backend code for updating a listing
# Port: 5001
# Routes: /updateListing (PUT), /createListing (POST)
# --- Consider renaming to manageListing.py

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
from bson import ObjectId
from flask import request

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route("/updateListing/<id>", methods=['PUT'])
def updateListing(id):
    
    
    listing_id=ObjectId(id)
    updatedListing = request.get_json()
    
    updatedListingName = updatedListing["listingName"]
    
    # existingBottle = db.Listings.find_one({"Expression Name": rawBottleName})
    existingBottle = db.Listing.find_one({"listingName": updatedListingName})
   

    # Check whether bottle with the same name exists in the database
    if(existingBottle != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": updatedListingName
                },
                "message": "Bottle already exists."
            }
        ), 400
    
    updatedBottle = data.listings(**updatedListing)
    # print(data.asdict(updatedBottle))
    # return "hello"
    
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
                    "code": 404,
                    "data": {
                        "_id":  id
                    },
                    "message": "Listing was not updated"
                }
            ), 404
        
    # If Id is invalid
    except InvalidId:
        return jsonify(
            {
                "code": 400,
                "data": {
                    "_id": id
                },
                "message": "Invalid listing ID."
            }
        ), 400
    
    # If listing does not work
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "_id": id
                },
                "message": "An error occurred updating the listing."
            }
        ), 500




# #[POST]
# # require bottle name, producer ID, bottler, country of origin, drink type, ABV, official description, photo
# # optional drink category, age, source link, review link
# @app.route("/createListing", methods= ['POST'])
# def createListings():
#     rawBottle = request.get_json()
#     rawBottleName = rawBottle["listingName"]


#     # existingBottle = db.Listings.find_one({"Expression Name": rawBottleName})
#     existingBottle = db.Listing.find_one({"listingName": rawBottleName})

#     # Check whether bottle with the same name exists in the database
#     if(existingBottle != None):
#         return jsonify(
#             {   
#                 "code": 400,
#                 "data": {
#                     "listingName": rawBottleName
#                 },
#                 "message": "Bottle already exists."
#             }
#         ), 400
    
    
#     newBottle = data.listings(**rawBottle)

#     try:
#         insertResult = db.Listing.insert_one(data.asdict(newBottle))

#         return jsonify( 
#             {   
#                 "code": 201,
#                 "data": rawBottleName
#             }
#         ), 201
#     except Exception as e:
#         print(str(e))
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "listingName": rawBottleName
#                 },
#                 "message": "An error occurred creating the listing."
#             }
#         ), 500
    

if __name__ == "__main__":
    app.run(debug=True, port = 5003)