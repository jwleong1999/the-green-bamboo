# Port: 5100
# Routes: /editDetails (POST), /updateBookmark (POST), /submitModRequest (POST)
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

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

# -----------------------------------------------------------------------------------------
# [POST] Edit user profile
# - Update user profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editDetails', methods=['POST'])
def editDetails():
    data = request.get_json()
    print(data)
    userID = data['userID']
    # if data contains image64
    if 'image64' in data:
        image64 = data['image64']
    drinkChoice = data['drinkChoice']

    try: 
        if 'image64' in data:
            updateImage = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'photo': image64}})
        updateDrinkChoice = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'choiceDrinks': drinkChoice}})

        return jsonify(
            {   
                "code": 201,
                "data": image64
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "image": image64[:8]
                },
                "message": "An error occurred updating the image."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Update user bookmark
# - Update user bookmark with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/updateBookmark', methods=['POST'])
def updateBookmark():
    data = request.get_json()
    print(data)
    userID = data['userID']
    bookmark = data['bookmark']

    try: 
        updateBookmark = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'drinkLists': bookmark}})

        return jsonify(
            {   
                "code": 201,
                "data": bookmark
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": bookmark
                },
                "message": "An error occurred updating the image."
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Update follow lists
# - Update user follow lists with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/updateFollowLists', methods=['POST'])
def updateFollowList():
    data = request.get_json()
    print(data)
    userID = data['userID']
    action = data['action']
    target = data['target']
    followerID = data['followerID']

    user_document = db.users.find_one({"_id": ObjectId(userID)})
    followLists = user_document['followLists']

    if action == "unfollow":
        followLists[target] = [user for user in user_document['followLists'][target] if user != ObjectId(followerID)]
    else:
        followLists[target].append(ObjectId(followerID))

    try: 
        updateFollowLists = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'followLists': followLists}})


        return jsonify(
            {   
                "code": 201,
                "data": userID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": userID
                },
                "message": "An error occurred updating the image."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Submit mod request
# - Submit mod request with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/submitModRequest', methods=['POST'])
def submitModRequest():
    data = request.get_json()
    print(data)
    userID = data['userID']
    drinkType = data['drinkType']
    modDesc = data['modDesc']

    try: 
        submitReq = db.modRequests.insert_one({
            'userID': ObjectId(userID),
            'drinkType': drinkType,
            'modDesc': modDesc
        })

        return jsonify(
            {   
                "code": 201,
                "data": userID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": userID
                },
                "message": "An error occurred updating the image."
            }
        ), 500

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5100)