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
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="helperSearch"> 
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
    <div class="collapse" id="navbarToggleExternalContent"> <!-- TODO: modify links accordingly -->
        <div class="row pt-2">
            <div class="col-7"></div>
            <!-- [specific] for different accounts -->
            <div class="col-2 navbar-dropdown text-end">
                <!-- Users -->
                <div class="p-4" id="Users">
                    <h3> Users </h3>
                    <!-- TODO: link to the user's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the user's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Drink Stats </h5>
                    </a>
                    <!-- TODO: link to lists -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Bookmarked Drinks </h5>
                    </a>
                </div>

                <!-- Venues -->
                <div class="p-4" id="Venues">
                    <h3> Venues </h3>
                    <!-- TODO: link to the venue's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the venues's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Dashboard </h5>
                    </a>
                    <!-- TODO: link to edit menu page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Menu </h5>
                    </a>
                </div>

                <!-- Producers -->
                <div class="p-4" id="Producers">
                    <h3> Producers </h3>
                    <!-- TODO: link to the producers's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the producer's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Dashboard </h5>
                    </a>
                    <!-- TODO: link to new listings page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> Add a New Listing </h5>
                    </a>
                </div>

                <!-- [common] for all accounts -->
                <a href="www.88bamboo.co" class="primary-clickable-text">
                    <h4> 
                        Read & Learn
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                        </svg>
                    </h4>
                </a>
            </div>
            <div class="col-3"></div>
        </div>
    </div>

    <!-- [if] no search input -->
    <div v-if="search == false">
        <!-- header -->
        <div class="container pt-5">
            <div class="row">
                <!-- tagline -->
                <div class="col-8">
                    <h1 class="text-start"> Your glass deserves the best. </h1>
                </div>
                <!-- button -->
                <div class="col-4">
                    <div class="d-grid gap-2">
                        <button class="btn secondary-btn btn-lg"> 
                            Sign Up to Start Pouring 
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- main content -->
        <div class="container pt-3">
            <div class="row">
                <!-- your drinks shelf & brands you follow -->
                <div class="col-3">
                    <div class="row">
                        <!-- your drinks shelf -->
                        <div class="col-12">
                            <div class="square primary-square rounded p-3 mb-3">
                                <!-- header text -->
                                <div class="square-inline">
                                    <h4 class="square-inline-text-start mr-auto"> Your Drink Shelf </h4>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                    </svg>
                                </div>
                                <!-- body -->
                                <div class="py-4"></div>
                                <div class="py-5">
                                    <h6 class="fst-italic"> No drinks added yet. </h6>
                                    <button class="btn secondary-btn-border btn-sm py-2 px-3"> Log in to add a drink to shelf </button>
                                </div>
                                <div class="py-4"></div>
                            </div>
                        </div>
                        <!-- brands you follow -->
                        <div class="col-12">
                            <div class="square primary-square rounded p-3 mb-3">
                                <!-- header text -->
                                <div class="square-inline">
                                    <h4 class="square-inline-text-start mr-auto"> Brands You Follow </h4>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                    </svg>
                                </div>
                                <!-- body -->
                                <div class="py-4"></div>
                                <div class="py-5">
                                    <h6 class="fst-italic"> No brands added yet. </h6>
                                    <button class="btn secondary-btn-border btn-sm py-2 px-3"> Log in to follow your favourite brand </button>
                                </div>
                                <div class="py-4"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- discover, following & filter by drink type -->
                <div class="col-9">
                    <div class="container">
                        <!-- buttons -->
                        <div class="row">
                            <!-- discover -->
                            <div class="col-3">
                                <div class="d-grid gap-2">
                                    <button class="btn primary-btn btn-sm">
                                        <h4> Discover </h4>
                                    </button>
                                </div>
                            </div>
                            <!-- following -->
                            <div class="col-3">
                                <div class="d-grid gap-2">
                                    <button class="btn primary-btn-outline btn-sm">
                                        <h4> Following </h4>
                                    </button>
                                </div>
                            </div>
                            <!-- filter by drink type -->
                            <div class="col-3">
                                <div class="d-grid gap-2 dropdown">
                                    <button class="btn primary-light-dropdown btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        {{ selectedDrinkType ? selectedDrinkType['drinkType'] : 'Filter by drink type' }}
                                        <span class="cross-icon" @click="clearSelection">&#10005;</span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <!-- Filter button for drink type -->

                                        <li v-for="drinkType in drinkTypes" v-bind:key="drinkType._id" class= "p-3">
                                        <a class="dropdown-item" @click="selectDrinkType(drinkType)"> {{ drinkType['drinkType'] }} </a>
                                        </li>       
                                    </ul>
                                </div>
                            </div>       

                            <!-- Dropdown based on category--> 
                            <div v-if="selectedDrinkType != ''" class="col-3">
                                <div class="d-grid gap-2 dropdown">
                                    <button class="btn primary-light-dropdown btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        {{ selectedCategory ? selectedCategory : 'Filter by drink category' }}
                                        <span class="cross-icon" @click="clearCategory">&#10005;</span>
                                    </button>
                                    <ul v-if="selectedTypeCategory != ''" class="dropdown-menu">
                                        <!-- Filter button for drink category -->

                                        <li v-for="category in selectedTypeCategory" @click="selectDrinkCategory(category)" v-bind:key="category" class= "p-3">
                                            <a class="dropdown-item"> {{ category }} </a>
                                        </li>       
                                        
                                    </ul>
                                    <ul v-else class="dropdown-menu">
                                        <li>There is no category for this</li>       
                                    </ul>
                                </div>
                            </div>                            
                        </div>

                        <!-- Display error message when no results for filter-->
                        <h5 v-if="filteredListings==''" style="display: inline-block;"> There is no listing available for the selected filter </h5>
                        
                        <!-- listings -->
                        <div class="row">
                            <!-- v-loop for each listing -->
                            <div class="container text-start">
                                <div v-for="listing in filteredListings" v-bind:key="listing._id" class="p-3">

                                    <div class="row">
                                        <!-- image -->
                                        <div class="col-4 image-container">
                                            <img v-if="listing['photo']" :src="'data:image/png;base64,'+listing['photo']" style="width: 300px; height: 300px;" class="img-border">
                                            <img v-else src="../../../Images/Drinks/Placeholder.png" style="width: 300px; height: 300px;" class="img-border">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark overlay-icon" viewBox="0 0 16 16">
                                                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                            </svg>
                                        </div>
                                        <!-- details -->
                                        <div class="col-8 ps-5">
                                            <!-- expression name -->
                                            <div class="row pt-1">
                                                <a class="primary-clickable-text" v-bind:href="'../Producers/Bottle-Listings?id=' + `${listing._id.$oid}`">
                                                    <h4> <b> {{ listing["listingName"] }} </b> </h4>
                                                </a>
                                            </div>
                                            <!-- producer -->
                                            <div class="row">
                                                <a class="primary-clickable-text" v-bind:href="'../Producers/Profile-Page?id=' + `${listing.producerID.$oid}`">
                                                    <h5> <b> {{ getProducerName(listing) }} </b> </h5>
                                                </a>
                                            </div>
                                            <!-- review -->
                                            <div class="row pt-3">
                                                <a class="default-clickable-text fst-italic scrollable" v-bind:href="'../Producers/Bottle-Listings?id=' + `${listing._id.$oid}`">
                                                    <h5> {{ listing["officialDesc"] }}. </h5>
                                                </a>
                                            </div>
                                            <!-- rating -->
                                            <div class="row pt-4"> 
                                                <div class="col-6">
                                                    <h1 class="rating-text">
                                                        {{ getRatings(listing) }}
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                        </svg>
                                                    </h1>
                                                </div>
                                                <div class="col-6">
                                                    <div class="d-grid gap-5">
                                                        <a class="btn secondary-btn btn-md" v-bind:href="'../Producers/Bottle-Listings?id=' + `${listing._id.$oid}`"> Read what the crowd thinks </a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div> <!-- end of listings -->
                    </div> <!-- end of container -->
                </div> <!--  end of discover, following & filter by drink type -->
            </div> <!-- end of row -->
        </div>
    </div>

    <!-- [else] with search inputs -->
    <div v-else class="pt-5">
        <div class="container default-text text-start">
            <div class="row">
                <!-- show matching # of search results -->
                <div class="col-8 d-flex align-items-center">
                    <!-- back button -->
                    <span style="display: inline-block;">
                        <span class="pe-2">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16" v-on:click="previousListing">
                                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                            </svg>
                        </span>
                        <h5 style="display: inline-block;"> Showing {{ filteredListings.length }} results for "{{ searchTerm }}" </h5> 
                        <h5 v-if="isFilterType" style="display: inline-block;"> and filter "{{ selectedDrinkType['drinkType'] }}"</h5> 
                        <h5 style="display: inline-block;"> &nbsp; | &nbsp; </h5>
                        <!-- show options to add listings -->
                        <div style="display: inline-block;"> 
                            <a href="#" class="link-underline-dark" @click="clearSelection">
                                <h5 style="display: inline-block;" class="default-text"> 
                                    <u>
                                        Clear Filter 
                                    </u>
                                </h5>
                            </a>
                        </div>
                        <div style="display: inline-block;"> 
                            <a href="#" class="link-underline-dark">
                                <h5 style="display: inline-block;" class="default-text"> 
                                    <u>
                                        Don't see what you're looking for? Add a listing here! 
                                    </u>
                                </h5>
                            </a>
                        </div>
                    </span>
                </div>
                <!-- filter by drink type -->
                <div class="col-2">
                    <div class="d-grid gap-2 dropdown">
                        <button class="btn primary-light-dropdown btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                            {{ selectedDrinkType ? selectedDrinkType['drinkType'] : 'Filter by drink type' }}

                        </button>
                        <ul class="dropdown-menu"> <!-- Filter button for drink type -->
                            <li v-for="drinkType in drinkTypes" v-bind:key="drinkType._id" class= "p-3">
                                <a class="dropdown-item" @click="selectDrinkType(drinkType)"> {{ drinkType['drinkType'] }} </a>
                            </li>       
                        </ul>
                    </div>
                </div>
                <!-- sort by -->
                <div class="col-2">
                    <div class="d-grid gap-2 dropdown">
                        <button class="btn primary-light-dropdown btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Sort By
                        </button>
                        <ul class="dropdown-menu"> <!-- TODO: sort button to be implemented -->
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- show listings based on search results -->
        <div class="container pt-3">
            <div class="row">
                <!-- v-loop for each listing -->
                <div class="container text-start">
                    <div v-for="listing in filteredListings" v-bind:key="listing._id" class="p-3">
                        <div class="row">
                            <!-- image -->
                            <div class="col-3 image-container">
                                <a v-bind:href="'../Producers/Bottle-Listings?id=' + `${listing._id.$oid}`">
                                    <img v-if="listing['photo']" :src="'data:image/png;base64,'+listing['photo']" style="width: 300px; height: 300px;" class="img-border">
                                    <img v-else src="../../../Images/Drinks/Placeholder.png" style="width: 300px; height: 300px;" class="img-border"> 
                                </a>
                            </div>
                            <!-- details -->
                            <div class="col-9 ps-5">
                                <!-- expression name, have tried & want to try & bookmark buttons -->
                                <div class="row">
                                    <!-- expression name -->
                                    <div class="col-7">
                                        <div class="row pt-2">
                                            <h4 class="default-text"> 
                                                <u> <b> {{ listing["listingName"] }}  </b> </u>
                                            </h4> 
                                        </div>
                                    </div>

                                    <!-- have tried button -->
                                    <div class="col-2 pe-0">
                                        <div v-html="checkDrinkLists(listing).buttons.haveTried" class="d-grid"> </div>
                                    </div>
                                    <!-- want to try button -->
                                    <div class="col-2 ps-0">
                                        <div v-html="checkDrinkLists(listing).buttons.wantToTry" class="d-grid"> </div>
                                    </div>
                                    <!-- bookmark button -->
                                    <div class="col-1 text-end">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16">
                                            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                        </svg>
                                    </div>
                                </div>
                                <div class="row py-2">
                                    <!-- official description -->
                                    <div class="col-10">
                                        <div class="row pt-2 pb-5">
                                            <h5 class="fst-italic scrollable-long"> {{ listing["officialDesc"] }} </h5>
                                        </div>
                                    </div>
                                    <!-- rating -->
                                    <div class="col-2">
                                        <h1 class="rating-text text-end">
                                            3.7 
                                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                            </svg>
                                        </h1>
                                    </div>
                                </div>
                                <!-- release date -->
                                <!-- NOTE: can exclude for now (no data) -->
                                <!-- <div class="row pt-5"> 
                                    <h5> 
                                        <b> Release Date:</b>
                                        date
                                    </h5>
                                </div> -->
                            </div>
                        </div>
                    </div>
                </div>
            </div> <!-- end of listings -->
        </div>

    </div>

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    // import NavBar from '@/components/NavBar.vue'

    export default {
        components:{
            
        },

        data() {
            return {
                // data from database
                // countries: [],
                listings: [],
                producers: [],
                reviews: [],
                // users: [],
                venues: [],
                venuesAPI: [],
                drinkTypes: [],
                requestListings: [],
                requestEdits: [],
                modRequests: [],

                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                searchHistory: [],

                // for filter by drink categories
                selectedDrinkType:"",
                selectedTypeCategory:[],
                selectedCategory:"",
                filterSearchResult: [],
                isFilterType:false,

                // customization for drinkLists buttons
                // [TODO] get drink list of user, for now is hardcoded
                drinkList:  {
                                "haveTried": ["Harmony Collection Inspired by Intense Arabica"],
                                "wantToTry": ["Catnip Gin No. 2", "Five Farms Irish Cream Liqueur"]
                            },
                haveTried: false,
                wantToTry: false,

            };
        },
        mounted() {
            this.loadData();
        },
        methods: {
            // load data from database
            async loadData() {
                // countries
                // _id, originCountry
                    // try {
                    //     const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                    //     this.countries = response.data;
                    // } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
                        // originally, make filteredListings the entire collection of listings
                        this.filteredListings = this.listings;
                    } 
                    catch (error) {
                        console.error(error);
                }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // reviews
                // _id, userID, reviewTarget, date, rating, reviewDesc, taggedUsers, reviewTitle, reviewType, flavorTag, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                        this.reviews = response.data;
                    }
                    catch (error) {
                        console.error(error);
                    }
                // users
                // _id, username, displayName, choiceDrinks, drinkLists, modType, photo
                    // try {
                    //     const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                    //     this.users = response.data;
                    // } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // venues
                // _id, venueName, venueDesc, originCountry, address, openingHours
                    // try {
                    //     const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                    //     this.venues = response.data;
                    // } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                // try {
                //         const response = await this.$axios.get('http://127.0.0.1:5000/getVenuesAPI');
                //         this.venuesAPI = response.data;
                //     } 
                //     catch (error) {
                //         console.error(error);
                //     }
                // drinkTypes
                // _id, drinkType, typeCategory
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                        this.drinkTypes = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // requestListings
                // _id, listingName, producerNew, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, sourceLink, brandRelation, reviewStatus, userID, photo
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                    //         this.requestListings = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                    //         this.requestEdits = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // modRequests
                // _id, userID, drinkType, modDesc
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                    //         this.modRequests = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
            },
            // Helper function for onkeyup search to reset filter
            helperSearch(){
                this.searchListings()
                this.isFilterType = false
                this.selectedDrinkType = ''
            },

            // for search button
            searchListings() {
                // flag to check if there are search inputs
                const searchInput = this.searchInput.toLowerCase();
                this.searchTerm = this.searchInput;

                // if there is something searched
                this.search = true;
                const searchResults = this.listings.filter((listing) => {
                    const expressionName = listing["listingName"].toLowerCase();
                    const producer = this.getProducerName(listing).toLowerCase();
                    return expressionName.includes(searchInput) || producer.includes(searchInput);
                });

                // add search results to search history
                this.searchHistory.push([searchInput, searchResults]);

                // if nothing found
                if (searchResults.length == 0) {
                    this.filteredListings = [];
                } 
                else {
                    this.filteredListings = searchResults;
                }

                // if there is nothing searched
                if (this.searchInput == '') {
                    this.resetListings();
                }
            },

            // for viewing previous listings (show previous search results)
            previousListing() {
                // more than 1 search result history
                if (this.searchHistory.length > 1) {
                    // remove current search result
                    this.searchHistory.pop();
                    // get previous search result
                    const previousSearch = this.searchHistory[this.searchHistory.length - 1];
                    this.searchInput = previousSearch[0];
                    this.searchTerm = this.searchInput;
                    this.filteredListings = previousSearch[1];
                }
                // only 1 search result history
                else {
                    this.resetListings();
                }
            },

            // for resetting listings (show full listings)
            resetListings() {
                this.searchInput = '';
                this.search = false;
                this.filteredListings = this.listings;
                this.searchHistory = [];
            },

            // get producerName for a listing based on listing
            getProducerName(listing) {
                const producer = this.producers.find((producer) => {
                    return producer["_id"]["$oid"] == listing["producerID"]["$oid"];
                });
                // ensures that producer is found before accessing "producerName"
                if (producer) {
                    const producerName = producer["producerName"];
                    return producerName;
                }
                else {
                    return null;
                }
            },

            // get reviews for a listing
            getReviews(listing) {
                // list of all reviews of the particular drink
                const reviews = this.reviews.filter((review) => {
                    return review["reviewTarget"] == listing["listingName"];
                });
                // choose random review from the list
                const randomReview = reviews[Math.floor(Math.random() * reviews.length)];
                // check if a review is found before accessing "Review Desc"
                const reviewDesc = randomReview ? randomReview["reviewDesc"] : null;
                return reviewDesc;
            },

            // get ratings for a listing
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"] == listing["listingName"];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                return averageRating;
        },

            // Handle select of drink type filter option like sake, gin, whiskey
            selectDrinkType(drinkType) {
                this.selectedCategory = null;
                this.selectedDrinkType = drinkType;
                for(let drinks of this.drinkTypes){
                    if(drinks['drinkType'] == drinkType['drinkType']){
                        this.selectedTypeCategory = drinks['typeCategory']
                    }
                }

                const drinkTypeSearch = this.selectedDrinkType['drinkType'].toLowerCase();

                if(this.search){
                    this.searchListings()
                    const searchResults = this.filteredListings.filter((listing) => {
                        const drinkTypeListing = listing["drinkType"].toLowerCase();
                        return drinkTypeListing.includes(drinkTypeSearch);
                    });
                    this.filterSearchResult=searchResults
                    this.isFilterType = true
                }
                
                // Dropdown for drink category after selecting drink type
                else{
                    const searchResults = this.listings.filter((listing) => {
                        const drinkTypeListing = listing["drinkType"].toLowerCase();
                        return drinkTypeListing.includes(drinkTypeSearch);
                    });
                    this.filterSearchResult=searchResults
                }
                // if nothing found
                if (this.filterSearchResult == null) {
                    this.filteredListings = null;
                } 
                else {
                    this.errorFound = false;
                    this.errorMessage = '';
                    this.filteredListings = this.filterSearchResult;
                }
        },

            //Select drink category like Blended for whiskey 
            selectDrinkCategory(drinkCategory) {
                
                this.selectDrinkType(this.selectedDrinkType)
                this.selectedCategory = drinkCategory;

                const drinkCategorySearch = this.selectedCategory.toLowerCase();
                const searchResults = this.filteredListings.filter((listing) => {
                    const drinkCategory = listing["typeCategory"].toLowerCase();
                    return drinkCategory.includes(drinkCategorySearch);
                });
                // if nothing found
                if (searchResults == null) {
                    this.errorFound = true;
                    this.errorMessage = 'No results found, please try again.';
                    this.filteredListings = null;
                } 
                else {
                    this.errorFound = false;
                    this.errorMessage = '';
                    this.filteredListings = searchResults;
                }
        },
            clearSelection() {
                // Handle the click event here
                this.searchListings(); // Or perform any other actions
                this.selectedDrinkType = ''
                this.selectedCategory = ''
                this.isFilterType = ''
        },
            clearCategory() {
                // Handle the click event here
                this.searchListings(); // Or perform any other actions
                this.selectDrinkType(this.selectedDrinkType)
        },

            // check if user has already added listing to shelf, add colour to button accordingly
            checkDrinkLists(listing) {
                const haveTried = this.drinkList.haveTried.includes(listing.listingName);
                const wantToTry = this.drinkList.wantToTry.includes(listing.listingName);

                const haveTriedButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${haveTried ? 'disabled' : ''}">
                    Have tried
                </button>
                `;

                const wantToTryButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${wantToTry ? 'disabled' : ''}">
                    Want to try
                </button>
                `;

                return {
                    buttons: {
                        haveTried: haveTriedButton,
                        wantToTry: wantToTryButton,
                    }
                }
            }
        }
    };
</script>


