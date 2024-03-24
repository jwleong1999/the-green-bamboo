<!-- Venue Dashboard -->
<!-- If venueID is specified, check if logged in user is administrator. Else, redirect to your own profile page / login. -->
<!-- If venueID is not specified, display logged in venue's dashboard. If not logged in as a venue, redirect to your own profile page / login. -->

<template>
    <NavBar />

    <!-- Main Content -->
    <div class="container pt-5">

        <!-- Display when data is still loading -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="dataLoaded == false">
            <span>Loading venue dashboard, please wait...</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <!-- Display when venue does not exist -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="venueExists == false || dataLoaded == null"> 
            <span>An error occurred while loading this page, please try again!</span>
            <br>
            <span class="text-danger-emphasis fw-normal">Are you sure that this venue exists?</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="this.$router.go(-1)">
                <span class="fs-5 fst-italic"> Return to previous page </span>
            </button>
            <router-link :to="'/'" class="mx-1">
                <button class="btn primary-btn btn-sm">
                    <span class="fs-5 fst-italic"> Go to Home page </span>
                </button>
            </router-link>
        </div>

        <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

        <div class="row" v-if="dataLoaded == true">

            <!-- left pane -->
            <div class="col-3">

                <!-- row 1: venue info -->
                <div class="row">
                    <!-- venue name -->
                    <div class="col-8 text-start">
                        <h2> {{ targetVenue['venueName'] }} </h2>
                    </div>
                    <!-- venue profile photo -->
                    <div class="col-4">
                        <img :src="'data:image/jpeg;base64,' + (targetVenue['photo'] || defaultProfilePhoto)" 
                            alt="" style="width: 100px; height: 100px; z-index: 1;">
                    </div>
                </div>

                <!-- row 2: return to profile -->
                <!-- Venue Version -->
                <div v-if="selfView" class="row pt-3">
                    <router-link :to="{ path: '/profile/venue' }" class="d-grid default-clickable-text">
                        <button type="button" class="btn primary-btn-outline-thick rounded-0"> Return To Profile </button>
                    </router-link>
                </div>
                <!-- Admin Version -->
                <div v-if="powerView" class="row pt-3">
                    <router-link :to="{ path: '/profile/venue/' + targetVenue._id['$oid'] }" class="d-grid default-clickable-text">
                        <button type="button" class="btn primary-btn-outline-thick rounded-0"> Return To Profile </button>
                    </router-link>
                </div>

                <!-- row 3: Q & A -->
                <div class="row pt-3">
                    <div class="col-12">
                        <div class="square primary-square rounded p-3 mb-3">

                            <!-- Header -->
                            <div class="square-inline text-start">

                                <!-- [if] Self Venue -->
                                <div v-if="selfView" class="mr-auto">
                                    <h4> Q&A for You! </h4>
                                    <router-link :to="{ path: '/Venues/VenuesQA/' + targetVenue._id['$oid'] }" class="default-text-no-background">
                                        <p class="reverse-text no-margin text-decoration-underline text-start pb-2"> View All </p>
                                    </router-link>
                                </div>

                                <!-- [else] -->
                                <h4 v-else class="mr-auto"> Q&As for {{ targetVenue["venueName"] }} </h4>

                            </div>

                            <!-- Buttons for Answered/Unanswered Questions -->
                            <div v-if="selfView" class="row text-center px-2">
                                <div class="col-6 d-grid gap-0 no-padding">
                                    <button type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="qaMode = 'answered'">
                                        Answered
                                    </button>
                                </div>
                                <div class="col-6 d-grid gap-0 no-padding">
                                    <button type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="qaMode = 'unanswered'">
                                        Unanswered
                                    </button>
                                </div>
                            </div>

                            <!-- Q & A Content -->
                            <div class="text-start pt-2 py-1">
                                <div class="carousel slide" id="carouselQA">
                                    <div class="carousel-inner px-4">

                                        <!-- Answered Questions -->
                                        <div v-if="qaMode == 'answered'">
                                            <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                                <p class="fw-bold">Q: {{ qa["question"] }}</p>
                                                <p> A: {{ qa["answer"] }} </p>
                                            </div>
                                        </div>

                                        <!-- Unanswered Questions -->
                                        <div v-if="qaMode == 'unanswered'">
                                            <div class="carousel-item" v-for="(qa, index) in unansweredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                                <p class="fw-bold">Q: {{ qa["question"] }}</p>
                                                <div class="input-group centered pt-2" v-if="selfView">
                                                    <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Respond to your fans' latest questions." v-model="qaAnswer"></textarea>
                                                    <div @click="sendAnswer(qa)" class="send-icon ps-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                    <!-- Carousel Control Buttons -->
                                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselQA" data-bs-slide="prev">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Previous</span>
                                    </button>
                                    <button class="carousel-control-next" type="button" data-bs-target="#carouselQA" data-bs-slide="next">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Next</span>
                                    </button>

                                </div>
                            </div>

                        </div>
                    </div>
                </div>

            </div>

            <!-- right pane -->
            <div class="col-9 ps-5">

                <!-- row 1: review count + spread of ratings of menu's drinks -->
                <div class="row">

                    <!-- col 1: review count -->
                    <div class="col text-start mx-3">
                        <h3> Review Count of Drinks </h3>
                        <Line :data="reviewsData" :options="chartOptions"></Line>
                    </div>

                    <!-- col 2: spread of ratings -->
                    <div class="col text-start mx-3">
                        <h3> Spread of Ratings for Drinks </h3>
                        <Bar :data="ratingsData" :options="chartOptions" />
                    </div>

                </div>

                <!-- row 2: most reviewed + best rated menu's drinks -->
                <div class="row mt-5">

                    <!-- col 1: most reviewed drinks on the menu -->
                    <div class="col text-start mx-3">
                        <h3> Most Reviewed Drinks </h3>
                        <div class="text-start pb-2" v-for="listing in listingsMostReviewed" v-bind:key="listing._id">
                            <router-link :to="{ path: '/listing/view/' + listing._id.$oid }" class="reverse-clickable-text">
                                <div class="d-flex align-items-center">
                                    <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                    <p class="ms-3 default-clickable-text"> 
                                        <b> {{ listing.listingName }} </b> 
                                        <br>
                                        {{ listing.reviews.length }} reviews
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>

                    <!-- col 2: best rated drinks on the menu -->
                    <div class="col text-start mx-3">
                        <h3> Best Rated Drinks </h3>
                        <div class="text-start pb-2" v-for="listing in listingsBestRated" v-bind:key="listing._id">
                            <router-link :to="{ path: '/listing/view/' + listing._id.$oid }" class="reverse-clickable-text">
                                <div class="d-flex align-items-center">
                                    <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                    <p class="ms-3 default-clickable-text"> 
                                        <b> {{ listing.listingName }} </b> 
                                        <br>
                                        {{ listing.avgRating }} 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                        </svg>
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>

                </div>

                <!-- row 3: most reviewed + best rated menu sections -->
                <div class="row mt-5">

                    <!-- col 1: most reviewed sections -->
                    <div class="col text-start mx-3">
                        <h3> Most Reviewed Sections </h3>
                        <div class="text-start pb-2" v-for="(section, index) in sectionsMostReviewed" v-bind:key="section._id">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> {{ index + 1 }} </h5>
                                </div>
                                <div class="col-10">
                                    <b> {{ section.sectionName }} </b>
                                    <br>
                                    {{ section.sectionDetails.sectionReviews.length }} reviews
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- col 2: best rated sections -->
                    <div class="col text-start mx-3">
                        <h3> Best Rated Sections </h3>
                        <div class="text-start pb-2" v-for="(section, index) in sectionsBestRated" v-bind:key="section._id">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> {{ index + 1 }} </h5>
                                </div>
                                <div class="col-10">
                                    <b> {{ section.sectionName }} </b>
                                    <br>
                                    {{ section.sectionDetails.sectionRating }} 
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

                <!-- row 4: venue menu summary + profile visits -->
                <div class="row">

                    <!-- col 1: venue menu summary -->
                    <div class="col text-start pt-5 mx-3">
                        <h3> Venue Menu Summary </h3>

                        <!-- Number of Menu Items + Unique Drinks -->
                        <div class="text-start pb-2">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> - </h5>
                                </div>
                                <div class="col-10">
                                    <b> Number of Menu Items </b> 
                                    <br>
                                    {{ menuItemsCount }} (Unique: {{ loadedListings.length }})
                                </div>
                            </div>
                        </div>

                        <!-- Number of Sections -->
                        <div class="text-start pb-2">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> - </h5>
                                </div>
                                <div class="col-10">
                                    <b> Number of Sections </b> 
                                    <br>
                                    {{ detailedMenu.length }} sections
                                </div>
                            </div>
                        </div>

                        <!-- Overall Average Rating -->
                        <div class="text-start pb-2">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> - </h5>
                                </div>
                                <div class="col-10">
                                    <b> Overall Average Rating </b> 
                                    <br>
                                    {{ overallRating }} 
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- col 2: profile visits -->
                    <!-- <div class="col text-start pt-5 mx-3">
                        <h3> Profile Visits </h3>
                        <Line :data="profileData" :options="chartOptions"></Line>
                    </div> -->

                </div>

            </div>

        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import { Bar } from 'vue-chartjs';
    import { Line } from 'vue-chartjs';
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
    import { LineElement, PointElement } from 'chart.js';

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
    ChartJS.register(LineElement, PointElement)

    export default {
        name: 'profileVenue',
        components: {
            NavBar,
            Bar,
            Line
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        data() {
            return {
                // Info
                viewerID: localStorage.getItem('88B_accID'),
                viewerType: localStorage.getItem('88B_accType'),
                targetVenue: '',
                defaultProfilePhoto: '',

                // Data
                loadedListings: [],
                allReviews: [],
                detailedMenu: [],
                listingsMostReviewed: [],
                listingsBestRated: [],
                sectionsMostReviewed: [],
                sectionsBestRated: [],
                venueViews: [],
                menuItemsCount: 0,
                overallRating: 0,

                // flags
                dataLoaded: false,
                venueExists: null,
                selfView: false,
                powerView: false,
                clipboardItem: false,

                // Q & A
                answeredQuestions: [],
                unansweredQuestions: [],
                qaMode: 'unanswered',
                qaAnswer: '',

                // chart options
                chartOptions: {
                    responsive: true,
                    type: Object,
                    default: () => {},
                    scales: {
                        y: {
                            beginAtZero: true,
                            precision: 0,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                },
                
            }
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        computed: {
            // Number of reviews
            reviewsData() {
                const dates = [...new Set(this.allReviews.map(review => this.formatDateMonthYear(review.createdDate.$date)))];
                dates.sort((a, b) => {
                    const [monthA, yearA] = a.split('/');
                    const [monthB, yearB] = b.split('/');
                    if (yearA !== yearB) {
                        return yearA - yearB;
                    } else {
                        return monthA - monthB;
                    }
                });
                const counts = dates.map(date => this.allReviews.filter(review => this.formatDateMonthYear(review.createdDate.$date) === date).length);
                return {
                    labels: dates,
                    datasets: [
                        {
                            label: 'Number of Reviews',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            },

            // Spread of ratings
            ratingsData() { 
                let roundedRatings = this.loadedListings.map(listing => Math.round(listing.avgRating));
                const ratings = Array.from({length: 11}, (_, i) => i);
                const counts = ratings.map(value => Object.values(roundedRatings).filter(v => v === value).length);
                return {
                    labels: [...new Set([...ratings, ...Array.from({length: 11}, (_, i) => i)])].sort((a, b) => a - b),
                    datasets: [
                        {
                            label: 'Number of Ratings',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            },

            // Profile visits
            // profileData() {
            //     const dates = [...new Set(this.venueViews.map(view => this.formatDateMonthYear(view.date.$date)))];
            //     dates.sort((a, b) => {
            //         const [monthA, yearA] = a.split('/');
            //         const [monthB, yearB] = b.split('/');
            //         if (yearA !== yearB) {
            //             return yearA - yearB;
            //         } else {
            //             return monthA - monthB;
            //         }
            //     });
            //     const counts = dates.map(date => this.venueViews.filter(view => this.formatDateMonthYear(view.date.$date) === date).reduce((total, view) => total + view.count, 0));
            //     return {
            //         labels: dates,
            //         datasets: [
            //             {
            //                 label: 'Number of Views',
            //                 backgroundColor: '#747D92',
            //                 data: counts
            //             }
            //         ]
            //     }
            // },
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        mounted() {

            // Check if route params "venueID" is present
            if (this.$route.params.venueID != "" && this.$route.params.venueID != undefined) {
                this.targetVenue = this.$route.params.venueID;

                // If logged in as a venue, check if the venueID matches the logged in venue's ID
                if (this.viewerType == 'venue' && this.viewerID == this.targetVenue) {
                    this.selfView = true;
                }
                // If logged in as a user, check if user is an administrator
                else if (this.viewerType == 'user' && this.viewerID != "" && this.viewerID != undefined) {
                    this.getUserData();
                }
                // If insufficient permissions, redirect to your own profile page / login
                else {
                    this.$router.push('/login');
                }
                
            }
            // If no venueID is specified, display logged in venue's profile page
            else if (this.viewerType == 'venue') {
                this.targetVenue = this.viewerID;
                this.selfView = true;
            }
            // If not logged in as a venue, redirect to your own profile page / login
            else {
                this.$router.push('/login');
            }

            // Obtain venue data
            if (this.targetVenue != "" && this.targetVenue != undefined) {
                if (this.selfView) {
                    this.getVenueData();
                }
            }
            else {
                this.venueExists = false;
            }

        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        methods: {
            
            // Obtain user data
            async getUserData() {
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getUser/' + this.viewerID);

                    if (response != null && response.data != null && response.data != "" && !(Array.isArray(response.data) && response.data.length == 0)) {

                        // Check if user is admin
                        if (response.data.isAdmin == true) {
                            this.powerView = true;
                        }
                        else {
                            this.$router.push('/login');
                        }

                        this.getVenueData();
                    }
                    else {
                        this.dataLoaded = null;
                    }
                }
                catch (error) {
                    this.dataLoaded = null;
                }
            },

            // Obtain venue data
            async getVenueData() {
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getVenue/' + this.targetVenue);

                    if (response != null && response.data != null && response.data != "" && !(Array.isArray(response.data) && response.data.length == 0)) {

                        this.targetVenue = response.data;

                        // Set questions and answers data
                        let qaData = this.targetVenue["questionsAnswers"];
                        if (qaData.length > 0) {
                            for (let qa in qaData) {
                                let answer = qaData[qa]["answer"];
                                if (answer != "") {
                                    this.answeredQuestions.push(qaData[qa]);
                                }
                                else {
                                    this.unansweredQuestions.push(qaData[qa]);
                                }
                            }
                        }

                        // Set and sort menu data
                        this.detailedMenu = this.targetVenue["menu"];
                        this.detailedMenu.sort((a, b) => (a.sectionOrder > b.sectionOrder) ? 1 : -1); // Sort by section order
                        for (let section of this.detailedMenu) {
                            section.sectionMenu.sort((a, b) => (a.itemOrder > b.itemOrder) ? 1 : -1); // Sort by item order
                        }

                        this.venueExists = true;
                        this.loadData();
                    }
                    else {
                        this.venueExists = false;
                    }
                }
                catch (error) {
                    this.dataLoaded = null;
                }
            },

            // Load other data
            async loadData() {

                // Get listing data for each item in menu
                try {

                    for (let section of this.detailedMenu) {

                        section.sectionDetails = {
                            sectionReviews: [],
                            sectionUniqueDrinks: [],
                            sectionRating: 0
                        };

                        for (let item of section.sectionMenu) {

                            // Find item in loadedListings
                            let listingData = this.loadedListings.find(i => i._id['$oid'] == item.itemID['$oid']);

                            // If not found, get from server
                            if (listingData == undefined) {
                                let response = await this.$axios.get('http://127.0.0.1:5000/getListing/' + item.itemID['$oid']);
                                listingData = response.data;

                                if (Array.isArray(listingData) && listingData.length == 0) {
                                    // Remove item from section
                                    section.sectionMenu = section.sectionMenu.filter(i => i.itemID['$oid'] != item.itemID['$oid']);
                                }
                                // If found, obtain additional data and add to loadedListings
                                else if (listingData != null && listingData != "") {

                                    // Get reviews
                                    let reviewResponse = await this.$axios.get('http://127.0.0.1:5000/getReviewByTarget/' + item.itemID['$oid']);
                                    let reviewData = reviewResponse.data;

                                    if (Array.isArray(reviewData) && reviewData.length == 0) {
                                        listingData["reviews"] = [];
                                        listingData["avgRating"] = 0;
                                    }
                                    else if (reviewData != null && reviewData != "") {
                                        listingData["reviews"] = reviewData;
                                        listingData["avgRating"] = reviewData.reduce((a, b) => a + b.rating, 0) / reviewData.length;
                                    }
                                    else {
                                        // Error
                                        throw "Error: Unexpected response from server!";
                                    }
                                    
                                }
                                else {
                                    // Error
                                    throw "Error: Unexpected response from server!";
                                }

                                // Add to loadedListings and allReviews
                                this.loadedListings.push(listingData);
                                this.allReviews.push(...listingData["reviews"]);
                            }

                            // Set item data (listingData should be valid here)
                            if (!(Array.isArray(listingData) && listingData.length == 0)) {

                                item.itemDetails = {
                                    itemPhoto: listingData["photo"],
                                    itemName: listingData["listingName"],
                                    itemType: listingData["drinkType"],
                                    itemTypeCategory: listingData["typeCategory"],
                                    itemABV: listingData["abv"],
                                    itemCountry: listingData["originCountry"],
                                    itemDesc: listingData["officialDesc"],
                                    itemReviews: listingData["reviews"],
                                    itemRating: listingData["avgRating"],
                                };

                                // Push item reviews to sectionDetails
                                if (!section.sectionDetails.sectionUniqueDrinks.includes(listingData["_id"])) {
                                    section.sectionDetails.sectionUniqueDrinks.push(listingData["_id"]);
                                    section.sectionDetails.sectionReviews.push(...listingData["reviews"]);
                                }

                            }

                        }

                        // Calculate section rating
                        if (section.sectionDetails.sectionReviews.length > 0) {
                            section.sectionDetails.sectionRating = section.sectionDetails.sectionReviews.reduce((a, b) => a + b.rating, 0) / section.sectionDetails.sectionReviews.length;
                        }

                    }

                    // Obtain mostReviewed listings
                    this.listingsMostReviewed = this.loadedListings.sort((a, b) => (a.reviews.length < b.reviews.length) ? 1 : -1).slice(0, 5);
                    
                    // Obtain bestRated listings
                    this.listingsBestRated = this.loadedListings.sort((a, b) => (a.avgRating < b.avgRating) ? 1 : -1).slice(0, 5);

                    // Obtain mostReviewed sections
                    this.sectionsMostReviewed = this.detailedMenu.sort((a, b) => (a.sectionDetails.sectionReviews.length < b.sectionDetails.sectionReviews.length) ? 1 : -1).slice(0, 5);

                    // Obtain bestRated sections
                    this.sectionsBestRated = this.detailedMenu.sort((a, b) => (a.sectionDetails.sectionRating < b.sectionDetails.sectionRating) ? 1 : -1).slice(0, 5);

                    // Obtain number of menu items
                    this.menuItemsCount = this.detailedMenu.reduce((a, b) => a + b.sectionMenu.length, 0);

                    // Obtain overall average rating
                    if (this.allReviews.length > 0) {
                        this.overallRating = this.allReviews.reduce((a, b) => a + b.rating, 0) / this.allReviews.length;
                    }

                    // Change rating of drinks to '-' if no reviews, else round to 1 decimal place
                    this.loadedListings.forEach(listing => {
                        if (listing.reviews.length == 0) {
                            listing.avgRating = '-';
                        }
                        else {
                            listing.avgRating = listing.avgRating.toFixed(1);
                        }
                    });

                    // Change rating of sections to '-' if no reviews, else round to 1 decimal place
                    this.detailedMenu.forEach(section => {
                        if (section.sectionDetails.sectionReviews.length == 0) {
                            section.sectionDetails.sectionRating = '-';
                        }
                        else {
                            section.sectionDetails.sectionRating = section.sectionDetails.sectionRating.toFixed(1);
                        }
                    });

                    // Set data loaded flag
                    this.dataLoaded = true;
                    
                }
                catch (error) {
                    this.dataLoaded = null;
                }

            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Helper function to format date to month/year
            formatDateMonthYear(dateTimeString) {
                let datePart = dateTimeString.split("T")[0];
                // splitting the date into year, month, and day
                let [year, month] = datePart.split("-");
                // formatting the date
                let formattedDate = `${month}/${year}`;
                return formattedDate
            },
            
            // Copy to Clipboard
            copyToClipboard(text) {
                navigator.clipboard.writeText(text)
                .then(() => {
                    this.clipboardItem = true;
                    setTimeout(() => {
                        this.clipboardItem = false;
                    }, 3000);
                })
                .catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            },

            // Send Answer to a Question
            async sendAnswer(qa) {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/sendAnswers', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            questionsAnswersID: qa._id['$oid'],
                            answer: this.qaAnswer,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                }
                catch (error) {
                    alert("An error occurred while attempting to send your answer, please try again!\nWe have tried to copy your answer's text to your clipboard.");
                    // Copy answer text to clipboard
                    this.copyToClipboard(this.qaAnswer);
                }

                // Refresh page
                this.$router.go(0);
            },

        }
    }
</script>