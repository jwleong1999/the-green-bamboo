# Port: 5001
# Routes: /createListing (POST)
# Dataclass: listings
# -----------------------------------------------------------------------------------------

import os
import json
import pytz
import data
import s3Images
from bson import json_util
from flask import Blueprint, g, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

# -----------------------------------------------------------------------------------------
# [POST] Creates a listing
# - Insert entry into the "listings" collection. Follows listings dataclass requirements.
# - Duplicate listing check: If a listing with the same name exists, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@blueprint.route("/createListing", methods= ['POST'])
def createListings():
    db = g.db
    rawBottle = request.get_json()
    # Add current datetime to the listing
    rawBottle['addedDate'] = datetime.now(pytz.timezone('Etc/GMT-8'))
    rawBottle["allowMod"] = True
    rawBottle['producerID'] = ObjectId(rawBottle['producerID'])
    # Duplicate listing check: Reject if listing with the same bottle name already exists in the database
    rawBottleName = rawBottle["listingName"]
    existingBottle = db.listings.find_one({"listingName": rawBottleName})
    if(existingBottle != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "Bottle already exists."
            }
        ), 400
    
    # Upload image into s3 bucket and retrieve url
    rawBottle['photo'] = s3Images.uploadBase64ImageToS3(rawBottle['photo'])
    
    # Insert new listing into database
    newBottle = data.listings(**rawBottle)

    try:
        insertResult = db.listings.insert_one(data.asdict(newBottle))

        return jsonify( 
            {   
                "code": 201,
                "data": rawBottleName
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "An error occurred creating the listing."
            }
        ), 500
