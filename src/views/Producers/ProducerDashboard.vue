<!-- HTML -->
<template>
    <NavBar />

    <!-- main content -->

    <div class="container pt-5">

        <div class="row">

            <!-- left pane -->
            <div class="col-3">

                <!-- row 1: producer info -->
                <div class="row">
                    <!-- producer name -->
                    <div class="col-8 text-start">
                        <h2> {{ specified_producer.producerName }} </h2>
                    </div>
                    <!-- producer profile photo -->
                    <div class="col-4">
                        <img :src="selectedImage || 'data:image/jpeg;base64,' + (specified_producer['photo'] || defaultProfilePhoto)" 
                            alt="" style="width: 100px; height: 100px; z-index: 1;">
                    </div>
                </div>

                <!-- row 2: return to profile -->
                <div class="row pt-3">
                    <button type="button" class="btn primary-btn-outline-thick rounded-0 default-clickable-text" v-on:click="goBack()"> 
                        Return to profile 
                    </button>
                </div>

                <!-- row 3: recent fan posted questions -->
                <div class="row pt-3">
                    <div class="square primary-square rounded p-3 mb-3 text-start">
                        <!-- header text -->
                        <div class="square-inline pb-2">
                            <h4 class="square-inline text-start mr-auto"> Recent Fan Posted Questions </h4>
                        </div>
                        <!-- body -->
                        <div>
                            <!-- v-for loop here-->
                            <div v-for="(qa, index) in unansweredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                <b> Q: </b> {{ qa.question }} 
                                <div class="d-flex align-items-center pb-3">
                                    <textarea class="search-bar form-control rounded fst-italic question-box flex-grow-1" type="text" placeholder="Reply to question" v-model="answers[qa._id.$oid]"></textarea>
                                    <div v-on:click="sendAnswer(qa)" class="send-icon ps-1">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- row 4: latest review -->
                <div class="row pt-3">
                    <div class="square primary-square rounded p-3 mb-3 text-start">
                        <!-- header text -->
                        <div class="square-inline pb-2">
                            <h4 class="square-inline text-start mr-auto"> Latest Reviews </h4>
                        </div>
                        <!-- body -->
                        <div>
                            <!-- v-for loop here-->
                            <div v-for="review in allReviews" v-bind:key="review._id" class="py-2">
                                <router-link :to="{ path: '/profile/user/' + review.userID.$oid }" class="reverse-clickable-text">
                                    <b> @{{ getUsernameFromID(review.userID.$oid) }}</b>
                                </router-link> 
                                rated 
                                <router-link :to="{ path: '/listing/view/' + getListingFromID(review.reviewTarget.$oid)._id.$oid }" class="reverse-clickable-text">
                                    <u> {{ getListingFromID(review.reviewTarget.$oid).listingName }} </u>
                                </router-link>
                                <span class="ps-2">
                                    <i> {{ review.rating }} 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                        </svg>
                                    </i>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- right pane -->
            <div class="col-9 ps-5">

                <!-- row 1: review of your expressions & profile visits -->
                <div class="row">

                    <!-- col 1: review of your expressions -->
                    <div class="col text-start pt-5 mx-3">
                        <h3> Review of Your Expressions </h3>
                        <Line :data="reviewsData" :options="chartOptions"></Line>
                    </div>

                    <!-- col 2: profile visits -->
                    <div class="col text-start pt-5 mx-3">
                        <h3> Profile Visits </h3>
                        <Line :data="profileData" :options="chartOptions"></Line>
                    </div>
\
                </div>

                <!-- row 2: your best rated expressions & your most reviewed expressions -->
                <div class="row">

                    <!-- col 1: your best rated expressions -->
                    <div class="col text-start pt-2 mx-3">
                        <h3> Your Best Rated Expressions </h3>
                        <div class="text-start pb-2" v-for="listing in mostPopular" v-bind:key="listing._id">
                            <router-link :to="{ path: '/listing/view/' + listing._id.$oid }" class="reverse-clickable-text">
                                <div class="d-flex align-items-center">
                                    <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                    <p class="ms-3 default-clickable-text"> 
                                        <b> {{ listing.listingName }} </b> 
                                        <br>
                                        {{ this.sortedAverageRatings[listing.listingName] || "-" }} 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                        </svg>
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>

                    <!-- col 2: your most reviewed expressions -->
                    <div class="col text-start pt-2 mx-3">
                        <h3> Your Most Reviewed Expressions </h3>
                        <div class="text-start pb-2" v-for="listing in mostDiscussed" v-bind:key="listing._id">
                            <router-link :to="{ path: '/listing/view/' + listing._id.$oid }" class="reverse-clickable-text">
                                <div class="d-flex align-items-center">
                                    <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                    <p class="ms-3 default-clickable-text"> 
                                        <b> {{ listing.listingName }} </b> 
                                        <br>
                                        {{ this.reviewCounts[listing.listingName] }} reviews
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>

                </div> <!-- end of row 2-->

                <!-- row 3: spread of ratings & your most reviewed categories -->
                <div class="row">

                    <!-- col 1: spread of ratings -->
                    <div class="col text-start pt-5 mx-3">
                        <h3> Spread of Ratings </h3>
                        <Bar :data="ratingsData" :options="chartOptions" />
                    </div>

                    <!-- col 2: your most reviewed categories -->
                    <div class="col text-start pt-5 mx-3">
                        <h3> Your Most Reviewed Categories </h3>
                        <div class="text-start pb-2" v-for="(category, index) in mostDiscussedCategories" v-bind:key="category">
                            <div class="row ms-3 default-clickable-text"> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> {{ index + 1 }} </h5>
                                </div>
                                <div class="col-10">
                                    <b> {{ category[0] }} </b> 
                                    <br>
                                    {{ category[1] || "-" }} reviews
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

        </div> <!-- end of row -->
        
    </div> <!-- end of main content -->

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    import NavBar from '@/components/NavBar.vue';
    import { Bar } from 'vue-chartjs'
    import { Line } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    import { LineElement, PointElement } from 'chart.js'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
    ChartJS.register(LineElement, PointElement)

    export default {
        components: {
            NavBar,
            Bar,
            Line
        },
        computed: {
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
            profileData() {
                const dates = [...new Set(this.producerViews.map(view => this.formatDateMonthYear(view.date.$date)))];
                dates.sort((a, b) => {
                    const [monthA, yearA] = a.split('/');
                    const [monthB, yearB] = b.split('/');
                    if (yearA !== yearB) {
                        return yearA - yearB;
                    } else {
                        return monthA - monthB;
                    }
                });
                const counts = dates.map(date => this.producerViews.filter(view => this.formatDateMonthYear(view.date.$date) === date).reduce((total, view) => total + view.count, 0));
                return {
                    labels: dates,
                    datasets: [
                        {
                            label: 'Number of Views',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            },
            ratingsData() { 
                const ratings = [...new Set(Object.values(this.roundedSortedRatings))].sort((a, b) => a - b);
                const counts = ratings.map(value => Object.values(this.roundedSortedRatings).filter(v => v === value).length);
                return {
                    labels: ratings,
                    datasets: [
                        {
                            label: 'Number of Ratings',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            },
        },
        data() {
            return {
                // data from database
                producers: [],
                listings: [],
                reviews: [],
                users: [],
                producersProfileViews: [],

                user_id: "",
                userType: "",
                correctProducer: false,

                // specified producer
                producer_id: null,
                specified_producer: {},

                // for Q&A
                unansweredQuestions: [],
                answers: {},

                // all drinks that producer has
                allDrinks: [],
                drinkCounts: {},
                drinkCategoryCounts: {},
                sortedDrinksCounts: {},
                sortedCategoryCounts: {},
                mostDiscussed: [],
                mostDiscussedCategories: [],

                // all reviews for producer's drinks
                allReviews: [],
                drinkRatings: {},
                reviewCounts: {},
                sortedReviewCounts: {},
                sortedAverageRatings: {},
                roundedSortedRatings: {},
                mostPopular: [],

                // all profile visits for producer
                producerViews: [],

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
            };
        },
        async mounted() {
            var userID = localStorage.getItem('88B_accID')
            if(userID != null){
                this.user_id = userID;
            }

            var userType = localStorage.getItem('88B_accType');
            if(userType != null){
                this.userType = userType;
                console.log(this.userType)
            }

            await this.loadData();
        },
        methods: {
            // load data from database
            async loadData() {
                // Get the query string parameters (listing ID) from the URL
                this.producer_id = this.$route.params.id;
                    if (this.producer_id == null) {
                        // redirect to page
                        this.$router.push('/');
                    }
                    else {
                        // check if user_id same as producer_id
                        if(this.user_id == this.producer_id && this.userType == "producer"){
                            this.correctProducer = true;
                        }
                    }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
                        this.specified_producer = this.producers.find(producer => producer["_id"]["$oid"] == this.producer_id); // find specified producer
                        this.checkProducerQuestions();

                    } 
                    catch (error) {
                        console.error(error);
                    }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
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
                 // producersProfileViews
                // _id, producerID, views
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducersProfileViews');
                        this.producersProfileViews = response.data;
                        let producerProfileViewInfo = this.producersProfileViews.find(view => view.producerID["$oid"] == this.producer_id);
                        let producerViews = producerProfileViewInfo.views;
                        this.producerViews = producerViews
                    }
                    catch (error) {
                        console.error(error);
                    }

                // fetch all methods
                this.getAllDrinks()
                this.getAllReviews()

                this.getCountsByType()
                this.getCountsByCategory()

                this.getTotalCounts()
                this.getTotalCategoryCounts()

                this.getRatingsByType()
                this.getAverageRatings()
                this.getReviewCounts()
                this.getTotalReviewCounts()
                this.roundSortedAverageRatings()

                this.getMostPopular()
                this.getMostDiscussed()
                this.getMostDiscussedCategory()
            },

            // go back to profile page
            goBack() {
                this.$router.go(-1)
            },

            // get producer's answered & unanswered questions
            checkProducerQuestions() {
                let answeredQuestions = this.specified_producer["questionsAnswers"];
                if (answeredQuestions.length > 0) {
                    for (let qa in answeredQuestions) {
                        let answer = answeredQuestions[qa]["answer"];
                        if (answer == "") {
                            this.unansweredQuestions.push(answeredQuestions[qa]);
                        }
                    }
                }
            },

            // send answer that producers give to users
            async sendAnswer (qa) {
                let q_and_a_id = qa._id.$oid;
                let answer = this.answers[q_and_a_id];
                try {
                    const response = await this.$axios.post('http://127.0.0.1:5200/sendAnswers', 
                        {
                            producerID: this.producer_id,
                            questionsAnswersID: q_and_a_id,
                            answer: answer,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // get all drinks that a producer has
            getAllDrinks() {
                let allProducerDrinks = this.listings.filter(listing => listing.producerID["$oid"] == this.producer_id);
                this.allDrinks = allProducerDrinks;
            },

            // get all reviews that a producer has
            getAllReviews() {
                let allProducerReviews = this.reviews.filter(review => {
                    let review_target = review.reviewTarget["$oid"];
                    let all_drinks = this.allDrinks;
                    return all_drinks.some(drink => drink._id["$oid"] === review_target);
                });
                this.allReviews = allProducerReviews;
            },

            getUserFromID(userID) {
                let user = this.users.find(user => user._id["$oid"] == userID);
                if (user) {
                    return user
                }
            },

            // get username from userID
            getUsernameFromID(userID) {
                let user = this.getUserFromID(userID);
                if (user) {
                    return user.username
                }
            },

            // get listing from listingID
            getListingFromID(listingID) {
                let listing = this.listings.find(listing => listing._id["$oid"] == listingID);
                if (listing) {
                    return listing
                }
            },

            // find drink name given reviewTarget
            findDrinkNameForReview(reviewTarget) {
                let drink_name = this.listings.find(listing => listing._id["$oid"] == reviewTarget["$oid"]).listingName;
                return drink_name;
            },

            // find drink name given listing
            findDrinkNameForListing(listing) {
                let drink_name = listing.listingName;
                return drink_name;
            },

            // find drink type given listing
            findDrinkTypeForListing(listing) {
                let drink_type = listing.drinkType;
                return drink_type;
            },

            // get compiled dictionary of ratings of each type of drink
            getRatingsByType() {
                let allProducerDrinkRatings = {};
                this.allReviews.forEach(review => {
                    let drink_name = this.findDrinkNameForReview(review.reviewTarget);
                    let rating = review["rating"];
                    allProducerDrinkRatings[drink_name] = allProducerDrinkRatings[drink_name] || [];
                                                            allProducerDrinkRatings[drink_name].push(rating);
                });
                this.drinkRatings = allProducerDrinkRatings;
            },

            // get compiled dictionary of count of each type of drink
            getCountsByType() {
                let allProducerDrinkCounts = {};
                this.allDrinks.forEach(listing => {
                    let drink_name = this.findDrinkNameForListing(listing);
                    allProducerDrinkCounts[drink_name] = allProducerDrinkCounts[drink_name] ? 
                                                            allProducerDrinkCounts[drink_name] + 1 : 1;
                });
                this.drinkCounts = allProducerDrinkCounts;
            },

            // get compiled dictionary of count of each category of drink
            getCountsByCategory() {
                let allCategoryDrinkCounts = {};
                this.allDrinks.forEach(listing => {
                    let drink_category = this.findDrinkTypeForListing(listing);
                    allCategoryDrinkCounts[drink_category] = allCategoryDrinkCounts[drink_category] ? 
                                                            allCategoryDrinkCounts[drink_category] + 1 : 1;
                });
                this.drinkCategoryCounts = allCategoryDrinkCounts;
            },

            // get average ratings for each listing
            getAverageRatings() {
                const averageRatings = {};
                for (const [drink, ratings] of Object.entries(this.drinkRatings)) {
                    const filteredRatings = ratings.filter(value => value !== "-").map(Number);
                    if (filteredRatings.length > 0) {
                        const averageRating = filteredRatings.reduce((sum, rating) => sum + rating, 0) / filteredRatings.length;
                        averageRatings[drink] = averageRating;
                    }
                }
                const sortedProducerAverageRatings = Object.fromEntries(Object.entries(averageRatings)
                                                        .sort((a, b) => b[1] - a[1]));
                this.sortedAverageRatings = sortedProducerAverageRatings;
            },

            // get number of reviews for each listing
            getReviewCounts() {
                const reviewCounts = {};
                // Iterate through all reviews
                this.allReviews.forEach(review => {
                    const reviewTargetName = this.findDrinkNameForReview(review.reviewTarget);
                    // Check if reviewTargetId is already in reviewCounts
                    if (reviewTargetName in reviewCounts) {
                        reviewCounts[reviewTargetName]++;
                    } else {
                        reviewCounts[reviewTargetName] = 1;
                    }
                });

                // Iterate through all drinks
                this.allDrinks.forEach(drink => {
                    const drinkName = drink.listingName;
                    // Check if drinkId is not in reviewCounts
                    if (! (drinkName in reviewCounts)) {
                        reviewCounts[drinkName] = 0;
                    }
                });

                this.reviewCounts = reviewCounts;
            },

            // get total counts for each listing
            getTotalCounts() {
                const drinkCountsArray = Object.entries(this.drinkCounts);
                drinkCountsArray.sort((a, b) => b[1] - a[1]);
                const sortedProducerDrinkCounts = Object.fromEntries(drinkCountsArray);
                this.sortedDrinksCounts = sortedProducerDrinkCounts;
            },

            // get total reviews for each listing
            getTotalReviewCounts() {
                const reviewCountsArray = Object.entries(this.reviewCounts);
                reviewCountsArray.sort((a, b) => b[1] - a[1]);
                const sortedProducerReviewCounts = Object.fromEntries(reviewCountsArray);
                this.sortedReviewCounts = sortedProducerReviewCounts;
                console.log(this.sortedReviewCounts)
            },

            // get total counts for each category
            getTotalCategoryCounts() {
                const drinkCategoryCountsArray = Object.entries(this.drinkCategoryCounts);
                drinkCategoryCountsArray.sort((a, b) => b[1] - a[1]);
                const sortedCategoryCounts = Object.fromEntries(drinkCategoryCountsArray);
                this.sortedCategoryCounts = sortedCategoryCounts;
            },

            // get the most popular drinks
            getMostPopular() {
                // get the average ratings
                const averageRatings = this.sortedAverageRatings;
                // get the first 5 items from the average ratings
                let firstFiveItems = Object.entries(averageRatings).slice(0, 5);
                firstFiveItems = firstFiveItems.map(item => {
                    const listing = this.listings.find(listing => listing.listingName === item[0]);
                    return listing ? [...item, listing._id] : item;
                });
                // if firstFiveItems is less than 5, get the remaining from this.allDrinks
                if (firstFiveItems.length < 5) {
                    this.allDrinks.forEach(drink => {
                        if (!firstFiveItems.some(item => item[0] == drink.listingName)) {
                            let drinkName = drink.listingName;
                            let drinkCount = this.drinkCounts[drink.listingName];
                            let drinkID = drink._id
                            firstFiveItems.push([drinkName, drinkCount, drinkID]);
                        }
                    });
                }
                firstFiveItems = firstFiveItems.slice(0,5)
                this.mostPopular = firstFiveItems;
                this.mostPopular = this.mostPopular.map(item => {
                    return this.listings.find(listing => listing._id["$oid"] == item[2]["$oid"]);
                });
            },

            // get the most discussed drinks
            getMostDiscussed() {
                // get the drink counts
                const drinkCounts = this.sortedReviewCounts;
                console.log(this.sortedReviewCounts)
                // get the first 5 items from the drink counts
                let firstFiveItems = Object.entries(drinkCounts).slice(0, 5);
                firstFiveItems = firstFiveItems.map(item => {
                    const listing = this.listings.find(listing => listing.listingName === item[0]);
                    return listing ? [...item, listing._id] : item;
                });
                // if firstFiveItems is less than 5, get the remaining from this.allDrinks
                if (firstFiveItems.length < 5) {
                    this.allDrinks.forEach(drink => {
                        if (!firstFiveItems.some(item => item[0] == drink.listingName)) {
                            let drinkName = drink.listingName;
                            let drinkCount = this.drinkCounts[drink.listingName];
                            let drinkID = drink._id
                            firstFiveItems.push([drinkName, drinkCount, drinkID]);
                        }
                    });
                }
                firstFiveItems = firstFiveItems.slice(0,5)
                this.mostDiscussed = firstFiveItems;
                this.mostDiscussed = this.mostDiscussed.map(item => {
                    return this.listings.find(listing => listing._id["$oid"] == item[2]["$oid"]);
                });
            },

            // get the most discussed categories
            getMostDiscussedCategory() {
                // get the drink category counts
                const drinkCategoryCounts = this.sortedCategoryCounts
                // get the first 5 items from the drink counts
                let firstFiveItems = Object.entries(drinkCategoryCounts).slice(0, 5);
                // get the first 5 items from the drink category counts
                this.mostDiscussedCategories = firstFiveItems;
            },

            roundSortedAverageRatings() {
                const roundedAverageRatings = {};
                for (const [drink, rating] of Object.entries(this.sortedAverageRatings)) {
                    roundedAverageRatings[drink] = Math.round(rating);
                }
                this.roundedSortedRatings = roundedAverageRatings;
                console.log(this.roundedSortedRatings)
            },

            formatDateMonthYear(dateTimeString) {
                let datePart = dateTimeString.split("T")[0];
                // splitting the date into year, month, and day
                let [year, month] = datePart.split("-");
                // formatting the date
                let formattedDate = `${month}/${year}`;
                return formattedDate
            }

        }
    };
</script>