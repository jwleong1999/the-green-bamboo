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
                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="What are you drinking today?" style="height: 50px;" v-model="searchInput" v-on:keyup.enter="helperSearch"> 
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
    <div class="collapse" id="navbarToggleExternalContent"> <!-- TODO: modify links accordingly -->
        <div class="row pt-2">
            <div class="col-7"></div>
            <!-- [specific] for different accounts -->
            <div class="col-2 navbar-dropdown text-end">
                <!-- Users -->
                <div class="p-4" id="Users">
                    <h3> Users </h3>
                    <!-- TODO: link to the user's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the user's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Drink Stats </h5>
                    </a>
                    <!-- TODO: link to lists -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Bookmarked Drinks </h5>
                    </a>
                </div>

                <!-- Venues -->
                <div class="p-4" id="Venues">
                    <h3> Venues </h3>
                    <!-- TODO: link to the venue's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the venues's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Dashboard </h5>
                    </a>
                    <!-- TODO: link to edit menu page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Menu </h5>
                    </a>
                </div>

                <!-- Producers -->
                <div class="p-4" id="Producers">
                    <h3> Producers </h3>
                    <!-- TODO: link to the producers's profile page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> View Profile </h5>
                    </a>
                    <!-- TODO: link to the producer's dashboard -->
                    <a href="" class="default-clickable-text"> 
                        <h5> My Dashboard </h5>
                    </a>
                    <!-- TODO: link to new listings page -->
                    <a href="" class="default-clickable-text"> 
                        <h5> Add a New Listing </h5>
                    </a>
                </div>

                <!-- [common] for all accounts -->
                <a href="www.88bamboo.co" class="primary-clickable-text">
                    <h4> 
                        Read & Learn
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                        </svg>
                    </h4>
                </a>
            </div>
            <div class="col-3"></div>
        </div>
    </div>

    <!-- main content -->

    <div class="container pt-5">
        <div class="row">
            <!-- producer information -->
            <div class="col-9 no-margin">
                <!-- header -->
                <div class="row">
                    <!-- image -->
                    <div class="col-3 image-container">
                        <img src="../../../Images/Drinks/Placeholder.png" style="width: 200px; height: 200px;" class="img-border">
                    </div>
                    <!-- details -->
                    <div class="col-9 text-start">
                        <div class="container text-start">
                            <!-- drink category -->
                            <div class="row">
                                <div class="col">
                                    <h5 class="text-body-secondary fst-italic"> {{ specified_listing["drinkType"] }} </h5>
                                </div>
                            </div>
                            <!-- expression name -->
                            <div class="row">
                                <div class="col-9">
                                    <h3 class="text-body-secondary"> <b> {{ specified_listing["listingName"] }} </b> </h3>
                                </div>
                                <!-- suggest edit & report duplicate -->
                                <div class="col-3">
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic"> Suggest Edit </p>
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic"> Report Duplicate </p>
                                </div>
                            </div>
                            <!-- producer & bottler -->
                            <div class="row">
                                <!-- producer -->
                                <div class="col-5">
                                    <h5 class="text-body-secondary"> <u> {{ getProducerName(specified_listing["producerID"]) }} </u> </h5>
                                </div>
                                <!-- bottler -->
                                <div class="col-4">
                                    <h5 class="text-body-secondary"> Bottler: <u> {{ specified_listing["bottler"] }} </u>  </h5>
                                </div>
                            </div>
                            <!-- description -->
                            <div class="row">
                                <div class="col">
                                    <div class="py-2"></div>
                                    <p> {{ specified_listing["officialDesc"] }} </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- more information (category, age, country of origin, abv, list buttons & bookmark)-->
                <div class="row pt-4">
                    <div class="col-7">
                        <div class="row">
                            <!-- category -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Category </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["typeCategory"] }} </b> </h5>
                            </div>
                            <!-- age --> 
                            <div class="col-2 text-start">
                                <!-- for wine listings -->
                                <div v-if="specified_listing['drinkType'] == 'Wine'">
                                    <p class="mb-2"> <u> Vintage </u> </p> <!-- to change this to calculate the age -->
                                    <h5 class="text-body-secondary"> <b>  {{ specified_listing["age"] }} </b> </h5>
                                </div>
                                <!-- for all other listings  -->
                                <div v-else>
                                    <p class="mb-2"> <u> Age </u> </p> 
                                    <h5 class="text-body-secondary"> <b>  {{ specified_listing["age"] }} </b> </h5>
                                </div>
                            </div>
                            <!-- country of origin -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Country of Origin </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["originCountry"] }} </b> </h5>
                            </div>
                            <!-- abv -->
                            <div class="col-2 text-start">
                                <p class="mb-1"> <u> ABV </u> </p>
                                <h5 class="text-body-secondary"> <b> {{ specified_listing["abv"] }} </b> </h5>
                            </div>
                        </div>
                    </div>
                    <!-- have tried button -->
                    <div class="col-2 pe-0">
                        <div v-html="checkDrinkLists(specified_listing).buttons.haveTried" class="d-grid"> </div>
                    </div>
                    <!-- want to try button -->
                    <div class="col-2 ps-0">
                        <div v-html="checkDrinkLists(specified_listing).buttons.wantToTry" class="d-grid"> </div>
                    </div>
                    <!-- bookmark button -->
                    <div class="col-1 text-end">
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16">
                            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                        </svg>
                    </div>
                </div>

                <!-- more information (average rating, would recommend, would drink again) -->
                <div class="row pt-3">
                    <div class="col-7">
                        <div class="row">
                            <!-- average rating -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Average Rating </u> </p>
                                <h5 class="text-body-secondary rating-text">
                                    {{ getRatings(specified_listing) }}
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </h5>
                            </div>
                            <!-- would recommend -->
                            <div class="col-4 text-start">
                                <p class="mb-2"> <u> Would Recommend </u> </p>
                                <h5 class="text-body-secondary rating-text"> <b> 88% </b> </h5>
                            </div>
                            <!-- would drink again -->
                            <div class="col-4 text-start">
                                    <p class="mb-2"> <u> Would Drink Again </u> </p>
                                    <h5 class="text-body-secondary rating-text"> <b> 83% </b> </h5>
                            </div>
                        </div>
                    </div>

                    <!-- add your review -->
                    <div class="col-5">
                        <div class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg" data-bs-toggle="modal" data-bs-target="#reviewModal"> 
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                </svg>
                                Add Your Review
                            </button>
                        </div>
                    </div>
                </div>
                    <!-- Modal -->
                    <div class="modal fade" id="reviewModal" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true" data-bs-backdrop="static">
                        <div class="modal-dialog modal-lg">
                            <div class="modal-content">
                                <!-- change modal header colour -->
                                <div class="modal-header" style="background-color: #0480be">
                                    <h5 class="modal-title" id="reviewModalLabel">Modal title</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <!-- This is where  -->
                                <div class="modal-body">
                                    <div class="container-fluid">
                                        <div class = 'row justify-content-start'>
                                            <div class="col-md-3"> 
                                                <p>Language</p>
                                                <div class="input-group">                                                    
                                                    <select class="form-select" id="inputGroupSelect01">
                                                        <!-- Add in the languages here -->
                                                        <option selected>ninabei</option>
                                                        <option selected>konichiwa</option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>
                                        <div class = 'row justify-content-start'>
                                            <div class = "col-md-9">
                                                <p>Review <span class="text-danger">*</span></p>
                                                <textarea class="form-control" id="reviewTextarea" rows="3" placeholder="Min 20 characters"></textarea>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-primary">Submit Review</button>
                                </div>
                            </div>
                        </div>
                    </div>


                <hr>

                <!-- photos posted by other users -->
                <div class="row text-start">
                    <div class="col">
                        <div class="d-flex justify-content-start">
                            <!-- add new photo -->
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded" v-on:click="addPhoto">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="75" height="75" fill="currentColor" class="bi bi-plus-lg" viewBox="0 0 16 16">
                                        <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
                                    </svg>
                                </div>
                            </div>
                            <!-- display other photos -->
                            <!-- [TODO] THIS FOLLOWING PART IS HARDCODED FOR NOW (FOR UI SAKE), need to loop thru db to get the photos and display here -->
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                            <div class="add-review-photo-container">
                                <div class="add-review-photo-background centered rounded">
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <hr>

                <!-- reviews -->
                <div>
                    <div class="row" v-for="review in getReviewsForListing(specified_listing)" v-bind:key="review._id">
                        <!-- profile photo -->
                        <div class="col-1">
                            <img :src=" 'data:image/jpeg;base64,' + (getPhotoFromReview(review) || defaultProfilePhoto)" alt="" class="profile-image">
                        </div>
                        <!-- user reviews -->
                        <div class="col-10">
                            <div class="row">
                                {{ getUsernameFromReview(review) }}
                            </div>
                        </div>

                        <!-- review photo -->
                        <div class="col-2">

                        </div>
                    </div>
                </div>

                <hr>

                
            </div> <!-- end of producer information -->
            
            <!-- where to try & 88 bamboo's review -->
            <div class="col-3">
                <div class="row">
                    <!-- where to try -->
                    <div class="col-12">
                        <div class="square primary-square rounded p-3 mb-3">
                            <!-- header text -->
                            <div class="square-inline">
                                <h4 class="square-inline-text-start mr-auto"> Where to Buy </h4>
                            </div>
                            <!-- body -->
                            <div class="text-start pt-2"> <!-- TODO: add hyperlink to link to producer page-->
                                <!-- [function] where to buy -->
                                <div v-for="producer in producerListings" v-bind:key="producer._id">
                                    <p class="no-margin"> {{ getProducerName(producer) }} </p>
                                </div>
                            </div>
                            <div class="py-5"></div>
                        </div>
                    </div>
                    <!-- 88 bamboo's review -->
                    <div class="col-12">
                        <div class="square secondary-square rounded p-3 mb-3">
                            <!-- header text -->
                            <div class="square-inline">
                                <h4 class="square-inline-text-start mr-auto"> 88 Bamboo's Review </h4>
                            </div>
                            <div class="py-2 text-start">
                                <a :href="specified_listing['reviewLink']" class="text-left default-text-no-background">
                                    {{ specified_listing['reviewLink'] }}
                                </a>
                            </div>
                            <div class="py-5">
                                <!-- TODO: where to try function -->
                            </div>
                            <div class="py-2"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- end of your drinks shelf & brands you follow -->

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    export default {
        data() {
            return {
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                venuesAPI: [],
                drinkTypes: [],
                requestListings: [],
                requestEdits: [],
                modRequests: [],

                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                // specified listing
                listing_id: null,
                specified_listing: {},
                // where to buy
                producerListings: [],

                // customization for drinkLists buttons
                // [TODO] get drink list of user, for now is hardcoded
                drinkList:  {
                                "haveTried": ["Harmony Collection Inspired by Intense Arabica"],
                                "wantToTry": ["Catnip Gin No. 2", "Five Farms Irish Cream Liqueur"]
                            },
                haveTried: false,
                wantToTry: false,

                // matched user
                matchedUser: {},

                defaultProfilePhoto: "/9j/4AAQSkZJRgABAQEASABIAAD/4Qm+aHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA0LjQuMC1FeGl2MiI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+IDxkYzpjcmVhdG9yPiA8cmRmOlNlcT4gPHJkZjpsaT5WZWN0b3JTdG9jay5jb20vNDI0MTE1NDA8L3JkZjpsaT4gPC9yZGY6U2VxPiA8L2RjOmNyZWF0b3I+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDw/eHBhY2tldCBlbmQ9InciPz7/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAD6APkDAREAAhEBAxEB/8QAHAABAAIDAQEBAAAAAAAAAAAAAAMGBAUH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",

            };
        },
        mounted() {
            this.created()
            this.loadData();
        },
        methods: {
            // fetch specific listing data
            async created() {
                // Get the query string parameters (listing ID) from the URL
                const urlParams = new URLSearchParams(window.location.search);
                this.listing_id = urlParams.get('id');
            },

            // load data from database
            async loadData() {
                // countries
                // _id, originCountry
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                        this.countries = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.listings = response.data;
                        this.filteredListings = this.listings; // originally, make filtered listings the entire collection of listings
                        this.specified_listing = this.listings.find(listing => listing._id.$oid == this.listing_id); // find specified listing
                        this.whereToBuy(); // find where to buy specified listing
                        this.getReviewsForListing(this.specified_listing);
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.producers = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // reviews
                // _id, userID, reviewTarget, date, rating, reviewDesc, taggedUsers, reviewTitle, reviewType, flavorTag, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                        this.reviews = response.data;
                    }
                    catch (error) {
                        console.error(error);
                    }
                // users
                // _id, username, displayName, choiceDrinks, drinkLists, modType, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                        this.users = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // venues
                // _id, venueName, venueDesc, origin
                // Country, address, openingHours
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                        this.venues = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getVenuesAPI');
                        this.venuesAPI = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // drinkTypes
                // _id, drinkType, typeCategory
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                        this.drinkTypes = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // requestListings
                // _id, listingName, producerNew, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, sourceLink, brandRelation, reviewStatus, userID, photo
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                            this.requestListings = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                            this.requestEdits = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
                // modRequests
                // _id, userID, drinkType, modDesc
                    try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                            this.modRequests = response.data;
                        } 
                    catch (error) {
                        console.error(error);
                    }
            },

            // view which producers have specified listing
            whereToBuy() {
                this.producerListings = this.listings
                    .filter(listing => listing["listingName"] == this.specified_listing["listingName"])
                    .map(listing => listing["producerID"]);
            },

            // get producerName for a listing based on producerID
            getProducerName(producerID) {
                const producer = this.producers.find((producer) => {
                    return producer["_id"]["$oid"] == producerID["$oid"];
                });
                // ensures that producer is found before accessing "producerName"
                if (producer) {
                    const producerName = producer["producerName"];
                    return producerName;
                }
                else {
                    return null;
                }
            },

            // check if user has already added listing to shelf, add colour to button accordingly
            checkDrinkLists(listing) {
                const haveTried = this.drinkList.haveTried.includes(listing.listingName);
                const wantToTry = this.drinkList.wantToTry.includes(listing.listingName);

                const haveTriedButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${haveTried ? 'disabled' : ''}">
                    Have tried
                </button>
                `;

                const wantToTryButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${wantToTry ? 'disabled' : ''}">
                    Want to try
                </button>
                `;

                return {
                    buttons: {
                        haveTried: haveTriedButton,
                        wantToTry: wantToTryButton,
                    }
                }
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
                return averageRating;
            },

            // add user's uploaded photo to database (TO BE IMPLEMENTED)
            addPhoto() {
                alert("This feature is not yet implemented.");
            },

            getReviewsForListing(listing) {
                const reviews = this.reviews.filter((review) => {
                    return review["reviewTarget"] == listing["listingName"];
                });
                return reviews;
            },

            getUsernameFromReview(review) {
                const user = this.users.find((user) => {
                    return user["_id"]["$oid"] == review["userID"]["$oid"];
                });
                if (user) {
                    return user["username"];
                }
            },

            getPhotoFromReview(review) {
                const user = this.users.find((user) => {
                    return user["_id"]["$oid"] == review["userID"]["$oid"];
                });
                if (user) {
                    return user["photo"];
                }
            }
        }
    };
</script>