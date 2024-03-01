<template>
    <NavBar />

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
        <span>The sign up details has successfully been submitted to our admins for approval!</span> <!-- for user -->
        <br>
        <button class="btn primary-btn btn-sm">
            <router-link :to="{ path: '/login' }" class="primary-clickable-text">
                <span class="fs-5 fst-italic" style="color: white;"> Click to login here! </span>
            </router-link>
        </button>
    </div>
    
    <!-- Display when bottle listing submission encounters an error -->
    <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
        <span v-if="errorMessage">An error occurred while attempting to send sign up details, please try again!</span>
        <span v-if="duplicateEntry">The sign up details have already been sent.</span>
        <br>
        <button class="btn primary-btn btn-sm" @click="reset">
            <span class="fs-5 fst-italic"> Retry sign up again! </span>
        </button>
    </div>

    <div class="row my-5" v-if="fillForm">
        <!-- spacer -->
        <div class="col-xl-2 col-lg-1 col-md-1"></div>
                
        <!-- start of the elements -->
        <div class="col-xl-5 col-lg-5 col-md-7 rounded" style="background-color:#DDC8A9;">
            <div class="d-grid gap-2 mb-3">
                <p class="fw-bold fs-2" style="font-style: italic; font-family: Radley, serif;">Are you a distiller, brewery or bar owner?</p>
            </div>

            <h3 class="text-start mb-5">Apply for a Business Account</h3>


            <!-- Start of form -->
            <form v-on:submit.prevent="submitListing" id="frm">

             
            <!-- Profile Type -->
            <!-- Radio for would recommend and would buy again -->
                <div class = 'row justify-content-start mb-3 text-start'>
                    <p class="text-start mb-1">Choose Your Profile Type *</p>
                    <div class = "col-md-12 justify-content-between">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="inlineCheckbox1" v-model="businessType" value="producer" name="business">
                            <label class="form-check-label text-start fw-bold" for="inlineCheckbox1">Brand</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" id="inlineCheckbox2" v-model="businessType" value="venue" name="business">
                            <label class="form-check-label text-start fw-bold" for="inlineCheckbox2">Venue</label>
                        </div>                                                                                                   
                    </div>   
                    <span v-if="missingBusinessType" class="text-danger">Please choose your business type.</span>                                      
                </div>

            <!-- Input: Username -->
                <div class="form-group mb-3">
                    <p class="text-start mb-1">Business Name *</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="businessName" id="businessName" placeholder="Business Name">
                    <span v-if="missingBusinessName" class="text-danger">Please enter a business name.</span>
                </div>

            <!-- Input: Business description -->
                <div class="form-group mb-3">
                    <p class="text-start mb-1">Business Description *</p>
                    <textarea rows=3 class="form-control" style="border-color: black" v-model="businessDesc" id="businessDesc" placeholder="Enter Business Description"></textarea>
                    <span v-if="missingBusinessDesc" class="text-danger">Please enter a business description.</span>
                </div>

             <!-- Input: Country of Origin -->
             <div class="form-group mb-3">
                <div class=" mb-3">
                    <p class="text-start mb-1">Country of Origin/Location *</p>
                    <div class="input-group">
                        <select class="form-select" id="countrySelect" v-model="selectedCountry" style="border-color: black;">
                            <option v-for="country in countries" :key="country" :value="country">
                            {{ country }}
                            </option>
                        </select>
                    </div>
                    <span v-if="missingSelectedCountry" class="text-danger">Please choose the country you are based in.</span>
                </div>
            </div>



             
            <!-- Input: Is business account on the site already, provide link -->
                <div class="form-group mb-3">
                    <p class="text-start mb-1">Is your brand/venue profile already on the site? If yes, Enter Link:</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="businessLink" id="businessLink" placeholder="Profile Link">
                </div>


            <!-- First name and last name -->
            <div class="row">
                <!-- Input: First Name -->
                <div class="form-group mb-3 col-6">
                    <p class="text-start mb-1">First Name *</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="firstName" id="firstName" placeholder="First Name">
                    <span v-if="missingFirstName" class="text-danger">Please enter your First Name.</span>
                </div>
                <!-- Input: Last Name -->
                <div class="form-group mb-3 col-6">
                    <p class="text-start mb-1">Last Name *</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="lastName" id="lastName" placeholder="Last Name">
                    <span v-if="missingLastName" class="text-danger">Please enter your Last Name.</span>
                </div>
            </div>

            <!-- Input: Email -->
                <div class="form-group mb-3">
                    <p class="text-start mb-1">Email *</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="email" id="email" placeholder="Email">
                    <span v-if="missingEmail" class="text-danger">Please enter an email.</span>
                    <span v-if="invalidEmail" class="text-danger">Please enter a valid email.</span>
                </div>


            <!-- Input: Is business account on the site already, provide link -->
                <div class="form-group mb-3">
                    <p class="text-start mb-1">Representative's Relationship to Brand/Venue *</p>
                    <input type="text" class="form-control" style="border-color: black" v-model="relationship" id="relationship" placeholder="Relationship">
                    <span v-if="missingRelationship" class="text-danger">Please enter your relationship with the business.</span>
                </div>


                <button type="submit" class="btn secondary-btn mx-1 mb-3" @click="signUp">Sign Up</button>
                <button type="button" class="btn primary-btn mx-1 mb-3" @click="goBack">Return</button>
            </form>
        </div>

        <!-- right side of elements -->
        <div class="col-xl-3 col-lg-5 col-md-7 rounded" style="background-color:#DDC8A9;">
            <div class="d-grid gap-2 mt-3">
                <p class="fs-3">Subscribe to a Business Account to connect directly with your fans and grow your business.</p>
            </div>
            <div class="row justify-content-center">
                <!-- <div class="col-xl-2 col-lg-1 col-md-1"></div> -->
                <button class="btn rounded p-3 text-start mx-3 mb-3 col-8" @click="toggleMonthlyPricing" :style="{ backgroundColor: selectedMonthlyPricing ? 'grey' :'white', borderColor: '#DD9E54', borderWidth:'3px' }">
                    <p class="fw-bold mb-1">Monthly plan</p>
                    $50.00/Month <br/>
                    <i class="text-secondary" style="font-size: 12px;">Billed monthly</i>
                </button>
            </div>
            <div class="row justify-content-center">
                <!-- <div class="col-xl-2 col-lg-1 col-md-1"></div> -->
                <button class="btn rounded p-3 text-start mx-3 mb-3 col-8" @click="toggleYearlyPricing" :style="{ backgroundColor: selectedYearlyPricing ? 'grey' :'white', borderColor: '#DD9E54', borderWidth:'3px' }">
                    <div class="row">
                        <p class="fw-bold mb-1 col-7">Yearly plan</p>
                        <div class="rounded col-5 text-center" style="background-color: green; color: white;">Save 16%</div>
                    </div>
                    $42.00/Month <br/>
                    <i class="text-secondary" style="font-size: 12px;">$504 Billed annually</i>
                </button>
            </div>
            <span v-if="missingPlan" class="text-danger">Please select a plan.</span>
        </div>
    </div>

</template>

<!-- ------------------------------------------------------------------------------ -->

<script>
    // import components used
    import NavBar from '@/components/NavBar.vue';

    export default{
        name: 'BusinessSignUpPage',
        components: {
            NavBar
        },
        data(){
            return{
                fillForm:true,
                submitForm:false,
                successSubmission:false,
                errorSubmission:false,
                errorMessage:false,
                duplicateEntry:false,

                // Form validation
                missingBusinessDesc:false,
                missingBusinessName:false,
                missingBusinessType:false,
                missingEmail:false,
                invalidEmail:false,
                missingFirstName:false,
                missingLastName:false,
                missingRelationship:false,
                missingSelectedCountry:false,
                missingPlan:false,

                // form variables
                businessType:'',
                businessName:'',
                businessDesc:'',
                businessLink:'',
                firstName:'',
                lastName:'',
                email:'',
                relationship:'',
                selectedCountry:'',
                countries: [],
                selectedMonthlyPricing:false,
                selectedYearlyPricing:false,
                selectedPricing:'',

            }
        },
        created() {
            let accountDetails = this.$route.query
            console.log(accountDetails);
            this.businessType = accountDetails.businessType
            this.businessName = accountDetails.businessName
            // this.businessDesc = accountDetails.businessDesc
            this.selectedCountry = accountDetails.originCountry
            console.log(this.selectedCountry);
        },
        mounted(){
            this.loadData()
        },
        methods:{
            toggleYearlyPricing(){
                if(this.selectedMonthlyPricing && !this.selectedYearlyPricing){
                    this.selectedMonthlyPricing= false
                }
                if(this.selectedYearlyPricing){
                    this.selectedYearlyPricing=false
                }else{
                    this.selectedYearlyPricing = true
                }
            },
            toggleMonthlyPricing(){
                if(this.selectedYearlyPricing && ! this.selectedMonthlyPricing){
                    this.selectedYearlyPricing= false
                }
                if(this.selectedMonthlyPricing){
                    this.selectedMonthlyPricing=false
                }else{
                    this.selectedMonthlyPricing = true
                }
            },
            async loadData(){
                const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                for (let country of response.data) {
                    this.countries.push(country.originCountry);
                }
                this.countries = this.countries.sort();
                
            },
            goBack(){
                this.$router.go(-1)
            },

            signUp(){
                this.resetError()
                this.selectedPricing=''

                let errorCount =0
                // Form validation

                // Business desc check
                if(this.businessDesc == ''){
                    this.missingBusinessDesc = true
                    errorCount++
                }
                // Business name check
                if(this.businessName == ''){
                    this.missingBusinessName = true
                    errorCount++
                }
                // Business type check
                if(this.businessType == ''){
                    this.missingBusinessType = true
                    errorCount++
                }
                // Select country check
                if(this.selectedCountry==''){
                    this.missingSelectedCountry = true
                    errorCount++
                }
                // Brand relationship check
                if(this.relationship==''){
                    this.missingRelationship = true
                    errorCount++
                }
                // Pricing select check
                if(!(this.selectedMonthlyPricing || this.selectedYearlyPricing)){
                    this.missingPlan=true
                    errorCount++
                }else if(this.selectedMonthlyPricing){
                    this.selectedPricing = 'monthly'
                }else{
                    this.selectedPricing = 'yearly'
                }

                // Email validation
                if(this.email==''){
                    this.missingEmail = true
                    errorCount++
                }else if(!this.email.match('.+@.+..+')){
                    this.invalidEmail = true
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

                if(errorCount>0){
                    return null
                }
`               `
                let joinDate = new Date().toISOString();
                let submitAPI =  "http://127.0.0.1:5031/createAccountRequest"
                let submitData = {
                    "businessName": this.businessName,
                    "businessType": this.businessType,
                    "businessDesc": this.businessDesc,
                    "country": this.selectedCountry,
                    "pricing": this.selectedPricing,
                    "profileLink": this.profileLink,
                    "firstName": this.firstName,
                    "lastName": this.lastName,
                    "email": this.email,
                    "relationship": this.relationship,
                    "photo": "",
                    "joinDate": joinDate,
                }
                this.createAccount(submitAPI,submitData)
            },

            async createAccount(submitAPI,submitData){
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

            reset(){
                this.fillForm = true
                this.errorMessage=false
                this.errorSubmission=false
                this.duplicateEntry=false
                this.successSubmission=false
                this.submitForm = false
            },
            resetError(){
                this.missingBusinessDesc=false
                this.missingBusinessName=false
                this.missingBusinessType=false
                this.missingEmail=false
                this.invalidEmail=false
                this.missingFirstName=false
                this.missingLastName=false
                this.missingRelationship=false
                this.missingSelectedCountry=false
            },
        },
    }

</script>