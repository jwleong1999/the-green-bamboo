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
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;"> 
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

    <!-- content -->
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
                        <div class="col-4">
                            <div class="d-grid gap-2">
                                <button class="btn primary-btn btn-sm">
                                    <h4> Discover </h4>
                                </button>
                            </div>
                        </div>
                        <!-- following -->
                        <div class="col-4">
                            <div class="d-grid gap-2">
                                <button class="btn primary-btn-outline btn-sm">
                                    <h4> Following </h4>
                                </button>
                            </div>
                        </div>
                        <!-- filter by drink type -->
                        <div class="col-4">
                            <div class="d-grid gap-2 dropdown">
                                <button class="btn primary-light-dropdown btn-lg dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Filter by drink type
                                </button>
                                <ul class="dropdown-menu"> <!-- TODO: filter button to be implemented -->
                                    <li><a class="dropdown-item" href="#">Action</a></li>
                                    <li><a class="dropdown-item" href="#">Another action</a></li>
                                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- listings -->
                    <div class="row">
                        <!-- v-loop for each listing -->
                        <div class="container text-start">
                            <div v-for="listing in listings" v-bind:key="listing._id" class="p-3">
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
                                        <div class="row pb-5">
                                            <p class="fst-italic"> "{{ listing["88B Website Review (if applicable)"] }}". </p> <!-- TODO: replace with actual review (use api) -->
                                        </div>
                                        <!-- rating -->
                                        <div class="row pt-5"> 
                                            <div class="col-6">
                                                <h1 class="rating-text"> <!-- TODO: replace with actual rating (need to get from 88 bamboo) -->
                                                    3.7 
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                    </svg>
                                                </h1>
                                            </div>
                                            <div class="col-6">
                                                <div class="d-grid gap-5">
                                                    <button class="btn secondary-btn btn-md"> Read what the crowd thinks </button>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- expression name -->
                                        <div class="row pt-2">
                                            <h4> {{ listing["Expression Name"] }} </h4> 
                                        </div>
                                        <!-- producer -->
                                        <div class="row">
                                            <h5> {{ listing["Producer"] }} </h5> 
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> <!-- end of listings -->
                </div> <!-- end of container -->
            </div> <!-- end of discover, following & filter by drink type -->
        </div> <!-- end of row -->
    </div>

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->
<style>

    body {
        color: black;
        background-color: #D9D9D9 ;
    }

    .navbar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        border-bottom: 3px solid #535C72;
    }

    .navbar {
        text-align: center;
        width: 75%;
    }

    .navbar-brand {
        margin-bottom: 10px;
    }

    .navbar-inner-container {
        width: 75%;
    }

    .primary-btn {
        color: whitesmoke;
        background-color: #535C72;
        border-radius: 30px;
    }

    .primary-btn-outline {
        color: #535C72;
        background-color: whitesmoke;
        border-radius: 30px;
        border: 4px solid #535C72;
    }

    .primary-square {
        color: whitesmoke;
        background-color: #535C72;
    }

    .primary-light-dropdown {
        color: whitesmoke;
        background-color: #747D92;
        border-radius: 10px;
    }

    .secondary-btn {
        color: whitesmoke;
        background-color: #DD9E54;
        border-radius: 30px;
    }

    .secondary-btn-border {
        color: whitesmoke;
        background-color: #DD9E54;
        border-radius: 30px;
        border: 1px solid whitesmoke;
    }

    .navbar-toggler,
    .navbar-toggler:focus,
    .navbar-toggler:active,
    .navbar-toggler-icon:focus {
        outline: none;
        border: none;
        box-shadow: none;
    }

    .search-bar {
        border: 2px solid #535C72;
    }

    .square-inline {
        display: flex;
        align-items: center;
    }

    .square-inline-text-start {
        margin-right: auto; /* Pushes the text to the left */
    }

    .img-border {
        border: 4px solid #535C72;
        border-radius: 30px;
    }

    .image-container {
        position: relative;
    }

    .overlay-icon {
        position: absolute;
        top: 15px;
        right: 15px;
    }

    .rating-text, .bi-star-fill {
        color: #DD9E54;
    }

</style>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                listings: [],
                producers: [],
                users: [],
                venues: []
            };
        },
        mounted() {
            this.loadData();
        },
        methods: {
            async loadData() {
                // Listings
                try {
                    const response = await axios.get('http://127.0.0.1:5000/getListings');
                    this.listings = response.data;
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


