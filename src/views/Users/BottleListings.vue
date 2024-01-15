<!-- HTML -->
<template>
    <!-- navbar-->
    <nav class="navbar m-2 p-2">
        <div class="container-fluid d-flex align-items-center justify-content-between">
            <!-- logo -->
            <div class="navbar-brand d-flex align-items-center" href="../login/index.html"> 
                <img src="../../../Images/Logo/88 Bamboo.png" style="width: 50px; height: 50px;">
            </div>
            <!-- search bar -->
            <div class="col-md-6">
                <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;"> 
            </div>
            <div>
                <!-- profile icon -->
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                </svg>
                <!-- collapsible button -->
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
        <!-- collapsible content -->
        <div class="collapse" id="navbarToggleExternalContent">
            <div class="p-4">
                <h5 class="text-body-emphasis h4">Collapsed content</h5>
                <span class="text-body-secondary">Toggleable via the navbar brand.</span>
            </div>
        </div>
    </nav>

    <!-- main content -->
    <div>
    <h1>Listings from Flask API: </h1>
        {{ listings }}
    </div>

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->
<style>
    body {
    /* colours */
    background-color: #D9D9D9 ;

    /* margins */
    margin-left: 10px;
    margin-right: 10px;

    /* padding */
    padding-left: 10px;
    padding-right: 10px;
}

.navbar {
    border-bottom: 3px solid #535C72;
}

.navbar-brand {
    margin-bottom: 10px;
}

.custom-btn {
    color: whitesmoke;
    background-color: #535C72;
}

.custom-btn:hover {
    color: whitesmoke;
    background-color: #747D92;
}

.custom-btn:focus {
    outline-color: transparent;
    outline-style:solid;
    box-shadow:2px #747D92;
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
</style>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
import axios from 'axios';

export default {
    data() {
        return {
        listings: [],
        };
    },
    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
        try {
            const response = await axios.get('http://127.0.0.1:5000/getListings');
            this.listings = response.data;
        } catch (error) {
            console.error(error);
        }
        },
    },
};
</script>


