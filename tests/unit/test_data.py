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
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"])
        self.assertEqual(producer.producerName, "Producer A")

        # Test case 2: Check if the producer description is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"])
        self.assertEqual(producer.producerDesc, "Description A")

        # Test case 3: Check if the origin country is set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"])
        self.assertEqual(producer.originCountry, "USA")

        # Test case 4: Check if the main drinks are set correctly
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"])
        self.assertEqual(producer.mainDrinks, ["Drink A", "Drink B"])

        # Test case 5: Check if the optional statusOB is None when not provided
        producer = producers(producerName="Producer A", producerDesc="Description A", originCountry="USA", mainDrinks=["Drink A", "Drink B"])
        self.assertIsNone(producer.statusOB)

    
    def test_reviews(self):
        # Test case 1: Check if the userID is set correctly
        user_id = object()
        review = reviews(userID=user_id, reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.userID, user_id)

        # Test case 2: Check if the review target is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.reviewTarget, "Product A")

        # Test case 3: Check if the date is set correctly
        now = datetime.now()
        review = reviews(userID=object(), reviewTarget="Product A", date=now, rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.date, now)

        # Test case 4: Check if the rating is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.rating, 5)

        # Test case 5: Check if the review description is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.reviewDesc, "Great product")

        # Test case 6: Check if the review title is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.reviewTitle, "Amazing")

        # Test case 7: Check if the review type is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.reviewType, "Positive")

        # Test case 8: Check if the photo is set correctly
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertEqual(review.photo, "review.jpg")

        # Test case 9: Check if the tagged users is None when not provided
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertIsNone(review.taggedUsers)

        # Test case 10: Check if the flavor tag is None when not provided
        review = reviews(userID=object(), reviewTarget="Product A", date=datetime.now(), rating=5, reviewDesc="Great product", reviewTitle="Amazing", reviewType="Positive", photo="review.jpg")
        self.assertIsNone(review.flavorTag)


    # Add more test methods for other dataclasses here

if __name__ == '__main__':
    unittest.main()


