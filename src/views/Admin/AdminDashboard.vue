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
            <div class="row text-center">
                <div class="col-12">
                    <h3><b>Tag Controls</b></h3>
                </div>
            </div>
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


            <hr>

            
        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';

        export default {
            name: 'adminDashboard',
            components: {
                NavBar
            },
            data() {
                return {
                    // data from database
                    observationTags: [],
                    editedObservationTags: [],
                    
                    //User 
                    user:null,
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
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getObservationTags');
                        this.observationTags = response.data;
                        this.editedObservationTags = JSON.parse(JSON.stringify(response.data));
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
                }
            }
        }
</script>