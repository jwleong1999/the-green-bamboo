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
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="searchListings"> 
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

     
    <div >
        <div class="text-success fst-italic fw-bold fs-3" v-if="successfulUpdate"> 
            <span>The bottle listing has successfully been updated</span> <!-- for user -->
            <br>
            <router-link :to="{ path: '/Producer/Producer-Edit-Listing/' }" class="text-secondary">
                <button class="btn primary-btn btn-sm">
                    <span class="fs-5 fst-italic"> Go back to listings </span>
                </button>
            </router-link>
        </div>

        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to update, please try again!</span>
            <span v-if="duplicateEntry">A bottle lisiting of the same name already exists. Please try another name!</span>
            <br>
            <router-link :to="{ path: '/Producer/Producer-Edit-Listing/' + this.listingID }">
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Go back to form </span>
            </button>
            </router-link>
        </div>
        

        <!-- main form -->
        <div v-if="updateForm" class="container pt-3">
            <div class="row">
                
                
                <!-- Back Button -->
                <div class="col-9">
                    <div class="container">
                        <!-- buttons -->
                        <div class="row">
                            <!-- discover -->
                            <div class="col-4">
                                <div class="d-grid gap-2">
                                     
                                    <router-link :to="{ path: '/Producer/Producer-Edit-Listing/' }" class="text-secondary">
                                    <span class="pe-2">
                                        
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16" v-on:click="previousListing">
                                            <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                                        </svg>
                                        <h5 style="display: inline-block;"> Back to listings </h5> 
                                        
                                    </span>
                                    </router-link>
                                </div>
                            </div>
                          
                        </div>

                        <form v-on:submit.prevent="updateListing" id="frm" >

                            <div class="row">
                                
                                <div class="container text-start">
                                    <div class="p-3">

                                        <div class="row">
                                            <!-- image -->
                                            <div class="col-4 image-container">

                                                <img v-if="image!=''" :src="'data:image/png;base64,'+image64"  style="width: 300px; height: 300px;" class="img-border">
                                                <img v-else src="../../../Images/Drinks/Placeholder.png" style="width: 300px; height: 300px;" class="img-border">

                                                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark overlay-icon" viewBox="0 0 16 16">
                                                    <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                                </svg>
                                            </div>

                                            
                                            <!-- details -->
                                            <div class="col-8 ps-5">
                                                <!-- review -->
                                                <label for="input">Enter Listing Name:</label><span class="text-danger">*</span>
                                                <div class="row">
                                                    <div class="mb-3">
                                                        <input type="Expression Name" class="form-control" id="exampleFormControlInput1" v-model="tempExpressionName">
                                                        <span v-if="missingName" class="text-danger">Please enter a valid expression name.</span>
                                                    </div>
                                                    
                                                </div>
                                                
      

                                                <div v-if="independentStatus" class="row">
                                                    <label for="input">Enter Producer Name:</label><span class="text-danger">*</span>
                                                    <div class="mb-1">
                                                        <input type="Bottler Name" class="form-control" id="exampleFormControlInput1" v-model="tempBottler" >
                                                        <span v-if="missingBottler" class="text-danger">Please enter a producer name.</span>
                                                    </div>
                                                    
                                                    <label for="checkbox">Is the producer independent?</label>
                                                    <div class="mb-3">
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox" id="checkbox" v-model="independentStatus" @change="independentBottler">
                                                            <label class="form-check-label" for="checkbox">
                                                                Independent
                                                            </label>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div v-else class="row">
                                                    <label for="input">Enter Producer Name:<span class="text-danger">*</span></label>
                                                    <div class="mb-1">
                                                        <input type="Bottler Name" class="form-control" id="exampleFormControlInput1" v-model="tempBottler" disabled>
                                                    </div>
                                                    <label for="checkbox">Is the producer independent?</label>
                                                    <div class="mb-3">
                                                        <div class="form-check">
                                                            <input class="form-check-input" type="checkbox" id="checkbox" v-model="independentStatus" @change="independentBottler">
                                                            <label class="form-check-label" for="checkbox">
                                                                Independent
                                                            </label>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col mb-3">
                                                        <label for="input">Enter Profile Photo:</label>
                                                        <input class="form-control" id="file" type="file" @change="loadFile" ref="fileInput"/>
                                                    </div>

                                                </div>

                                                <!-- to input checkbox to indicate producer is independent or dependent -->
                                                <div class="row">
                                                    
                                                    <div class=" mb-3">
                                                        <label for="dropdown">Select Country of Origin:</label><span class="text-danger">*</span>
                                                        <div class="input-group">
                                                            
                                                            <select class="form-select" id="inputGroupSelect01" v-model="tempCountry">
                                                                <option selected>{{this.tempCountry }}</option>
                                                                <option v-for="country in countries" :key="country" :value="country">
                                                                {{ country}}
                                                                </option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>    
                                                <div class="row">
                                                    <div class="col-md-6 mb-3">
                                                        <label for="dropdown">Select Drink Type:</label><span class="text-danger">*</span>
                                                        <div class="input-group">
                                                            <select class="form-select" id="inputGroupSelect01" v-model="tempDrinkType" @change="getDrinkCategoryList">
                                                                <option v-for="taste in drinkCategoriesList" :key="taste" :value="taste">
                                                                {{ taste }}
                                                                </option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                
                                                    <div v-if="tempTypeCategoryList.length>1" class="col-md-6 mb-3"  >
                                                        <label for="dropdown">Select Drink Type Category:</label><span class="text-danger">*</span>
                                                        <div class="col-md-6 mb-3">
                                                            <div class="input-group">
                                                                <select class="form-select" id="inputGroupSelect01" v-model="tempTypeCategory">
                                                                    <option v-for="cat in tempTypeCategoryList.sort()" :key="cat" :value="cat" >
                                                                        {{ cat }}
                                                                    </option>
                                                                    
                                                                </select>
                                                                <span v-if="missingTypeCategory" class="text-danger">Please select a type category.</span>
                                                            </div>
                                                            
                                                        </div>
                                                    </div>
                                                </div>
                                                
                                                <div class="row">
                                                    <label for="input">Enter Bottle Age :</label>
                                                    <div class="col-md-6 mb-3">
                                                        <input type="Expression Name" class="form-control" id="age" v-model="tempAge">
                                                    </div>
                                                    
                                                    <label for="input">Enter Bottle ABV (%):<span class="text-danger">*</span></label>
                                                    <div class="col-md-6 mb-3">
                                                        <input type="Expression Name" class="form-control" id="abv" v-model="tempABV" >
                                                        <span v-if="missingABV" class="text-danger">Please enter an ABV.</span>
                                                    </div>
                                                    
                                                </div>
                                                
                                                <div class="mb-3">
                                                    <label for="input">Enter Bottle Description:</label><span class="text-danger">*</span>
                                                    <textarea class="form-control" id="exampleFormControlInput1" v-model="tempDescription" style="height: 200px;" ></textarea>
                                                    <span v-if="missingDescription" class="text-danger">Please enter a Description.</span>
                                                </div>

                                                <div class="row pt-5"> 
                                                    <div class="col-6">
                                                        <button class="btn secondary-btn btn-md" type="submit" > Save </button>
                                                    </div>
                                                </div>
                                                <!-- expression name -->
                                                
                                                <!-- producer -->
                                                
                                            </div>
                                        </div>
                                    </div>
                                    
                                    
                                </div>
                            </div> <!-- end of form content -->
                        </form> <!-- end of form -->
                    </div> <!-- end of container -->
                </div> <!-- end of back button -->
            </div> <!-- end of row -->
        </div> <!-- end of main form -->

    </div>
    

    

</template>



<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    export default {
        props: ['id'],
        data() {
            return {
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                editable: [],
                drinkCategories:null,
                drinkCategoriesList:[],
                listingID:null,
                updateStatus: false,
                tempExpressionName: '',
                tempProducerID: '',
                tempProducer: '',
                tempCountry: '',
                tempDrinkType: '',
                tempTypeCategory:"",
                tempTypeCategoryList: [],
                tempAge: '',
                tempABV: null,
                tempReviewLink: '',
                tempSourceLink: '',
                tempDescription: '',
                tempBottler: '',
                independentStatus:false,
                responseCode: "",
                image64: '',
                selectedImage:'',
                successfulUpdate:null,
                updateForm:true,
                errorSubmission:false,
                duplicateEntry:false,
                errorMessage:false,
                missingName:false,
                missingBottler:false,
                
                missingABV:false,
                missingDescription:false,
                errors:0


                
            };
        },
        mounted() {
            this.loadData();
            this.created();
            
        },
        
        methods: {

            // Get id for the listing
            async created() {
                // Get the id from the route params
                this.listingID = this.$route.params.id;
            },

            
            // load data from database
            
            async loadData() {
                // Countries
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                    for (let country of response.data) {
                        // console.log(country.originCountry)
                        this.countries.push(country.originCountry);
                    }
                    this.countries=this.countries.sort();

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
                    
                    this.editable = this.listings.find(listing => listing._id["$oid"] == this.listingID);
                    console.log(this.editable)
                    this.tempExpressionName = this.editable["listingName"];
                    this.tempProducerID = this.editable["producerID"];
                    this.tempBottler = this.editable["bottler"];
                    this.tempCountry = this.editable["originCountry"];
                    this.tempDrinkType = this.editable["drinkType"];
                    this.tempTypeCategory = this.editable["typeCategory"];
                    this.tempAge = this.editable["age"];
                    this.tempABV = this.editable["abv"];
                    this.tempReviewLink = this.editable["reviewLink"];
                    this.tempDescription = this.editable["officialDesc"];
                    this.tempSourceLink = this.editable["sourceLink"];
                    this.image64 = this.editable["photo"];
                    // this.tempTypeCategoryList=this.editable
                } 
                catch (error) {
                    console.error(error);
                }
                // Producers
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                    this.producers = response.data;

                    for (let producer of this.producers) {
                    if (JSON.stringify(producer._id) == JSON.stringify(this.tempProducerID)) {
                        this.tempProducer = producer.producerName;
                        
                    }
                    }
                    
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
                } 
                catch (error) {
                    console.error(error);
                }
                // Venues
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                    this.venues = response.data;
                } 
                catch (error) {
                    console.error(error);
                }
                // Drink Categories
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                    this.drinkCategories = response.data;
                    for (let drink of this.drinkCategories) {
                        this.drinkCategoriesList.push(drink.drinkType);
                    }
                    this.drinkCategoriesList=this.drinkCategoriesList.sort();
                    this.tempTypeCategoryList=this.drinkCategories.find(cat => cat.drinkType == this.tempDrinkType).typeCategory.sort();
                } 
                catch (error) {
                    console.error(error);
                }
            },
            getDrinkCategoryList() {
            
                this.tempTypeCategoryList=this.drinkCategories.find(cat => cat.drinkType == this.tempDrinkType).typeCategory;
                this.tempTypeCategory=""

            },

            
            temp() {
                console.log(this.editable)
                console.log(this.tempBottler)

            },
            
            independentBottler(event) {
                this.independentStatus = event.target.checked;
                // Declare producerNamePlaceholder outside of the loop
                let bottlerNamePlaceholder = "";

                if (this.independentStatus == true) {
                    // May need to work on this 
                    this.tempBottler = bottlerNamePlaceholder;
                    bottlerNamePlaceholder=this.tempBottler;
                } else {
                    // bottlerNamePlaceholder=this.tempBottler;
                    this.tempBottler = 'OB'
                    
                }

            },
            reset(){
                this.errorSubmission=false;
                this.successfulUpdate=false;
                this.updateForm=true;
                this.duplicateEntry=false;
                this.errorMessage=false;
            },

            async loadFile(event) {
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onloadend = async () => {
                this.selectedImage = reader.result;
                const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');

                this.image64 = base64String;
              
                // console.log("image64");
                // console.log(this.image64);

            };
            reader.readAsDataURL(file);
        
            },
            async updateListing(){
                this.errors=0;
                if(this.tempExpressionName.trim() == ''){
                    this.missingName = true;
                    this.errors++
                }
                if(this.tempBottler.trim() == ''){
                    this.missingBottler = true;
                    this.errors++
                }
                
                if(this.tempABV == '' | this.tempABV == null){
                    this.missingABV = true;
                    this.errors++
                }
                if(this.tempDescription.trim() == ''){
                    this.missingDescription = true;
                    this.errors++
                }

                if(this.errors==0){
                    let updateAPI = `http://127.0.0.1:5003/updateListing/${this.listingID}`;
                
                let updatedData = {
                    "listingName": this.tempExpressionName.trim(),
                    "producerID": this.tempProducerID,
                    "bottler": this.tempBottler.trim(),
                    "originCountry": this.tempCountry.trim(),
                    "drinkType": this.tempDrinkType.trim(),
                    "abv": this.tempABV,
                    "officialDesc": this.tempDescription.trim(),
                    "photo": this.image64.trim(),
                    "age":this.tempAge.trim(),
                    "typeCategory": this.tempTypeCategory.trim(),
                    "reviewLink": this.tempReviewLink.trim(),
                    "sourceLink": this.tempSourceLink.trim(),
                }

                const response = await this.$axios.put(updateAPI, updatedData)
                .then((response)=>{
                    this.responseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.responseCode = error.response.data.code
                });

                if(this.responseCode==200){
                    this.successfulUpdate=true; // Display success message
                    this.updateForm=false; // Hide submission in progress message
                }
                else{
                    this.errorSubmission=true; // Display error message
                    this.updateForm=false; // Hide submission in progress message
                    if(this.responseCode==410){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                console.log(this.responseCode)
                return response
                }
                
            },
            async writeListing(submitAPI, submitData) {

                this.fillForm = false; // Hide form
                this.submitForm = true; // Display submission in progress message

                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    this.responseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.responseCode = error.response.data.code
                });
                console.log(this.responseCode)
               
                return response
            },




            
            // for search button
            searchListings() {

                // flag to check if there are search inputs
                this.search = true;

                const searchInput = this.searchInput.toLowerCase();
                this.searchTerm = this.searchInput;

                // if there is something searched
                const searchResults = this.listings.filter((listing) => {
                    const expressionName = listing["Expression Name"].toLowerCase();
                    const producer = listing["Producer"].toLowerCase();
                    return expressionName.includes(searchInput) || producer.includes(searchInput);
                });

                console.log(searchResults)

                // if nothing found
                if (searchResults.length == 0) {
                    this.errorFound = true;
                    this.errorMessage = 'No results found, please try again.';
                } 
                else {
                    this.errorFound = false;
                    this.errorMessage = '';
                    this.filteredListings = searchResults;
                }

                // if there is nothing searched
                if (this.searchInput == '') {
                    this.resetListings();
                }
            },

            // for resetting listings (show full listings)
            resetListings() {
                this.filteredListings = this.listings;
                this.search = false;
                this.searchInput = '';
            },

            // get reviews for a listing
            getReviews(listing) {
                // list of all reviews of the particular drink
                const reviews = this.reviews.filter((review) => {
                    return review["reviewTarget"] == listing["listingName"];
                });
                // choose random review from the list
                const randomReview = reviews[Math.floor(Math.random() * reviews.length)];
                // check if a review is found before accessing "Review Desc"
                const reviewDesc = randomReview ? randomReview["reviewDesc"] : null;
                return reviewDesc;
            },

            // get ratings for a listing
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"] == listing["listingName"];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                // Format the averageRating to 1 decimal place
                const formattedRating = parseFloat(averageRating.toFixed(1));
                return formattedRating;
            }
        },
    };
</script>


