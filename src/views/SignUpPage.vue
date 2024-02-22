<template>
    <!-- navbar -->
    <NavBar></NavBar>

    <!-- Display when form is being submitted -->
    <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="submitForm"> 
            <span>The form is being submitted, please hold on!</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div class="text-success fst-italic fw-bold fs-3"  v-if="successSubmission"> 
            <span>The account has successfully been created!</span> <!-- for user -->
            <br>
            <button class="btn primary-btn btn-sm">
                <router-link :to="{ path: '/login' }" class="primary-clickable-text">
                    <span class="fs-5 fst-italic" style="color: white;"> Click to login here! </span>
                </router-link>
            </button>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to create account, please try again!</span>
            <span v-if="duplicateEntry">The account has already been created.</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Retry sign up again! </span>
            </button>
        </div>


         <!-- div for the whole form plus header plus col-->
         <div class="row" v-if="fillForm">
            
            <!-- spacer -->
            <div class="col-xl-3 col-lg-2 col-md-1"></div>
            
            <!-- start of the elements -->
            <div class="col-xl-6 col-lg-8 col-md-10 rounded" style="background-color:#DDC8A9;">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1" style="font-style: italic; font-family: Radley, serif;">Create an Account</p>
                </div>

                <!-- Start of form -->
                <form v-on:submit.prevent="submitListing" id="frm">
                
                    <!-- Input: Username -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="username" id="username" placeholder="Username">
                    </div>
                    <!-- Input: Email -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="email" id="email" placeholder="Email">
                    </div>
                    <!-- Input: Password -->
                    <div class="form-group mb-3">
                        <input type="password" class="form-control" style="border-color: black" v-model="password" id="password" placeholder="Password">
                    </div>
                    <!-- Input: Repeat Password -->
                    <div class="form-group mb-3">
                        <input type="password" class="form-control" style="border-color: black" v-model="passwordRepeat" id="passwordRepeat" placeholder="Repeat Password">
                    </div>
                    <!-- Input: First Name -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="firstName" id="firstName" placeholder="First Name">
                    </div>
                    <!-- Input: Last Name -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="lastName" id="lastName" placeholder="Last Name">
                    </div>
                    <!-- Input: Birthday -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="birthday" id="birthday" placeholder="Birthday">
                    </div>

                    
                    <button type="submit" class="btn secondary-btn mx-1 mb-3" @click="signUp">Sign Up</button>
                    <button type="button" class="btn primary-btn mx-1 mb-3" @click="goBack">Return</button>
                
                </form>
                <!-- End of Form -->
            </div>
            <!-- End of the elements  -->
        </div>

    
</template>

<!-- ------------------------------------------------------------------------------ -->

<!-- JavaScript -->
<script>
    // import components used
    import NavBar from '@/components/NavBar.vue';

    export default{
        name: 'SignUpPage',
        components: {
            NavBar
        },
        data(){
            return{
                // Form variables
                username:"",
                email:'',
                password:'',
                passwordRepeat:'',
                firstName:'',
                lastName:'',
                birthday:'',
                
                // Submission variables
                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                fillForm: true,
                responseCode: "",
            }
        },
        // mounted:(){

        // },
        methods:{
            goBack() {
                this.$router.go(-1)
            },
            signUp(){
                let hashedPassword = this.hashPassword(this.username, this.password)
                let joinDate = new Date().toISOString() + '+00:00';
                let submitAPI =  "http://127.0.0.1:5202/createAccount"
                let submitData = {
                    "username": this.username,
                    "displayName": this.username,
                    "choiceDrinks": [],
                    "drinkLists": {
                        "Drinks I Have tried":{
                            "listDesc":"",
                            "listItems":[]
                        },
                        "Drinks I Want To Try":{
                            "listDesc":"",
                            "listItems":[]
                        }
                    },
                    "modType": [],
                    "photo": "",
                    "hashedPassword": hashedPassword.toString(),
                    "joinDate": joinDate,
                    "followLists": {
                        "users":[],
                        "producers":[],
                        "venues":[]
                    },
                }
                this.createAccount(submitAPI, submitData);
            },
            async createAccount(submitAPI, submitData){
                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    this.reviewResponseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.reviewResponseCode = error.response.data.code
                });
                if(this.reviewResponseCode==201){
                    this.successSubmission=true; // Display success message
                    this.addingReview=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.addingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },
            // create unique hash based on username and password
            hashPassword(username, password) {
                const combinedString = username.toString() + password;
                let hash = 0;

                for (let i = 0; i < combinedString.length; i++) {
                    const char = combinedString.charCodeAt(i);
                    hash = (hash << 5) - hash + char;
                    hash |= 0; // convert to 32-bit integer
                }

                return hash;
            },
            reset(){
                this.$router.go(0)
            }
        }
    }

</script>