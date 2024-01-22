<template>
  <div v-if="user" class="userprofile">

    <div class="container text-start">
        <div class="row">
            <!-- user profile -->
            <div class="col-12 col-md-4 mb-5">

                <div class="container">

                    <!-- basic information -->
                    <div class="row">
                        <div class="col-8">
                            <h3>{{ user.Name }}</h3> 
                            <b>@{{ user.Username }}</b> 
                            <br/>
                            <!-- todo --> 0 Drinks tasted 
                            <br/>
                        </div>
                        <!-- profile picture -->
                        <div class="col-4 text-end">
                            <img src="https://cdn.vectorstock.com/i/preview-1x/15/40/blank-profile-picture-image-holder-with-a-crown-vector-42411540.jpg" 
                                alt="" class="rounded-circle border border-dark profile-img">  
                        </div>
                    </div>

                    <!-- additional information -->
                    <div class="mt-3">
                        <span class="float-start"><b>Member since</b></span>
                        <!-- todo --> <span class="float-end">Sept 2021</span>
                        <br/>
                        <span class="float-start"><b>Drink of Choice</b></span>
                        <span class="float-end">{{ drinkOfChoice }}</span>
                        <br/>
                    </div>

                    <!-- buttons -->
                    <div class="row mt-3">
                        <button class="btn btn-outline-primary">Edit Profile</button>
                        <button class="btn btn-warning mt-3">View My Analytics</button>
                        <a href="#" class="mt-3">Want to be a moderator? Apply here!</a>
                    </div>

                    <!-- badges -->
                    <div class="mt-3">
                        <h3>Badges Unlocked</h3>
                        <hr>

                        <div class="container text-center">
                            <div class="row">
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                            </div>
                            <div class="row mt-3">
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                                <div class="col">
                                    <img src="https://img.freepik.com/free-vector/realistic-vector-icon-golden-king-queen-crown-isolated-white-background_134830-2012.jpg" 
                                        alt="" class="rounded-circle border border-dark badge-img">
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-3">
                            <a href="#">Learn more about badges.</a>
                        </div>

                    </div>
                    
                </div>

            </div>

            <!-- reviews and lists -->
            <div class="col-12 col-md-8">

                <ul class="nav nav-pills">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" data-bs-toggle="pill" href="#reviews">Reviews</a>
                    </li>
                    <li class="nav-item ms-2">
                        <a class="nav-link" data-bs-toggle="pill" href="#lists">My Drink Lists</a>
                    </li>
                </ul>

                <div class="tab-content container mt-2">
                    <!-- reviews tab -->
                    <div class="tab-pane fade show active" id="reviews">
                        <h4 class="mt-3">Favourite Drinks</h4>
                        <div>
                            <div class="image-container">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="rounded border border-dark-subtle border-2 bottle-img me-3">
                                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512" class="icon">
                                    <path d="M0 48C0 21.5 21.5 0 48 0l0 48V441.4l130.1-92.9c8.3-6 19.6-6 27.9 0L336 441.4V48H48V0H336c26.5 0 48 21.5 48 48V488c0 9-5 17.2-13 21.3s-17.6 3.4-24.9-1.8L192 397.5 37.9 507.5c-7.3 5.2-16.9 5.9-24.9 1.8S0 497 0 488V48z"/>
                                </svg>
                            </div>

                            <div class="image-container">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="rounded border border-dark-subtle border-2 bottle-img me-3">
                                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512" class="icon">
                                    <path d="M0 48C0 21.5 21.5 0 48 0l0 48V441.4l130.1-92.9c8.3-6 19.6-6 27.9 0L336 441.4V48H48V0H336c26.5 0 48 21.5 48 48V488c0 9-5 17.2-13 21.3s-17.6 3.4-24.9-1.8L192 397.5 37.9 507.5c-7.3 5.2-16.9 5.9-24.9 1.8S0 497 0 488V48z"/>
                                </svg>
                            </div>
                        </div>

                        <h4 class="mt-4">Recent Activity</h4>
                        <div>
                            <div class="image-container">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="rounded border border-dark-subtle border-2 bottle-img me-3">
                                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512" class="icon">
                                    <path d="M0 48C0 21.5 21.5 0 48 0l0 48V441.4l130.1-92.9c8.3-6 19.6-6 27.9 0L336 441.4V48H48V0H336c26.5 0 48 21.5 48 48V488c0 9-5 17.2-13 21.3s-17.6 3.4-24.9-1.8L192 397.5 37.9 507.5c-7.3 5.2-16.9 5.9-24.9 1.8S0 497 0 488V48z"/>
                                </svg>
                            </div>

                            <div class="image-container">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="rounded border border-dark-subtle border-2 bottle-img me-3">
                                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512" class="icon">
                                    <path d="M0 48C0 21.5 21.5 0 48 0l0 48V441.4l130.1-92.9c8.3-6 19.6-6 27.9 0L336 441.4V48H48V0H336c26.5 0 48 21.5 48 48V488c0 9-5 17.2-13 21.3s-17.6 3.4-24.9-1.8L192 397.5 37.9 507.5c-7.3 5.2-16.9 5.9-24.9 1.8S0 497 0 488V48z"/>
                                </svg>
                                <!-- for bookmarked bottles -->
                                <!-- <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512"><path d="M0 48V487.7C0 501.1 10.9 512 24.3 512c5 0 9.9-1.5 14-4.4L192 400 345.7 507.6c4.1 2.9 9 4.4 14 4.4c13.4 0 24.3-10.9 24.3-24.3V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48z"/></svg> -->
                            </div>
                        </div>

                        <h4 class="mt-4">Recent Reviews</h4>
                        <div>
                            <div style="display: flex" class="mb-3">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="border border-dark-subtle border-2 bottle-img me-3">
                                <div>
                                    <h3>Bombay</h3>
                                    <h2>
                                        3.8 
                                        <svg class="mb-2" xmlns="http://www.w3.org/2000/svg" height="18" width="20.25" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>
                                    </h2>
                                    <!-- max 2 lines of review -->
                                    <p>Review</p>
                                    <span class="badge rounded-pill text-bg-primary me-2">Primary</span>
                                    <span class="badge rounded-pill text-bg-success me-2">Success</span>
                                </div>
                            </div>

                            <div style="display: flex">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="border border-dark-subtle border-2 bottle-img me-3">
                                <div>
                                    <h3>Bombay</h3>
                                    <h2>
                                        3.8 
                                        <svg class="mb-2" xmlns="http://www.w3.org/2000/svg" height="18" width="20.25" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>
                                    </h2>
                                    <!-- max 2 lines of review -->
                                    <p>Review</p>
                                    <span class="badge rounded-pill text-bg-primary me-2">Primary</span>
                                    <span class="badge rounded-pill text-bg-success me-2">Success</span>
                                </div>
                            </div>

                        </div>

                    </div>

                    <!-- lists tab -->
                    <div class="tab-pane fade" id="lists">
                        <!-- drink lists -->
                        <div v-if="showCurrentContent" class="mt-3">

                            <button type="button" class="btn btn-outline-primary mb-3">Create New List</button>

                            <div style="display: flex" class="mb-5">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="border border-dark-subtle border-2 bottle-img me-3">
                                <div style="height: 150px; display: flex; flex-direction: column;" >
                                    <h3 class="mt-1">Drinks I Have Tried</h3>
                                    <p>List Description (Optional)</p>
                                    <div style="display: flex; margin-top: auto" class="mb-1">
                                        <a class="me-4" @click="toggleView" href="#">View List</a>
                                        <a class="me-4" @click="toggleView" href="#">Edit List</a>
                                        <a @click="toggleView" href="#">Delete List</a>
                                    </div>
                                </div>
                            </div>

                            <div style="display: flex" class="mb-5">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="border border-dark-subtle border-2 bottle-img me-3">
                                <div style="height: 150px; display: flex; flex-direction: column;" >
                                    <h3 class="mt-1">Drinks I Have Tried</h3>
                                    <p>List Description (Optional)</p>
                                    <div style="display: flex; margin-top: auto" class="mb-1">
                                        <a class="me-4" @click="toggleView" href="#">View List</a>
                                        <a class="me-4" href="#">Edit List</a>
                                        <a href="#">Delete List</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- list details -->
                        <div v-else>
                            <div class="row">
                                <div class="col-12 col-md-6">
                                    <h3>Drinks I Have Tried</h3>
                                </div>
                                <div class="col-12 col-md-6">
                                    <button @click="toggleView" type="button" class="btn btn-outline-primary">Back to Lists</button>
                                    <button type="button" class="btn btn-outline-primary ms-3" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Drink to List</button>
                                </div>
                            </div>
                            <!-- add drink modal -->
                            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered">
                                    <div class="modal-content">
                                    <!-- <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div> -->
                                    <div class="modal-body">
                                        <h3>Add drink to list</h3>
                                        <!-- search bar  -->
                                        <div class="input-group mb-3">
                                            <input type="text" class="form-control" placeholder="Search for drink" aria-label="Recipient's username" aria-describedby="button-addon2">
                                            <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                                        </div>
                                        <div>
                                            <button type="button" class="btn btn-primary">Add to List</button>
                                        </div>
                                    </div>
                                    <!-- <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary">Save changes</button>
                                    </div> -->
                                    </div>
                                </div>
                            </div>

                            <div style="display: flex" class="mb-3">
                                <img src="https://www.theliquorshop.com.sg/cdn/shop/products/jinro-chamisul-soju-one_700x700.jpg?v=1660441866" alt="" class="border border-dark-subtle border-2 bottle-img me-3">
                                <div style="height: 150px; display: flex; flex-direction: column;">
                                    <h3>Bombay</h3>
                                    <p>Drink information </p>
                                    <div style="display: flex; margin-top: auto" class="mb-0">
                                        <a @click="toggleView" href="#" style="text-decoration: none;">
                                            <!-- cross icon -->
                                            <svg class=mb-1 xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                                <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
                                            </svg>
                                            Delete from list
                                        </a>
                                    </div>

                                </div>
                                <div>
                                    <h2>
                                        3.8 
                                        <svg class="mb-2" xmlns="http://www.w3.org/2000/svg" height="18" width="20.25" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        
    </div>
    


 
  </div>
</template>

<script>
// for bookmarking of bottles
// export default {
//   methods: {
//     handleIconClick() {
//       // Add your logic for the icon click action here
//       alert("Icon clicked!");
//     },
//   },
// };

// toggling between lists and list details
export default {
    data() {
        return {
            // user detail [TODO: CHANGE BASED ON USER]
            userID: "659ed6047edad51baf9d3362",
            user: {},
            drinkOfChoice: "",
            // data from database
            countries: [],
            listings: [],
            producers: [],
            reviews: [],
            users: [],
            venues: [],
            // data for tab
            showCurrentContent: true, // Initially show the current content
        };
    },
    mounted() {
        this.loadData();
        this.getUser(this.userID);
    },
    methods: {
        // load data from database
        async loadData() {
            // Countries
            try {
                const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                this.countries = response.data;
            } 
            catch (error) {
                console.error(error);
            }
            // Listings
            try {
                const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                this.listings = response.data;
                // originally, make filteredListings the entire collection of listings
                this.filteredListings = this.listings;
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
            // Reviews
            try {
                const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                this.reviews = response.data;
            }
            catch (error) {
                console.error(error);
            }
            // Users
            try {
                const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                this.users = response.data;

                this.getUser(this.userID);
                console.log(this.user);
                this.getDrinkOfChoice();
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
        // get user from user ID
        getUser(id) {
            this.user =  this.users.find(user => user._id.$oid === id);
        },
        getDrinkOfChoice() {
            // convert the array into string with , as delimeter
            this.drinkOfChoice = this.user["Drink of Choice"].join(", ");
        },
        toggleView() {
            this.showCurrentContent = !this.showCurrentContent; // Toggle the value
        },
    },
};
</script>

<style>

.badge-img, .profile-img {
    width: 80px;
    height: 80px;
}

.bottle-img {
    width: 150px;
    height: 150px;
}

.image-container {
    position: relative;
    display: inline-block;
}

.image-container .icon {
    position: absolute;
    top: 0;
    right: 0;
    margin-top: 10px;
    margin-right: 25px;
    z-index: 1;
}

</style>
