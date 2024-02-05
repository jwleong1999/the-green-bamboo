<!-- HTML -->
<template>

    <!-- navbar -->
    <NavBar></NavBar>

    <!-- title -->
    <h2 class="p-5 text-center"> Login </h2>

    <!-- select buttons -->
    <div class="container pt-5 ">
        <form id="login" v-on:submit.prevent="checkLogin">
            <div class="row">
                <!-- user -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/User.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input class="form-check-input" type="radio" v-model="role" :value="'user'" name="roleSelect" id="roleUser">
                    <br>
                    <label class="form-check-label" for="roleUser">User</label>
                </div>
                <!-- producer -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/Producer.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input class="form-check-input" type="radio" v-model="role" :value="'producer'" name="roleSelect" id="roleProducer">
                    <br>
                    <label class="form-check-label" for="roleProducer">Producer</label>
                </div>
                <!-- venue -->
                <div class="col-md-4 text-center">
                    <img src="../../Images/Profile/Venue.png" style="width: 100px; height: 100px">
                    <br><br>
                    <input class="form-check-input" type="radio" v-model="role" :value="'venue'" name="roleSelect" id="roleVenue">
                    <br>
                    <label class="form-check-label" for="roleVenue">Venue</label>
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
                    <button type="submit" class="btn primary-square">Submit</button>
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
                producers: [],
                users: [],
                venues: [],
                accountID: {},

                // form values
                ID: '',
                role: '',
                password: '',
                errors: []

            };
        },
        mounted() {
            this.loginCheck();
        },
        methods: {
            loginCheck() {
                // Check if user is already logged in
                if (localStorage.getItem("88B_accID") != null) {
                    this.accountID = localStorage.getItem("88B_accID");
                    this.role = localStorage.getItem("88B_accType");
                    this.redirectPage();
                } else {
                    this.loadData();
                }
            },
            // load data from database
            async loadData() {
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
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
            },

            // toggle password visibility
            showPassword() {
                var password = document.getElementById("password");
                if (password.type === "password") {
                        password.type = "text";
                    } 
                else {
                    password.type = "password";
                }
            },

            // Form Submission Function
            checkLogin() {
                // // clear previous values
                this.errors = []

                // [if] check if all details keyed in
                if (this.role == "" || this.ID == "" || this.password == "") {
                    // check if role selected
                    if (this.role == "") {
                        this.errors.push("No role selected")
                    }
                    // check if ID keyed in
                    if (this.ID == "") {
                        this.errors.push("No username entered")
                    }
                    // check if password keyed in
                    if (this.password == "") {
                        this.errors.push("No password entered")
                    }
                }

                // [else] all details keyed in
                else {

                    // Check login validity
                    let accountExists = false
                    let passwordMatch = false
                    let hashedPassword = this.hashPassword(this.ID, this.password)

                    // [user]
                    if (this.role == "user") {
                        for (let i = 0; i < this.users.length; i++) {
                            if (this.users[i].username == this.ID) {
                                accountExists = true
                                if (this.users[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    this.accountID = this.users[i]._id["$oid"]
                                }
                                break
                            }
                        }
                    }
                    // [producer]
                    if (this.role == "producer") {
                        for (let i = 0; i < this.producers.length; i++) {
                            if (this.producers[i].producerName == this.ID) {
                                accountExists = true
                                if (this.producers[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    this.accountID = this.producers[i]._id["$oid"]
                                }
                                break
                            }
                        }
                    }
                    // [venue]
                    else if (this.role == "venue") {
                        for (let i = 0; i < this.venues.length; i++) {
                            if (this.venues[i].venueName == this.ID) {
                                accountExists = true
                                if (this.venues[i].hashedPassword == hashedPassword) {
                                    passwordMatch = true
                                    this.accountID = this.venues[i]._id["$oid"]
                                }
                                break
                            }
                        }
                    }

                    if (!accountExists || !passwordMatch) {
                        this.errors.push("Invalid username or password")
                    }
                }

                // no errors
                if (this.errors.length == 0) {
                    localStorage.setItem("88B_accID", this.accountID);
                    localStorage.setItem("88B_accType", this.role);
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

            redirectPage() {
                // Redirect for selected roles 
                
                // [TODO] change to correct page and use router pushing

                // [User]
                if (this.role == "user") {
                    window.location.href = "../Users/Bottle-Listings";
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