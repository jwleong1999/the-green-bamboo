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
        # drinkChoice = data['drinkChoice']

    try: 
        if 'image64' in data:
            updateImage = db.producers.update_one({'_id': ObjectId(producerID)}, {'$set': {'photo': image64}})
            # updateDrinkChoice = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'choiceDrinks': drinkChoice}})

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

if __name__ == '__main__':
    app.run(debug=True, port=5200)