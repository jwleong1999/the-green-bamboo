<!-- Component for submitting new listings: Create (Producers, Moderators, Admins) / Request (Users) -->

<!--
    TODO:
    - "Return" button may bring user back to same page, but with form cleared. Prevent that by returning to last notable page. (optional)
    - Consider another backend check to ensure that submitter is authorized to submit listing in specified mode, with valid producerID for producers.
    - Should we save the form data for easier retry when invoking reset()? Should reset() just hard refresh the page?
-->

<template>
    <!-- Header -->
    <div class="container pt-3">

        <!-- Display when data is still loading -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="!dataLoaded"> 
            <span>Loading form, please wait...</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when form is being submitted -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="submitForm"> 
            <span>The form is being submitted, please hold on!</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div class="text-success fst-italic fw-bold fs-3" v-if="successSubmission"> 
            <span v-if="mode == 'user'">The bottle listing has successfully been submitted!</span> <!-- for user -->
            <span v-if="mode == 'power'">The bottle listing has successfully been created!</span> <!-- for producer -->
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Submit another bottle listing here! </span>
            </button>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to submit, please try again!</span>
            <span v-if="duplicateEntry">The bottle listing you are trying to submit already exists.</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Retry your submission here! </span>
            </button>
        </div>


        <!-- div for the whole form plus header plus col-->
        <div class="row" v-if="fillForm">
            
            <!-- spacer -->
            <div class="col-xl-3 col-lg-2 col-md-1"></div>
            
            <!-- start of the elements -->
            <div class="col-xl-6 col-lg-8 col-md-10">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1">Submit A New Bottle Listing</p>
                </div>

                <!-- Start of form -->
                <form v-on:submit.prevent="submitListing" id="frm">
                
                    <!-- Input: Bottle Name -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Name of Bottle <span class="text-danger">*</span></p>
                        <input type="text" v-model="form['listingName']" class="form-control" id="bottleName" placeholder="Enter Bottle Name" required>
                    </div>

                    <!-- Input: drinkType (eg. Whiskey) + typeCategory (eg. Single Malt) -->
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <p class="text-start mb-1">Drink Type <span class="text-danger">*</span></p>
                            <div class="input-group">
                                <select class="form-select" id="drinkTypeSelect" v-model="tempDrinkType" @change="getDrinkCategoryList">
                                    <option v-for="taste in drinkCategoriesList" :key="taste" :value="taste">
                                    {{ taste }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    
                        <div class="col-md-6 mb-3">
                            <p class="text-start mb-1">Drink Category</p>

                            <!-- For drink types that have serveral categories to choose from -->
                            <div class="input-group" v-if="tempTypeCategoryList.length > 1">
                                <select class="form-select" id="inputGroupSelect01" v-model="tempTypeCategory">
                                    <option v-for="cat in tempTypeCategoryList.sort()" :key="cat" :value="cat" >
                                        {{ cat }}
                                    </option>
                                </select>
                            </div>
                            
                            <!-- If there are no categories to select, display disabled dummy selection field -->
                            <div class="input-group" v-else>
                                <select class="form-select" disabled>
                                    <option selected>-</option>
                                </select>
                            </div>

                        </div>
                    </div>
                    
                    <!-- (ONLY FOR CREATION) Input: Drink Description -->
                    <div class="form-group mb-3" v-if="mode == 'power'">
                        <p class="text-start mb-1">Official Description <span class="text-danger">*</span></p>
                        <textarea rows=3 class="form-control" v-model="form['officialDesc']" id="officialDesc" placeholder="Enter description of bottle"></textarea>
                    </div>

                    <!-- Input: Link to website or source (optional for creation, mandatory for request) -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Link to website or source <span class="text-danger" v-if="mode == 'user'">*</span></p>
                        <input type="text" class="form-control" v-model="form['sourceLink']" id="sourceLink" placeholder="Enter source link">
                    </div>

                    <!-- Input: Link to 88 Bamboo review -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Link to 88 Bamboo review</p>
                        <input type="text" class="form-control" v-model="form['reviewLink']" id="reviewLink" placeholder="Enter review link">
                    </div>

                    <!-- Input: Photo file -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Photo of bottle</p>
                        <input class="form-control" type="file" id="formFile" @change="handleFileSelect">
                    </div>

                    <!-- Input: Producer Name -->
                    <!-- [IF] Producer is creating listing, lock Producer selection -->
                    <div class="form-group mb-3" v-if="isProducer != false">
                        <p class="text-start mb-1">Producer Name <span class="text-danger">*</span></p>
                        <select class="form-select" disabled>
                            <option selected>{{ isProducer }}</option>
                        </select>
                    </div>
                    <!-- [ELSE] Dropdown menu tied to producerID, show producerNew textbox only if "Other" selected (no producerID). -->
                    <!-- set name only, then before submitting request, put the id, save computation -->
                    <div class="form-group mb-3" v-else>
                        <p class="text-start mb-1">Producer Name <span class="text-danger">*</span></p>
                        <select class="form-select" id="producerSelect" v-model="tempProducer" @change="getProducerID">
                            <!-- <option selected>{{this.tempProducer }}</option> -->
                            <option v-for="producer in producerList" :key="producer.producerName" :value="producer.producerName">
                            {{ producer.producerName }}
                            </option>
                            <option v-if="mode == 'user'" value="Other">[ Other ]</option>
                        </select>
                    </div>

                    <!-- Input: New Producer Name (Request Only: if "Other" is selected in Producer Name) -->
                    <div class="form-group mb-3" v-if="this.tempProducer == 'Other'">
                        <p class="text-start mb-1">New Producer Name <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['producerNew']" id="producerNew" placeholder="Enter Producer Name">
                    </div>

                    <!-- Input: Independent Bottler Check -->
                    <p class="text-start mb-1">Is this bottle by an independent bottler? <span class="text-danger">*</span></p>
                    <!-- Toggleable Switch -->
                    <div class="text-start mb-3">
                        <div class="form-check form-switch form-check-inline">
                            <input class="form-check-input" type="checkbox" role="switch" id="IBCheck" name="IBCheck" v-model="indOperator">
                            <label class="form-check-label" for="IBCheck" v-if="indOperator">Yes</label>
                            <label class="form-check-label" for="IBCheck" v-if="!indOperator">No</label>
                        </div>
                    </div>
                    <!-- (ONLY IF above toggled to "Yes") Input Text for Independent Bottler -->
                    <div class="form-group mb-3" v-if="indOperator">
                        <p class="text-start mb-1">If yes, who is the independent bottler? <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['bottler']" :disabled="!indOperator" id="bottlerName" placeholder="Enter Bottler Name">
                    </div>

                    <!-- Input: Country of Origin -->
                    <div class="form-group mb-3">
                        <div class=" mb-3">
                            <p class="text-start mb-1">Country of Origin <span class="text-danger" v-if="mode == 'power'">*</span></p>
                            <div class="input-group">
                                
                                <select class="form-select" id="countrySelect" v-model="form['originCountry']">
                                    <option selected>{{this.form['originCountry'] }}</option>
                                    <option v-for="country in countries" :key="country" :value="country">
                                    {{ country}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- Input: Alcohol Strength (% ABV) + Alcohol Age / Vintage (years old / Year Bottled) -->
                    <div class="row mb-3">
                        <div class="form-group col-6">
                            <p class="text-start mb-1">Strength <span class="text-danger" v-if="mode == 'power'">*</span></p>
                            <div class="form-group row">
                                <div class="col-6 pe-1">
                                    <input type="number" v-model="form['abv']" class="form-control" id="abv" min="0" max="100" step="0.01">
                                </div>
                                <label for="abv" class="col-6 col-form-label ps-1 text-start">% ABV</label>
                            </div>
                        </div>
                        <div class="form-group col-6">
                            <p class="text-start mb-1" v-if="tempDrinkType == 'Liqueur'">Vintage (Year Bottled)</p>
                            <p class="text-start mb-1" v-else>Age</p>
                            <div class="form-group row">
                                <div class="col-6 pe-1">
                                    <input type="number" v-model="form['age']" class="form-control" id="age" min="0">
                                </div>
                                <label for="age" class="col-6 col-form-label ps-1 text-start" v-if="tempDrinkType != 'Liqueur'">years old</label>
                            </div>
                        </div>
                    </div>

                    <!-- (ONLY FOR USERS) Input: Relationship with Brand -->
                    <p class="text-start mb-1" v-if="mode == 'user'">Your Relationship with the Brand <span class="text-danger">*</span></p>
                    <div class="text-start mb-3" v-if="mode == 'user'">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Customer'" name="brandRelationCustomer" id="brandRelationCustomer">
                            <label class="form-check-label" for="brandRelationCustomer">Customer</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Employee'" name="brandRelationEmployee" id="brandRelationEmployee">
                            <label class="form-check-label" for="brandRelationEmployee">Employee</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Public Relations'" name="brandRelationPR" id="brandRelationPR">
                            <label class="form-check-label" for="brandRelationPR">Public Relations</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Distributor'" name="brandRelationDist" id="brandRelationDist">
                            <label class="form-check-label" for="brandRelationDist">Distributor</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Others'" name="brandRelationOther" id="brandRelationOther">
                            <label class="form-check-label" for="brandRelationOther">Others</label>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn secondary-btn mx-1 mb-3">Submit Bottle Listing</button>
                    <button type="button" class="btn primary-btn mx-1 mb-3" @click="goBack">Return</button>
                
                </form>
                <!-- End of Form -->

            </div>
            <!-- End of the elements  -->
        </div>
    </div>
    <!-- End of whole page -->
</template>

<script>
    export default {
        name: "SubmitListingNew",
        props: {
            mode: String
        },
        data () {
            return {
                form: {
                    "listingName": "",
                    "drinkType": "",
                    "typeCategory": "",
                    "officialDesc": "", // For creation only
                    "sourceLink": "",
                    "reviewLink": "",
                    "producerID": {
                        "$oid": ""
                    }, // Fill in producerID with producerID of specified producer. May be blank for request: new producer.
                    "bottler": "",
                    "originCountry": "",
                    "abv": "",
                    "age": "",
                    "photo": "",
                    // For request only
                    "producerNew": "", // If producerID is blank, this must not be blank.
                    "brandRelation": "Others",
                    "reviewStatus": false,
                    "userID": {
                        "$oid": "defaultUser"
                    }
                },
                // Pre-check form variables
                prevListing: false,
                dataLoaded: false,
                isProducer: false,

                // Dropdown variables
                countries: [],
                drinkCategoriesList: [],
                producerList: [],

                // Form variables
                tempDrinkType: "",
                tempTypeCategoryList: [],
                tempTypeCategory: "",
                tempProducer: "",
                indOperator: true,

                // Submission variables
                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                fillForm: false,
                responseCode: "",
            }
        },
        mounted() {

            // Get userID
            this.form['userID'] = {
                "$oid": localStorage.getItem('88B_accID')
            };

            // Check if route params "id" is present
            if (this.$route.params.id != "" && this.$route.params.id != undefined) {
                this.prevListing = true;
            }

            // Load data
            this.loadData();
        },
        methods:{
            async loadData(){
                // add countries variable
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

                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                    this.drinkCategories = response.data;
                    for (let drink of this.drinkCategories) {
                        this.drinkCategoriesList.push(drink.drinkType);
                    }
                    this.drinkCategoriesList=this.drinkCategoriesList.sort();
                    // this.tempTypeCategoryList=this.drinkCategories.find(cat => cat.drinkType == this.tempDrinkType).typeCategory.sort();
                    // --- code line not necessary as drink type is not yet selected on data loading
                } 
                catch (error) {
                    console.error(error);
                }

                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                    this.producerList = response.data;

                    // Check if user is a producer
                    if (localStorage.getItem('88B_accType') == "producer") {
                        this.isProducer = this.producerList.find(producer => producer._id["$oid"] == this.form['userID']["$oid"]).producerName;
                        this.form['producerID'] = this.form['userID'];
                    }
                } 
                catch (error) {
                    console.error(error);
                }

                // Only run when route params "id" is present (modifying previously submitted request)
                // TODO (Probably): Modify to allow for edit listing as well
                if (this.prevListing) {
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                        let previousData = response.data.find(listing => listing._id["$oid"] == this.$route.params.id);

                        // Check if user is the owner of the request (for request only)
                        if (previousData.userID["$oid"] != this.form['userID']["$oid"] && this.mode == "user") {
                            alert("You can only edit requests that you have submitted!");
                            this.$router.go(-1);
                        }

                        // Check if request is already reviewed (for request only)
                        if (previousData.reviewStatus != false && this.mode == "user") {
                            alert("Your request is already under review, and can no longer be edited!\nPlease submit a new request!");
                            this.$router.go(-1);
                        }

                        // If user is a producer, check if request producerID is the same as user producerID
                        if (this.isProducer != false) {
                            if (previousData.producerID["$oid"] != this.form['userID']["$oid"]) {
                                alert("This request is specified for a different producer!");
                                this.$router.go(-1);
                            }
                        }

                        // Fill form with previous data
                        this.form["listingName"] = previousData.listingName;
                        this.tempDrinkType = previousData.drinkType;
                        this.getDrinkCategoryList();
                        this.tempTypeCategory = previousData.typeCategory;
                        this.form["sourceLink"] = previousData.sourceLink;
                        this.form["reviewLink"] = previousData.reviewLink;
                        this.form["photo"] = previousData.photo;
                        this.form["producerID"] = previousData.producerID;

                        // Check if producerID is blank
                        if (this.form["producerID"]["$oid"] == "") {
                            // In request mode, fill in producerNew
                            if (this.mode == "user") {
                                this.form["producerNew"] = previousData.producerNew;
                                this.tempProducer = "Other";
                            } else if (this.mode == "power") {
                                // In creation mode, fill in tempProducer
                                this.tempProducer = previousData.producerNew;
                            }
                        } else {
                            this.tempProducer = this.producerList.find(producer => producer._id["$oid"] == previousData.producerID["$oid"]).producerName;
                        }

                        // If independent bottler, fill in bottler
                        if (previousData.bottler != "OB") {
                            this.indOperator = true;
                            this.form["bottler"] = previousData.bottler;
                        } else {
                            this.indOperator = false;
                        }

                        this.form["originCountry"] = previousData.originCountry;

                        // If abv has % sign, remove it. Change abv to number.
                        if (previousData.abv.includes("%")) {
                            this.form["abv"] = parseFloat(previousData.abv.slice(0, -1));
                        } else {
                            this.form["abv"] = previousData.abv;
                        }

                        // If age has value, change age to number.
                        if (previousData.age) {
                            this.form["age"] = parseInt(previousData.age);
                        }

                        this.form["brandRelation"] = previousData.brandRelation;
                    }
                    catch (error) {
                        console.error(error);
                    }
                }

                this.fillForm = true;
                this.dataLoaded = true;
            },

            getDrinkCategoryList() {
            
                this.tempTypeCategoryList=this.drinkCategories.find(cat => cat.drinkType == this.tempDrinkType).typeCategory;
                this.tempTypeCategory=""

            },
            getProducerID() {
                if(this.tempProducer!= 'Other'){
                    this.form['producerID'] = this.producerList.find(producer => producer.producerName == this.tempProducer)._id;
                } else {
                    this.form['producerID'] = {
                        "$oid": ""
                    }
                }

            },

            goBack() {
                this.$router.go(-1)
            },

            reset(){
                this.$router.go(0) // check if refreshing the page just works as well
                // this.indOperator = true
                // this.submitForm = false
                // this.successSubmission = false
                // this.errorSubmission = false
                // this.errorMessage = false
                // this.duplicateEntry = false
                // this.fillForm = true
                // this.responseCode= ""
                // this.tempTypeCategory = ""
                // this.tempProducer = ""
                // this.tempDrinkType = ""

                // for (const key in this.form) {
                //     this.form[key] = "";
                // }
                // this.form["brandRelation"] = "Others"
                // this.form["reviewStatus"] = false

                // this.form["producerID"] = {
                //     "$oid": "defaultProducer"
                // } // temporary until we have a way to get producerID
                // this.form["userID"] = {
                //     "$oid": "defaultUser"
                // } // temporary until we have a way to get userID
            },

            handleFileSelect(event){
                const file = event.target.files[0];
                const reader = new FileReader;
                
                reader.onload = () => {
                    const base64String = reader.result.split(',')[1];
                    this.form["photo"] = base64String
                };
                
                reader.readAsDataURL(file);
            },

            async submitListing(){
                // --- Form Validation ---
                let alertPhrase = "Your submission is incomplete:\n";

                // Validate Bottle Name
                if (!this.form["listingName"].trim()) {
                    alertPhrase += "- Name of Bottle is needed.\n"
                }

                // Validate Drink Type
                if (!this.tempDrinkType.trim()) {
                    alertPhrase += "- Drink Type is needed.\n"
                }

                // Validate Independent Bottler Name (if OB, will be handled by database writing method)
                if (!this.form["bottler"].trim() && this.indOperator == true) {
                    alertPhrase += "- Name of independent bottler is needed.\n"
                }

                // Validation ONLY FOR REQUEST
                if (this.mode == "user") {

                    // Validate Source Link
                    if (!this.form["sourceLink"].trim()) {
                        alertPhrase += "- Link to website or source is needed.\n"
                    }

                    // Validate Producer Name
                    if (Object.prototype.hasOwnProperty.call(this.form["producerID"], "$oid")) {
                        // If producerID is blank, check if producerNew is blank
                        if (!this.form["producerID"]["$oid"].trim() && !this.form["producerNew"].trim()) {
                            alertPhrase += "- Producer Name is needed.\n"
                        }
                    } else {
                        // Check if producerNew is blank
                        if (!this.form["producerNew"].trim()) {
                            alertPhrase += "- Producer Name is needed.\n"
                        }
                    }

                }

                // Validation ONLY FOR CREATION
                if (this.mode == "power") {

                    // Validate Official Description
                    if (!this.form["officialDesc"].trim()) {
                        alertPhrase += "- Official Description is needed.\n"
                    }

                    // Validate Producer ID
                    if (Object.prototype.hasOwnProperty.call(this.form["producerID"], "$oid")) {
                        // If producerID is blank, check if producerNew is blank
                        if (!this.form["producerID"]["$oid"].trim()) {
                            alertPhrase += "- Producer ID is needed: Create new producer first!\n"
                        }
                    } else {
                        alertPhrase += "- Producer ID is needed: Create new producer first!\n"
                    }

                    // Validate Country of Origin
                    if (!this.form["originCountry"].trim()) {
                        alertPhrase += "- Country of Origin is needed.\n"
                    }

                    // Validate Alcohol Strength (% ABV)
                    if (!this.form["abv"].toString().trim()) {
                        alertPhrase += "- Alcohol Strength is needed.\n"
                    }
                    
                }

                if (alertPhrase != "Your submission is incomplete:\n") {
                    // If errors, alert user and return
                    alertPhrase += "\nPlease fill in the required fields and try again."
                    alert(alertPhrase)
                    return "Submission Incomplete"
                } else {
                    // If no errors, pass corresponding API into database writing method
                    let submitAPI = ""
                    let submitData = {}
                    console.log(this.form['producerID'])
                    if (this.mode == "user") {
                        submitAPI = "http://127.0.0.1:5002/requestListing"
                        submitData = {
                            "listingName": this.form["listingName"].trim(),
                            "drinkType": this.tempDrinkType.trim(),
                            "typeCategory": this.tempTypeCategory.trim(),
                            "sourceLink": this.form["sourceLink"].trim(),
                            "reviewLink": this.form["reviewLink"].trim(),
                            "producerID": this.form["producerID"],
                            "producerNew": this.form["producerNew"].trim(),
                            "bottler": this.form["bottler"].trim(),
                            "originCountry": this.form["originCountry"].trim(),
                            "abv": this.form["abv"].toString().trim(),
                            "age": this.form["age"].toString().trim(),
                            "photo": this.form["photo"],
                            "brandRelation": this.form["brandRelation"],
                            "reviewStatus": this.form["reviewStatus"],
                            "userID": this.form["userID"]
                        }

                        if (this.prevListing) {
                            submitAPI = "http://127.0.0.1:5002/requestListingModify/" + this.$route.params.id
                        }

                    } else if (this.mode == "power") {
                        submitAPI = "http://127.0.0.1:5001/createListing"

                        // Default to tanglin gin producer ID
                        // await this.$axios.get('http://127.0.0.1:5000/getProducers')
                        // .then((response)=>{
                        //     this.form["producerID"] = response.data[0]._id
                        // })
                        // .catch((error)=>{
                        //     console.log(error);
                        //     this.responseCode = error.response.data.code
                        // });
                        // End of setting default to tanglin producer ID
                        
                        submitData = {
                            "listingName": this.form["listingName"].trim(),
                            "drinkType": this.tempDrinkType.trim(),
                            "typeCategory": this.tempTypeCategory.trim(),
                            "officialDesc": this.form["officialDesc"].trim(),
                            "sourceLink": this.form["sourceLink"].trim(),
                            "reviewLink": this.form["reviewLink"].trim(),
                            "producerID": this.form["producerID"],
                            "bottler": this.form["bottler"].trim(),
                            "originCountry": this.form["originCountry"].trim(),
                            "abv": this.form["abv"].toString().trim(),
                            "age": this.form["age"].toString().trim(),
                            "photo": this.form["photo"]
                        }

                    } else {
                        // Catching statement for invalid mode
                        alert("There was an issue with submission. Try to reopen the page after saving your inputs!")
                        return "Invalid Mode"
                    }

                    // If not independent bottler, set bottler to "OB"
                    if (this.indOperator == false) {
                        submitData["bottler"] = "OB"
                    }

                    // If abv has value, add % sign
                    if (submitData["abv"]) {
                        submitData["abv"] = submitData["abv"].toString() + "%"
                    }

                    // If no photo, set default photo
                    // TODO Set defaultPhoto to a default base64 string
                    if (!submitData["photo"]) {
                        submitData["photo"] = "defaultPhoto"
                    }

                    this.writeListing(submitAPI, submitData)
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
                if(this.responseCode==201){
                    this.successSubmission=true; // Display success message
                    this.submitForm=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.submitForm=false; // Hide submission in progress message
                    if(this.responseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

        }
    }
</script>