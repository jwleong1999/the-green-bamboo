import { mount } from '@vue/test-utils';
import BottleListings from '../../src/views/Users/BottleListings.vue';


// COMMAND TO RUN TEST: npm run test:unit

// ------- SEARCH BOTTLE LISTINGS -------
describe('Search Listings', () => {
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
        }
    ];

    // Mock the fetchData method
    const fetchDataMock = jest.fn(() => Promise.resolve(all_listings));

    // // Search input matches listings
    // it('returns listings that match the search input', () => {
    //     const wrapper = mount(BottleListings, {
    //         data() {
    //             return {
    //                 listings: all_listings,
    //                 searchInput: 'Macallan'
    //             };
    //         },
    //     });

    //     // Log initial state
    //     console.log('Initial state:', {
    //         searchInput: wrapper.vm.searchInput,
    //         listingsWithID: wrapper.vm.listingsWithID,
    //         searchResults: wrapper.vm.searchResults,
    //         filteredListings: wrapper.vm.filteredListings,
    //     });

    //     // Call the searchListings method
    //     wrapper.vm.searchInput = 'Macallan';
    //     wrapper.vm.searchListings();

    //     // Log state after calling searchListings
    //     console.log('State after calling searchListings:', {
    //         searchInput: wrapper.vm.searchInput,
    //         listingsWithID: wrapper.vm.listingsWithID,
    //         searchResults: wrapper.vm.searchResults,
    //         filteredListings: wrapper.vm.filteredListings,
    //     });


    //     expect(wrapper.vm.filteredListings).toEqual([
    //         {
    //             "_id":{"$oid":"65ab760933b616ccc14b9f69"},
    //             "Expression Name":"Nikka From The Barrel",
    //             "Producer":"Nikka Whisky",
    //             "Bottler (OB or Specify name of IB)":"OB",
    //             "Country of Origin":"Japan",
    //             "Drink Type":"Whiskey / Whisky",
    //             "Drink Category":"Blended",
    //             "Age":"NAS",
    //             "ABV":"51%",
    //             "88B Website Review (if applicable)":"https://88bamboo.co/blogs/whisky-reviews/nikka-from-the-barrel",
    //             "Official Description":"This strong Japanese blend aged in bourbon barrels comes from the blend of two Nikka single malts Miyagikyo and Yoichi and a single grain whisky. Nikka from the Barrel was chosen best Japanese blended whisky under 12 years old at the World Whiskies Awards 2007."
    //         }
    //     ]);
    // });

    // Search input does not match listings
    it('returns no listings that match the search input', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: 'lol'
                };
            },
        });
        wrapper.vm.searchListings();
        expect(wrapper.vm.searchResults).toStrictEqual([]);
    });

    // No search input
    it('returns no listings that match the search input', () => {
        const wrapper = mount(BottleListings, {
            data() {
                return {
                    listings: all_listings,
                    searchInput: ''
                };
            },
        });
        wrapper.vm.searchListings();
        expect(wrapper.vm.searchResults).toStrictEqual([]);
    });
});

