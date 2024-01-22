<!-- HTML -->
<template>
    <!-- navbar-->
    <div class="navbar-container">
        <nav class="navbar p-2">
            <div class="navbar-inner-container container-fluid d-flex align-items-center justify-content-between">
                <!-- logo -->
                <div class="navbar-brand d-flex align-items-center" href="../login/index.html"> 
                    <img src="../../../Images/Logo/88 Bamboo.png" style="width: 70px; height: 70px;">
                </div>
                <!-- search bar -->
                <div class="col-md-6">
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="searchListings"> 
                </div>
                <div>
                    <!-- profile icon -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                    </svg>
                    <!-- collapsible button -->
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </div>
            </div>
        </nav>
    </div>
    <!-- collapsible content -->
    <div class="collapse" id="navbarToggleExternalContent"> <!-- TODO: check what content to put here -->
        <div class="p-4">
            <h5 class="text-body-emphasis h4">Collapsed content</h5>
            <span class="text-body-secondary">Toggleable via the navbar brand.</span>
        </div>
    </div>

     <!-- [if] no search input -->
    <div>
        <!-- header -->

        <!-- end of header -->

        <!-- main content -->
        <div class="container pt-3">
            <div class="row">
                <!-- your drinks shelf & brands you follow -->
                
                <!-- discover, following & filter by drink type -->
                <div class="col-9">
                    <div class="container">
                        <!-- buttons -->
                        <div class="row">
                            <!-- discover -->
                            <div class="col-4">
                                <div class="d-grid gap-2">
                                    <router-link :to="{ path: '/Producer/Producer-Create-Listing' }">
                                        <button class="btn primary-btn btn-sm">
                                            <h4> Add </h4>
                                        </button>
                                    </router-link>
                                </div>
                            </div>
                          
                        </div>

                        <!-- listings -->
                        <div class="row">
                            <!-- v-loop for each listing -->
                            <div v-if="updateStatus == false" class="container text-start">
                                <div class="p-3">

                                    <div class="row">
                                        <!-- image -->
                                        <div class="col-4 image-container">
                                            <img src="../../../Images/Sample/beer.png" style="width: 300px; height: 300px;" class="img-border">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark overlay-icon" viewBox="0 0 16 16">
                                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                            </svg>
                                        </div>
                                        <!-- details -->
                                        <div class="col-8 ps-5">
                                            <!-- review -->
                                            <div class="row">
                                                <a class="default-clickable-text fst-italic scrollable">
                                                    <h5> "{{ getReviews(editable) }}". </h5>
                                                </a>
                                            </div>
                                            <!-- rating -->
                                            <div class="row pt-5"> 
                                                <div class="col-6">
                                                    <h1 class="rating-text">
                                                        {{ getRatings(editable) }}
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                        </svg>
                                                    </h1>
                                                </div>
                                                <div class="col-6">
                                                    <a class="btn secondary-btn btn-md" @click="updateListing" > Edit </a>
                                                    <a class="btn secondary-btn btn-md" @click="temp" > temp </a>

                                                </div>
                                            </div>
                                            <!-- expression name -->
                                            <div class="row pt-2">
                                                <a class="primary-clickable-text">
                                                    <h4> <b> {{ editable["Expression Name"] }} </b> </h4>
                                                </a>
                                            </div>
                                            <!-- producer -->
                                            <div class="row">
                                                <h5> {{ editable["Producer"] }} </h5> 
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="container text-start">
                                <div class="p-3">

                                    <div class="row">
                                        <!-- image -->
                                        <div class="col-4 image-container">
                                            <img src="../../../Images/Sample/beer.png" style="width: 300px; height: 300px;" class="img-border">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark overlay-icon" viewBox="0 0 16 16">
                                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                            </svg>
                                        </div>
                                        <!-- details -->
                                        <div class="col-8 ps-5">
                                            <!-- review -->
                                            <label for="input">Enter Lisitng Name:</label>
                                            <div class="row">
                                                <div class="mb-3">
                                                    <input type="Expression Name" class="form-control" id="exampleFormControlInput1" v-model="tempExpressionName">
                                                </div>
                                            </div>
                                            <div class="row">
                                                <label for="input">Enter Bottler Name:</label>
                                                <div class="mb-3">
                                                    <input type="Bottler Name" class="form-control" id="exampleFormControlInput1" v-model="tempBottler">
                                                </div>
                                            </div>
                                            <div class="row">
                                                
                                                <div class="col-md-6 mb-3">
                                                    <label for="dropdown">Select Country of Origin:</label>
                                                    <div class="input-group">
                                                        
                                                        <select class="form-select" id="inputGroupSelect01">
                                                            <option selected>{{this.tempCountry }}</option>
                                                            <option v-for="country in countries" :key="country['Country Name']" :value="country['Country Name']">
                                                            {{ country['Country of Origin']  }}
                                                        </option>
                                                        </select>
                                                    </div>
                                                </div>

                                                <div class="col-md-6 mb-3">
                                                    <label for="dropdown">Select Drink Type:</label>
                                                    <div class="input-group">
                                                        <select class="form-select" id="inputGroupSelect01">
                                                            <option selected>{{this.tempDrinkType }}</option>
                                                            <option v-for="taste in drinkCategories" :key="taste['Drink Type']" :value="taste['Drink Type']">
                                                            {{ taste['Drink Type']  }}
                                                            </option>
                                                        </select>

                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <label for="dropdown">Select Drink Category:</label>
                                                <div class="input-group mb-3">
                                                    
                                                    <select class="form-select" id="inputGroupSelect01">
                                                        <option selected>Drink Category</option>
                                                        <option v-for="taste in drinkCategories" :key="taste['Drink Type']" :value="taste['Drink Type']">
                                                            {{ taste }}
                                                        </option>
                                                    </select>
                                                </div>
                                            </div>

                                            <div class="row ">
                                                <label for="input">Enter Bottle Age :</label>
                                                <div class="col-md-6 mb-3">
                                                    <input type="Expression Name" class="form-control" id="age" v-model="tempAge">
                                                </div>
                                                
                                                <label for="input">Enter Bottle ABV (%):</label>
                                                <div class="col-md-6 mb-3">
                                                    <input type="Expression Name" class="form-control" id="abv" v-model="tempABV">
                                                </div>
                                                
                                            </div>
                                            <div class="mb-3">
                                                <label for="input">Enter Review Link (if available):</label>
                                                <input type="Expression Name" class="form-control" id="exampleFormControlInput1" v-model="tempReviewLink">
                                            </div>
                                            <div class="mb-3">
                                                <label for="input">Enter Bottle Description:</label>
                                                <input type="Expression Name" class="form-control" id="exampleFormControlInput1" v-model="tempDescription">
                                            </div>

                                            
                                            
                                            <!-- <div class="row">
                                                <div class="col-md-6">
                                                    <label for="dropdown">Select Option:</label>
                                                    <div class="input-group">
                                                        <select class="form-select" id="inputGroupSelect01">
                                                            <option selected>Drink Type</option>
                                                            <option value="1">One</option>
                                                            <option value="2">Two</option>
                                                            <option value="3">Three</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label for="dropdown">Select Option:</label>
                                                    <div class="input-group">
                                                        <select class="form-select" id="inputGroupSelect01">
                                                            <option selected>Drink Category</option>
                                                            <option value="1">One</option>
                                                            <option value="2">Two</option>
                                                            <option value="3">Three</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div> -->
                                            <!-- rating -->
                                            <div class="row pt-5"> 
                                                
                                                <div class="col-6">
                                                    <a class="btn secondary-btn btn-md" @click="saveListing" > Save </a>
                                                </div>
                                            </div>
                                            <!-- expression name -->
                                            
                                            <!-- producer -->
                                            
                                        </div>
                                    </div>
                                </div>
                                
                                
                            </div>
                        </div> <!-- end of listings -->
                    </div> <!-- end of container -->
                </div> <!-- end of discover, following & filter by drink type -->
            </div> <!-- end of row -->
        </div>
    </div>
    

    

</template>



<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    export default {
        data() {
            return {
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                editable: [],
                drinkCategories:[],
                updateStatus: false,
                tempExpressionName: '',
                tempProducer: '',
                tempCountry: '',
                tempDrinkType: '',
                tempDrinkCategory: '',
                tempAge: '',
                tempABV: '',
                tempReviewLink: '',
                tempDescription: '',
                tempBottler: ''


                
            };
        },
        mounted() {
            this.loadData();
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
                    this.editable = this.listings[0];
                    this.tempExpressionName = this.editable["Expression Name"];
                    this.tempProducer = this.editable["Producer"];
                    this.tempCountry = this.editable["Country of Origin"];
                    this.tempDrinkType = this.editable["Drink Type"];
                    this.tempDrinkCategory = this.editable["Drink Category"];
                    this.tempAge = this.editable["Age"];
                    this.tempABV = this.editable["ABV"];
                    this.tempReviewLink = this.editable["88B Website Review (if applicable)"];
                    this.tempDescription = this.editable["Official Description"];
                    this.tempBottler = this.editable["Bottler (OB or Specify name of IB)"];
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
                    const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkCategories');
                    this.drinkCategories = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
            },

            updateListing() {
                this.updateStatus = true;
            },

            saveListing() {
                this.updateStatus = false;
            },
            temp() {
                console.log(this.drinkCategories);
            },

            // for search button
            searchListings() {

                // flag to check if there are search inputs
                this.search = true;

                const searchInput = this.searchInput.toLowerCase();
                this.searchTerm = this.searchInput;

                // if there is something searched
                const searchResults = this.listings.filter((listing) => {
                    const expressionName = listing["Expression Name"].toLowerCase();
                    const producer = listing["Producer"].toLowerCase();
                    return expressionName.includes(searchInput) || producer.includes(searchInput);
                });

                console.log(searchResults)

                // if nothing found
                if (searchResults.length == 0) {
                    this.errorFound = true;
                    this.errorMessage = 'No results found, please try again.';
                } 
                else {
                    this.errorFound = false;
                    this.errorMessage = '';
                    this.filteredListings = searchResults;
                }

                // if there is nothing searched
                if (this.searchInput == '') {
                    this.resetListings();
                }
            },

            // for resetting listings (show full listings)
            resetListings() {
                this.filteredListings = this.listings;
                this.search = false;
                this.searchInput = '';
            },

            // get reviews for a listing
            getReviews(listing) {
                // list of all reviews of the particular drink
                const reviews = this.reviews.filter((review) => {
                    return review["Reviewed subject"] == listing["Expression Name"];
                });
                // choose random review from the list
                const randomReview = reviews[Math.floor(Math.random() * reviews.length)];
                // check if a review is found before accessing "Review Desc"
                const reviewDesc = randomReview ? randomReview["Review Desc"] : null;
                return reviewDesc;
            },

            // get ratings for a listing
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["Reviewed subject"] == listing["Expression Name"];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["Rating"];
                }, 0) / ratings.length;
                // Format the averageRating to 1 decimal place
                const formattedRating = parseFloat(averageRating.toFixed(1));
                return formattedRating;
            }
        },
    };
</script>


