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

    <!-- main content -->

    <div class="container pt-5">
        <div class="row">
            <!-- producer information -->
            <div class="col-9 no-margin">
                <!-- header -->
                <div class="row">
                    <!-- image -->
                    <div class="col-3 image-container">
                        <img src="../../../Images/Drinks/Placeholder.png" style="width: 200px; height: 200px;" class="img-border">
                    </div>
                    <!-- details -->
                    <div class="col-9 text-start">
                        <div class="container text-start">
                            <!-- drink category -->
                            <div class="row">
                                <div class="col">
                                    <h5 class="text-body-secondary fst-italic"> {{ specified_listing["drinkType"] }} </h5>
                                </div>
                            </div>
                            <!-- expression name -->
                            <div class="row">
                                <div class="col-9">
                                    <h3 class="text-body-secondary"> <b> {{ specified_listing["listingName"] }} </b> </h3>
                                </div>
                                <!-- suggest edit & report duplicate -->
                                <div class="col-3">
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic"> Suggest Edit </p>
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic"> Report Duplicate </p>
                                </div>
                            </div>
                            <!-- producer & bottler -->
                            <div class="row">
                                <!-- producer -->
                                <div class="col-5">
                                    <h5 class="text-body-secondary"> <u> {{ getProducerName(specified_listing["producerID"]) }} </u> </h5>
                                </div>
                                <!-- bottler -->
                                <div class="col-4">
                                    <h5 class="text-body-secondary"> Bottler: <u> {{ specified_listing["bottler"] }} </u>  </h5>
                                </div>
                            </div>
                            <!-- description -->
                            <div class="row">
                                <div class="col">
                                    <div class="py-2"></div>
                                    <p> {{ specified_listing["officialDesc"] }} </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- more information (category, age, country of origin, abv, list buttons & bookmark)-->
                <div class="row pt-4">
                    <div class="col-7">
                        <div class="row">
                            <!-- category -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Category </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["typeCategory"] }} </b> </h5>
                            </div>
                            <!-- age -->
                            <div class="col-2 text-start">
                                <p class="mb-2"> <u> Age </u> </p>
                                <h5 class="text-body-secondary"> <b>  {{ specified_listing["age"] }} </b> </h5>
                            </div>
                            <!-- country of origin -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Country of Origin </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["originCountry"] }} </b> </h5>
                            </div>
                            <!-- abv -->
                            <div class="col-2 text-start">
                                <p class="mb-1"> <u> ABV </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["abv"] }} </b> </h5>
                            </div>
                        </div>
                    </div>
                    <!-- have tried button -->
                    <div class="col-2 pe-0">
                        <div v-html="checkDrinkLists(specified_listing).buttons.haveTried" class="d-grid"> </div>
                    </div>
                    <!-- want to try button -->
                    <div class="col-2 ps-0">
                        <div v-html="checkDrinkLists(specified_listing).buttons.wantToTry" class="d-grid"> </div>
                    </div>
                    <!-- bookmark button -->
                    <div class="col-1 text-end">
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16">
                            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                        </svg>
                    </div>
                </div>

                <!-- more information (average rating, would recommend, would drink again) -->
                <div class="row pt-3">
                    <div class="col-7">
                        <!-- average rating -->
                        <div class="col-4 text-start">
                                <p class="mb-2"> <u> Average Rating </u> </p>
                                <h5 class="text-body-secondary rating-text ">
                                    {{ getRatings(specified_listing) }}
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </h5>
                            </div>

                        <!-- would recommend -->

                        <!-- would drink again -->
                    </div>

                    <div class="col-5">
                        <div class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg"> 
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                </svg>
                                Add Your Review
                            </button>
                        </div>
                    </div>


                </div>
                
            </div> <!-- end of producer information -->
            
            <!-- where to try & 88 bamboo's review -->
            <div class="col-3">
                <div class="row">
                    <!-- where to try -->
                    <div class="col-12">
                        <div class="square primary-square rounded p-3 mb-3">
                            <!-- header text -->
                            <div class="square-inline">
                                <h4 class="square-inline-text-start mr-auto"> Where to Buy </h4>
                            </div>
                            <!-- body -->
                            <div class="text-start pt-2"> <!-- TODO: add hyperlink to link to producer page-->
                                <!-- [function] where to buy -->
                                <div v-for="producer in producerListings" v-bind:key="producer._id">
                                    <p class="no-margin"> {{ getProducerName(producer) }} </p>
                                </div>
                            </div>
                            <div class="py-5"></div>
                        </div>
                    </div>
                    <!-- 88 bamboo's review -->
                    <div class="col-12">
                        <div class="square secondary-square rounded p-3 mb-3">
                            <!-- header text -->
                            <div class="square-inline">
                                <h4 class="square-inline-text-start mr-auto"> 88 Bamboo's Review </h4>
                            </div>
                            <div class="py-2"></div>
                            <!-- body -->
                            <div class="py-5">
                                <!-- TODO: where to try function -->
                            </div>
                            <div class="py-2"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- end of your drinks shelf & brands you follow -->

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
                // specified listing
                listing_id: null,
                specified_listing: {},
                // where to buy
                producerListings: [],

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
            this.created()
            this.loadData();
        },
        methods: {
            // fetch specific listing data
            async created() {
                // Get the query string parameters (listing ID) from the URL
                const urlParams = new URLSearchParams(window.location.search);
                this.listing_id = urlParams.get('id');
            },

            // load data from database
            async loadData() {
                // countries
                // _id, originCountry
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                        this.countries = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
                        this.filteredListings = this.listings; // originally, make filtered listings the entire collection of listings
                        this.specified_listing = this.listings.find(listing => listing._id.$oid == this.listing_id); // find specified listing
                        this.whereToBuy(); // find where to buy specified listing
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
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                        this.users = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // venues
                // _id, venueName, venueDesc, origin
                // Country, address, openingHours
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                        this.venues = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenuesAPI');
                        this.venuesAPI = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
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
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                            this.requestListings = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                            this.requestEdits = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // modRequests
                // _id, userID, drinkType, modDesc
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                            this.modRequests = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
            },

            // view which producers have specified listing
            whereToBuy() {
                this.producerListings = this.listings
                    .filter(listing => listing["listingName"] == this.specified_listing["listingName"])
                    .map(listing => listing["producerID"]);
            },

            // get producerName for a listing based on producerID
            getProducerName(producerID) {
                const producer = this.producers.find((producer) => {
                    return producer["_id"]["$oid"] == producerID["$oid"];
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
        },
    };
</script>