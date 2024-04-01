<!-- Component for global Navigation Bar. Used in most pages on the application. -->

<!-- Requires Review. Search function is not complete, and may require modification. -->
<!-- TODO: Implement this component into all pages that require them, replacing in-built navbar code -->

<template>
    <!-- Main NavBar -->
    <div class="navbar-container">
        <nav class="navbar">
            <div class="container-fluid align-items-center col-xxl-8 col-xl-9 col-lg-10 col-md-11 col-sm-12">

                <!-- logo -->
                <div class="align-items-center col-3">
                    <router-link :to="'/'">
                        <img src="../../Images/Logo/88 Bamboo.png" style="width: 70px; height: 70px;">
                    </router-link>
                </div>

                <!-- search bar -->
                <div class="col-6">
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="goSearch">
                </div>

                <div class="col-3 dropdown">

                    <!-- profile icon -->
                    <router-link :to="profileURL" class="me-1">
                        <button type="button" class="btn p-0">
                            <svg v-if="photo == ''" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                            </svg>
                            <img v-else :src="'data:image/png;base64,'+ photo"  style="width: 30px; height: 30px;" class="img-border">
                        </button>
                    </router-link>

                    <!-- dropdown button -->
                    <button class="navbar-toggler p-0" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <!-- dropdown menu -->
                    <ul class="dropdown-menu dropdown-menu-end">
                        <li><router-link :to="'/'" class="dropdown-item">Home</router-link></li>
                        <li><router-link :to="profileURL" class="dropdown-item">My Profile</router-link></li>
                        <li v-if="accType == 'producer'"><router-link :to="'/listing/create'" class="dropdown-item">Create New Listing</router-link></li>
                        <li v-if="accType == 'user'"><router-link :to="'/request/new'" class="dropdown-item">Request New Listing</router-link></li>
                        <li v-if="accType == 'user' || accType == 'producer'"><router-link :to="'/request/view'" class="dropdown-item">View Requests</router-link></li>
                        <li v-if="isAdmin"><router-link :to="'/admin/dashboard'" class="dropdown-item">Admin Dashboard</router-link></li>
                        <li v-if="isAdmin"><router-link :to="'/admin/importListings'" class="dropdown-item">Import Listings</router-link></li>
                        <li><hr class="dropdown-divider"></li>
                        <li v-if="profileURL == '/login'"><router-link :to="'/login'" class="dropdown-item">Login</router-link></li>
                        <li v-if="profileURL == '/login'"><router-link :to="'/signup'" class="dropdown-item">Sign Up</router-link></li>
                        <li v-if="profileURL != '/login'"><span class="dropdown-item" @click="logout">Log Out</span></li>
                    </ul>

                </div>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "NavBar",
        data() {
            return {
                searchInput: '',
                accType: '',
                photo: '',
                profileURL: '/login',
                isAdmin:false,
            }
        },
        mounted() {
            // Obtain user's profile picture + set profile URL
            if (localStorage.getItem('88B_accID') != null) {

                this.accType = localStorage.getItem('88B_accType');
                let accID = localStorage.getItem('88B_accID');
                let url = 'http://127.0.0.1:5000/get';

                if (this.accType == 'user') {
                    url = url + 'User/' + accID;
                    this.loadData(url);

                    // this.profileURL = '/userprofile';
                    this.profileURL = '/profile/user/'+accID;
                } 
                else if (this.accType == 'producer') {
                    url = url + 'Producer/' + accID;
                    this.loadData(url);

                    this.profileURL = '/profile/producer/' + accID;
                    
                } 
                else if (this.accType == 'venue') {
                    url = url + 'Venue/' + accID;
                    this.loadData(url);

                    this.profileURL = '/profile/venue';
                }
            }
        },
        methods: {
            // load data from database (profile picture)
            async loadData(url) {
                    try {
                        const response = await this.$axios.get(url);
                        this.photo = response.data["photo"];
                        if(this.accType=='user' && response.data.isAdmin){
                            this.isAdmin = true
                        }else{
                            this.isAdmin = false
                        }
                    } 
                    catch (error) {
                        console.error(error);
                    }
            },

            // for search feature
            goSearch() {
                if (this.searchInput != '') {
                    // remove any '/' from search input
                    this.searchInput = this.searchInput.replace(/\//g, '');

                    // if already on search page, refresh the page with new search input
                    if (this.$route.path.split('/')[1] == 'search') {
                        window.location.href = '/search/' + this.searchInput;
                    }
                    else {
                        // re-route to search page
                        this.$router.push({path: '/search/' + this.searchInput});
                    }
                }
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