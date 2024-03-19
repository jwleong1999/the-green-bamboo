<!-- Search page from navigation bar. Globally available, and should still use NavBar for new search queries. -->

<template>
    <NavBar />
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when search is in progress -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="!dataLoaded"> 
            <span>Currently searching, please hold on!</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when searching encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="loadError"> 
            <span>An error occurred while searching, please try refreshing the page!</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="()=>{this.$router.go(0)}">
                <span class="fs-5 fst-italic"> Refresh Page </span>
            </button>
        </div>

        <!-- Display requests after data loaded -->
        <div v-if="dataLoaded && !loadError">

            <div class="row">
                
                <!-- Back Button -->
                <div class="d-grid col-sm-1 col-2">
                    <button class="btn primary-light-dropdown btn-sm" @click="()=>{this.$router.go(-1)}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16" v-on:click="previousListing">
                            <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                        </svg>
                    </button>
                </div>

                <!-- Form Title -->
                <div class="d-grid col-lg-4 col-md-5 col-sm-6 col-10">
                    <p class="fw-bold fs-3 m-0 text-start">Search Results for:</p>
                </div>

                <!-- Spacer Column -->
                <div class="d-md-grid d-none col-lg-3"></div>

                <!-- Filter Options: On smaller screens, this is "moved below" Search Term -->
                <div class="d-sm-grid d-none col-lg-2 col-md-3 dropdown">
                    <button class="btn primary-light-dropdown dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                        Filter: {{ searchFilter.drinkType != '' ? searchFilter.drinkType : 'by Drink Type' }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><span class="dropdown-item" @click="filterByDrinkType('')">Clear Filter</span></li>
                        <li><hr class="dropdown-divider"></li>
                        <li v-for="drinkType in drinkTypeList" :key="drinkType._id">
                            <span class="dropdown-item" @click="filterByDrinkType(drinkType['drinkType'])">{{ drinkType['drinkType'] }}</span>
                        </li>
                    </ul>
                </div>

                <!-- Sort Options -->
                <div class="d-sm-grid d-none col-lg-2 col-md-3 dropdown">
                    <button class="btn primary-light-dropdown dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                        Sort: {{ sortSelection.category != '' ? sortSelection.category : 'by Category' }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><span class="dropdown-item" @click="sortByCategory('')"> Clear Sort </span></li>
                        <li><hr class="dropdown-divider"></li>
                        <li v-for="category in sortCategoryList" :key="category">
                            <span class="dropdown-item" @click="sortByCategory(category)"> {{ category }} </span>
                        </li>
                    </ul>
                </div>

            </div>

            <!-- Search Term -->
            <div class="row">
                <!-- Aligner Column (Back Button) -->
                <div class="col-sm-1 col-2"></div>

                <div class="col-sm-11 col-10">
                    <p class="fs-3 m-0 text-start" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">"{{ this.$route.params.input }}"</p>
                </div>
            </div>

            <!-- Filter Options: On larger screens, this is "moved above" Search Term -->
            <div class="row">
                <div class="d-grid d-sm-none col-12 dropdown">
                    <button class="btn primary-light-dropdown dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                        Filter: {{ searchFilter.drinkType != '' ? searchFilter.drinkType : 'by Drink Type' }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><span class="dropdown-item" @click="filterByDrinkType('')">Clear Filter</span></li>
                        <li><hr class="dropdown-divider"></li>
                        <li v-for="drinkType in drinkTypeList" :key="drinkType._id">
                            <span class="dropdown-item" @click="filterByDrinkType(drinkType['drinkType'])">{{ drinkType['drinkType'] }}</span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <!-- Request / Create Listing Link (font size reduced at smaller screen width) -->
            <div class="row">
                <router-link class="col-12 text-decoration-none" v-if="role == 'producer'" :to="{ path: '/Producer/Producer-Create-Listing/' }">
                    <p class="d-none d-md-block fs-5 fst-italic text-start">Don't see what you're looking for? Create a new listing here!</p>
                    <p class="d-md-none fs-6 fst-italic text-start">Don't see what you're looking for? Create a new listing here!</p>
                </router-link>
                <router-link class="col-12 text-decoration-none" v-if="role == 'user'" :to="{ path: '/request/new/' }">
                    <p class="d-none d-md-block fs-5 fst-italic text-start">Don't see what you're looking for? Request a new listing here!</p>
                    <p class="d-md-none fs-6 fst-italic text-start">Don't see what you're looking for? Request a new listing here!</p>
                </router-link>
                <router-link class="col-12 text-decoration-none" v-if="role != 'producer' && role != 'user'" :to="{ path: '/login' }">
                    <p class="d-none d-md-block fs-5 fst-italic text-start">Don't see what you're looking for? Login to request a new listing!</p>
                    <p class="d-md-none fs-6 fst-italic text-start">Don't see what you're looking for? Login to request a new listing!</p>
                </router-link>
            </div>

            <!-- Dropdown Buttons -->
            <!-- <hr>
            <p class="gap-1">
                <button class="btn primary-btn mx-1" type="button" data-bs-toggle="collapse" data-bs-target="#collapseListings" aria-expanded="false" aria-controls="collapseListings">
                    Listings
                </button>
            </p> -->
            
            <!-- Display Listings -->
            <div class="collapse show row" id="collapseListings">
                <hr>
                <p class="fw-bold fst-italic fs-5 m-0" v-if="resultListings.length > 0">Viewing: {{ resultListings.length }} Listing Search Results</p>
                <p class="fw-bold fst-italic fs-5 m-0" v-else>No Listing Results Found!</p>

                <div class="container pt-3 text-start">
                    <div class="row" v-for="resultListing in resultListings" :key="resultListing._id">
                        <hr>

                        <!-- Image -->
                        <div class="col-3 image-container-256">
                            <router-link :to="{ path: '/listing/view/' + resultListing._id['$oid'] }">
                                <img v-if="resultListing['photo']" :src="'data:image/png;base64,' + resultListing['photo']" class="img-border img-fluid object-fit-cover" style="width:256px; height:256px">
                                <img v-else src="../../Images/Drinks/Placeholder.png" class="img-border img-fluid object-fit-cover" style="width:256px; height:256px"> 
                            </router-link>
                            <BookmarkIcon 
                                v-if="user" 
                                :user="user" 
                                :listing="resultListing" 
                                :overlay="true"
                                size="30"
                                @icon-clicked="handleIconClick" />
                        </div>

                        <!-- Details -->
                        <div class="row col-9">

                            <div class="col-8">
                                <!-- Listing Name + Router Link -->
                                <router-link class="text-dark text-decoration-none" :to="{ path: '/listing/view/' + resultListing._id['$oid'] }">
                                    <h4 class="fw-bold">{{ resultListing['listingName'] }}</h4>
                                </router-link>
                                <!-- Producer Name + Router Link -->
                                <router-link class="text-secondary-emphasis text-decoration-none" :to="{ path: '/profile/producer/' + resultListing.producerID['$oid'] }">
                                    <h5 class="fw-bold mb-0">{{ resultListing['producerName'] }}</h5>
                                    <p class="fw-bold fst-italic" v-if="resultListing['bottler'] != 'OB'">Bottler: {{ resultListing['bottler'] }}</p>
                                </router-link>
                            </div>

                            <div class="col-4 text-end" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                <!-- Drink Type / Type Category -->
                                <p class="m-0">
                                    <b> Type: </b>
                                    {{ resultListing['drinkType'] }}
                                </p>
                                <p class="m-0" v-if="resultListing['typeCategory']">
                                    <b> Category: </b>
                                    {{ resultListing['typeCategory'] }}</p>
                                <!-- Country of Origin -->
                                <p class="m-0">
                                    <b> Origin: </b>
                                    {{ resultListing['originCountry'] }}
                                </p>
                                <!-- Added Date -->
                                <p class="m-0">
                                    <b> Date Added: </b>
                                    {{ formatDate(resultListing['addedDate'].$date) }}
                                </p>
                                <!-- Rating -->
                                <p class="d-flex justify-content-end">
                                    <b> Rating: </b> &nbsp;
                                    {{ getRatings(resultListing) }}
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </p>
                            </div>

                            <!-- Description -->
                            <p class="fst-italic scrollable-long">{{ resultListing["officialDesc"] }}</p>

                        </div>
                    </div>
                </div>
            </div>
            <BookmarkModal 
                v-if="user"
                :user="user" 
                :listings="listings" 
                :listingID="bookmarkListingID" />
        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import BookmarkIcon from '@/components/BookmarkIcon.vue';
    import BookmarkModal from '@/components/BookmarkModal.vue';

    export default {
        name: "SearchView",
        components: {
            NavBar,
            BookmarkIcon, 
            BookmarkModal
        },
        data() {
            return {
                dataLoaded: false,
                loadError: false,
                role: localStorage.getItem('88B_accType'),
                searchTerm: this.$route.params.input,
                searchFilter: {
                    drinkType: ''
                },
                drinkTypeList: [],
                producerList: [],
                originalResults: [],
                resultListings: [],
                listings: [],

                // reviews
                reviews: [],

                // for sort function
                sortSelection: {
                    category: ''
                },
                sortCategoryList: [
                                    'Alphabetical (A - Z)',
                                    'Alphabetical (Z - A)',
                                    'Date (Newest - Oldest)',
                                    'Date (Oldest - Newest)',
                                    'Ratings (Highest - Lowest)',
                                    'Ratings (Lowest - Highest)',
                                ],
                sortedListings: [],

                userID: "",
                userType: "",

                // for bookmark
                user: null,
                userBookmarks: [],

                // for bookmark component
                bookmarkListingID: {},
            }
        },
        mounted() {
            // Load local storage variables
            const accID = localStorage.getItem("88B_accID");
            if(accID !== null){
                this.userID = localStorage.getItem('88B_accID')
            }
            let userType = localStorage.getItem('88B_accType')
            if(userType !=null){
                this.userType = userType
            }

            // if there is a search input
            if (this.searchTerm != '' || this.searchTerm != null) {
                this.searchTerm = this.searchTerm.toLowerCase();
                this.runSearch();
            }
            else {
                this.$router.push({path: '/'});
            }
        },
        methods: {
            async runSearch() {
                // Search Criteria: if any of the following attributes includes the search term
                // - Listings: listingName, producerName, bottler, originCountry, drinkType, typeCategory
                // - [NOT IMPLEMENTED, TO BE CONSIDERED] Users: username, displayName
                // - [NOT IMPLEMENTED, TO BE CONSIDERED] Producers: producerName, originCountry
                // - [NOT IMPLEMENTED, TO BE CONSIDERED] Venues: venueName, originCountry, address

                // Drink Types
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                    this.drinkTypeList = response.data;
                }
                catch (error) {
                    console.error(error);
                    this.loadError = true;
                }

                // Users
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                    this.users = response.data;
                    this.user = this.users.find(user => user._id.$oid == this.userID)
                    if (this.user) {
                        this.userBookmarks = this.user.drinkLists;
                    }
                } 
                catch (error) {
                    console.error(error);
                }

                // Producers
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                    this.producerList = response.data;
                }
                catch (error) {
                    console.error(error);
                    this.loadError = true;
                }

                // Listings
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                    this.listings = response.data;

                    for (let listing of response.data) {
                        const producer = this.producerList.find((producer) => {
                            return producer["_id"]["$oid"] == listing["producerID"]["$oid"];
                        });
                        if (producer) {
                            listing["producerName"] = producer["producerName"];
                        }
                        else {
                            listing["producerName"] = "";
                        }
                        this.resultListings.push(listing);
                    }

                    this.resultListings = this.resultListings.filter((listing) => {
                        return listing["listingName"].toLowerCase().includes(this.searchTerm) || listing["producerName"].toLowerCase().includes(this.searchTerm) || listing["bottler"].toLowerCase().includes(this.searchTerm) || listing["originCountry"].toLowerCase().includes(this.searchTerm) || listing["drinkType"].toLowerCase().includes(this.searchTerm) || listing["typeCategory"].toLowerCase().includes(this.searchTerm);
                    });
                    this.originalResults = this.resultListings;
                }
                catch (error) {
                    console.error(error);
                    this.loadError = true;
                }

                // Reviews
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                    this.reviews = response.data;
                }
                catch (error) {
                    console.error(error);
                    this.loadError = true;
                }

                this.dataLoaded = true;
            },

            // Main Filter Function
            filterResults() {
                this.resultListings = this.originalResults;
                
                // Filter by Drink Type
                if (this.searchFilter.drinkType != '') {
                    this.resultListings = this.resultListings.filter((listing) => {
                        return listing["drinkType"] == this.searchFilter.drinkType;
                    });
                }
            },

            // Filter Support Function (Drink Type)
            filterByDrinkType(drinkType) {
                // Check if the selected filter is the same as the current filter
                if (this.searchFilter.drinkType == drinkType) {
                    return;
                }
                else {
                    this.searchFilter.drinkType = drinkType;
                    this.filterResults();
                }
            },

            sortResults() {
                let category = this.sortSelection.category;
                // #1: Alphabetical (A - Z)
                if (category == 'Alphabetical (A - Z)') {
                    this.resultListings.sort((a, b) => {
                        return a.listingName.localeCompare(b.listingName);
                    });
                }

                // #2: Alphabetical (Z - A)
                else if (category == 'Alphabetical (Z - A)') {
                    this.resultListings.sort((a, b) => {
                        return b.listingName.localeCompare(a.listingName);
                    });
                }

                // #3: Date (Newest - Oldest)
                else if (category == 'Date (Newest - Oldest)') {
                    this.resultListings.sort((a, b) => {
                        return new Date(b.addedDate.$date) - new Date(a.addedDate.$date);
                    });
                }

                // [DEFAULT] #4: Date (Oldest - Newest)
                else if (category == '' || category == 'Date (Oldest - Newest)') {
                    this.resultListings.sort((a, b) => {
                        return new Date(a.addedDate.$date) - new Date(b.addedDate.$date);
                    });
                }

                // #5: Ratings (Highest - Lowest)
                else if (category == 'Ratings (Highest - Lowest)') {
                    this.resultListings.sort((a, b) => {
                        return this.getAllRatings(b) - this.getAllRatings(a);
                    });
                }

                // #6: Ratings (Lowest - Highest)
                else if (category == 'Ratings (Lowest - Highest)') {
                    this.resultListings.sort((a, b) => {
                        return this.getAllRatings(a) - this.getAllRatings(b);
                    });
                }
            },

            // Sort Support Function (Category)
            sortByCategory(category) {
                // Check if the selected filter is the same as the current filter
                if (this.sortSelection.category == category) {
                    return;
                }
                else {
                    this.sortSelection.category = category
                    this.sortResults();
                }
            },

            // get ratings for a listing --> return "-" if no ratings
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"]["$oid"] == listing["_id"]["$oid"];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                // round to 1 decimal place
                const roundedRating = Math.round(averageRating * 10) / 10;
                return roundedRating;
            },

            // get ratings for a listing --> return 0 if no ratings
            getAllRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"]["$oid"] == listing["_id"]["$oid"];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return 0;
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                // round to 1 decimal place
                const roundedRating = Math.round(averageRating * 10) / 10;
                return roundedRating;
            },

            // for bookmark component
            handleIconClick(data) {
                this.bookmarkListingID = data
            },

            // format date
            formatDate(dateTimeString) {
                let datePart = dateTimeString.split("T")[0];
                // splitting the date into year, month, and day
                let [year, month, day] = datePart.split("-");
                // formatting the date
                let formattedDate = `${day}/${month}/${year}`;
                return formattedDate;
            },
        }
    }
</script>