<!-- Component for submitting new listings: Create (Producers, Admins?) / Request (Users) -->

<!--
    TODO:
    - "Return" button may bring user back to same page, but with form cleared. Prevent that by returning to last notable page.
    - Dropdown Selection for Drink Type + Drink Category (with option for "Other"), Country of Origin
    - Make Producer field a dropdown list (for non-producer) / autofill and non-changeable (for producer). This fills in producerID in backend as well.
    - If messages show, consider hiding / disabling the form
    - Independent Bottler Yes/No radio buttons should be styled to look like checkboxes.
        -- [?] Consider using switch / single checkbox instead (if so, flip isOperator: rename to indOperator).

    - Form Methods (needs to do different things based on mode)
    - Input: Relationship with Brand (ONLY FOR USERS)
    
    - Styling Discussion / Fixes
    - Accept pre-filled information from users to be created by power users.
    - Consider if any duplicate submission has to be detected / prevented. Includes requests for bottles that already exist.
    - Consider use of character counters and character limits if/when necessary.
    - [?] Relationship with Brand: If "Others" is selected, should there be a text box to fill in for users to specify their relationship?
    - [?] Should we save the form data for easier retry when invoking reset()? Should reset() just hard refresh the page?
-->

<template>
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when form is being submitted -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="submitForm"> 
            <span>The form is being submitted, please hold on!</span>
            <hr>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div class="text-success fst-italic fw-bold fs-3" v-if="successSubmission"> 
            <span v-if="mode == 'user'">The bottle listing has successfully been submitted!</span> <!-- for user -->
            <span v-if="mode == 'power'">The bottle listing has successfully been created!</span> <!-- for producer -->
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Submit another bottle listing here! </span>
            </button>
            <hr>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to submit, please try again!</span>
            <span v-if="duplicateEntry">The bottle listing you are trying to submit already exists.</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Retry your submission here! </span>
            </button>
            <hr>
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
                    <div class="row mb-3">
                        <div class="form-group col-md-6">
                            <p class="text-start mb-1">Drink Type <span class="text-danger">*</span></p>
                            <input type="text" class="form-control" v-model="form['drinkType']" id="drinkType" placeholder="Enter Drink Type" required>
                        </div>
                        <div class="form-group col-md-6">
                            <p class="text-start mb-1">Drink Category</p>
                            <input type="text" class="form-control" v-model="form['typeCategory']" id="typeCategory" placeholder="Enter Drink Category">
                        </div>
                    </div>
                    
                    <!-- (ONLY FOR CREATION) Input: Drink Description -->
                    <div class="form-group mb-3" v-if="mode == 'power'">
                        <p class="text-start mb-1">Official Description <span class="text-danger">*</span></p>
                        <textarea rows=3 class="form-control" v-model="form['officialDesc']" id="officialDesc" placeholder="Enter description of bottle" required></textarea>
                    </div>

                    <!-- Input: Link to website or source (optional for creation, mandatory for request) -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Link to website or source <span class="text-danger" v-if="mode == 'user'">*</span></p>
                        <input type="text" class="form-control" v-model="form['sourceLink']" id="sourceLink" placeholder="Enter link">
                    </div>

                    <!-- Input: Link to 88 Bamboo review -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Link to 88 Bamboo review</p>
                        <input type="text" class="form-control" v-model="form['reviewLink']" id="reviewLink" placeholder="Enter link">
                    </div>

                    <!-- Input: Photo file -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Photo of bottle</p>
                        <input class="form-control" type="file" id="formFile" @change="handleFileSelect">
                    </div>

                    <!-- Input: Producer Name -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Producer Name <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['producer']" id="producer" placeholder="Enter Producer Name" required>
                    </div>

                    <!-- Input: Independent Bottler Check -->
                    <p class="text-start mb-1">Is this bottle by an independent bottler? <span class="text-danger">*</span></p>
                        <!-- Radio Buttons -->
                    <div class="text-start mb-3">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="isOperator" :value="false" name="checkIBYes" id="independentBottler">
                            <label class="form-check-label" for="independentBottler">Yes</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="isOperator" :value="true" name="checkIBNo" id="originalBottler">
                            <label class="form-check-label" for="originalBottler">No</label>
                        </div>
                    </div>
                        <!-- (ONLY IF above toggled to "Yes") Input Text for Independent Bottler -->
                    <div class="form-group mb-3" v-if="isOperator == false">
                        <p class="text-start mb-1">If yes, who is the independent bottler? <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['bottler']" :disabled="isOperator" id="bottlerName" placeholder="Enter Bottler Name">
                    </div>

                    <!-- Input: originCountry -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Country of Origin</p>
                        <input type="text" class="form-control" v-model="form['originCountry']" id="originCountry" placeholder="Enter Country">
                    </div>

                    <!-- Input: Alcohol Strength (% ABV) + Alcohol Age (years old) -->
                    <div class="row mb-3">
                        <div class="form-group col-6">
                            <p class="text-start mb-1">Strength</p>
                            <div class="form-group row">
                                <div class="col-6 pe-1">
                                    <input type="number" v-model="form['abv']" class="form-control" id="abv" min="0" max="100">
                                </div>
                                <label for="abv" class="col-6 col-form-label ps-1 text-start">% ABV</label>
                            </div>
                        </div>
                        <div class="form-group col-6">
                            <p class="text-start mb-1">Age</p>
                            <div class="form-group row">
                                <div class="col-6 pe-1">
                                    <input type="number" v-model="form['age']" class="form-control" id="age" min="0">
                                </div>
                                <label for="age" class="col-6 col-form-label ps-1 text-start">years old</label>
                            </div>
                        </div>
                    </div>

                    <!-- (ONLY FOR USERS) Input: Relationship with Brand -->
                    <p class="text-start mb-1" v-if="mode == 'user'">Your Relationship with the Brand <span class="text-danger">*</span></p>
                    <div class="text-start mb-3" v-if="mode == 'user'">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" v-model="form['brandRelation']" :value="'Customer'" name="brandRelationCustomer" id="brandRelationCustomer">
                            <label class="form-check-label" for="brandRelationCustomer">Customer</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" v-model="form['brandRelation']" :value="'Employee'" name="brandRelationEmployee" id="brandRelationEmployee">
                            <label class="form-check-label" for="brandRelationEmployee">Employee</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" v-model="form['brandRelation']" :value="'Public Relations'" name="brandRelationPR" id="brandRelationPR">
                            <label class="form-check-label" for="brandRelationPR">Public Relations</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" v-model="form['brandRelation']" :value="'Distributor'" name="brandRelationDist" id="brandRelationDist">
                            <label class="form-check-label" for="brandRelationDist">Distributor</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="checkbox" v-model="form['brandRelation']" :value="'Others'" name="brandRelationOther" id="brandRelationOther">
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
                    "officialDesc": "",
                    "sourceLink": "",
                    "reviewLink": "",
                    "producer": "",
                    "bottler": "",
                    "originCountry": "",
                    "abv": "",
                    "age": "",
                    "brandRelation": "",
                    "photo": ""
                },
                isOperator: false,
                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                fillForm: true,
                responseCode: ""
            }
        },
        methods:{
            goBack() {
                this.$router.go(-1)
            },

            reset(){
                this.isOperator = false
                this.submitForm = false
                this.successSubmission = false
                this.errorSubmission = false
                this.errorMessage = false   // is this required?
                this.duplicateEntry = false
                this.fillForm = true
                this.responseCode= ""
                for (const key in this.form) {
                    this.form[key] = "";
                }
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

            submitListing(){
                if(this.mode == "power"){
                    this.createListing()
                }
            },

            async createListing(){
                // form validation first
                console.log(this.form["photo"]) // REMOVE this line later

                let alertPhrase = "";
                if(this.isOperator){
                    this.form["bottler"] = "OB"
                }

                // TODO Set default to a default base64 string
                if(!this.form["photo"]){
                    this.form["photo"] = "scam"
                }

                
                if (!this.form["listingName"].trim()){
                    alertPhrase += "Name of bottle is needed.\n"
                }
                if (!this.form["producer"].trim()){
                    alertPhrase += "Name of producer is needed.\n"
                }
                if(!this.form["drinkType"].trim()){
                    alertPhrase += "Type of drink is needed.\n"
                }
                if(!this.form["reviewLink"].trim()){
                    alertPhrase += "Link to website or source is needed.\n"
                }
                if(!this.form["bottler"].trim()){
                    alertPhrase += "Name of bottler is needed.\n"
                }
                if(alertPhrase){
                    alert(alertPhrase)
                    return "error"
                }
                
                this.fillForm=false;
                this.submitForm=true;


                const response = await this.$axios.post('http://127.0.0.1:5001/createListings',this.form)
                .then((response)=>{
                    this.responseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.responseCode = error.response.data.code
                });
                console.log(this.responseCode)
                if(this.responseCode==201){
                    this.successSubmission=true;
                    this.submitForm=false;
                }else{
                    this.errorSubmission=true;
                    this.submitForm=false;
                    if(this.responseCode==400){
                        this.duplicateEntry = true
                    }else{
                        this.errorMessage = true
                    }
                }
                return response

            },

        }
    }
</script>