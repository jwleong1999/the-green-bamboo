from dataclasses import dataclass, asdict
from typing import Optional, Union
import pymongo
import json
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority")
database = client["GreenBamboo"]
# collection = database['your_collection']

#NOTE TO DEVELOPERS, TO INSERT DATA INTO MONGO, CREATE A DATA INSTANCE OF THE DATACLASS NEEDED, THEN USE 
# asdict(data) TO INSERT INTO MONGO

# Dataclass (countries)
@dataclass
class countries:
    originCountry: str

# Dataclass (listings)
@dataclass
class listings:
    listingName: str
    producerID: object
    bottler: str
    originCountry: str
    drinkType: str
    typeCategory: Optional[str]
    abv: float
    age: Optional[str]
    reviewLink: Optional[str]
    officialDesc: str
    sourceLink: Optional[str]
    photo: str

# Dataclass (producers)
@dataclass
class producers:
    producerName: str
    producerDesc: str
    originCountry: str
    statusOB: Optional[str]
    mainDrinks: list

# Dataclass (reviews)
@dataclass
class reviews:
    userID: object
    reviewTarget: str
    date: datetime
    rating: int
    reviewDesc: str
    taggedUsers: Optional[list]
    reviewTitle: str
    reviewType: str
    flavorTag: Optional[list]
    photo: str # Optional[binary]

# Dataclass (users)
@dataclass
class users:
    username: str
    displayName: str
    choiceDrinks: list
    drinkLists: object
    modType: list
    photo: str

# Dataclass (venues)
@dataclass
class venues:
    venueName: str
    venueDesc: str
    originCountry: str
    address: str
    openingHours: object

# Dataclass (venuesAPI) --> Using Google Maps API
@dataclass
class venuesAPI:
    venueAPIName: str
    venueAPIDesc: str
    originCountry: str

# Dataclass (drinkTypes)
@dataclass
class drinkTypes:
    drinkType: str
    typeCategory: Optional[list]

# Dataclass (requestListings)
@dataclass
class requestListings:
    listingName: str
    producerNew: Optional[str]
    producerID: Optional[object]
    bottler: str
    originCountry: Optional[str]
    drinkType: str
    typeCategory: Optional[str]
    age: Optional[str]
    abv: Optional[str]
    reviewLink: Optional[str]
    sourceLink: str
    brandRelation: str
    reviewStatus: bool
    userID: object
    photo: str

# Dataclass (requestEdits)
@dataclass
class requestEdits:
    duplicateLink: Optional[str]
    editDesc: str
    sourceLink: Optional[str]
    brandRelation: str
    listingID: object
    userID: object
    reviewStatus: bool

# Dataclass (modRequests)
@dataclass
class modRequests:
    userID: object
    drinkType: str
    modDesc: str

def convert_to_json(data):
    return json.dumps(data.__dict__)



# # Example usage
# listing = Listings(drinkName="Whiskey", producerName="ABC Distillery", Bottler="ABC Bottler", originCountry="USA", drinkType="Whiskey", drinkCategory="Single Malt", Age="12 years", ABV="40%", reviewLink=None, listingDesc="A smooth and rich whiskey.")
# json_data = convert_to_json(listing)
# print(json_data)

# country = Country(countryName="USA")
# json_data = convert_to_json(country)
# print(json_data)

# drink_category = drinkCategory(drinkType="Whiskey", Category=["Single Malt", "Bourbon"])
# json_data = convert_to_json(drink_category)
# print(json_data)

# producer = Producers(producerName="ABC Distillery", originCountry="USA", obStatus="Active", mainDrink=["Whiskey", "Vodka"])
# json_data = convert_to_json(producer)
# print(json_data)

# review = Reviews(reviwerName="John Doe", reviewedSubject="Whiskey", Date="2022-01-01", Rating=5, reviewDesc="Great whiskey!", taggedUsers=["Jane Doe"], reviewTitle="Amazing Whiskey")
# json_data = convert_to_json(review)
# print(json_data)

# user = Users(Username="johndoe", Name="John Doe", drinkOfChoice=["Whiskey", "Beer"])
# json_data = convert_to_json(user)
# print(json_data)

# venue = Venues(venueName="ABC Bar", venueDesc="Cozy bar with live music", countryLocated="USA", Address="123 Main St", openingHours=["Mon-Fri: 5pm-12am", "Sat-Sun: 12pm-2am"])
# json_data = convert_to_json(venue)
# print(json_data)





