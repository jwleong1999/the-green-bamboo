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
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;"> 
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

    <!-- header -->
    <div class="container pt-3">
        <!-- Display when form is being submitted -->
        <div v-if="submitForm"> 
            <p>The form is being submitted, please hold on!</p>
        </div>
        
        <!-- Display when bottle listing is successfully created -->
        <div v-if="successCreation"> 
            <h2>The bottle listing has successfully been created!</h2>
            <button class="btn primary-btn btn-sm" @click="reset">
                <h4> Create another bottle listing here! </h4>
            </button>
        </div>
        
        <!-- Display when bottle listing creation encounters an error -->
        <div v-if="errorCreation"> 
            <h2 v-if="errorMessage">There is an error in creating the bottle, please try again!</h2>
            <h2 v-if="duplicateEntry">The bottle listing you are trying to create already exists.</h2>
            <button class="btn primary-btn btn-sm" @click="reset">
                <h4> Retry creating another bottle listing here! </h4>
            </button>
        </div>


        <!-- div for the whole form plus header plus col-->
        <div class="row" v-if="fillForm">
            
            <!-- button -->
            <div class="col-4">
            </div>
            <!-- start of the elements -->
            <div class="col-4">
                <div class="d-grid gap-2">
                    <p style="font-weight: bold; font-size:x-large;">Submit A New Bottle Listing</p>
                </div>

                <!-- Start of form -->
                <form v-on:submit.prevent="createListing" id="frm">
                    <!-- Input for bottle Name -->
                    <div class="form-group" style="margin-bottom: 20px;">
                        <p style="text-align: left;margin-bottom: 5px;">Name of Bottle*</p>
                        <input type="text" v-model="form['Expression Name']" class="form-control" id="bottleName" placeholder="Enter Bottle Name">
                    </div>

                    <!-- Input for Drink type and category -->
                    <div class="row" style="margin-bottom: 20px;">
                        <div class="form-group col-md-6">
                            <p style="text-align: left;margin-bottom: 5px;">Drink Type*</p>
                            <input type="text" class="form-control" v-model="form['Drink Type']" id="bottleType" placeholder="Type of Drink">
                        </div>
                        <div class="form-group col-md-6">
                            <p style="text-align: left;margin-bottom: 5px;">Drink Category</p>
                            <input type="text" class="form-control" v-model="form['Drink Category']" id="bottleCategory" placeholder="Category of Drink">
                        </div>
                    </div>
                    
                    <!-- Input for description of drink -->
                    <div class="form-group" style="margin-bottom: 20px;">
                        <p style="text-align: left;margin-bottom: 5px;">Official Description</p>
                        <textarea class="form-control" v-model="form['Official Description']" id="description" placeholder="Enter description of bottle"></textarea>
                    </div>

                    <!-- Input for link to website or source/88B website review -->
                    <div class="form-group" style="margin-bottom: 20px;">
                        <p style="text-align: left;margin-bottom: 5px;">Link to website or source*</p>
                        <input type="text" class="form-control" v-model="form['88B Website Review (if applicable)']" id="bottleName" placeholder="Enter link">
                    </div>

                    <!-- Input text and radios for bottler -->
                    <p style="text-align: left;margin-bottom: 5px;">Is this bottle by an independent bottler?*</p>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" @change="checkRadio" v-model="isOperator" :value = "false" name="inlineRadioOptions" id="independentBottler">
                        <label class="form-check-label" for="inlineRadio1">Yes</label>
                    </div>
                    <div class="form-check form-check-inline" style="margin-bottom: 20px;">
                        <input class="form-check-input" type="radio" @change="checkRadio" v-model="isOperator" :value="true" name="inlineRadioOptions" id="notIndependent">
                        <label class="form-check-label" for="inlineRadio2">No</label>
                    </div>
                    <!-- End of radios -->
                    <div class="form-group" style="margin-bottom: 20px;">
                        <p style="text-align: left;margin-bottom: 5px;">If yes, who is the independent bottler</p>
                        <input type="text" class="form-control" v-model="form['Bottler (OB or Specify name of IB)']" :disabled="isOperator" id="bottlerName" placeholder="Enter Bottler Name">
                    </div>
                    <!-- End of input text for independent bottler -->

                    <!-- Input for country of origin of bottle -->
                    <div class="form-group" style="margin-bottom: 20px;">
                        <p style="text-align: left;margin-bottom: 5px;">Country of Origin</p>
                        <input type="text" class="form-control" v-model="form['Country of Origin']" id="countryOfOrigin" placeholder="Enter country">
                    </div>

                    <!-- Input for Strength of alcohol -->
                    <p style="text-align: left;margin-bottom: 5px;">Strength</p>
                    <div class="form-group row">
                        <div class="col-sm-3" style="padding-right: 0;">
                            <input type="number" max="100" v-model="form['ABV']"  class="form-control" id="ABV" style="width:100px;">
                        </div>
                        <label for="ABV" class="col-sm-2 col-form-label" style="padding-left: 0;">%ABV</label>
                        
                    </div>

                    <!-- Input for age of alcohol -->
                    <p style="text-align:left;margin-bottom: 5px;">Age</p>
                    <div class="form-group row">
                        <div class="col-sm-3" style="padding-right: 0;">
                            <input type="number" class="form-control" v-model="form['Age']" id="ABV" style="width:100px;">
                        </div>
                        <label for="ABV" class="col-sm-3 col-form-label" style="padding-left: 0;">years old</label>
                        
                    </div>

                    
                    <button type="submit" class="primary-btn">Submit</button>
                
                </form>
                <!-- End of Form -->

            </div>
            <!-- End of the elements  -->
        </div>
    </div>
    <!-- End of whole page -->

    <!-- content -->
    <div class="container pt-3">
        
    </div>

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->
<style>

    body {
        color: black;
        background-color: #D9D9D9 ;
    }

    .navbar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        border-bottom: 3px solid #535C72;
    }

    .navbar {
        text-align: center;
        width: 75%;
    }

    .navbar-brand {
        margin-bottom: 10px;
    }

    .navbar-inner-container {
        width: 75%;
    }

    .primary-btn {
        color: whitesmoke;
        background-color: #535C72;
        border-radius: 30px;
    }

    .primary-btn-outline {
        color: #535C72;
        background-color: whitesmoke;
        border-radius: 30px;
        border: 4px solid #535C72;
    }

    .primary-square {
        color: whitesmoke;
        background-color: #535C72;
    }

    .primary-light-dropdown {
        color: whitesmoke;
        background-color: #747D92;
        border-radius: 10px;
    }

    .secondary-btn {
        color: whitesmoke;
        background-color: #DD9E54;
        border-radius: 30px;
    }

    .secondary-btn-border {
        color: whitesmoke;
        background-color: #DD9E54;
        border-radius: 30px;
        border: 1px solid whitesmoke;
    }

    .navbar-toggler,
    .navbar-toggler:focus,
    .navbar-toggler:active,
    .navbar-toggler-icon:focus {
        outline: none;
        border: none;
        box-shadow: none;
    }

    .search-bar {
        border: 2px solid #535C72;
    }

    .square-inline {
        display: flex;
        align-items: center;
    }

    .square-inline-text-start {
        margin-right: auto; /* Pushes the text to the left */
    }

    .img-border {
        border: 4px solid #535C72;
        border-radius: 30px;
    }

    .image-container {
        position: relative;
    }

    .overlay-icon {
        position: absolute;
        top: 15px;
        right: 15px;
    }

    .rating-text, .bi-star-fill {
        color: #DD9E54;
    }

</style>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    // import axios from 'axios';
    export default {
    data() {
        return {
        responseCode:"",
        isOperator: false,
        fillForm: true,
        submitForm: false,
        successCreation: false,
        errorCreation: false,
        duplicateEntry:false,
        errorMessage:false,
        form:{
            "Expression Name": "",
            "Producer": "",
            "Bottler (OB or Specify name of IB)": "",
            "Country of Origin": "",
            "Drink Type": "",
            "Drink Category": "",
            "Age": "",
            "ABV": "",
            "88B Website Review (if applicable)": "",
            "Official Description": "",
        },
        };
    },
    methods: {
        checkRadio(){
            if(this.isOperator){
                this.form['Bottler (OB or Specify name of IB)'] = ""
            }
        },

        // Method to send post request, upon button click, hide the form, then display the results

        async createListing(){
            // form validation first
            this.fillForm=false;
            this.submitForm=true;
            let alertPhrase = "";
            if(this.isOperator){
                this.form["Bottler (OB or Specify name of IB)"] = "OB"
            }
            if (!this.form["Expression Name"].trim()){
                alertPhrase += "Name of bottle is needed.\n"
            }
            if(!this.form["Drink Type"].trim()){
                alertPhrase += "Type of drink is needed.\n"
            }
            if(!this.form["88B Website Review (if applicable)"].trim()){
                alertPhrase += "Link to website or source is needed.\n"
            }
            if(!this.form["Bottler (OB or Specify name of IB)"].trim()){
                alertPhrase += "Name of bottler is needed.\n"
            }
            if(alertPhrase){
                alert(alertPhrase)
                return "error"
            }


            // const response = await axios.post('http://127.0.0.1:5000/createListings',this.form)
            // .then((response)=>{
            //     this.responseCode = response.data.code
            // })
            // .catch((error)=>{
            //     console.log(error);
            //     this.responseCode = error.response.data.code
            // });
            // console.log(this.responseCode)
            // if(this.responseCode==201){
            //     this.successCreation=true;
            //     this.submitForm=false;
            // }else{
            //     this.errorCreation=true;
            //     this.submitForm=false;
            //     if(this.responseCode==400){
            //         this.duplicateEntry = true
            //     }else{
            //         this.errorMessage = true
            //     }
            // }

        },

        reset(){
            this.fillForm=true
            this.successCreation=false
            this.submitForm=false
            this.errorCreation= false
            this.duplicateEntry= false
            
            this.responseCode= ""
            this.isOperator = false
            for (const key in this.form) {
                this.form[key] = "";
            }
        },

    }
    };
    
</script>


