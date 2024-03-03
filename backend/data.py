# Imported file for MongoDB dataclasses

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
    legalAge:str

# Dataclass (listings)
@dataclass
class listings:
    listingName: str
    producerID: object
    bottler: str
    originCountry: str
    drinkType: str
    abv: float
    officialDesc: str
    addedDate: datetime
    allowMod: bool
    age: Optional[str] = None
    photo: Optional[str] = None
    typeCategory: Optional[str] = None
    reviewLink: Optional[str] = None
    sourceLink: Optional[str] = None
    

# Dataclass (producers)
@dataclass
class producers:
    producerName: str
    producerDesc: str
    originCountry: str
    mainDrinks: list
    hashedPassword: str
    photo: str
    hashedPassword:str
    questionAnswers: Optional[list] = None
    updates:Optional[list]=None
    statusOB: Optional[str] = None
    producerLink: Optional[str] = None

# Dataclass (reviews)
@dataclass
class reviews:
    userID: object
    reviewTarget: object
    rating: int
    reviewDesc: str
    reviewType: str
    createdDate: datetime
    language: str
    finish: str
    willRecommend: bool
    wouldBuyAgain: bool
    userVotes: object
    photo: Optional[str] = None
    colour: Optional[str] = None
    aroma: Optional[str] = None
    location: Optional[object] = None
    taste: Optional[str] = None
    taggedUsers: Optional[list] = None
    flavorTag: Optional[list] = None
    observationTag: Optional[list] = None
    

# Dataclass (users)
@dataclass
class users:
    username: str
    displayName: str
    choiceDrinks: list
    drinkLists: object
    modType: list
    photo: str
    hashedPassword: str
    joinDate: datetime
    followLists: object
    firstName:str
    lastName:str
    email:str

# Dataclass (venues)
@dataclass
class venues:
    venueName: str
    address: str
    venueType: str
    venueDesc: str
    originLocation: str
    venueDesc: str
    menu: list
    photo: str
    claimStatus: bool
    openingHours: object
    hashedPassword: str
    questionAnswers: Optional[list] = None
    updates:Optional[list]=None


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
    typeCategory: Optional[list] = None

# Dataclass (requestListings)
@dataclass
class requestListings:
    listingName: str
    bottler: str
    drinkType: str
    sourceLink: str
    brandRelation: str
    reviewStatus: bool
    userID: object
    photo: str
    producerNew: Optional[str] = None
    producerID: Optional[object] = None
    originCountry: Optional[str] = None
    typeCategory: Optional[str] = None
    age: Optional[str] = None
    abv: Optional[str] = None
    reviewLink: Optional[str] = None

# Dataclass (requestEdits)
@dataclass
class requestEdits:
    editDesc: str
    brandRelation: str
    listingID: object
    userID: object
    reviewStatus: bool
    duplicateLink: Optional[str] = None
    sourceLink: Optional[str] = None

# Dataclass (requestInaccuracy)
@dataclass
class requestInaccuracy:
    listingID: object
    userID: object
    venueID:object
    inaccurateReason: Optional[str] = None
    
# Dataclass (modRequests)
@dataclass
class modRequests:
    userID: object
    drinkType: str
    modDesc: str

# Dataclass (flavourTags)
@dataclass
class flavourTags:
    hexcode: str
    familyTag: str
    subtag: list

# Dataclass (languages)
@dataclass
class languages:
    language: str

# Dataclass (observationTags)
@dataclass
class observationTags:
    observationTag: str

# Dataclass (colours)
@dataclass
class colours:
    hexcode: str

# Dataclass (specialColours)
@dataclass
class specialColours:
    hexList: list
    colour: str

def convert_to_json(data):
    return json.dumps(data.__dict__)







