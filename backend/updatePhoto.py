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

@app.route('/upload', methods=['POST'])
def editProfile():
    data = request.get_json()

    # profile picture
    if 'image' not in data or 'filename' not in data:
        return 'Invalid request', 400
    
    image = data['image']
    filename = data['filename']
    try: 
        updateImage = db.Users.update_one({'Username': 'lotursroot518'}, {'$set': {'profile_picture': image}})

        return jsonify(
            {   
                "code": 201,
                "data": image
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "image": filename
                },
                "message": "An error occurred updating the image."
            }
        ), 500

if __name__ == '__main__':
    app.run(debug=True, port=5100)