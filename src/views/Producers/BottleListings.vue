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

    <!-- main content -->

    <div class="container pt-5">
        <div class="row">
            <!-- producer information -->
            <div class="col-9">
                <!-- header -->
                <div class="row"> <!-- TODO: edit this information (NEXT SPRINT) -->
                    <!-- image -->
                    <div class="col-3 image-container">
                        <img src="../../../Images/Sample/beer.png" style="width: 200px; height: 200px;" class="img-border">
                    </div>
                    <!-- details -->
                    <div class="col-9 text-start">
                        <div class="container text-start">
                            <!-- drink category -->
                            <div class="row">
                                <div class="col">
                                    <h5 class="text-body-secondary fst-italic"> {{ specified_listing["typeCategory"] }} </h5>
                                </div>
                            </div>
                            <!-- expression name -->
                            <div class="row">
                                <div class="col">
                                    <h3 class="text-body-secondary"> <b> {{ specified_listing["listingName"] }} </b> </h3>
                                </div>
                            </div>
                            <!-- producer & bottler -->
                            <div class="row">
                                <!-- producer -->
                                <div class="col-6">
                                    <h5 class="text-body-secondary"> <u> {{ getProducerName(specified_listing["producerID"]) }} </u> </h5>
                                </div>
                                <!-- bottler -->
                                <div class="col-6">
                                    <h5 class="text-body-secondary"> Bottler: <u> {{ specified_listing["bottler"] }} </u>  </h5>
                                </div>
                            </div>
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
                            <div class="text-start"> <!-- TODO: add hyperlink to link to producer page-->
                                <!-- [function] where to buy -->
                                <div v-for="producer in producerListings" v-bind:key="producer._id">
                                    <p> {{ getProducerName(producer) }} </p>
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
                listings: [],
                producers: [],
                users: [],
                venues: [],
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
                // Listings
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
                // Producers
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
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
                        this.users = response.data;
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
        },
    };
</script>