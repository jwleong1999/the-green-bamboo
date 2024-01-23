from dataclasses import dataclass, asdict
from typing import Optional, Union
import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority")
database = client["GreenBamboo"]
# collection = database['your_collection']

#NOTE TO DEVELOPERS, TO INSERT DATA INTO MONGO, CREATE A DATA INSTANCE OF THE DATACLASS NEEDED, THEN USE 
# asdict(data) TO INSERT INTO MONGO

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
    listingName: str
    producer: str
    bottler: str
    originCountry: str
    drinkType: str
    abv: str
    officialDesc: str
    photo: str
    typeCategory: Optional[str] = None
    age: Optional[str] = None
    reviewLink: Optional[str] = None
    sourceLink: Optional[str] = None

# Dataclass (Producers)
@dataclass
class Producers:
    producerName: str
    producerDesc: str
    originCountry: str
    statusOB: Optional[str]
    mainDrinks: list

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

# # Example usage
# listing = Listings(drinkName="Whiskey", producerName="ABC Distillery", Bottler="ABC Bottler", originCountry="USA", drinkType="Whiskey", drinkCategory="Single Malt", Age="12 years", ABV="40%", reviewLink=None, listingDesc="A smooth and rich whiskey.")
# json_data = convert_to_json(listing)
# print(json_data)

country = Country(countryName="USA")
json_data = convert_to_json(country)
print(json_data)

drink_category = drinkCategory(drinkType="Whiskey", Category=["Single Malt", "Bourbon"])
json_data = convert_to_json(drink_category)
print(json_data)

producer = Producers(producerName="ABC Distillery", originCountry="USA", obStatus="Active", mainDrink=["Whiskey", "Vodka"])
json_data = convert_to_json(producer)
print(json_data)

review = Reviews(reviwerName="John Doe", reviewedSubject="Whiskey", Date="2022-01-01", Rating=5, reviewDesc="Great whiskey!", taggedUsers=["Jane Doe"], reviewTitle="Amazing Whiskey")
json_data = convert_to_json(review)
print(json_data)

user = Users(Username="johndoe", Name="John Doe", drinkOfChoice=["Whiskey", "Beer"])
json_data = convert_to_json(user)
print(json_data)

venue = Venues(venueName="ABC Bar", venueDesc="Cozy bar with live music", countryLocated="USA", Address="123 Main St", openingHours=["Mon-Fri: 5pm-12am", "Sat-Sun: 12pm-2am"])
json_data = convert_to_json(venue)
print(json_data)





