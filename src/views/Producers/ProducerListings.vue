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
            
            <!-- button -->
            <div class="col-4">
                <div class="d-grid gap-2">
                    <!-- <router-link to="/Producer/Producer-Listings">Producer Listings</router-link> | -->
                    <router-link :to="{ path: '/Producer/Producer-Create-Listing' }">
                        <button class="btn primary-btn btn-sm">
                            <h4> Create bottle listing here! </h4>
                        </button>
                    </router-link>
                </div>
            </div>
        </div>
    </div>

    <!-- content -->
    <div class="container pt-3">
        
    </div>

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->
<!-- <style>

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

</style> -->

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    // import axios from 'axios';

    // export default {
    //     data() {
    //         return {
    //             listings: [],
    //             producers: [],
    //             users: [],
    //             venues: []
    //         };
    //     },
    //     mounted() {
    //         this.loadData();
    //     },
    //     methods: {
    //         
    //     },
    // };
</script>


