# Flask backend for editing producer profile
# Port: 5300
# Routes: /editDetails (POST)

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

from bson.objectid import ObjectId
from gridfs import GridFS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

@app.route('/editDetails', methods=['POST'])
def editDetails():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    venueName = data['venueName']
    venueDesc = data['venueDesc']
    originLocation = data['originLocation']
    image64 = data['image64']

    try: 
        updateImage = db.venues.update_one({'_id': ObjectId(venueID)}, {'$set': {'photo': image64}})
        updateName = db.venues.update_one({'_id': ObjectId(venueID)}, {'$set': {'venueName': venueName}})
        updateDesc = db.venues.update_one({'_id': ObjectId(venueID)}, {'$set': {'venueDesc': venueDesc}})
        updateCountry = db.venues.update_one({'_id': ObjectId(venueID)}, {'$set': {'originLocation': originLocation}})

        return jsonify(
            {   
                "code": 201,
                "message": "Updated profile successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "image": image64[:8],
                    "name": venueName,
                    "desc": venueDesc,
                    "country": originLocation,
                },
                "message": "An error occurred updating profile!"
            }
        ), 500

@app.route('/addUpdates', methods=['POST'])
def addUpdates():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    text = data['text']
    image64 = data['image64']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$push': {'updates': 
                        {
                            "_id": ObjectId(),
                            'date': date,
                            'text': text,
                            'photo': image64,
                            'likes': []
                        }
                    }
            }
        )

        return jsonify( 
            {   
                "code": 201,
                "data": data
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred creating the update."
            }
        ), 500

@app.route('/sendQuestions', methods=['POST'])
def sendQuestions():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    question = data['question']
    answer = data['answer']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$push': {'questionsAnswers': 
                        {
                            '_id': ObjectId(),
                            'question': question,
                            'answer': answer
                        }
                    }
            }
        )

        return jsonify( 
            {   
                "code": 201,
                "data": venueID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": venueID,
                "message": "An error occurred creating the update."
            }
        ), 500
    
@app.route('/sendAnswers', methods=['POST'])
def sendAnswers():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    questionsAnswersID = data['questionsAnswersID']
    answer = data['answer']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID), 'questionsAnswers._id': ObjectId(questionsAnswersID)},
            {'$set': {'questionsAnswers.$.answer': answer}}
        )
        return jsonify( 
            {   
                "code": 201,
                "data": venueID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": venueID,
                "message": "An error occurred creating the update."
            }
        ), 500

@app.route('/likeUpdates', methods=['POST'])
def likeUpdates():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updateID = data['updateID']
    userID = data['userID']

    try: 
        likeUpdate = db.venues.update_one(
            {'_id': ObjectId(venueID), 'updates._id': ObjectId(updateID)},
            {'$push': {'updates.$.likes': ObjectId(userID)}}
        )
        return jsonify(
            {   
                "code": 201,
                "data": venueID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": venueID
                },
                "message": "An error occurred liking the update."
            }
        ), 500

@app.route('/unlikeUpdates', methods=['POST'])
def unlikeUpdates():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updateID = data['updateID']
    userID = data['userID']

    try: 
        unlikeUpdate = db.venues.update_one(
            {'_id': ObjectId(venueID), 'updates._id': ObjectId(updateID)},
            {'$pull': {'updates.$.likes': ObjectId(userID)}}
        )
        return jsonify(
            {   
                "code": 201,
                "data": venueID
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": venueID
                },
                "message": "An error occurred liking the update."
            }
        ), 500

if __name__ == '__main__':
    app.run(debug=True, port=5300)