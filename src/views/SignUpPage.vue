<!-- HTML -->
<template>
    <!-- navbar -->
    <NavBar></NavBar>

    <!-- TODO First Name and Last Name on the same line -->

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
                        <span v-if="missingUsername" class="text-danger">Please enter a username.</span>
                        <span v-if="duplicateUser" class="text-danger">Username is already taken, if this is you, login instead!</span>
                    </div>
                    <!-- Input: Email -->
                    <div class="form-group mb-3">
                        <input type="text" class="form-control" style="border-color: black" v-model="email" id="email" placeholder="Email">
                        <span v-if="missingEmail" class="text-danger">Please enter an email.</span>
                        <span v-if="invalidEmail" class="text-danger">Please enter a valid email.</span>
                    </div>
                    <!-- Input: Password -->
                    <div class="form-group mb-3">
                        <input type="password" class="form-control" style="border-color: black" v-model="password" id="password" placeholder="Password">
                        <span v-if="missingPassword" class="text-danger">Please enter a password.</span>

                    </div>
                    <!-- Input: Repeat Password -->
                    <div class="form-group mb-3">
                        <input type="password" class="form-control" style="border-color: black" v-model="passwordRepeat" id="passwordRepeat" placeholder="Repeat Password">
                        <span v-if="missingPasswordRepeat && !missingPassword" class="text-danger">Please repeat your password.</span>
                        <span v-if="passwordMismatch && !missingPasswordRepeat" class="text-danger">Passwords do not match, please try again.</span>
                    </div>
                    <div class="row">
                        <!-- Input: First Name -->
                        <div class="form-group mb-3 col-6">
                            <input type="text" class="form-control" style="border-color: black" v-model="firstName" id="firstName" placeholder="First Name">
                            <span v-if="missingFirstName" class="text-danger">Please enter your First Name.</span>
                        </div>
                        <!-- Input: Last Name -->
                        <div class="form-group mb-3 col-6">
                            <input type="text" class="form-control" style="border-color: black" v-model="lastName" id="lastName" placeholder="Last Name">
                            <span v-if="missingLastName" class="text-danger">Please enter your Last Name.</span>
                        </div>
                    </div>
                    <!-- Input: Birthday -->
                    
                    <div class="input-group mb-0">
                        <span class="input-group-text" id="basic-addon1">Birthday</span>
                        <input type="date" class="form-control" style="border-color: black" v-model="birthday" id="birthday" placeholder="Birthday">
                    </div>
                    <div class="text-center mb-3">
                        <span v-if="missingBirthday" class="text-danger mt-0 mb-3">Please enter your birthday.</span>
                    </div>

                    <div class="text-center mt-3">
                        <div class="form-check form-check-inline">
                            <label class="form-check-label">I verify I am above legal drinking age in my country of location</label>
                            <input class="form-check-input" type="checkbox" v-model="ageCheck">
                        </div>
                    </div>
                    <div class="text-center mb-3">
                        <span v-if="missingAgeCheck" class="text-danger">Please verify this.</span>
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

                // Initial user variable
                response:[],

                // Form variables
                username:"",
                email:'',
                password:'',
                passwordRepeat:'',
                firstName:'',
                lastName:'',
                birthday:'',
                ageCheck:'',
                
                // Submission variables

                missingUsername:false,
                missingEmail:false,
                invalidEmail:false,
                passwordMismatch:false,
                missingPassword:false,
                missingPasswordRepeat:false,
                missingFirstName:false,
                missingLastName:false,
                missingBirthday:false,
                missingAgeCheck:false,
                duplicateUser:false,

                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                fillForm: true,
                responseCode: "",
            }
        },
        // mounted() {
        // },
        methods:{
            goBack() {
                this.$router.go(-1)
            },
            signUp(){

                // Reset all errors/success message, just in case
                this.resetError()
                
                // Form validation
                let errorCount = 0

                // username validation
                if(this.username==''){
                    this.missingUsername = true
                    errorCount++
                }else{
                    this.checkUsername(this.username)
                    if(this.duplicateUser){
                        errorCount++
                    }
                }

                // Email validation
                if(this.email==''){
                    this.missingEmail = true
                    errorCount++
                }else if(!this.email.match('.+@.+..+')){
                    this.invalidEmail = true
                    errorCount++
                }
                // Password validation
                if(this.password !== this.passwordRepeat){
                    this.passwordMismatch = true
                    errorCount++
                }
                if(this.password == ''){
                    this.missingPassword = true
                    errorCount++
                }
                if(this.passwordRepeat == ''){
                    this.missingPasswordRepeat = true
                    errorCount++
                }

                // First name validation
                if(this.firstName == ''){
                    this.missingFirstName = true
                    errorCount++
                }

                // Last name validation
                if(this.lastName == ''){
                    this.missingLastName = true
                    errorCount++
                }

                // Birthday validation
                if(this.birthday == ''){
                    this.missingBirthday = true
                    errorCount++
                }else{
                    var dob = new Date(this.birthday);
                    dob.setDate(dob.getDate() - 1);
                    var month_diff = Date.now() - dob.getTime();
                    var age_dt = new Date(month_diff);  
                    var year = age_dt.getUTCFullYear();  
                    var age = Math.abs(year - 1970);  
                    if(age<18){
                        this.underAge = true
                    }
                }

                // Age Check validation
                if(!this.ageCheck){
                    this.missingAgeCheck = true
                    errorCount++
                }
                
                if(errorCount > 0){
                    return null
                }


                let hashedPassword = this.hashPassword(this.username, this.password)
                let joinDate = new Date().toISOString() + '+00:00';
                let submitAPI =  "http://127.0.0.1:5400/createAccount"
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
                    // "birthday":this.birthday,
                }
                this.createAccount(submitAPI, submitData);
            },
            async createAccount(submitAPI, submitData){
                this.submitForm = true
                this.fillForm = false
                try{
                    const response = await this.$axios.post(submitAPI, submitData)
                    .then((response)=>{
                        this.reviewResponseCode = response.data.code
                    })
                    .catch((error)=>{
                        console.log(error);
                        this.reviewResponseCode = error.response.data.code
                        this.submitForm = false
                    });
                    if(this.reviewResponseCode==201){
                        this.successSubmission=true; // Display success message
                        this.submitForm = false  // Hide submission in progress message
                    }else{
                        this.errorSubmission=true; // Display error message
                        this.submitForm = false  // Hide submission in progress message
    
                        if(this.reviewResponseCode==400){
                            this.duplicateEntry = true // Display duplicate entry message
                        }else{
                            this.errorMessage = true // Display generic error message
                        }
                    }
                    return response
                }
                catch(error){
                    console.log(error)
                    this.errorSubmission = true
                    this.errorMessage = true
                    this.submitForm = false
                }
                
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
                this.fillForm = true
                this.errorMessage=false
                this.errorSubmission=false
                this.duplicateEntry=false
                this.successSubmission=false
            },
            resetError(){
                this.missingUsername=false
                this.missingEmail=false
                this.invalidEmail=false
                this.passwordMismatch=false
                this.missingPassword=false
                this.missingPasswordRepeat=false
                this.missingFirstName=false
                this.missingLastName=false
                this.missingBirthday=false
            },

            async checkUsername(username){
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                    let duplicateUser = response.data.filter((user)=>{
                        return user.username == username
                    })

                    if(duplicateUser.length==0){
                        this.duplicateUser = false
                    }else{
                        this.duplicateUser = true
                    }
                } 
                catch (error) {
                    console.error(error);
                }
            },
            
        }
    }

</script>