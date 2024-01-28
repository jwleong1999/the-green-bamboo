<!-- Producers can access this page to view requests of bottle listings that have them specified as the producer. -->
<!-- Admins can access this page to view user-submitted requests of ALL bottle listings. -->
<!-- Moderators can access this page to view user-submitted requests of bottle listings related to their drink type(s). -->

<!-- LAYOUT TEMPORARY, FOCUSING ON FUNCTIONALITY -->

<template>
    <NavBar />
    <!-- Header -->
    <div class="container pt-3">
        
        <!-- Display when data is being loaded -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="!dataLoaded"> 
            <span>Currently loading data, please hold on!</span>
        </div>
        
        <!-- Display when data loading encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="loadError"> 
            <span>An error occurred while loading data, please try refreshing the page!</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="()=>{this.$router.go()}">
                <span class="fs-5 fst-italic"> Refresh Page </span>
            </button>
        </div>

        <!-- Display requests after data loaded -->
        <div class="row" v-if="dataLoaded">

            <!-- start of the elements -->
            <div class="col">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1">View Bottle Listing Requests</p>
                </div>

                <!-- Display requests -->
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">Request</th>
                            <th scope="col">Name</th>
                            <th scope="col">Type</th>
                            <th scope="col">Category</th>
                            <th scope="col">Producer</th>
                            <th scope="col">Bottler</th>
                            <th scope="col">Age</th>
                            <th scope="col">ABV</th>
                            <th scope="col">Country</th>
                            <th scope="col">Source Link</th>
                            <th scope="col">Review Link</th>
                            <th scope="col">Photo</th>
                            <th scope="col">Submitter</th>
                            <th scope="col">Relation</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="requestNew in requestListings" :key="requestNew._id">
                            <td>New</td>
                            <td>{{ requestNew["listingName"] }}</td>
                            <td>{{ requestNew["drinkType"] }}</td>
                            <td>{{ requestNew["typeCategory"] }}</td>
                            <td>{{ findProducer(requestNew) }}</td>
                            <td>{{ requestNew["bottler"] }}</td>
                            <td>{{ requestNew["age"] }}</td>
                            <td>{{ requestNew["abv"] }}</td>
                            <td>{{ requestNew["originCountry"] }}</td>
                            <td>{{ requestNew["sourceLink"] }}</td>
                            <td>{{ requestNew["reviewLink"] }}</td>
                            <td>{{ requestNew["photo"] }}</td>
                            <td>{{ findUser(requestNew) }}</td>
                            <td>{{ requestNew["brandRelation"] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';

        export default {
            name: 'RequestListingNew',
            components: {
                NavBar
            },
            data() {
                return {
                    // data from database
                    listings: [],
                    producers: [],
                    users: [],
                    requestListings: [],
                    requestEdits: [],
                    // flags
                    dataLoaded: false,
                    loadError: false
                }
            },
            mounted() {
                this.loadData();
            },
            methods: {
                // find producer name from producer ID
                findProducer(request) {
                    const producerID = request["producerID"];
                    const producer = this.producers.find((producer) => {
                        return producer["_id"] == producerID;
                    });
                    if (producer == undefined) {
                        return request["producerNew"];
                    }
                    return producer["producerName"];
                },

                // find user name from user ID
                findUser(request) {
                    const userID = request["userID"];
                    const user = this.users.find((user) => {
                        return user["_id"] == userID;
                    });
                    if (user == undefined) {
                        return "(Anonymous)";
                    }
                    return user["username"];
                },

                // load data from database
                async loadData() {
                    // Listings
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // Producers
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // Users
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                        this.users = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // Request Listings
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                        this.requestListings = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }
                    // Request Edits
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                        this.requestEdits = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.loadError = true;
                    }

                    this.dataLoaded = true;
                    console.log(this.listings);
                    console.log(this.producers);
                    console.log(this.users);
                    console.log(this.requestListings);
                    console.log(this.requestEdits);
                }
            }
        }
</script>