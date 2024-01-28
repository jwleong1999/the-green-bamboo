<!-- Component for fetching data. Calls loadData() and returns it in relevantly named lists. -->
<!-- Does not include VenuesAPI, drinkTypes, requestListings, requestEdits, modRequests. -->
<!-- TODO: Check potentially outdated API link. -->

<script>
    export default {
        name: "FetchData",
        data() {
            return {
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                drinkCategories: [],
            }
        },
        methods: {
            // load data from database
            async loadData() {
                // Countries
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                    this.countries = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Listings
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                    this.listings = response.data;
                    // originally, make filteredListings the entire collection of listings
                    this.filteredListings = this.listings;
                } 
                catch (error) {
                    console.error(error);
                }
                // Producers
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                    this.producers = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Reviews
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                    this.reviews = response.data;
                }
                catch (error) {
                    console.error(error);
                }
                // Users
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                    this.users = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Venues
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                    this.venues = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Drink Categories
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkCategories'); // Outdated? Please check.
                    this.drinkCategories = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
            },

        }
    }
</script>