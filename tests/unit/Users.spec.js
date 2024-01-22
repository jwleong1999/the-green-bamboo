import { mount } from '@vue/test-utils';
import BottleListings from '../../src/views/Users/BottleListings.vue';


// COMMAND TO RUN TEST: npm run test:unit

// ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// -- [TGB-5] VIEW LISTINGS --
describe('View Listings', () => {

    // Sample reviews data
    const all_reviews = [
        {
            "_id":{"$oid":"65a65ad60719072d03e5c6cd"},
            "Username":"CharSiuCharlie",
            "Reviewed subject":"Harmony Collection Inspired by Intense Arabica",
            "Date":"1/25/2024",
            "Rating": 5,
            "Review Desc":"Best drink ever",
            "Taged Users":["111hotpot","lotursroot519"],
            "Review Title":"Sample review title"
        },
        {
            "_id":{"$oid":"65a65ad60719072d03e5c6ce"},
            "Username":"lotursroot519",
            "Reviewed subject":"Ube Cream Liqueur",
            "Date":"12/23/2023",
            "Rating": 4,
            "Review Desc":"Tasty drink",
            "Taged Users":[],
            "Review Title":"Sample review title"
        },
        {
            "_id":{"$oid":"65a65ad60719072d03e5c6cf"},
            "Username":"111hotpot",
            "Reviewed subject":"Junglebird",
            "Date":"2/5/2024",
            "Rating": 1,
            "Review Desc":"Poor Service",
            "Taged Users":["lotusroot518"],
            "Review Title":"Sample review title"
        },
        {
            "_id":{"$oid":"65a65ad60719072d03e5c6d0"},
            "Username":"111hotpot",
            "Reviewed subject":"Malt Grain Cane",
            "Date":"3/4/2024",
            "Rating": 3,
            "Review Desc":"Drinks are mediorce",
            "Taged Users":[],
            "Review Title":"Sample review title"
        },
        {
            "_id":{"$oid":"65a65ad60719072d03e5c6d1"},
            "Username":"lotursroot518",
            "Reviewed subject":"Nikka From The Barrel",
            "Date":"1/15/2022"
            ,"Rating": 2,
            "Review Desc":"Not very nice",
            "Taged Users":["111hotpot","CharSiuCharlie"],
            "Review Title":"Sample review title"
        }
    ];

    // - GET REVIEWS -
    describe('Get Reviews', () => {

        // Mock the fetchData method
        const fetchDataMock = jest.fn(() => Promise.resolve(all_reviews));

        // Get reviews of listing with reviews
        it('[Reviews returned] Get reviews of listing with reviews', () => {
            const wrapper = mount(BottleListings, {
                data() {
                    return {
                        reviews: all_reviews
                    };
                },
            });
            // Mock the listing data
            const listing = {
                                "_id":{"$oid":"65a65ad60719072d03e5c6cd"},
                                "Expression Name":"Harmony Collection Inspired by Intense Arabica",
                                "Producer":"The Macallan Distillery",
                                "Bottler (OB or Specify name of IB)":"OB",
                                "Country of Origin":"Scotland",
                                "Drink Type":"Whiskey / Whisky",
                                "Drink Category":"Single Malt",
                                "Age":"NAS",
                                "ABV":"44%",
                                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/the-macallan-harmony-collection-inspired-by-intense-arabica-single-malt-44-abv",
                                "Official Description":"The second edition in our limited annual release series, this special single malt exudes flavours of sweet oak, tiramisu and dark chocolate, and provides a delightful whisky and coffee pairing experience."
                            };
            // Mock the randomReview
            const randomReview = all_reviews[0];
            // Call the getReviews method
            const reviewDesc = wrapper.vm.getReviews(listing);
            expect(reviewDesc).toBe("Best drink ever");
        });

        // Get reviews of listing with no reviews
        it('[No reviews returned] Get reviews of listing with no reviews', () => {
            const wrapper = mount(BottleListings, {
                data() {
                    return {
                        reviews: all_reviews
                    };
                },
            });
            // Mock the listing data
            const listing = {
                                "_id":{"$oid":"65ab760933b616ccc14b9f6a"},
                                "Expression Name":"Ardbeg Ardcore",
                                "Producer":"Ardbeg Distillery",
                                "Bottler (OB or Specify name of IB)":"OB",
                                "Country of Origin":"Scotland",
                                "Drink Type":"Whiskey / Whisky",
                                "Drink Category":"Single Malt",
                                "Age":"NAS",
                                "ABV":"46%",
                                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/ardbeg-ardcore-46-abv",
                                "Official Description":"From a Distillery with more ups and downs that a pogoing punk comes Ardcore. Created with roasted black malt, roasted to the extreme, this spirit is all about what happens up front & centre stage. The malt is what defines its distinctive profile. Described as tasting like ‘biting on a spiky ball’, Ardcore is a dram that wears its heart on its sleeve… its black heart!"
                            };
            // Mock the randomReview
            const randomReview = {};
            // Call the getReviews method
            const reviewDesc = wrapper.vm.getReviews(listing);
            expect(reviewDesc).toBe(null);
        });

    });

    // - GET RATINGS -
    describe('Get Ratings', () => {

        // Mock the fetchData method
        const fetchDataMock = jest.fn(() => Promise.resolve(all_reviews));

        // Get reviews of listing with ratings
        it('[Ratings returned] Get reviews of listing with ratings', () => {
            const wrapper = mount(BottleListings, {
                data() {
                    return {
                        reviews: all_reviews
                    };
                },
            });
            // Mock the listing data
            const listing = {
                                "_id":{"$oid":"65ab760933b616ccc14b9f69"},
                                "Expression Name":"Nikka From The Barrel",
                                "Producer":"Nikka Whisky",
                                "Bottler (OB or Specify name of IB)":"OB",
                                "Country of Origin":"Japan",
                                "Drink Type":"Whiskey / Whisky",
                                "Drink Category":"Blended",
                                "Age":"NAS",
                                "ABV":"51%",
                                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/nikka-from-the-barrel",
                                "Official Description":"This strong Japanese blend aged in bourbon barrels comes from the blend of two Nikka single malts Miyagikyo and Yoichi and a single grain whisky. Nikka from the Barrel was chosen best Japanese blended whisky under 12 years old at the World Whiskies Awards 2007."
                            }
            // Mock the ratings data
            const ratings = {
                                "_id":{"$oid":"65ab760933b616ccc14b9f69"},
                                "Expression Name":"Nikka From The Barrel",
                                "Producer":"Nikka Whisky",
                                "Bottler (OB or Specify name of IB)":"OB",
                                "Country of Origin":"Japan",
                                "Drink Type":"Whiskey / Whisky",
                                "Drink Category":"Blended",
                                "Age":"NAS",
                                "ABV":"51%",
                                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/nikka-from-the-barrel",
                                "Official Description":"This strong Japanese blend aged in bourbon barrels comes from the blend of two Nikka single malts Miyagikyo and Yoichi and a single grain whisky. Nikka from the Barrel was chosen best Japanese blended whisky under 12 years old at the World Whiskies Awards 2007."
                            }
            // Call the getRatings method
            const averageRating = wrapper.vm.getRatings(listing);
            expect(averageRating).toBe(2);
        });

        // Get reviews of listing with no ratings
        it('[No ratings returned] Get reviews of listing with no ratings', () => {
            const wrapper = mount(BottleListings, {
                data() {
                    return {
                        reviews: all_reviews
                    };
                },
            });
            // Mock the listing data
            const listing = {
                                "_id":{"$oid":"65a65ad60719072d03e5c6ce"},
                                "Username":"lotursroot519",
                                "Reviewed subject":"Ube Cream Liqueur",
                                "Date":"12/23/2023",
                                "Rating": 4,
                                "Review Desc":"Tasty drink",
                                "Taged Users":[],
                                "Review Title":"Sample review title"
                            }
            // Mock the ratings data
            const ratings = {}
            // Call the getRatings method
            const averageRating = wrapper.vm.getRatings(listing);
            expect(averageRating).toBe("-");
        });

    });

});

// ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// --- [TGB-6] SEARCH LISTINGS ---
describe('Search Listings', () => {
    // Sample listings data
    const all_listings = [
        {
            "_id":{"$oid":"65ad1b67ce3fc2aff52a874b"},
            "Expression Name":"Harmony Collection Inspired by Intense Arabica",
            "Producer":"The Macallan Distillery",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"Scotland",
            "Drink Type":"Whiskey / Whisky",
            "Drink Category":"Single Malt",
            "Age":"NAS",
            "ABV":"44%",
            "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/the-macallan-harmony-collection-inspired-by-intense-arabica-single-malt-44-abv",
            "Official Description":"The second edition in our limited annual release series, this special single malt exudes flavours of sweet oak, tiramisu and dark chocolate, and provides a delightful whisky and coffee pairing experience."
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9f69"},
            "Expression Name":"Nikka From The Barrel",
            "Producer":"Nikka Whisky",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"Japan",
            "Drink Type":"Whiskey / Whisky",
            "Drink Category":"Blended",
            "Age":"NAS",
            "ABV":"51%",
            "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/nikka-from-the-barrel",
            "Official Description":"This strong Japanese blend aged in bourbon barrels comes from the blend of two Nikka single malts Miyagikyo and Yoichi and a single grain whisky. Nikka from the Barrel was chosen best Japanese blended whisky under 12 years old at the World Whiskies Awards 2007."
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9f6a"},
            "Expression Name":"Ardbeg Ardcore",
            "Producer":"Ardbeg Distillery",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"Scotland",
            "Drink Type":"Whiskey / Whisky",
            "Drink Category":"Single Malt",
            "Age":"NAS",
            "ABV":"46%",
            "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/ardbeg-ardcore-46-abv",
            "Official Description":"From a Distillery with more ups and downs that a pogoing punk comes Ardcore. Created with roasted black malt, roasted to the extreme, this spirit is all about what happens up front & centre stage. The malt is what defines its distinctive profile. Described as tasting like ‘biting on a spiky ball’, Ardcore is a dram that wears its heart on its sleeve… its black heart!"
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9fb7"},
            "Expression Name":"Clase Azul Tequila Reposado",
            "Producer":"Clase Azul",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"Mexico",
            "Drink Type":"Tequila",
            "Drink Category":"Reposado",
            "Age":"",
            "ABV":"40%",
            "88B Website Review (if applicable)":"https://88bamboo.co/blogs/tequila-mezcal-reviews/clase-azul-tequila-reposado-40-abv",
            "Official Description":""
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9fbb"},
            "Expression Name":"Tequila Tapatio Excelencia Extra Anejo",
            "Producer":"Tapatio",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"Mexico",
            "Drink Type":"Tequila",
            "Drink Category":"Extra Anejo",
            "Age":"",
            "ABV":"40%",
            "88B Website Review (if applicable)":"https://88bamboo.co/blogs/tequila-mezcal-reviews/tequila-tapatio-excelencia-extra-anejo",
            "Official Description":""
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9f7f"},
            "Expression Name":"Fords Gin",
            "Producer":"Fords Gin",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"United Kingdom",
            "Drink Type":"Gin",
            "Drink Category":"London Dry / Classic",
            "Age":"",
            "ABV":"45%",
            "88B Website Review (if applicable)":"",
            "Official Description":"Fords Gin is found in the very best gin joints around the world, from iconic hotel bars to frequently visited neighborhood spots. Created with respect to the traditions that have historically defined gin making, this classic London Dry is keen for all your cocktail adventures."
        },
        {
            "_id":{"$oid":"65ab760933b616ccc14b9f80"},
            "Expression Name":"Fords Gin Officers' Reserve",
            "Producer":"Fords Gin",
            "Bottler (OB or Specify name of IB)":"OB",
            "Country of Origin":"United Kingdom",
            "Drink Type":"Gin",
            "Drink Category":"London Dry / Classic",
            "Age":"",
            "ABV":"55%",
            "88B Website Review (if applicable)":"",
            "Official Description":"Over-proof gin was traditionally reserved for officers of the British Royal Navy. Today, it’s for everyone! Fords Gin Officers’ Reserve is rested and aged in Amontillado Sherry casks for three weeks. Characteristics of the barrel’s wood shape the spirit’s flavour. It is then bottled at 54.5 ABV. This limited release is Fords Gin’s first Journey in Gin as a homage to the Navy Strength Gin category."
        }
    ];

    // Mock the fetchData method
    const fetchDataMock = jest.fn(() => Promise.resolve(all_listings));

    // Search for bottle listing based on Expression Name
    it('[Listings returned] Search for bottle listing based on Expression Name', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: 'Tequila'
                };
            },
        });
        // Call the searchListings method
        wrapper.vm.searchListings();
        expect(wrapper.vm.filteredListings).toEqual([
            {
                "_id":{"$oid":"65ab760933b616ccc14b9fb7"},
                "Expression Name":"Clase Azul Tequila Reposado",
                "Producer":"Clase Azul",
                "Bottler (OB or Specify name of IB)":"OB",
                "Country of Origin":"Mexico",
                "Drink Type":"Tequila",
                "Drink Category":"Reposado",
                "Age":"",
                "ABV":"40%",
                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/tequila-mezcal-reviews/clase-azul-tequila-reposado-40-abv",
                "Official Description":""
            },
            {
                "_id":{"$oid":"65ab760933b616ccc14b9fbb"},
                "Expression Name":"Tequila Tapatio Excelencia Extra Anejo",
                "Producer":"Tapatio",
                "Bottler (OB or Specify name of IB)":"OB",
                "Country of Origin":"Mexico",
                "Drink Type":"Tequila",
                "Drink Category":"Extra Anejo",
                "Age":"",
                "ABV":"40%",
                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/tequila-mezcal-reviews/tequila-tapatio-excelencia-extra-anejo",
                "Official Description":""
            }
        ]);
    });

        // Search for bottle listing based on Expression Name, regardless of case
        it('[Listings returned] Search for bottle listing based on Expression Name, regardless of case', () => {
            const wrapper = mount(BottleListings, {
                data() {
                    return {
                        listings: all_listings,
                        searchInput: 'mAcAllan'
                    };
                },
            });
            // Call the searchListings method
            wrapper.vm.searchListings();
            expect(wrapper.vm.filteredListings).toEqual([
                {
                    "_id":{"$oid":"65ad1b67ce3fc2aff52a874b"},
                    "Expression Name":"Harmony Collection Inspired by Intense Arabica",
                    "Producer":"The Macallan Distillery",
                    "Bottler (OB or Specify name of IB)":"OB",
                    "Country of Origin":"Scotland",
                    "Drink Type":"Whiskey / Whisky",
                    "Drink Category":"Single Malt",
                    "Age":"NAS",
                    "ABV":"44%",
                    "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/the-macallan-harmony-collection-inspired-by-intense-arabica-single-malt-44-abv",
                    "Official Description":"The second edition in our limited annual release series, this special single malt exudes flavours of sweet oak, tiramisu and dark chocolate, and provides a delightful whisky and coffee pairing experience."
                }
            ]);
        });

    // Search for bottle listing based on Producer
    it('[Listings returned] Search for bottle listing based on Producer', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: 'Fords Gin'
                };
            },
        });
        // Call the searchListings method
        wrapper.vm.searchListings();
        expect(wrapper.vm.filteredListings).toEqual([
            {
                "_id":{"$oid":"65ab760933b616ccc14b9f7f"},
                "Expression Name":"Fords Gin",
                "Producer":"Fords Gin",
                "Bottler (OB or Specify name of IB)":"OB",
                "Country of Origin":"United Kingdom",
                "Drink Type":"Gin",
                "Drink Category":"London Dry / Classic",
                "Age":"",
                "ABV":"45%",
                "88B Website Review (if applicable)":"",
                "Official Description":"Fords Gin is found in the very best gin joints around the world, from iconic hotel bars to frequently visited neighborhood spots. Created with respect to the traditions that have historically defined gin making, this classic London Dry is keen for all your cocktail adventures."
            },
            {
                "_id":{"$oid":"65ab760933b616ccc14b9f80"},
                "Expression Name":"Fords Gin Officers' Reserve",
                "Producer":"Fords Gin",
                "Bottler (OB or Specify name of IB)":"OB",
                "Country of Origin":"United Kingdom",
                "Drink Type":"Gin",
                "Drink Category":"London Dry / Classic",
                "Age":"",
                "ABV":"55%",
                "88B Website Review (if applicable)":"",
                "Official Description":"Over-proof gin was traditionally reserved for officers of the British Royal Navy. Today, it’s for everyone! Fords Gin Officers’ Reserve is rested and aged in Amontillado Sherry casks for three weeks. Characteristics of the barrel’s wood shape the spirit’s flavour. It is then bottled at 54.5 ABV. This limited release is Fords Gin’s first Journey in Gin as a homage to the Navy Strength Gin category."
            }
        ]);
    });

    // Search for bottle listing based on Producer, regardless of case
    it('[Listings returned] Search for bottle listing based on Producer, regardless of case', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: 'niKKA fROM the BARrel'
                };
            },
        });
        // Call the searchListings method
        wrapper.vm.searchListings();
        expect(wrapper.vm.filteredListings).toEqual([
            {
                "_id":{"$oid":"65ab760933b616ccc14b9f69"},
                "Expression Name":"Nikka From The Barrel",
                "Producer":"Nikka Whisky",
                "Bottler (OB or Specify name of IB)":"OB",
                "Country of Origin":"Japan",
                "Drink Type":"Whiskey / Whisky",
                "Drink Category":"Blended",
                "Age":"NAS",
                "ABV":"51%",
                "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/nikka-from-the-barrel",
                "Official Description":"This strong Japanese blend aged in bourbon barrels comes from the blend of two Nikka single malts Miyagikyo and Yoichi and a single grain whisky. Nikka from the Barrel was chosen best Japanese blended whisky under 12 years old at the World Whiskies Awards 2007."
            },
        ]);
    });

    // Search for specific bottle listings that do not exist
    it('[No listings returned] Search for specific bottle listings that do not exist', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: 'nothing'
                };
            },
        });
        // Call the searchListings method
        wrapper.vm.searchListings();
        expect(wrapper.vm.searchResults).toStrictEqual([]);
    });

    // Search for nothing (blank input)
    it('[No listings returned] Search for nothing (blank input)', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: ''
                };
            },
        });
        // Call the searchListings method
        wrapper.vm.searchListings();
        expect(wrapper.vm.searchResults).toStrictEqual([]);
    });
});

// ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------