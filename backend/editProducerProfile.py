# Flask backend for editing producer profile
# Port: 5200
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
    producerID = data['producerID']

    # if data contains image64
    if 'image64' in data:
        image64 = data['image64']
        producerName = data['producerName']
        producerDesc = data['producerDesc']
        originCountry = data['originCountry']
        # drinkChoice = data['drinkChoice']

    try: 
        if 'image64' in data:
            updateImage = db.producers.update_one({'_id': ObjectId(producerID)}, {'$set': {'photo': image64}})
            updateName = db.producers.update_one({'_id': ObjectId(producerID)}, {'$set': {'producerName': producerName}})
            updateDesc = db.producers.update_one({'_id': ObjectId(producerID)}, {'$set': {'producerDesc': producerDesc}})
            updateCountry = db.producers.update_one({'_id': ObjectId(producerID)}, {'$set': {'originCountry': originCountry}})
            # updateDrinkChoice = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'choiceDrinks': drinkChoice}})

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
                    "name": producerName,
                    "desc": producerDesc,
                    "country": originCountry,
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
    producerID = data['producerID']
    date = data['date']
    text = data['text']
    image64 = data['image64']

    try:
        submitReq = db.listings.insert_one(
            {'producerID': ObjectId(producerID)},
            {'$push': {'updates': {
                'date': date,
                'text': text,
                'photo': image64
            }}}
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
    

if __name__ == '__main__':
    app.run(debug=True, port=5200)