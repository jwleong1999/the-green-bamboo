# Port: 5200
# Routes: /voteReview (POST)
# -----------------------------------------------------------------------------------------

import bson
import json
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

from gridfs import GridFS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

# -----------------------------------------------------------------------------------------
# [POST] Vote review
# - Update review with new votes
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/voteReview', methods=['POST'])
def voteReview():
    data = request.get_json()
    print(data)
    reviewID = data['reviewID']
    userVotes = data['userVotes']

    try: 
        voteReview = db.reviews.update_one({'_id': ObjectId(reviewID['$oid'])}, {'$set': {'userVotes': userVotes}})

        return jsonify(
            {   
                "code": 201,
                "data": userVotes
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": userVotes
                },
                "message": "An error occurred updating the image."
            }
        ), 500

# -----------------------------------------------------------------------------------------
    
# [POST] Vote review
# - Update review with new votes
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/updateReview/<id>', methods=['PUT'])
def updateReview(id):
    data = request.get_json()
    existingReview = db.reviews.find_one({'_id': ObjectId(id)})
    data['reviewTarget'] = ObjectId(data['reviewTarget'])  # Convert reviewTarget to ObjectId
    data['userID'] = ObjectId(data['userID'])  # Convert userID to ObjectId
    if(existingReview == None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": data['reviewDesc']
                },
                "message": "Review does not exist."
            }
        ), 400

    try: 
        voteReview = db.reviews.update_one({'_id': ObjectId(id)}, {'$set': data})

        return jsonify(
            {   
                "code": 200,
                "data": data['reviewDesc']
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": data['reviewDesc']
                },
                "message": "An error occurred updating the review."
            }
        ), 500

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5200)