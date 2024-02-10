<!-- User Form: Request for Bottle Listing Modification -->

<!--
    TODO:
    - [Access Control] This form should only be accessible from a Bottle Listing page's "Suggest Edit" / "Report Duplicate" button
    --- This form should only function if a bottle listing information is parsed into the form. Show bottle listing information in the form.
    --- If no bottle listing information is parsed into the form, error message should be displayed. Redirect to previous page after short delay.
    - "Return" button may bring user back to same page, but with form cleared. Prevent that by returning to last notable page.
-->

<template>
    <NavBar />
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when form is being submitted -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="submitForm"> 
            <span>The form is being submitted, please hold on!</span>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div class="text-success fst-italic fw-bold fs-3" v-if="successSubmission"> 
            <span v-if="mode == 'edit'">The edit request has successfully been submitted!</span> <!-- for edit requests -->
            <span v-if="mode == 'duplicate'">The duplicate report has successfully been submitted!</span> <!-- for duplicate reports -->
            <br>
            <button type="button" class="btn primary-btn mx-1 mb-3" @click="goBack">Return</button>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to submit, please try again!</span>
            <span v-if="invalidListing">Your request is not linked to a valid listing, please try again!</span>
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
                    <p class="fw-bold fs-1" v-if="mode == 'edit'">Propose Edit to Bottle Listing</p>
                    <p class="fw-bold fs-1" v-if="mode == 'duplicate'">Report Duplicate Bottle Listing</p>
                </div>

                <!-- TODO: Show Linked Bottle Listing Information -->

                <!-- Start of form -->
                <form v-on:submit.prevent="submitEdit" id="frm">
                    <!-- Input: Proposed Edits / Duplicate Report Information -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1" v-if="mode == 'edit'">What edits do you propose? <span class="text-danger">*</span></p>
                        <p class="text-start mb-1" v-if="mode == 'duplicate'">Reason for duplicate report: <span class="text-danger">*</span></p>
                        <textarea rows=3 class="form-control" v-model="form['editDesc']" id="editDesc" placeholder="Enter your comments..." required></textarea>
                    </div>

                    <!-- (ONLY FOR EDITS) Input: Link to source -->
                    <div class="form-group mb-3" v-if="mode == 'edit'">
                        <p class="text-start mb-1">Link to source, if applicable.</p>
                        <input type="text" class="form-control" v-model="form['sourceLink']" id="sourceLink" placeholder="Enter source link">
                    </div>

                    <!-- (ONLY FOR DUPLICATES) Input: Link to duplicate -->
                    <div class="form-group mb-3" v-if="mode == 'duplicate'">
                        <p class="text-start mb-1">Link to duplicate listing <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['duplicateLink']" id="duplicateLink" placeholder="Enter duplicate link">
                    </div>

                    <!-- Input: Relationship with Brand -->
                    <p class="text-start mb-1">Your Relationship with the Brand <span class="text-danger">*</span></p>
                    <div class="text-start mb-3">
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
                    
                    <button type="submit" class="btn secondary-btn mx-1 mb-3" v-if="mode == 'edit'">Submit Edit Request</button>
                    <button type="submit" class="btn secondary-btn mx-1 mb-3" v-if="mode == 'duplicate'">Submit Duplicate Report</button>
                    <button type="button" class="btn primary-btn mx-1 mb-3" @click="goBack">Return</button>
                
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';

        export default {
            name: 'RequestListingModify',
            components: {
                NavBar
            },
            data() {
                return {
                    mode: this.$route.params.mode,
                    form: {
                        editDesc: '',
                        sourceLink: '',
                        duplicateLink: '',
                        brandRelation: 'Others',
                        listingID: {
                            "$oid": "65b34a06915a4e4e9e08876d"
                        }, // TODO: Fill in listingID with listingID of linked listing (where user clicked from)
                        userID: {
                            "$oid": "defaultUser"
                        }, // TODO: Fill in userID with userID of user submitting form
                        reviewStatus: false
                    },
                    submitForm: false,
                    successSubmission: false,
                    errorSubmission: false,
                    errorMessage: false,
                    invalidListing: false,
                    fillForm: true,
                    responseCode: ""
                }
            },
            mounted() {
                if (localStorage.getItem('88B_accType') != "user") {
                    this.$router.push({path: '/login'});
                }
            },
            methods: {
                goBack() {
                    this.$router.go(-1)
                },

                reset() {
                    this.submitForm = false;
                    this.successSubmission = false;
                    this.errorSubmission = false;
                    this.errorMessage = false;
                    this.invalidListing = false;
                    this.fillForm = true;
                    this.responseCode = "";

                    for (const key in this.form) {
                        this.form[key] = "";
                    }
                    this.form["brandRelation"] = "Others";
                    this.form["reviewStatus"] = false;

                    this.form["listingID"] = {
                        "$oid": "65b26ac6d583c059ba33ff10"
                    }; // temporary until we can get listingID from linked listing
                    this.form["userID"] = {
                        "$oid": "defaultUser"
                    }; // temporary until we can get userID from user
                },

                submitEdit() {
                    // --- Form Validation ---
                    let alertPhrase = "Your submission is incomplete:\n";

                    // Validate Edit Description
                    if (!this.form["editDesc"].trim()) {
                        alertPhrase += "- Please enter your comments.\n";
                    }

                    // Validate Duplicate Link
                    if (this.mode == "duplicate" && !this.form["duplicateLink"].trim()) {
                        alertPhrase += "- Please enter the duplicate listing link.\n";
                    }

                    if (alertPhrase != "Your submission is incomplete:\n") {
                        // If errors, alert user and return
                        alertPhrase += "\nPlease fill in the required fields and try again.";
                        alert(alertPhrase);
                        return "Submission Incomplete";
                    } else {
                        // If no errors, call database writing method
                        this.writeEdit();
                    }
                },

                async writeEdit() {

                    this.fillForm = false; // Hide form
                    this.submitForm = true; // Display submission in progress message

                    const response = await this.$axios.post("http://127.0.0.1:5002/requestEdits", this.form)
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
                            this.invalidListing = true // Display invalid listing error message
                        }else{
                            this.errorMessage = true // Display generic error message
                        }
                    }
                    return response
                },
            }
        }
</script>