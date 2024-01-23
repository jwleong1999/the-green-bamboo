<!-- Component for submitting new listings: Create (Producers, Admins?) / Request (Users) -->

<!--
    TODO:
    - Form Methods (needs to do different things based on mode)
    - Input: Relationship with Brand (ONLY FOR USERS)
    - Return Button
    - Styling Discussion / Fixes
    - Accept pre-filled information from users to be created by power users.
    - Consider if any duplicate submission has to be detected / prevented. Includes requests for bottles that already exist.
    - Consider use of character counters and character limits if/when necessary.
-->

<template>
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when form is being submitted -->
        <div v-if="submitForm"> 
            <p>The form is being submitted, please hold on!</p>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div v-if="successSubmission"> 
            <h2 v-if="mode == 'user'">The bottle listing has successfully been submitted!</h2> <!-- for user -->
            <h2 v-if="mode == 'power'">The bottle listing has successfully been created!</h2> <!-- for producer -->
            <button class="btn primary-btn btn-sm" @click="reset">
                <h4> Submit another bottle listing here! </h4>
            </button>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div v-if="errorSubmission"> 
            <h2 v-if="errorMessage">An error occurred while attempting to submit, please try again!</h2>
            <h2 v-if="duplicateEntry">The bottle listing you are trying to submit already exists.</h2>
            <button class="btn primary-btn btn-sm" @click="reset">
                <h4> Retry your submission here! </h4>
            </button>
        </div>


        <!-- div for the whole form plus header plus col-->
        <div class="row" v-if="fillForm">
            
            <!-- button (WHAT DOES THIS DO) -->
            <div class="col-3">
            </div>
            <!-- start of the elements -->
            <div class="col-6">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1">Submit A New Bottle Listing</p>
                </div>

                <!-- Start of form -->
                <form v-on:submit.prevent="submitListing" id="frm">
                    <!-- Input: Bottle Name -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Name of Bottle <span class="text-danger">*</span></p>
                        <input type="text" v-model="form['Expression Name']" class="form-control" id="bottleName" placeholder="Enter Bottle Name">
                    </div>

                    <!-- Input: Drink Type + Category -->
                    <div class="row mb-3">
                        <div class="form-group col-md-6">
                            <p class="text-start mb-1">Drink Type <span class="text-danger">*</span></p>
                            <input type="text" class="form-control" v-model="form['Drink Type']" id="bottleType" placeholder="Type of Drink">
                        </div>
                        <div class="form-group col-md-6">
                            <p class="text-start mb-1">Drink Category</p>
                            <input type="text" class="form-control" v-model="form['Drink Category']" id="bottleCategory" placeholder="Category of Drink">
                        </div>
                    </div>
                    
                    <!-- Input: Drink Description (ONLY FOR PRODUCERS) -->
                    <div class="form-group mb-3" v-if="mode == 'power'">
                        <p class="text-start mb-1">Official Description</p>
                        <textarea class="form-control" v-model="form['Official Description']" id="description" placeholder="Enter description of bottle"></textarea>
                    </div>

                    <!-- Input: Link to website or source -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Link to website or source <span class="text-danger">*</span></p>
                        <input type="text" class="form-control" v-model="form['88B Website Review (if applicable)']" id="bottleName" placeholder="Enter link">
                    </div>

                    <!-- Input: Independent Bottler Check -->
                    <p class="text-start mb-1">Is this bottle by an independent bottler? <span class="text-danger">*</span></p>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" @change="checkRadio" v-model="isOperator" :value = "false" name="inlineRadioOptions" id="independentBottler">
                        <label class="form-check-label" for="inlineRadio1">Yes</label>
                    </div>
                    <div class="form-check form-check-inline mb-3">
                        <input class="form-check-input" type="radio" @change="checkRadio" v-model="isOperator" :value="true" name="inlineRadioOptions" id="notIndependent">
                        <label class="form-check-label" for="inlineRadio2">No</label>
                    </div>
                    <!-- End of radios -->
                    <div class="form-group mb-3" v-if="isOperator == false">
                        <p class="text-start mb-1">If yes, who is the independent bottler?</p>
                        <input type="text" class="form-control" v-model="form['Bottler (OB or Specify name of IB)']" :disabled="isOperator" id="bottlerName" placeholder="Enter Bottler Name">
                    </div>
                    <!-- End of input text for independent bottler (ONLY APPEARS IF INDEPENDENT BOTTLER = TRUE) -->

                    <!-- Input: Country of Origin -->
                    <div class="form-group mb-3">
                        <p class="text-start mb-1">Country of Origin</p>
                        <input type="text" class="form-control" v-model="form['Country of Origin']" id="countryOfOrigin" placeholder="Enter country">
                    </div>

                    <!-- Input: Alcohol Strength % ABV -->
                    <p class="text-start mb-1">Strength</p>
                    <div class="form-group row">
                        <div class="col-sm-3 pe-1">
                            <input type="number" max="100" v-model="form['ABV']"  class="form-control" id="ABV">
                        </div>
                        <label for="ABV" class="col-sm-3 col-form-label ps-1 text-start">% ABV</label>
                        
                    </div>

                    <!-- Input: Alcohol Age (ONLY FOR PRODUCERS) -->
                    <p class="text-start mb-1" v-if="mode == 'power'">Age</p>
                    <div class="form-group row" v-if="mode == 'power'">
                        <div class="col-sm-3 pe-1">
                            <input type="number" class="form-control" v-model="form['Age']" id="ABV">
                        </div>
                        <label for="ABV" class="col-sm-3 col-form-label ps-1 text-start">years old</label>
                        
                    </div>

                    <!-- TODO Input: Relationship with Brand (ONLY FOR USERS) -->
                    
                    <button type="submit" class="primary-btn">Submit</button>
                    <!-- TODO: Return Button -->
                
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
                    "Expression Name": "",
                    "Drink Type": "",
                    "Drink Category": "",
                    "Official Description": "",
                    "88B Website Review (if applicable)": "",
                    "Bottler (OB or Specify name of IB)": "",
                    "Country of Origin": "",
                    "ABV": "",
                    "Age": ""
                },
                isOperator: false,
                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                fillForm: true
            }
        }
    }
</script>