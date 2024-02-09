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
# require 
# optional 
@app.route("/createReview", methods= ['POST'])
def createReviews():
    rawReview = request.get_json()
    rawReviewBottle = rawReview["listing_id"]
    rawReviewUserID = rawReview["userID"]


    existingReview = db.reviews.find_one({"reviewTarget": rawReviewBottle, "userID": rawReviewUserID})

    # Check whether review with the same userID and reviewTarget exists in the database
    if(existingReview != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": rawReview['reviewDesc']
                },
                "message": "Review already exists."
            }
        ), 400
    
    
    newReview = data.listings(**rawReview)

    try:
        insertResult = db.listings.insert_one(data.asdict(newReview))

        return jsonify( 
            {   
                "code": 201,
                "data": rawReview['reviewDesc']
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawReview['reviewDesc']
                },
                "message": "An error occurred creating the listing."
            }
        ), 500
    

if __name__ == "__main__":
    app.run(debug=True, port = 5001)