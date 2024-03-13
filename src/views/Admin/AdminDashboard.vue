<!-- Admin can access this page to handle admin controls. -->

<template>
    <NavBar />
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when data is being loaded -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="!dataLoaded"> 
            <span>Currently loading data, please hold on!</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when data loading encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="loadError"> 
            <span>An error occurred while loading data, please try refreshing the page!</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="()=>{this.$router.go(0)}">
                <span class="fs-5 fst-italic"> Refresh Page </span>
            </button>
        </div>

        <!-- Display requests after data loaded -->
        <div v-if="dataLoaded && !loadError">

            <!-- Form Title -->
            <div class="col-12">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1 m-0">Admin Dashboard</p>
                </div>
            </div>

            <hr>
            <!-- tag controls -->
            <div class="row text-center">
                <div class="col-12">
                    <h3><b>Tag Controls</b></h3>
                </div>
            </div>
            <div>
                <p class="gap-1">
                    <!-- Open a modal prompting to edit or add tags -->
                    <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#observationModal">
                        Observation Tags
                    </button>
                    <button class="btn tertiary-btn reverse-clickable-text m-1" type="button">
                        Flavour Tags
                    </button>
                
                </p>
                <!-- modal for lock listing to moderators -->
                <div class="modal fade" id="observationModal" tabindex="-1" aria-labelledby="observationModalLabel" aria-hidden="true" data-bs-backdrop="static">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header" style="background-color: #535C72">
                                <h1 v-if="selectingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Observation Tag Control</h1>
                                <h1 v-if="addingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Add Observation Tag</h1>
                                <h1 v-if="editingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Edit Observation Tag</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>

                            <!-- Modal for success and error message -->
                            <div v-if="successUpdateObservation" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                <span>Observation tags have successfully been updated!</span>
                            </div>

                            <div v-if="successCreateObservation" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                <span>Observation tags have successfully been created!</span>
                            </div>

                            <div v-if="updatingObservation" class="modal-body text-center text-primary fst-italic fw-bold fs-3">
                                <span>Observation tags are being updated!</span>
                            </div>

                            <div v-if="submittingObservation" class="modal-body text-center text-primary fst-italic fw-bold fs-3">
                                <span>Observation tags are being added!</span>
                            </div>

                            <div v-if="errorUpdateObservation" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                <span v-if="invalidTag"> The observation tag you are trying to update does not exist</span>
                                <span v-if="errorMessage">An error occurred updating the observation tags. Please try again.</span>
                            </div>

                            <div v-if="errorCreateObservation" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                <span v-if="duplicateTag"> The observation tag you are trying to create already exists!</span>
                                <span v-if="errorMessage">An error occurred updating the observation tags. Please try again.</span>
                            </div>
                            

                            <!-- Modal body for selecting mode for observation operations -->
                            <div v-if="selectingObservation" class="modal-body">
                                <button class="btn btn-warning reverse-clickable-text text-dark" @click="addObservation" type="button">
                                    Add Observation Tags
                                </button> 

                                <button class="btn btn-primary mx-1 reverse-clickable-text" @click="editObservation" type="button">
                                    Edit Observation Tags
                                </button>
                            </div>
                            <!-- Modal body for adding observation -->
                            <div v-if="addingObservation" class="modal-body">
                                <input v-model="newObservation" type="text" class="form-control">
                                <p v-if="newObservation ==''" class='text-danger text-start mb-2 fw-bold'>Observation Tag cannot be empty</p>
                            </div>
                            <!-- Modal body for editing observation -->
                            <div v-if="editingObservation" class="modal-body">
                                <div class="row">
                                    <div v-for="tag in editedObservationTags" class="mb-2 col-md-6"  v-bind:key="tag._id">
                                        <input v-model="tag.observationTag" type="text" class="form-control">
                                        <p v-if="tag.observationTag==''" class='text-danger text-start mb-2 fw-bold'>Observation Tag cannot be empty</p>
                                    </div>
                                </div>
                                <p class='text-danger text-center mb-2 fw-bold' v-if="nothingChanged">There is no changed observation tag</p>
                            </div>

                            <div class="modal-footer">
                                <button v-if="selectingObservation" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button v-if="!selectingObservation" @click="resetObservation" type="button" class="btn btn-secondary">Return</button>
                                <button v-if="editingObservation" @click="updateObservation" type="button" class="btn btn-primary">Save Updates</button>
                                <button v-if="addingObservation" @click="createNewObservation" type="button" class="btn btn-primary">Add Tag</button>
                                <button v-if="successUpdateObservation || errorUpdateObservation" @click="resetErrors" type="button" data-bs-dismiss="modal" class="btn btn-secondary">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- end of modal-->
            </div>
            <!-- tag control end -->
            <hr>
            <!-- add business -->
            <div class="row text-center">
                <div class="col-12">
                    <h3><b>Add Businesses</b></h3>
                </div>
            </div>
            <div>
                <p class="gap-1">
                    <!-- Open a modal prompting to edit or add tags -->
                    <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#addBusinessModal">
                        Add a Business
                    </button>
                </p>
                <!-- add business modal start -->
                <div class="modal fade" id="addBusinessModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add a Business</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body text-start">
                            <div>
                                <div class="mb-2">
                                    Profile Type
                                </div>
                                <div class="mb-4">
                                    <div class="form-check form-check-inline">
                                            <input class="form-check-input" type="radio" id="inlineCheckbox1" v-model="businessType" value="producer" name="business">
                                        <label class="form-check-label text-start fw-bold" for="inlineCheckbox1">Brand/Producer</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" id="inlineCheckbox2" v-model="businessType" value="venue" name="business">
                                        <label class="form-check-label text-start fw-bold" for="inlineCheckbox2">Venue</label>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <div class="mb-2">
                                    Name
                                </div>
                                <div class="mb-4">
                                    <input type="text" class="form-control" v-model="businessName">
                                </div>
                            </div>
                            <div>
                                <div class="mb-2">
                                    Description
                                </div>
                                <div class="mb-4">
                                    <input type="text" class="form-control" v-model="businessDesc">
                                </div>
                            </div>
                            <div>
                                <div class="mb-2">
                                    Country
                                </div>
                                <div class="mb-4">
                                    <div class="input-group">
                                        <select class="form-select" id="countrySelect" v-model="businessCountry" style="border-color: black;">
                                            <option v-for="country in countries" :key="country" :value="country.originCountry">
                                                {{ country.originCountry }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <div class="mb-2">
                                    Claim Status
                                </div>
                                <div class="mb-4">
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" id="claimed" v-model="businessClaimStatus" value="true" name="claim">
                                        <label class="form-check-label text-start fw-bold" for="claimed">Claimed</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" id="unclaimed" v-model="businessClaimStatus" value="false" name="claim">
                                        <label class="form-check-label text-start fw-bold" for="unclaimed">Unclaimed</label>
                                    </div>
                                </div>
                            </div>
                            <div class="alert alert-danger" role="alert" v-if="addBizError != '' ">{{addBizError}}</div>
                        </div>

                        
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" @click="createBusiness" data-bs-dismiss="modal">Save changes</button>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- add business modal end -->
            </div>
            <!-- add business end -->
            <hr>
            <!-- mod request -->
            <div class="row text-center">
                <div class="col-12">
                    <h3><b>Moderator Request</b></h3>
                </div>
            </div>
            <div>
                <div v-if="pendingModRequests.length > 0" class="row" style="height: 300px; overflow: auto">
                    <div v-for="request in pendingModRequests" class="col-3 pb-4" v-bind:key="request._id">
                        <div class="card h-100" style="background-color: white">
                            <div class="card-body">
                            <ul class="list-group list-group-flush text-start">
                                <li class="list-group-item"><span class="fw-bold">Requested By: </span > <br/>
                                    @<router-link :to="{ path: '/profile/user/' + request.userID.$oid }" style="color: inherit;">
                                        {{ getUserbyID(request.userID).username }}
                                    </router-link> 
                                </li>
                                <li class="list-group-item"><span class="fw-bold">Drink Type: </span> <br/> {{ request.drinkType }} </li>
                                <li class="list-group-item"><span class="fw-bold">Description: </span> <br/> {{ request.modDesc }} </li>
                            </ul>
                            </div>
                            <div class="card-footer">
                                <button class="btn btn-success btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewModRequest(request, 'approve')">Approve</button>
                                <button class="btn btn-danger btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewModRequest(request, 'reject')">Reject</button>
                            </div>
                        </div>
                    </div>
                            
                    
                </div>
                <div v-else>
                    No New Moderator Request
                </div>
            </div>
            <!-- mod request end -->
            <hr>
            <!-- business sign up -->
            <div class="row text-center">
                <div class="col-12">
                    <h3><b>Business Account Request</b></h3>
                </div>
            </div>
            <div>
                <div v-if="pendingAccountRequests.length > 0" class="row" style="height: 525px; overflow: auto">
                    <div v-for="request in pendingAccountRequests" class="col-3 pb-4" v-bind:key="request._id">
                        <div class="card h-100" style="background-color: white">
                            <div class="card-body">
                            <ul class="list-group list-group-flush text-start">
                                <li class="list-group-item"><span class="fw-bold">Type: </span> {{ request.businessType }} </li>
                                <li class="list-group-item"><span class="fw-bold">Name: </span> {{ request.businessName }} </li>
                                <li class="list-group-item"><span class="fw-bold">Description: </span> {{ request.businessDesc }} </li>
                                <li class="list-group-item"><span class="fw-bold">Country: </span> {{ request.country }} </li>
                                <li class="list-group-item"><span class="fw-bold">Site: </span> 
                                    <router-link v-if="request.businessLink" :to="{ path: request.businessLink }" style="color: inherit;">
                                        Link
                                    </router-link> 
                                    <span v-if="!request.businessLink">N/A</span>
                                </li>
                                <li class="list-group-item"><span class="fw-bold">First Name: </span> {{ request.firstName }} </li>
                                <li class="list-group-item"><span class="fw-bold">Last Name: </span> {{ request.lastName }} </li>
                                <li class="list-group-item"><span class="fw-bold">Email: </span> {{ request.email }} </li>
                                <li class="list-group-item"><span class="fw-bold">Relationship: </span> {{ request.relationship }} </li>
                                <li class="list-group-item"><span class="fw-bold">Price Plan: </span> {{ request.pricing }} </li>


                            </ul>
                            </div>
                            <div class="card-footer">
                                <button v-if="checkBusinessExist(request.businessLink)" class="btn btn-success btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'approve')">Approve</button>
                                <button v-else class="btn btn-success btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'add')">Add</button>
                                <button class="btn btn-danger btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'reject')">Reject</button>
                            </div>
                        </div>
                    </div>
                            
                    
                </div>
                <div v-else>
                    No New Business Account Request
                </div>
            </div>
            <!-- business sign up end -->
            
        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import { hashPassword } from '../../../backend/other/hashPassword.js'

        export default {
            name: 'adminDashboard',
            components: {
                NavBar
            },
            data() {
                return {
                    // data from database
                    observationTags: [],
                    modRequests: [],
                    accountRequests: [],
                    producers: [],
                    venues: [],
                    countries: [],

                    editedObservationTags: [],
                    pendingModRequests: [],
                    pendingAccountRequests: [],
                    
                    //User 
                    user: null,
                    users: [],

                    // creation of new observation tag
                    newObservation:'',

                    // Error messages
                    errorMessages:'',

                    // flags
                    dataLoaded: false,
                    loadError: false,
                    editingObservation:false,
                    addingObservation:false,
                    selectingObservation:true,
                    nothingChanged:false,
                    successUpdateObservation:false,
                    invalidTag:false,
                    errorMessage:false,
                    errorUpdateObservation:false,
                    updatingObservation:false,
                    duplicateTag:false,
                    successCreateObservation:false,
                    submittingObservation:false,
                    errorCreateObservation:false,

                    // Logged in user details
                    userID: null,
                    userType: localStorage.getItem('88B_accType'),

                    // create business
                    businessType: "",
                    businessName: "",
                    businessDesc: "",
                    businessCountry: "",
                    businessClaimStatus: "",
                    addBizError: "",
                    tempPassword: "",

                }
            },
            mounted() {
                // Check if user is logged in
                this.userID = localStorage.getItem('88B_accID');

                if (this.userID == null) {
                    this.$router.push('/login');
                }
                else {
                    this.loadData();
                }
            },
            methods: {
                async loadData(){

                    // Check if admin, if not reroute to home page
                    // users
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                        this.users = response.data;
                        if (this.userType == "user") {
                            this.user = this.users.find(user => user["_id"]["$oid"] == this.userID);
                            if(!this.user.isAdmin){
                                this.$router.push('/');
                            }
                        }else{
                            this.$router.push('/');
                        }
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // observation tags
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getObservationTags');
                        this.observationTags = response.data;
                        this.editedObservationTags = JSON.parse(JSON.stringify(response.data));
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // mod requests
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                        this.modRequests = response.data;
                        this.pendingModRequests = this.modRequests.filter(request => request.reviewStatus);
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // account requests
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getAccountRequests');
                        this.accountRequests = response.data;
                        this.pendingAccountRequests = this.accountRequests.filter(request => request.reviewStatus);
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // producer
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
                        // check for producer with no producer name and retrieve id
                        for (let i = 0; i < this.producers.length; i++) {
                            if (!this.producers[i].producerName) {
                                console.log("no name");
                                console.log(this.producers[i]._id.$oid);
                            }
                        }
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // venues
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                        this.venues = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // countries
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                        this.countries = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }

                    this.dataLoaded = true;
                },

                addObservation(){
                    this.addingObservation=true
                    this.editingObservation=false
                    this.selectingObservation=false
                },

                editObservation(){
                    this.addingObservation=false
                    this.editingObservation=true
                    this.selectingObservation=false
                },

                resetObservation(){
                    this.editingObservation=false
                    this.addingObservation=false
                    this.selectingObservation=true
                    this.updatingObservation = false
                    this.resetErrors()
                },

                updateObservation(){
                    this.nothingChanged=false
                    let submitData = []
                    // Check if theres a change in observationTag, if there is, submit the data
                    for( let i=0;i<this.editedObservationTags.length;i++){
                        if(this.editedObservationTags[i].observationTag!= this.observationTags[i].observationTag){
                            submitData.push(this.editedObservationTags[i])
                            this.observationTags[i].observationTag = this.editedObservationTags[i].observationTag
                        }
                    }
                    if(submitData.length<=0){
                        let randoVariable = this.editedObservationTags[0].observationTag
                        this.editedObservationTags[0].observationTag="a"
                        this.editedObservationTags[0].observationTag= randoVariable
                        this.nothingChanged = true
                        return null
                    }
                    this.editingObservation=false;
                    this.updatingObservation = true;
                    if(this.observationTags.find((tag)=> tag.observationTag == '')){
                        this.emptyObservation = true
                    }
                    let submitAPI = "http://127.0.0.1:5051/updateObservationTag"
                    this.updateTags(submitAPI,submitData)
                },

                async updateTags(submitAPI,submitData){
                    let responseCode = ''
                    const response = await this.$axios.put(submitAPI, submitData)
                    .then((response)=>{
                        responseCode = response.data.code
                    })
                    .catch((error)=>{
                        console.error(error);
                        responseCode = error.response.data.code
                        this.errorMessages+=error.response.data.message
                    });
                    this.updatingObservation = false
                    if(responseCode==201){
                        this.successUpdateObservation=true; // Display success message
                    }else{
                        this.errorUpdateObservation = true
                        if(responseCode==400){
                            this.invalidTag = true // Display duplicate entry message
                        }else{
                            this.errorMessage = true // Display generic error message
                        }
                    }
                    return response
                },

                resetErrors(){
                    this.successUpdateObservation = false
                    this.errorUpdateObservation = false
                    this.invalidTag = false
                    this.errorMessage = false
                    this.successCreateObservation = false
                    this.errorCreateObservation = false
                    this.duplicateTagTag = false
                    this.errorMessage = false
                    this.selectingObservation = true
                },

                createNewObservation(){
                    if(this.newObservation==""){
                        alert('Please fill in the observation tag')
                        return null
                    }
                    this.submittingObservation=true
                    this.addingObservation=false
                    let submitAPI = "http://127.0.0.1:5052/createObservationTag"
                    let submitData = {"observationTag":this.newObservation}
                    this.createTag(submitAPI, submitData)
                },

                async createTag(submitAPI, submitData){
                    let responseCode = ''
                    const response = await this.$axios.post(submitAPI, submitData)
                    .then((response)=>{
                        responseCode = response.data.code
                    })
                    .catch((error)=>{
                        console.error(error);
                        responseCode = error.response.data.code
                    });
                    this.submittingObservation = false
                    if(responseCode==201){
                        this.successCreateObservation=true; // Display success message
                    }else{
                        this.errorCreateObservation = true
                        if(responseCode==400){
                            this.duplicateTag = true // Display duplicate entry message
                        }else{
                            this.errorMessage = true // Display generic error message
                        }
                    }
                    return response
                }, 
                getUserbyID(userID) {
                    return this.users.find(user => user["_id"]["$oid"] == userID["$oid"]);
                }, 
                async reviewModRequest(request, action) {
                    const requestID = request._id.$oid;
                    // update users db
                    if (action == "approve") {
                        const userID = request.userID.$oid;
                        const newModType = request.drinkType;

                        try {
                            const response = await this.$axios.post('http://127.0.0.1:5100/updateModType', 
                                {
                                    userID: userID,
                                    newModType: newModType,
                                }, {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            });
                            console.log(response.data);
                        } catch (error) {
                            console.error(error);
                        }
                    }
                    
                    // update mod request db
                    try {
                        const response = await this.$axios.post('http://127.0.0.1:5101/updateModRequest', 
                            {
                                requestID: requestID,
                                reviewStatus: false,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                        console.log(response.data);
                    } catch (error) {
                        console.error(error);
                    }
                    
                    // update frontend
                    const index = this.modRequests.findIndex(request => request._id.$oid == requestID);
                    this.modRequests[index].reviewStatus = false;
                    this.pendingModRequests = this.modRequests.filter(request => request.reviewStatus);

                }, 
                checkBusinessExist(businessLink) {
                    if (businessLink) {
                        const businessID = businessLink.split("/").pop()
                        if (this.producers.find(producer => producer._id.$oid == businessID)) {
                            return true;
                        }
                        if (this.venues.find(venue => venue._id.$oid == businessID)) {
                            return true;
                        }
                    }
                    return false;
                },
                async reviewAccountRequest(request, action) {
                    const requestID = request._id.$oid;
                    if (action == "approve") {
                        const newBusinessData = {
                            businessName: request.businessName,
                            businessDesc: request.businessDesc,
                            country: request.country,
                            claimStatus: true,
                        }
                        const businessID = request.businessLink.split("/").pop()
                        // producers
                        if (request.businessType == "producer") {
                            try {
                                const response = await this.$axios.post('http://127.0.0.1:5200/updateProducerStatus', 
                                    {
                                        businessID: businessID,
                                        newBusinessData: newBusinessData,
                                    }, {
                                    headers: {
                                        'Content-Type': 'application/json'
                                    }
                                });
                                console.log(response.data);
                            } catch (error) {
                                console.error(error);
                            }
                        }
                        // venues 
                        else if (request.businessType == "venue") {
                            try {
                                const response = await this.$axios.post('http://127.0.0.1:5300/updateVenueStatus', 
                                    {
                                        businessID: businessID,
                                        newBusinessData: newBusinessData,
                                    }, {
                                    headers: {
                                        'Content-Type': 'application/json'
                                    }
                                });
                                console.log(response.data);
                            } catch (error) {
                                console.error(error);
                            }
                        }
                    }
                    if (action == "add") {
                        this.businessType = request.businessType;
                        this.businessName = request.businessName;
                        this.businessDesc = request.businessDesc;
                        this.businessCountry = request.country;
                        this.businessClaimStatus = "true";
                        this.createBusiness();
                    }

                    // update review status
                    try {
                        const response = await this.$axios.post('http://127.0.0.1:5031/updateAccountRequest', 
                            {
                                requestID: requestID,
                                reviewStatus: false,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                        console.log(response.data);
                    } catch (error) {
                        console.error(error);
                    }

                    // update frontend
                    const index = this.accountRequests.findIndex(request => request._id.$oid == requestID);
                    this.accountRequests[index].reviewStatus = false;
                    this.pendingAccountRequests = this.accountRequests.filter(request => request.reviewStatus);

                }, 
                async createBusiness() {

                    // form control
                    if (this.businessType == "" || this.businessName == "" || this.businessDesc == "" || this.businessCountry == "" || this.businessClaimStatus == "") {
                        this.addBizError = "Please fill in all fields";
                    }
                    else {
                        this.addBizError = "";
                        this.tempPassword = hashPassword(this.businessName).toString();
                        this.tempPassword = this.tempPassword.replace(/-/g, '');
                        const hashedPassword = hashPassword(this.businessName, this.tempPassword);
                        if (this.businessType == "producer") {
                            const newBusinessData = {
                                producerName: this.businessName,
                                producerDesc: this.businessDesc,
                                originCountry: this.businessCountry,
                                statusOB: "",
                                mainDrinks: [],
                                photo: "",
                                hashedPassword: hashedPassword,
                                questionsAnswers: [],
                                updates: [],
                                producerLink: "",
                                claimStatus: this.businessClaimStatus === "true",
                            }
                            console.log(newBusinessData);
                            try {
                                const response = await this.$axios.post('http://127.0.0.1:5031/createProducerAccount', 
                                    {
                                        newBusinessData
                                    }, {
                                    headers: {
                                        'Content-Type': 'application/json'
                                    }
                                });
                                console.log(response.data);
                            } catch (error) {
                                console.error(error);
                            }
                            alert("Producer account created successfully. Please save login details. \nProducer account: " + this.businessName + "\nTemporary password: " + this.tempPassword);
                        }

                        // reset form details
                        this.businessType = "";
                        this.businessName = "";
                        this.businessDesc = "";
                        this.businessCountry = "";
                        this.businessClaimStatus = "";

                    }
                }
            }
        }
</script>