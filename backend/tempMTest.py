# Manual testing for data.py

from data import Listings, Producers, Reviews, Users, VenuesAPI, Venues,convert_to_json, Country, drinkCategory

# # Example usage
listing = Listings(drinkName="Whiskey", producerName="ABC Distillery", Bottler="ABC Bottler", originCountry="USA", drinkType="Whiskey", drinkCategory="Single Malt", Age="12 years", ABV="40%", reviewLink=None, listingDesc="A smooth and rich whiskey.")
json_data = convert_to_json(listing)
print(json_data)

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
