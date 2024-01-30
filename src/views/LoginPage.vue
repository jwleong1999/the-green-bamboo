<!-- HTML -->
<template>

    <!-- navbar -->
    <NavBar></NavBar>

    <!-- title -->
    <h2 class="p-5" style="text-align: center"> Login </h2>

    <!-- select buttons -->
    <div class="container pt-5 ">
        <form id="login">
            <div class="row">
                <!-- user -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/User.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input type="radio" id="user" name="role" value="user">
                    <br>
                    <label for="user"> User </label>
                </div>
                <!-- producer -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/Producer.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input type="radio" id="producer" name="role" value="producer">
                    <br>
                    <label for="producer"> Producer </label>
                </div>
                <!-- venue -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/Venue.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input type="radio" id="venue" name="role" value="venue">
                    <br>
                    <label for="venue"> Venue </label>
                </div>
            </div>
            <!-- username -->
            <div class="row pt-5">
                <div class="d-grid gap-2 col-5 mx-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="id" placeholder="Username" v-model="ID">
                        <label for="username"> Username </label>
                    </div>
                </div>
            </div>
            <!-- password -->
            <div class="row pt-2">
                <div class="d-grid gap-2 col-5 mx-auto">
                    <div class="form-floating">
                        <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                        <label for="password"> Password </label>
                    </div>
                </div>
            </div>
            <!-- checkbox -->
            <div class="row pt-1 pb-3">
                <div class="d-grid gap-2 col-5 mx-auto">
                    <!-- Use Bootstrap grid classes for layout -->
                    <div class="row g-2">
                        <!-- Column for the checkbox -->
                        <div class="col-12 text-start">
                            <input type="checkbox" v-on:click="showPassword()" class="form-check-input">
                            <label for="password" class="form-check-label"> &nbsp; Show password </label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- error handling -->
            <div class="row p-3 text-left" v-show="errors.length > 0">
                <div class="d-grid gap-2 col-5 mx-auto">
                    <div class="alert alert-danger" role="alert">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                        <path d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z"/>
                        <path d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z"/>
                        </svg>
                        <h5> Error </h5>
                        <li v-for="error in errors" :key="error"> {{ error }} </li>
                    </div>
                </div>
            </div>
            <!-- Confirm Selection -->
            <div class="row pt-3">
                <div class="d-grid gap-2 col-1 mx-auto">
                    <button class="btn primary-square" type="button" v-on:click="fetchFormValues"> Submit </button>
                </div>
            </div>
        </form>
    </div>

</template>

<script>
    // import components used
    import NavBar from '@/components/NavBar.vue';

    // specify components used
    export default {
        name: 'LoginPage',
        components: {
            NavBar
        },

        data() {
            return {
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                venuesAPI: [],
                drinkTypes: [],
                requestListings: [],
                requestEdits: [],
                modRequests: [],

                // form values
                ID: '',
                role: '',
                password: '',
                errors: []

            };
        },
        mounted() {
            this.loadData();
        },
        methods: {
            // load data from database
            async loadData() {
                // countries
                // _id, originCountry
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                        this.countries = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
                        // originally, make filteredListings the entire collection of listings
                        this.filteredListings = this.listings;
                    } 
                    catch (error) {
                        console.error(error);
                }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
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
                // venues
                // _id, venueName, venueDesc, origin
                // Country, address, openingHours
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                        this.venues = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenuesAPI');
                        this.venuesAPI = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // drinkTypes
                // _id, drinkType, typeCategory
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                        this.drinkTypes = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // requestListings
                // _id, listingName, producerNew, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, sourceLink, brandRelation, reviewStatus, userID, photo
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                            this.requestListings = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                            this.requestEdits = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // modRequests
                // _id, userID, drinkType, modDesc
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                            this.modRequests = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
            },

            showPassword() {
                var password = document.getElementById("password");
                if (password.type === "password") {
                        password.type = "text";
                    } 
                else {
                    password.type = "password";
                }
            },

            // fetches the user's input (role, id and password)
            fetchFormValues() {
                // clear previous values
                this.clearFormValues()
                this.clearErrors()

                // [role]
                const roleRadios = document.getElementsByName("role");
                // loop through the radio buttons to find the selected one
                let selectedValue = "";
                for (let i = 0; i < roleRadios.length; i++) {
                    if (roleRadios[i].checked) {
                        selectedValue = roleRadios[i].value;
                        break; // Exit the loop when a selected radio button is found
                    }
                }
                this.role = selectedValue

                // [username]
                this.ID = document.getElementById("id").value;

                // [password]
                this.password = document.getElementById("password").value;

                // check if role selected, and ID & password keyed in
                this.checkRole()
            },

            checkRole() {
                // // clear previous values
                this.clearErrors()

                // [if] check if all details keyed in
                if (this.role == "" || this.ID == "" || this.password == "") {
                    // check if role selected
                    if (this.role == "") {
                        this.errors.push("No role selected")
                    }
                    // check if ID keyed in
                    if (this.ID == "") {
                        this.errors.push("No username keyed in")
                    }
                    // check if password keyed in
                    if (this.password == "") {
                        this.errors.push("No password keyed in")
                    }
                }

                // [else] all details keyed in
                else {
                    // check if username matches role
                    // [user]
                    if (this.role == "user") {
                        // check if username exists
                        let userExists = false
                        for (let i = 0; i < this.users.length; i++) {
                            if (this.users[i].username == this.ID) {
                                userExists = true
                                break
                            }
                        }
                        if (!userExists) {
                            this.errors.push("User does not exist")
                        }
                    }
                    // [producer]
                    if (this.role == "producer") {
                        // check if username exists
                        let producerExists = false
                        for (let i = 0; i < this.producers.length; i++) {
                            if (this.producers[i].producerName == this.ID) {
                                producerExists = true
                                break
                            }
                        }
                        if (!producerExists) {
                            this.errors.push("Producer does not exist")
                        }
                    }
                    // [venue]
                    else if (this.role == "venue") {
                        // check if username exists
                        let venueExists = false
                        for (let i = 0; i < this.venues.length; i++) {
                            if (this.venues[i].venueName == this.ID) {
                                venueExists = true
                                break
                            }
                        }
                        if (!venueExists) {
                            this.errors.push("Venue does not exist")
                        }
                    }

                    // if role exists, check if password matches username
                    if (this.errors.length == 0) {
                        let passwordMatch = false
                        let hashedPassword = this.hashPassword(this.ID, this.password)

                        // [user]
                        if (this.role == "user") {
                            for (let i = 0; i < this.users.length; i++) {
                                if (this.users[i].username == this.ID && this.users[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    break
                                }
                            }
                            // password does not match username
                            if (!passwordMatch) {
                                this.errors.push("Password does not match username")
                            }
                        }
                        // [producer]
                        else if (this.role == "producer") {
                            for (let i = 0; i < this.producers.length; i++) {
                                if (this.producers[i].producerName == this.ID && this.producers[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    break
                                }
                            }
                            if (!passwordMatch) {
                                this.errors.push("Password does not match username")
                            }
                        }
                        // [venue]
                        else if (this.role == "venue") {
                            for (let i = 0; i < this.venues.length; i++) {
                                if (this.venues[i].venueName == this.ID && this.venues[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    break
                                }
                            }
                            if (!passwordMatch) {
                                this.errors.push("Password does not match username")
                            }
                        }
                    }
                }

                // no errors
                if (this.errors.length == 0) {
                    this.redirectPage()
                }

            },

            // create unique hash based on ID and password
            hashPassword(id, password) {
                const combinedString = id.toString() + password;
                let hash = 0;

                for (let i = 0; i < combinedString.length; i++) {
                    const char = combinedString.charCodeAt(i);
                    hash = (hash << 5) - hash + char;
                    hash |= 0; // convert to 32-bit integer
                }

                return hash;
            },

            submitFormOnEnter(event) {
                if (event.key === 'Enter') {
                event.preventDefault(); // prevent the default form submission
                this.fetchFormValues(); // manually trigger validation logic
                }
            },

            // Clear previous values
            clearFormValues() {
                this.role = ""
                this.ID = ""
                this.password = ""
            },
            clearErrors() {
                this.errors = []
            },

            redirectPage() {
                // Redirect for selected roles 
                
                // [TODO] change to correct page

                // [User]
                if (this.role == "user") {
                    window.location.href = "../Users/Bottle-Listings";
                    localStorage.setItem("data", this.ID);
                    }
                // [Producer]
                if (this.role == "producer") {
                window.location.href = "../Producer/Producer-Listings"; 
                }
                // [Venue]
                if (this.role == "venue") {
                window.location.href = "../Venues/Bottle-Listings";
                }
            }
        }
    };

</script>