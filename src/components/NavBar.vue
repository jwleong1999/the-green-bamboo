<!-- Component for global Navigation Bar. Used in most pages on the application. -->

<!-- Requires Review. Search function is not complete, and may require modification. -->
<!-- TODO: Implement this component into all pages that require them, replacing in-built navbar code -->
<!-- TODO: Check and adjust for responsiveness on mobile devices! -->

<template>
    <!-- Main NavBar -->
    <div class="navbar-container">
        <nav class="navbar">
            <div class="container-fluid align-items-center col-xxl-8 col-xl-9 col-lg-10 col-md-11 col-sm-12">
                <!-- logo -->
                <div class="align-items-center col-3" href="../login/index.html"> 
                    <img src="../../Images/Logo/88 Bamboo.png" style="width: 70px; height: 70px;">
                </div>
                <!-- search bar -->
                <div class="col-6">
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="searchListings"> 
                </div>
                <div class="col-3">
                    <!-- profile icon -->
                    <svg v-if="photo == ''" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                    </svg>
                    <img v-else :src="'data:image/png;base64,'+ photo"  style="width: 30px; height: 30px;" class="img-border">
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
</template>

<script>
    export default {
        name: "NavBar",
        data() {
            return {
                searchInput: '',
                photo: '',
            }
        },
        mounted() {
            // Obtain user's profile picture
            if (localStorage.getItem('88B_accID') != null) {

                let accType = localStorage.getItem('88B_accType');
                let accID = localStorage.getItem('88B_accID');
                let url = 'http://127.0.0.1:5000/get';

                if (accType == 'user') {
                    url = url + 'User/' + accID;
                    this.loadData(url);
                } 
                else if (accType == 'producer') {
                    url = url + 'Producer/' + accID;
                    this.loadData(url);
                } 
                else if (accType == 'venue') {
                    url = url + 'Venue/' + accID;
                    this.loadData(url);
                }
            }
        },
        methods: {
            // load data from database
            async loadData(url) {
                    try {
                        const response = await this.$axios.get(url);
                        this.photo = response.data["photo"];
                    } 
                    catch (error) {
                        console.error(error);
                    }
            },

            // searchListings() {
            //     this.$router.push({name: 'search', query: {input: this.searchInput}})
            // }
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

            // for resetting listings (show full listings)
            resetListings() {
                this.searchInput = '';
                this.search = false;
                this.filteredListings = this.listings;
            },

            // logout function
            logout() {
                localStorage.removeItem('88B_accID');
                localStorage.removeItem('88B_accType');
                this.$router.push({path: '/login'});
            }

        }
    }
</script>