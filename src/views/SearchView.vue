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
                <div class="d-md-grid d-none col-lg-4 col-md-2"></div>

                <!-- Filter Options: On smaller screens, this is "moved below" Search Term -->
                <div class="d-sm-grid d-none col-lg-3 col-md-4 col-sm-5 dropdown">
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
                <router-link class="col-12 text-decoration-none" v-if="role == 'user'" :to="{ path: '/Users/request/new/' }">
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
                            <router-link :to="{ path: '/Producers/Bottle-Listings/' + resultListing._id['$oid'] }">
                                <img v-if="resultListing['photo']" :src="'data:image/png;base64,' + resultListing['photo']" class="img-border img-fluid object-fit-cover" style="width:256px; height:256px">
                                <img v-else src="../../Images/Drinks/Placeholder.png" class="img-border img-fluid object-fit-cover" style="width:256px; height:256px"> 
                            </router-link>
                            <!-- bookmark icon -->
                            <svg v-if="checkBookmarkStatus(resultListing._id.$oid) && user" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark-fill overlay-icon-256" viewBox="0 0 16 16"
                                data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(resultListing._id)">
                                <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
                            </svg>
                            <svg v-else-if="user" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark overlay-icon-256" viewBox="0 0 16 16"
                                data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(resultListing._id)">
                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                            </svg>
                        </div>

                        <!-- Details -->
                        <div class="row col-9">

                            <div class="col-8">
                                <!-- Listing Name + Router Link -->
                                <router-link class="text-dark text-decoration-none" :to="{ path: '/Producers/Bottle-Listings/' + resultListing._id['$oid'] }">
                                    <h4 class="fw-bold">{{ resultListing['listingName'] }}</h4>
                                </router-link>
                                <!-- Producer Name + Router Link -->
                                <router-link class="text-secondary-emphasis text-decoration-none" :to="{ path: '/Producers/Profile-Page/' + resultListing.producerID['$oid'] }">
                                    <h5 class="fw-bold mb-0">{{ resultListing['producerName'] }}</h5>
                                    <p class="fw-bold fst-italic" v-if="resultListing['bottler'] != 'OB'">Bottler: {{ resultListing['bottler'] }}</p>
                                </router-link>
                            </div>

                            <div class="col-4 text-end" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                <!-- Drink Type / Type Category -->
                                <p class="m-0">Type: {{ resultListing['drinkType'] }}</p>
                                <p class="m-0" v-if="resultListing['typeCategory']">Category: {{ resultListing['typeCategory'] }}</p>
                                <!-- Country of Origin -->
                                <p>Origin: {{ resultListing['originCountry'] }}</p>
                            </div>

                            <!-- Description -->
                            <p class="fst-italic scrollable-long">{{ resultListing["officialDesc"] }}</p>

                        </div>
                    </div>
                </div>

                <!-- bookmark modal start -->
                <div v-if="user" class="modal fade" id="bookmarkModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add {{bookmarkModalItem}} to List</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body text-start">
                            <div class="form-check" v-for="(listItems, listName) in user.drinkLists" :key="listName">
                                <input class="form-check-input" type="checkbox" :value="listName" :id="listName" 
                                    v-model="selectedBookmarkList">
                                <label class="form-check-label" :for="listName">
                                    {{listName}}
                                </label>
                            </div>

                            <div class="form-check mt-3">
                                <input class="form-check-input" type="checkbox" value="saveToNewList" id="saveToNewList" v-model="saveToNewList">
                                <label class="form-check-label" for="saveToNewList">
                                    Create New List
                                </label>
                                <div v-if="saveToNewList">
                                    <div class="mt-2">New List Name</div>
                                    <input type="text" class="form-control" v-model="othersListName" placeholder="New List Name">
                                    <div v-if="othersListNameError" class="text-danger text-sm">
                                        *{{ othersListNameError }}
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" @click="bookmarkItem">Save changes</button>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- modal end -->
                
            </div>

        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue'

    export default {
        name: "SearchView",
        components: {
            NavBar
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

                userID: "",
                userType: "",

                // for bookmark
                user: null,
                userBookmarks: [],
                bookmarkModalItem: {},
                selectedBookmarkList: [],
                saveToNewList: false,
                othersListName: "",
                othersListNameError: "",
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
                this.$router.push({path: '/Users/Bottle-Listings'});
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
                    console.log(this.user);
                    this.userBookmarks = this.user.drinkLists;
                    console.log(this.userBookmarks);
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

            // bookmarks
            // checks if an item has been bookmarked
            checkBookmarkStatus(listingID) {
                for (const category of Object.values(this.userBookmarks)) {
                    if (category.listItems) {
                        if (category.listItems.some(item => item[1].$oid === listingID)) {
                            return true;
                        }
                    }
                }
            },
            getListingName(listingID) {
                if (this.listings) {
                    return this.listings.find(listing => listing._id.$oid === listingID.$oid).listingName;
                }
            },
            getListingID(listingName) {
                const listing = this.listings.find(listing => listing.listingName === listingName);
                console.log(listing);
                return listing._id;
            },
            // checks which lists the item is in
            populateBookmarkModal(listingID) {
                // param: objectId
                this.bookmarkModalItem = this.getListingName(listingID);
                this.selectedBookmarkList = [];
                for (const listName in this.userBookmarks) {
                    if (Object.hasOwnProperty.call(this.userBookmarks, listName)) {
                        const bookmarkItems = this.userBookmarks[listName].listItems;
                        if (bookmarkItems) {
                            if (bookmarkItems.some(item => item[1].$oid === listingID.$oid)) {
                                if (!this.selectedBookmarkList.includes(listName)) {
                                    this.selectedBookmarkList.push(listName);
                                }
                            }
                        } 
                    }
                }
            },
            // bookmark item through bookmark icon
            async bookmarkItem() {
                console.log(this.bookmarkModalItem);
                let addListingId = this.getListingID(this.bookmarkModalItem);
                console.log(addListingId);

                for (const listName in this.userBookmarks) {
                    if (Object.hasOwnProperty.call(this.userBookmarks, listName)) {
                        const bookmarkItems = this.userBookmarks[listName].listItems;
                        let itemExist = bookmarkItems.some(item => item[1].$oid === addListingId.$oid);
                        if (this.selectedBookmarkList.includes(listName)) {
                            if (!itemExist) {
                                bookmarkItems.push([new Date(), addListingId]);
                            }
                        } else {
                            if (itemExist) {
                                const index = bookmarkItems.findIndex(item => item[1].$oid === addListingId.$oid);
                                bookmarkItems.splice(index, 1);
                            }
                        }
                    }
                }

                if (this.saveToNewList) {
                    if (this.othersListName === "") {
                        this.othersListNameError = "Please enter a list name";
                        return;
                    } else if (this.userBookmarks[this.othersListName]) {
                        this.othersListNameError = "List name already exists";
                        return;
                    } else {
                        this.othersListNameError = "";
                        this.userBookmarks[this.othersListName] = {
                            listDesc: "",
                            listItems: [[new Date(), addListingId]],
                        };
                    }
                }

                try {
                    const response = await this.$axios.post('http://127.0.0.1:5100/updateBookmark', 
                        {
                            userID: this.userID,
                            bookmark: this.userBookmarks,
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } catch (error) {
                    console.error(error);
                }
                
                window.location.reload();

            },
        }
    }
</script>