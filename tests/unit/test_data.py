import unittest
from backend.data import countries, listings, producers, reviews, users, venues, drinkTypes, requestEdits, requestListings,modRequests
from datetime import datetime

class TestData(unittest.TestCase):
    def test_countries(self):
        # Test case 1: Check if the origin country is set correctly
        country = countries(originCountry="USA")
        self.assertEqual(country.originCountry, "USA")

        # Test case 2: Check if the origin country is set correctly for a different country
        country = countries(originCountry="Japan")
        self.assertEqual(country.originCountry, "Japan")

        # Test case 3: Check if the origin country is None when not provided
        self.assertRaises(TypeError, countries)

    def test_listings(self):
        # Test case 4: Check if the listing name is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.listingName, "Product A")

        # Test case 5: Check if the producer ID is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.producerID, 123)

        # Test case 6: Check if the bottler is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.bottler, "Bottler A")

        # Test case 7: Check if the origin country is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.originCountry, "USA")

        # Test case 8: Check if the drink type is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.drinkType, "Whiskey")

        # Test case 9: Check if the ABV is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.abv, 40.0)

        # Test case 10: Check if the official description is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.officialDesc, "Description A")

        # Test case 11: Check if the photo is set correctly
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertEqual(listing.photo, "product.jpg")

        # Test case 12: Check if the type category is None when not provided
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertIsNone(listing.typeCategory)

        # Test case 13: Check if the age is None when not provided
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertIsNone(listing.age)

        # Test case 14: Check if the review link is None when not provided
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertIsNone(listing.reviewLink)

        # Test case 15: Check if the source link is None when not provided
        listing = listings(listingName="Product A", producerID=123, bottler="Bottler A", originCountry="USA", drinkType="Whiskey", abv=40.0, officialDesc="Description A", photo="product.jpg")
        self.assertIsNone(listing.sourceLink)


    def test_producers(self):
        # Test case 1: Check if the producer name is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.producerName, "Producer A")

        # Test case 2: Check if the producer description is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.producerDesc, "Description A")

        # Test case 3: Check if the origin country is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.originCountry, "USA")

        # Test case 4: Check if the main drinks are set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.mainDrinks, ["Drink A", "Drink B"])

        # Test case 5: Check if the hashed password is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.hashedPassword, "password123")

        # Test case 6: Check if the photo is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertEqual(producer.photo, "producer.jpg")

        # Test case 7: Check if the statusOB is None when not provided
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"], hashedPassword="password123", photo="producer.jpg")
        self.assertIsNone(producer.statusOB)

    def test_producers(self):
        # Test case 8: Check if the hashed password is present
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="Country A", mainDrinks=[], hashedPassword="password123", photo="producer.jpg", statusOB=None)
        self.assertTrue(hasattr(producer, "hashedPassword"))

    

        
    def test_reviews(self):
        # Test case 1: Check if the userID is set correctly
        user_id = object()
        review = reviews(userID=user_id, reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.userID, user_id)

        # Test case 2: Check if the review target is set correctly
        review_target = object()
        review = reviews(userID=object(), reviewTarget=review_target, rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.reviewTarget, review_target)

        # Test case 3: Check if the rating is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.rating, 5)

        # Test case 4: Check if the review description is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.reviewDesc, "Great product")

        # Test case 5: Check if the review title is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.reviewTitle, "Amazing")

        # Test case 6: Check if the review type is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.reviewType, "Venue")

        # Test case 7: Check if the created date is set correctly
        now = datetime.now()
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=now, language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.createdDate, now)

        # Test case 8: Check if the language is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.language, "English")

        # Test case 9: Check if the finish is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.finish, "Smooth")

        # Test case 10: Check if the will recommend flag is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertTrue(review.willRecommend)

        # Test case 11: Check if the would buy again flag is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertTrue(review.wouldBuyAgain)

        # Test case 12: Check if the photo is set correctly
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertEqual(review.photo, "review.jpg")

        # Test case 13: Check if the colour is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.colour)

        # Test case 14: Check if the aroma is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.aroma)

        # Test case 15: Check if the location is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.location)

        # Test case 16: Check if the taste is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.taste)

        # Test case 17: Check if the tagged users is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.taggedUsers)

        # Test case 18: Check if the flavor tag is None when not provided
        review = reviews(userID=object(), reviewTarget=object(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Venue", createdDate=datetime.now(), language="English", finish="Smooth", willRecommend=True, wouldBuyAgain=True, photo="review.jpg")
        self.assertIsNone(review.flavorTag)
        
    

    def test_users(self):
        # Test case 1: Check if the username is set correctly
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=[], photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.username, "john_doe")

        # Test case 2: Check if the display name is set correctly
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=[], photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.displayName, "John Doe")

        # Test case 3: Check if the choice drinks list is set correctly
        choice_drinks = ["Drink A", "Drink B", "Drink C"]
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=choice_drinks, drinkLists=None, modType=[], photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.choiceDrinks, choice_drinks)

        # Test case 4: Check if the drink lists object is set correctly
        drink_lists = object()
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=[], drinkLists=drink_lists, modType=[], photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.drinkLists, drink_lists)

        # Test case 5: Check if the mod type list is set correctly
        mod_type = ["Type A", "Type B", "Type C"]
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=mod_type, photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.modType, mod_type)

        # Test case 6: Check if the photo is set correctly
        user = users(username="john_doe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=[], photo="john.jpg", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertEqual(user.photo, "john.jpg")

        # Test case 7: Check if the hashed password is present
        user = users(username="JohnDoe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=[], photo="", hashedPassword="password123", joinDate=datetime.now(), followLists=None)
        self.assertTrue(hasattr(user, "hashedPassword"))

        # Test case 8: Check if followList is an object 
        follow_lists = object()
        user = users(username="JohnDoe", displayName="John Doe", choiceDrinks=[], drinkLists=None, modType=[], photo="", hashedPassword="password123", joinDate=datetime.now(), followLists=follow_lists)
        self.assertEqual(user.followLists, follow_lists)
        

    def test_venues(self):
        # Test case 1: Check if the venue name is set correctly
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=object(), hashedPassword="password123")
        self.assertEqual(venue.venueName, "Venue A")

        # Test case 2: Check if the venue description is set correctly
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=object(), hashedPassword="password123")
        self.assertEqual(venue.venueDesc, "Description A")

        # Test case 3: Check if the origin country is set correctly
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=object(), hashedPassword="password123")
        self.assertEqual(venue.originCountry, "Country A")

        # Test case 4: Check if the address is set correctly
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=object(), hashedPassword="password123")
        self.assertEqual(venue.address, "Address A")

        # Test case 5: Check if the opening hours object is set correctly
        opening_hours = object()
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=opening_hours, hashedPassword="password123")
        self.assertEqual(venue.openingHours, opening_hours)

        # Test case 6: Check if the hashed password is present
        venue = venues(venueName="Venue A", venueDesc="Description A", originCountry="Country A", address="Address A", openingHours=None, hashedPassword="password123")
        self.assertEqual(venue.hashedPassword, "password123")

    def test_drinkTypes(self):
        # Test case 1: Check if the drink type is set correctly
        drink_type = "Type A"
        dt = drinkTypes(drinkType=drink_type)
        self.assertEqual(dt.drinkType, drink_type)

        # Test case 2: Check if the type category is set correctly
        type_category = ["Category A", "Category B", "Category C"]
        dt = drinkTypes(drinkType="Type A", typeCategory=type_category)
        self.assertEqual(dt.typeCategory, type_category)

        # Test case 3: Check if the type category is None by default
        dt = drinkTypes(drinkType="Type A")
        self.assertIsNone(dt.typeCategory)

    def test_requestListings(self):
        # Test case 1: Check if the listing name is set correctly
        listing_name = "Listing A"
        request_listing = requestListings(listingName=listing_name, bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A")
        self.assertEqual(request_listing.listingName, listing_name)

        # Test case 2: Check if the bottler is set correctly
        bottler = "Bottler A"
        request_listing = requestListings(listingName="Listing A", bottler=bottler, drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A")
        self.assertEqual(request_listing.bottler, bottler)

        # Test case 3: Check if the drink type is set correctly
        drink_type = "Drink Type A"
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType=drink_type, sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A")
        self.assertEqual(request_listing.drinkType, drink_type)

        # Test case 4: Check if the source link is set correctly
        source_link = "Source Link A"
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink=source_link, brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A")
        self.assertEqual(request_listing.sourceLink, source_link)

        # Test case 5: Check if the brand relation is set correctly
        brand_relation = "Brand Relation A"
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation=brand_relation, reviewStatus=True, userID=object(), photo="Photo A")
        self.assertEqual(request_listing.brandRelation, brand_relation)

        # Test case 6: Check if the review status is set correctly
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A")
        self.assertTrue(request_listing.reviewStatus)

        # Test case 7: Check if the user ID is set correctly
        user_id = object()
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=user_id, photo="Photo A")
        self.assertEqual(request_listing.userID, user_id)

        # Test case 8: Check if the photo is set correctly
        photo = "Photo A"
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo=photo)
        self.assertEqual(request_listing.photo, photo)

        # Test case 9: Check if the optional fields are set correctly
        producer_new = "Producer New A"
        producer_id = object()
        origin_country = "Origin Country A"
        type_category = "Type Category A"
        age = "Age A"
        abv = "ABV A"
        review_link = "Review Link A"
        request_listing = requestListings(listingName="Listing A", bottler="Bottler A", drinkType="Drink Type A", sourceLink="Source Link A", brandRelation="Brand Relation A", reviewStatus=True, userID=object(), photo="Photo A", producerNew=producer_new, producerID=producer_id, originCountry=origin_country, typeCategory=type_category, age=age, abv=abv, reviewLink=review_link)
        self.assertEqual(request_listing.producerNew, producer_new)
        self.assertEqual(request_listing.producerID, producer_id)
        self.assertEqual(request_listing.originCountry, origin_country)
        self.assertEqual(request_listing.typeCategory, type_category)
        self.assertEqual(request_listing.age, age)
        self.assertEqual(request_listing.abv, abv)
        self.assertEqual(request_listing.reviewLink, review_link)

    

    def test_requestEdits(self):
        # Test case 1: Check if the edit description is set correctly
        edit_desc = "Edit Description A"
        request_edit = requestEdits(editDesc=edit_desc, brandRelation="Brand Relation A", listingID=object(), userID=object(), reviewStatus=True)
        self.assertEqual(request_edit.editDesc, edit_desc)

        # Test case 2: Check if the brand relation is set correctly
        brand_relation = "Brand Relation A"
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation=brand_relation, listingID=object(), userID=object(), reviewStatus=True)
        self.assertEqual(request_edit.brandRelation, brand_relation)

        # Test case 3: Check if the listing ID is set correctly
        listing_id = object()
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=listing_id, userID=object(), reviewStatus=True)
        self.assertEqual(request_edit.listingID, listing_id)

        # Test case 4: Check if the user ID is set correctly
        user_id = object()
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=object(), userID=user_id, reviewStatus=True)
        self.assertEqual(request_edit.userID, user_id)

        # Test case 5: Check if the review status is set correctly
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=object(), userID=object(), reviewStatus=True)
        self.assertTrue(request_edit.reviewStatus)

        # Test case 6: Check if the duplicate link is set correctly
        duplicate_link = "Duplicate Link A"
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=object(), userID=object(), reviewStatus=True, duplicateLink=duplicate_link)
        self.assertEqual(request_edit.duplicateLink, duplicate_link)

        # Test case 7: Check if the source link is set correctly
        source_link = "Source Link A"
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=object(), userID=object(), reviewStatus=True, sourceLink=source_link)
        self.assertEqual(request_edit.sourceLink, source_link)

        # Test case 8: Check if the optional fields are set correctly
        request_edit = requestEdits(editDesc="Edit Description A", brandRelation="Brand Relation A", listingID=object(), userID=object(), reviewStatus=True)
        self.assertIsNone(request_edit.duplicateLink)
        self.assertIsNone(request_edit.sourceLink)

    def test_modRequests(self):
        # Test case 1: Check if the userID is set correctly
        user_id = object()
        mod_request = modRequests(userID=user_id, drinkType="Drink Type A", modDesc="Mod Description A")
        self.assertEqual(mod_request.userID, user_id)

        # Test case 2: Check if the drink type is set correctly
        drink_type = "Drink Type A"
        mod_request = modRequests(userID=object(), drinkType=drink_type, modDesc="Mod Description A")
        self.assertEqual(mod_request.drinkType, drink_type)

        # Test case 3: Check if the mod description is set correctly
        mod_desc = "Mod Description A"
        mod_request = modRequests(userID=object(), drinkType="Drink Type A", modDesc=mod_desc)
        self.assertEqual(mod_request.modDesc, mod_desc)

    # TEST FOR PRESENCE OF HASHED PASSWORD
    

    

    

    
if __name__ == '__main__':
    unittest.main()


