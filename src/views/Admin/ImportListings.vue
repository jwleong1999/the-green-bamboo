<!-- Admin can access this page to handle admin controls. -->

<template>
    <NavBar />
    <div v-if="!importSuccess" class="container mt-5 mb-5">

            
            
            <div>
                <div class="form-group mb-2" >
                    <h1>Bulk Import Listings</h1>

                    <h3 class="mt-5"> 
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                            <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"/>
                            <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z"/>
                        </svg>
                        Download Listings Import Template 
                    </h3>
                    <button type="button" class="btn secondary-btn-less-round"  v-on:click="downloadCSV()"> Download Template </button>

                    <h3 class="mt-5"> 
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-upload" viewBox="0 0 16 16">
                            <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"/>
                            <path d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z"/>
                        </svg>
                        Upload Listings CSV File 
                    </h3>
                    <div class="row align-items-center my-3">
                        <div class="col-3"></div>
                        <div class="col-6"> 
                            <input type="file" name="file" id="csvFile" accept=".csv" @change="handleFileUpload" class="form-control">
                        </div>
                        <div class="col-3"></div>
                    </div>

                    <button v-if="csvFile" type="button" class="btn primary-btn-less-round" @click="importCSV">Import</button>
                    <button v-else type="button" class="btn primary-btn-less-round" @click="importCSV" disabled>Import</button>

                    
                </div>

                <!-- TO CHECK -->
            </div>
        </div>

        <div v-else class="container mt-5 mb-5">

            <h1 class="text-success">Import Success</h1>

            <button type="button" class="btn primary-btn-less-round me-2" @click="moreImports">Import more listings</button>

            <router-link :to="'/'" class="btn secondary-btn-less-round ms-2" @click="importCSV" disabled>
                Back to home
            </router-link>


        </div>

        

</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    // import { hashPassword } from '../../../backend/other/hashPassword.js'

        export default {
            name: 'adminDashboard',
            components: {
                NavBar
            },
            data() {
                return {

                    // csv data
                    fileFormat: [],
                    csvData: [],

                    // TO DELETE IF NOT NEEDED

                    // // data from database
                    // observationTags: [],
                    // modRequests: [],
                    // accountRequests: [],
                    // producers: [],
                    // venues: [],
                    // countries: [],

                    // editedObservationTags: [],
                    // pendingModRequests: [],
                    // pendingAccountRequests: [],
                    
                    // //User 
                    // user: null,
                    // users: [],

                    // // creation of new observation tag
                    // newObservation:'',

                    // // Error messages
                    // errorMessages:'',

                    // // flags
                    // dataLoaded: false,
                    // loadError: false,
                    // editingObservation:false,
                    // addingObservation:false,
                    // selectingObservation:true,
                    // nothingChanged:false,
                    // successUpdateObservation:false,
                    // invalidTag:false,
                    // errorMessage:false,
                    // errorUpdateObservation:false,
                    // updatingObservation:false,
                    // duplicateTag:false,
                    // successCreateObservation:false,
                    // submittingObservation:false,
                    // errorCreateObservation:false,

                    // // create business
                    // businessType: "",
                    // businessName: "",
                    // businessDesc: "",
                    // businessCountry: "",
                    // businessClaimStatus: "",
                    // addBizError: "",
                    // tempPassword: "",


                    // Logged in user details
                    userID: null,
                    userType: localStorage.getItem('88B_accType'),

                    
                    // csv file import
                    csvFile: null,
                    importSuccess: false,
                    responseCode :0,

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

                    // csv
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5052/readCSV');
                        this.fileFormat = response.data.data;
                        console.log(this.fileFormat);
                        this.convertToCSV();
                    }
                    catch (error) {
                        console.error(error);
                    }

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

                // TO DELETE IF NOT NEEDED

                // addObservation(){
                //     this.addingObservation=true
                //     this.editingObservation=false
                //     this.selectingObservation=false
                // },

                // editObservation(){
                //     this.addingObservation=false
                //     this.editingObservation=true
                //     this.selectingObservation=false
                // },

                // resetObservation(){
                //     this.editingObservation=false
                //     this.addingObservation=false
                //     this.selectingObservation=true
                //     this.updatingObservation = false
                //     this.resetErrors()
                // },

                // updateObservation(){
                //     this.nothingChanged=false
                //     let submitData = []
                //     // Check if theres a change in observationTag, if there is, submit the data
                //     for( let i=0;i<this.editedObservationTags.length;i++){
                //         if(this.editedObservationTags[i].observationTag!= this.observationTags[i].observationTag){
                //             submitData.push(this.editedObservationTags[i])
                //             this.observationTags[i].observationTag = this.editedObservationTags[i].observationTag
                //         }
                //     }
                //     if(submitData.length<=0){
                //         let randoVariable = this.editedObservationTags[0].observationTag
                //         this.editedObservationTags[0].observationTag="a"
                //         this.editedObservationTags[0].observationTag= randoVariable
                //         this.nothingChanged = true
                //         return null
                //     }
                //     this.editingObservation=false;
                //     this.updatingObservation = true;
                //     if(this.observationTags.find((tag)=> tag.observationTag == '')){
                //         this.emptyObservation = true
                //     }
                //     let submitAPI = "http://127.0.0.1:5051/updateObservationTag"
                //     this.updateTags(submitAPI,submitData)
                // },

                // async updateTags(submitAPI,submitData){
                //     let responseCode = ''
                //     const response = await this.$axios.put(submitAPI, submitData)
                //     .then((response)=>{
                //         responseCode = response.data.code
                //     })
                //     .catch((error)=>{
                //         console.error(error);
                //         responseCode = error.response.data.code
                //         this.errorMessages+=error.response.data.message
                //     });
                //     this.updatingObservation = false
                //     if(responseCode==201){
                //         this.successUpdateObservation=true; // Display success message
                //     }else{
                //         this.errorUpdateObservation = true
                //         if(responseCode==400){
                //             this.invalidTag = true // Display duplicate entry message
                //         }else{
                //             this.errorMessage = true // Display generic error message
                //         }
                //     }
                //     return response
                // },

                // resetErrors(){
                //     this.successUpdateObservation = false
                //     this.errorUpdateObservation = false
                //     this.invalidTag = false
                //     this.errorMessage = false
                //     this.successCreateObservation = false
                //     this.errorCreateObservation = false
                //     this.duplicateTagTag = false
                //     this.errorMessage = false
                //     this.selectingObservation = true
                // },

                // createNewObservation(){
                //     if(this.newObservation==""){
                //         alert('Please fill in the observation tag')
                //         return null
                //     }
                //     this.submittingObservation=true
                //     this.addingObservation=false
                //     let submitAPI = "http://127.0.0.1:5052/createObservationTag"
                //     let submitData = {"observationTag":this.newObservation}
                //     this.createTag(submitAPI, submitData)
                // },

                // async createTag(submitAPI, submitData){
                //     let responseCode = ''
                //     const response = await this.$axios.post(submitAPI, submitData)
                //     .then((response)=>{
                //         responseCode = response.data.code
                //     })
                //     .catch((error)=>{
                //         console.error(error);
                //         responseCode = error.response.data.code
                //     });
                //     this.submittingObservation = false
                //     if(responseCode==201){
                //         this.successCreateObservation=true; // Display success message
                //     }else{
                //         this.errorCreateObservation = true
                //         if(responseCode==400){
                //             this.duplicateTag = true // Display duplicate entry message
                //         }else{
                //             this.errorMessage = true // Display generic error message
                //         }
                //     }
                //     return response
                // }, 
                // getUserbyID(userID) {
                //     return this.users.find(user => user["_id"]["$oid"] == userID["$oid"]);
                // }, 
                // async reviewModRequest(request, action) {
                //     const requestID = request._id.$oid;
                //     // update users db
                //     if (action == "approve") {
                //         const userID = request.userID.$oid;
                //         const newModType = request.drinkType;

                //         try {
                //             const response = await this.$axios.post('http://127.0.0.1:5100/updateModType', 
                //                 {
                //                     userID: userID,
                //                     newModType: newModType,
                //                 }, {
                //                 headers: {
                //                     'Content-Type': 'application/json'
                //                 }
                //             });
                //             console.log(response.data);
                //         } catch (error) {
                //             console.error(error);
                //         }
                //     }
                    
                //     // update mod request db
                //     try {
                //         const response = await this.$axios.post('http://127.0.0.1:5101/updateModRequest', 
                //             {
                //                 requestID: requestID,
                //                 reviewStatus: false,
                //             }, {
                //             headers: {
                //                 'Content-Type': 'application/json'
                //             }
                //         });
                //         console.log(response.data);
                //     } catch (error) {
                //         console.error(error);
                //     }
                    
                //     // update frontend
                //     const index = this.modRequests.findIndex(request => request._id.$oid == requestID);
                //     this.modRequests[index].reviewStatus = false;
                //     this.pendingModRequests = this.modRequests.filter(request => request.reviewStatus);

                // }, 
                // checkBusinessExist(businessLink) {
                //     if (businessLink) {
                //         const businessID = businessLink.split("/").pop()
                //         if (this.producers.find(producer => producer._id.$oid == businessID)) {
                //             return true;
                //         }
                //         if (this.venues.find(venue => venue._id.$oid == businessID)) {
                //             return true;
                //         }
                //     }
                //     return false;
                // },
                // async reviewAccountRequest(request, action) {
                //     const requestID = request._id.$oid;
                //     if (action == "approve") {
                //         const newBusinessData = {
                //             businessName: request.businessName,
                //             businessDesc: request.businessDesc,
                //             country: request.country,
                //             claimStatus: true,
                //         }
                //         const businessID = request.businessLink.split("/").pop()
                //         // producers
                //         if (request.businessType == "producer") {
                //             try {
                //                 const response = await this.$axios.post('http://127.0.0.1:5200/updateProducerStatus', 
                //                     {
                //                         businessID: businessID,
                //                         newBusinessData: newBusinessData,
                //                     }, {
                //                     headers: {
                //                         'Content-Type': 'application/json'
                //                     }
                //                 });
                //                 console.log(response.data);
                //             } catch (error) {
                //                 console.error(error);
                //             }
                //         }
                //         // venues 
                //         else if (request.businessType == "venue") {
                //             try {
                //                 const response = await this.$axios.post('http://127.0.0.1:5300/updateVenueStatus', 
                //                     {
                //                         businessID: businessID,
                //                         newBusinessData: newBusinessData,
                //                     }, {
                //                     headers: {
                //                         'Content-Type': 'application/json'
                //                     }
                //                 });
                //                 console.log(response.data);
                //             } catch (error) {
                //                 console.error(error);
                //             }
                //         }
                //     }
                //     if (action == "add") {
                //         this.businessType = request.businessType;
                //         this.businessName = request.businessName;
                //         this.businessDesc = request.businessDesc;
                //         this.businessCountry = request.country;
                //         this.businessClaimStatus = "true";
                //         this.createBusiness();
                //     }

                //     // update review status
                //     try {
                //         const response = await this.$axios.post('http://127.0.0.1:5031/updateAccountRequest', 
                //             {
                //                 requestID: requestID,
                //                 reviewStatus: false,
                //             }, {
                //             headers: {
                //                 'Content-Type': 'application/json'
                //             }
                //         });
                //         console.log(response.data);
                //     } catch (error) {
                //         console.error(error);
                //     }

                //     // update frontend
                //     const index = this.accountRequests.findIndex(request => request._id.$oid == requestID);
                //     this.accountRequests[index].reviewStatus = false;
                //     this.pendingAccountRequests = this.accountRequests.filter(request => request.reviewStatus);

                // }, 
                // async createBusiness() {

                //     // form control
                //     if (this.businessType == "" || this.businessName == "" || this.businessDesc == "" || this.businessCountry == "" || this.businessClaimStatus == "") {
                //         this.addBizError = "Please fill in all fields";
                //     }
                //     else {
                //         this.addBizError = "";
                //         this.tempPassword = hashPassword(this.businessName).toString();
                //         this.tempPassword = this.tempPassword.replace(/-/g, '');
                //         const hashedPassword = hashPassword(this.businessName, this.tempPassword);
                //         if (this.businessType == "producer") {
                //             const newBusinessData = {
                //                 producerName: this.businessName,
                //                 producerDesc: this.businessDesc,
                //                 originCountry: this.businessCountry,
                //                 statusOB: "",
                //                 mainDrinks: [],
                //                 photo: "",
                //                 hashedPassword: hashedPassword,
                //                 questionsAnswers: [],
                //                 updates: [],
                //                 producerLink: "",
                //                 claimStatus: this.businessClaimStatus === "true",
                //             }
                //             console.log(newBusinessData);
                //             try {
                //                 const response = await this.$axios.post('http://127.0.0.1:5031/createProducerAccount', 
                //                     {
                //                         newBusinessData
                //                     }, {
                //                     headers: {
                //                         'Content-Type': 'application/json'
                //                     }
                //                 });
                //                 console.log(response.data);
                //             } catch (error) {
                //                 console.error(error);
                //             }
                //             alert("Producer account created successfully. Please save login details. \nProducer account: " + this.businessName + "\nTemporary password: " + this.tempPassword);
                //         }

                //         // reset form details
                //         this.businessType = "";
                //         this.businessName = "";
                //         this.businessDesc = "";
                //         this.businessCountry = "";
                //         this.businessClaimStatus = "";

                //     }
                // },

                // To recognise which csv file is to be imported
                async handleFileUpload(event) {
                    this.csvFile = event.target.files[0];
                    console.log(this.csvFile);
                },


                // Calling of backend to import csv file
                async importCSV() {
                    
                    if (this.csvFile != []) {
                        const formData = new FormData();
                    formData.append('file', this.csvFile);
                    
                    
                        try {
                            const response = await this.$axios.post('http://127.0.0.1:5052/importListings', 
                                formData, {
                                headers: {
                                    'Content-Type': 'multipart/form-data'
                                }
                            })
                            .then((response)=>{
                            this.responseCode = response.data.code
                            if(this.responseCode == 201){
                            this.importSuccess=true; // Display success message
                            }else{
                                this.importSuccess = false
                            }
                            })
                            .catch((error)=>{
                                console.error(error);
                                this.responseCode = error.response.data.code
                                
                            });
                            
                            
                        return response
                        } catch (error) {
                            console.error('Error:', error);
                        }
                        
                        console.log(this.responseCode)
                        console.log(this.importSuccess)
                    }
                },

                // To import more listings
                moreImports(){
                    this.importSuccess = false
                    this.csvFile = []
                },

                convertToCSV() {
                    let keepColumns = this.fileFormat.filter(item => Object.values(item).some(value => value !== ''));
                    console.log(keepColumns)
                    const keys = keepColumns[0];
                    const values = keepColumns[1];

                    let result = values.reduce((acc, value, index) => {
                        acc[keys[index]] = value;
                        return acc;
                    }, {});

                    this.csvData = result
                },

                downloadCSV() {
                    const keys = Object.keys(this.csvData);
                    const values = Object.values(this.csvData);
                    let csvContent = "data:text/csv;charset=utf-8," + keys.join(",") + "\n" + values.join(",");
                    const encodedUri = encodeURI(csvContent);
                    const link = document.createElement("a");
                    link.setAttribute("href", encodedUri);
                    link.setAttribute("download", "listingsFormat.csv");
                    document.body.appendChild(link);
                    link.click();
                }

                
            }
        }
</script>