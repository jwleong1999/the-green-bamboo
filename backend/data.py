from dataclasses import dataclass
from typing import Optional
import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority")
database = client["GreenBamboo"]
# collection = database['your_collection']

# Dataclass (Country)
@dataclass
class Country:
    countryName: str

# Dataclass (drinkCatgeories)
@dataclass
class drinkCategory:
    drinkType: str
    Category: list

# Dataclass (Listing)
@dataclass
class Listings:
    drinkName: str
    producerName: str
    Bottler: str
    originCountry: str
    drinkType: str
    drinkCategory: str
    Age: str
    ABV: str
    reviewLink: Optional[str]
    listingDesc: str

# Dataclass (Producers)
@dataclass
class Producers:
    producerName: str
    originCountry: str
    obStatus: Optional[str]
    mainDrink: list

# Dataclass (Reviews)
@dataclass
class Reviews:
    reviwerName: str
    reviewedSubject: str
    Date: str
    Rating:int
    reviewDesc: str
    taggedUsers: Optional[list]
    reviewTitle: str

@dataclass
class Users:
    Username: str
    Name: str
    drinkOfChoice: Optional[list]

# Dataclass (Venue) --> Using Google Maps API
@dataclass
class VenuesAPI:
    venueName: str
    venueDesc: str
    countryLocated: str


# Dataclass (Venue)
@dataclass
class Venues:
    venueName: str
    venueDesc: str
    countryLocated: str
    Address: str
    openingHours: Optional[list]


def convert_to_json(data):
    return json.dumps(data.__dict__)







