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
    <div class="container pt-3">
        <div class="row">
            <!-- producer information -->
            <div class="col-9">
                <!-- header -->
                <div class="row">
                    
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
                                <h4 class="square-inline-text-start mr-auto"> Where to Try </h4>
                            </div>
                            <div class="py-2"></div>
                            <!-- body -->
                            <div class="py-5">
                                <!-- TODO: where to try function -->
                            </div>
                            <div class="py-2"></div>
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
    import axios from 'axios';
    import '../../assets/global.css'

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
            };
        },
        mounted() {
            this.loadData();
        },
        methods: {
            // load data from database
            async loadData() {
                // Listings
                try {
                    const response = await axios.get('http://127.0.0.1:5000/getListings');
                    this.listings = response.data;
                    this.filteredListings = this.listings; // originally, make filtered listings the entire collection of listings
                } 
                catch (error) {
                    console.error(error);
                }
                // Producers
                try {
                    const response = await axios.get('http://127.0.0.1:5000/getProducers');
                    this.producers = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Users
                try {
                    const response = await axios.get('http://127.0.0.1:5000/getUsers');
                    this.users = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Venues
                try {
                    const response = await axios.get('http://127.0.0.1:5000/getVenues');
                    this.users = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
            },

        },
    };
</script>