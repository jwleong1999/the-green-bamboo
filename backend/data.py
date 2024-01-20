from dataclasses import dataclass
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority")
database = client["GreenBamboo"]
# collection = database['your_collection']

# Dataclass (Country)
@dataclass
class Country:
    countryName: str

# Dataclass (Drink)
@dataclass
class Drink:
    drinkType: str
    drinkCategory: list

# Dataclass (Venue)
class Venue:
    venueName: str
    venueAddress: str
    venueCity: str
    venueState: str
    venueCountry: Country
    venueWebsite: str
    venuePhone: str
    venueEmail: str
    venueDescription: str


