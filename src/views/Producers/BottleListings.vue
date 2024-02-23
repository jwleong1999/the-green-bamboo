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
                        <img :src=" 'data:image/jpeg;base64,' + ( defaultProfilePhoto)" style="width: 200px; height: 200px;">
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
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic" @click="this.$router.push(`/Users/request/modify/edit/${this.listing_id}`)"> Suggest Edit </p>
                                    <p class="text-body-secondary no-margin text-decoration-underline fst-italic" @click="this.$router.push(`/Users/request/modify/duplicate/${this.listing_id}`)"> Report Duplicate </p>
                                </div>
                            </div>
                            <!-- producer & bottler -->
                            <div class="row">
                                <!-- producer -->
                                <div class="col-5">
                                    <h5 class="text-body-secondary">
                                        <router-link :to="{ path: '/Producers/Profile-Page/' + this.producer_id }" class="default-text-no-background">
                                            <p> {{ getProducerName(specified_listing["producerID"]) }} </p>
                                        </router-link>
                                    </h5>
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
                    <!-- Display Add review or Review already added accordingly to whether user already left review -->
                    <div v-if="userID !== 'defaultUser'" class="col-5">
                        <div v-if="!inEdit" class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg" data-bs-toggle="modal" data-bs-target="#reviewModal"> 
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                </svg>
                                Add Your Review
                            </button>
                        </div>
                        <div v-else class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg"> 
                                Review already added
                            </button>
                        </div>

                    </div>
                    <div v-else class="col-5">
                        <div class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg"> 
                                Login to leave a Review
                            </button>
                        </div>
                    </div>
                </div>
                    
                    <!-- Modal -->
                    <!-- TODO component for modal <ReviewModal :isEditing='false' :reviewData="reviewData" :showReviewButton="userID.$oid !== 'defaultUser'" /> -->
                    <div v-if="userID !== 'defaultUser'" class="modal fade" id="reviewModal" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true" data-bs-backdrop="static">
                        <div class="modal-dialog modal-lg">
                            <div class="text-success fst-italic fw-bold fs-3 modal-content" v-if='successSubmission'>
                                <span v-if="!inEdit">Your review has successfully been submitted!</span>
                                <span v-else>Your review has successfully been updated!</span>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" @click="reloadRoute" data-bs-dismiss="modal">Close</button>
                                </div>
                            </div>

                            <div class="text-danger fst-italic fw-bold fs-3 modal-content" v-if="errorSubmission"> 
                                <div v-if="errorMessage" class = "row"> 
                                    <span v-if="!inEdit">An error occurred while attempting to submit, please try again!</span>
                                    <span v-else>An error occurred while attempting to update, please try again!</span>
                                    <br>
                                    <button class="btn primary-btn btn-sm" @click="reset">
                                        <span class="fs-5 fst-italic"> Retry your submission here! </span>
                                    </button>
                                </div>
                                <div v-if="duplicateEntry">
                                    <span v-if="!inEdit">You've already submitted a review for this bottle listing!</span>
                                    <span v-else>There is no review for this bottle listing!</span>
                                </div>
                                <br>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                </div>
                            </div>

                            <div v-if='addingReview' class="modal-content">
                                <!-- change modal header colour -->
                                <div class="modal-header" style="background-color: #535C72">
                                    <!-- V-if to edit or add review -->
                                    <h5 v-if="!inEdit" class="modal-title" id="reviewModalLabel" style="color: white;">Add Your Review</h5>
                                    <h5 v-else class="modal-title" id="reviewModalLabel" style="color: white;">Edit Your Review</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>

                                <!-- This is where modal starts for review-->
                                <div class="modal-body">

                                    <div class="row">
                                    <!-- Start of left side elements -->
                                    <div class="col-md-9">                                     
                                        <div class="container-fluid">

                                            <!-- Dropdown for language selection -->
                                            <div class = 'row justify-content-start mb-4'>
                                                <div class="col-md-4"> 
                                                    <p class = 'text-start mb-2 fw-bold'>Language <span class="text-danger">*</span></p>
                                                    <div class="input-group">                                                    
                                                        <select v-model="selectedLanguage" class="form-select" id="inputGroupSelect01">
                                                            <!-- Add in the languages here -->
                                                            <option v-for="language in languages" v-bind:key="language['_id']">{{ language['language'] }}</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- end of dropdown for language selection -->

                                            <!-- Text input are for review -->
                                            <div class = 'row justify-content-start mb-3'>
                                                <div class = "col-md-12">
                                                    <p class='text-start mb-2 fw-bold'>Review <span class="text-danger">*</span></p>
                                                    <textarea v-model="reviewDesc" class="form-control" id="reviewTextarea" rows="3" placeholder="Min 20 characters"></textarea>
                                                </div>
                                                <div v-if="reviewDescError!==''" class ="col-md-12">
                                                    <p class='text-danger text-start mb-2 fw-bold'>{{ reviewDescError }}</p>
                                                </div>
                                            </div>

                                            <!-- Checkboxes for would recommend and would buy again -->
                                            <div class = 'row justify-content-start mb-3 text-start'>
                                                <div class = "col-md-12">
                                                    <div class="form-check form-check-inline">
                                                        <input class="form-check-input" type="checkbox" id="inlineCheckbox1" v-model="wouldRecommend" value="option1">
                                                        <label class="form-check-label text-start fw-bold" for="inlineCheckbox1">Would Recommend</label>
                                                    </div>
                                                    <div class="form-check form-check-inline">
                                                        <input class="form-check-input" type="checkbox" id="inlineCheckbox2" v-model="wouldBuyAgain" value="option2">
                                                        <label class="form-check-label text-start fw-bold" for="inlineCheckbox2">Would Buy Again</label>
                                                    </div>                                                                                                   
                                                </div>                                         
                                            </div>
                                            <!-- End of checkboxes -->

                                            <!-- Buttons to expand -->
                                            <div v-if="!extendReview" class = 'row justify-content-start mb-3 text-start'>
                                                <div class = "col-md-12 text-center">
                                                    <button class="btn primary-btn-less-round btn-sm" @click="controlModal"> 
                                                        Extend Review <span style="color: white;">&#9660;</span>
                                                    </button>                                                                  
                                                </div>                                         
                                            </div>

                                            <!-- Button to collapse -->
                                            <div v-if="extendReview" class = 'row justify-content-start mb-3 text-start'>
                                                <div class = "col-md-12 text-center">
                                                    <button class="btn primary-btn-less-round btn-sm" @click="controlModal"> 
                                                        Condense Review <span style="color: white;">&#9650;</span>
                                                    </button>                                                                  
                                                </div>                                         
                                            </div>
                                            <!-- end of button -->

                                            <!-- Dashed line -->
                                            <div class = 'row justify-content-start mb-1 text-start'>
                                                <div class = "col-md-12 text-center">
                                                    <p class="dotted-line">
                                                    </p>
                                                </div>
                                            </div>
                                            <!-- end of dash line -->


                                            <!-- DONE: Make a colour grid/tables containing all the colour -->
                                            <div v-if="extendReview">
                                                <div class="row">
                                                    <div class="col-md-2">
                                                        <p class="text-start mb-1 fw-bold">Colour:</p>    
                                                    </div>
                                                    <div v-if="selectedColour=== ''" class="col-md-2"></div>
                                                    <div v-else-if="selectedColour.includes('#')" class="col-md-1">
                                                        <button class="btn text-start mb-1" :style="{ 
                                                                        width: '30px', 
                                                                        height: '30px', 
                                                                        backgroundColor: selectedColour, 
                                                                        color: selectedColour, 
                                                                        borderRadius: '0', 
                                                                        borderColor:'grey', 
                                                                        borderWidth:'1px'
                                                                    }"></button>
                                                    </div>
                                                    <div v-else class="col-md-1">
                                                        <button class="btn text-start mb-1" :style="{ width: '30px', height: '30px', borderRadius: '0', borderColor:'grey', borderWidth:'1px', backgroundImage: `linear-gradient(to bottom right, ${specialColours[selectedColour][0]}, ${specialColours[selectedColour][1]}`}"></button>
                                                    </div>
                                                    <div v-if="selectedColour!== ''" class="col-md-4">
                                                        <button @click="clearColour" class="btn text-start mb-1" style="background-color: #535C72;color: white;">Clear Selection</button>
                                                    </div>
                                                </div>                                   
                                                <div class="row justify-content-start mb-1 text-start">
                                                    <div class="col-md-5 mr-0 text-start">
                                                        <div class="row">
                                                            <div class="col">
                                                            <button @click="displaySelectColour(colour)" v-for="(colour, i) in colours.slice(0, 7)" :key="i" :value="colour" class="btn" data-bs-toggle="button"
                                                                    :style="{ 
                                                                        width: '30px', 
                                                                        height: '30px', 
                                                                        backgroundColor: colour, 
                                                                        color: colour, 
                                                                        borderRadius: '0', 
                                                                        borderColor:'grey', 
                                                                        borderWidth:'1px'
                                                                    }">                                
                                                            </button>
                                                            </div>
                                                        </div>
                                                        <div class="row">
                                                            <div class="col">
                                                            <button @click="displaySelectColour(colour)" v-for="(colour, i) in colours.slice(7, 14)" :key="i" :value="colour" class="btn" data-bs-toggle="button" 
                                                                    :style="{ 
                                                                        width: '30px', 
                                                                        height: '30px', 
                                                                        backgroundColor: colour, 
                                                                        color: colour, 
                                                                        borderRadius: '0', 
                                                                        borderColor:'grey', 
                                                                        borderWidth:'1px'
                                                                    }">                                
                                                            </button>
                                                            </div>
                                                        </div>
                                                        </div>

                                                    <!-- Special gradient -->
                                                    <div class="col-md-5 ml-0 text-start">
                                                        <button @click="displaySelectColour(key)" v-for="(value, key) in specialColours" :key="key" type="button" :value="key" class="btn" data-bs-toggle="button" :style="{ width: '30px', height: '30px', borderRadius: '0', borderColor:'grey', borderWidth:'1px', backgroundImage: `linear-gradient(to bottom right, ${value[0]}, ${value[1]}`}">                                
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- END OF COLOURS -->


                                            <!-- Aroma taste and finish inputs -->
                                            <div v-if="extendReview" class="form-group mb-3">
                                                <p class="text-start mb-1 fw-bold">Aroma:</p>
                                                <input v-model="aroma" type="text" class="form-control" id="aroma">
                                            </div>
                                            <div v-if="extendReview" class="form-group mb-3">
                                                <p class="text-start mb-1 fw-bold">Taste:</p>
                                                <input v-model="taste" type="text" class="form-control" id="taste">
                                            </div>
                                            <div v-if="extendReview" class="form-group mb-3">
                                                <p class="text-start mb-1 fw-bold">Finish:</p>
                                                <input v-model="finish" type="text" class="form-control" id="finish">
                                            </div>
                                            <!-- End of armoa taste and finish inputs -->

                                            <!-- Range slider for rating -->
                                            <div class="col-md-5 mb-3"> 
                                                <div class="row align-items-center text-start">
                                                    <label for="customRange2" class="form-label fw-bold">Rating<span class="text-danger">*</span>: {{ rating }}</label>
                                                    <div class="col-auto">
                                                        <label for="customRange" class="form-label fw-bold">1</label>
                                                    </div>
                                                    <div class="col">
                                                        <input v-model="rating" type="range" class="form-range" min="1" max="10" step="0.5" id="customRange">
                                                    </div>
                                                    <div class="col-auto">
                                                        <label for="customRange" class="form-label fw-bold">10</label>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Start of flavour tag -->
                                            <div class="form-group mb-3">
                                                <p class="text-start mb-1 fw-bold">Flavour Tags</p> 

                                                <div class ='container'>
                                                    <button class="btn mb-2 me-2" @click="toggleBox(family)" v-for="family in flavourTags" v-bind:key="family['_id']" :style="{ color:'white', backgroundColor: family['hexcode'], borderColor:family['hexcode'], borderWidth:'1px' }">{{ family['familyTag'] }}</button>
                                                    
                                                    <!-- This is the conatiner/dropdown box for the subtags -->
                                                    <div v-for="family in flavourTags" :key="family['_id']">
                                                        <div v-if="family.showBox" class="rounded p-3" :style="{border: '3px solid ' + family['hexcode'] }">
                                                            <div class="row">
                                                                <div class="col-3" v-for="(element, index) in family.subtag" :key="index">
                                                                    <button @click="toggleFlavourSelection(element, family['hexcode'])" class="btn mb-2" :style="{ width: '100px', height: '60px',color:'white', backgroundColor: selectedFlavourTags.includes(element+family['hexcode']) ? 'grey' :family['hexcode'], borderColor: family['hexcode'], borderWidth:'1px' }">{{ element }}</button>
                                                                </div>                        
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <!-- End of dropdown -->
                                                </div>
                                            </div>
                                            <!-- End of flavour tag -->

                                            <!-- Start of observation tags -->
                                            <!-- Make this a search/dropdown -->
                                            <div class="form-group mb-3">
                                                <p class="text-start mb-1 fw-bold">Observation Tags</p>
                                                <!-- Buttons for the first 8 observations -->
                                                <button v-for="observation in observationTags.slice(0, 8)" @click="toggleObservationSelection(observation)" v-bind:key="observation" class="btn mb-2 me-2" data-bs-toggle="button" :style="{ color:'white', backgroundColor: selectedObservations.includes(observation) ? 'blue' : 'grey', borderColor:'grey', borderWidth:'1px' }">{{ observation }}</button>
                                                
                                                <!-- Buttons for additional observations (shown only when extendObservation is true) -->
                                                <div v-if="extendObservation">
                                                    <button v-for="observation in observationTags.slice(8)" @click="toggleObservationSelection(observation)" v-bind:key="observation" class="btn mb-2 me-2" :style="{ color:'white', backgroundColor: selectedObservations.includes(observation) ? 'blue' : 'grey', borderColor:'grey', borderWidth:'1px' }">{{ observation }}</button>
                                                </div>
                                                
                                                <!-- Button to toggle between View All and View Less -->
                                                <button @click="toggleObservations" class="btn" style="color:black; background-color:white; border-color:black; border-width: 1px;" v-if="!extendObservation">
                                                    View All
                                                </button>
                                                <button @click="toggleObservations" class="btn" style="color:black; background-color:white; border-color:black; border-width: 1px;" v-else>
                                                    View Less
                                                </button>
                                                
                                            </div>


                                        </div>
                                    </div>
                                     <!-- End of left side elements -->

                                    <!-- Start of right side elements, photo, location and friend tags -->
                                    <div class="col-md-3">
                                        <p class = 'text-start mb-2 fw-bold'>Add Photo</p>
                                        <div class="mb-3">
                                            <!-- DONE v:model here the file -->
                                            <input class="form-control mb-2" @change="onFileChange" type="file" id="reviewPhoto">
                                            <div class = "row">
                                                <img :src="image64 ? 'data:image/jpeg;base64,' + image64 : 'none'" alt="" id="output">
                                            </div>
                                            <button v-if="image64!==null" class="btn text-start mb-1" style="background-color: #535C72;color: white;" @click="clearPhoto">Clear Photo</button>
                                        </div>
                                        
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1 fw-bold">Tag Friends</p>
                                            <input type="text" class="form-control" id="friendTag">
                                        </div>
                                        
                                        <!-- Start of location input -->
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1 fw-bold">Location</p>                                            
                                                               
                                            <!-- Link filteredOptions to venues location -->
                                            <div class="input-group">
                                                <select class="form-control" v-model="selectedLocation" @input="filterOptions($event)">
                                                    <option v-for="option in filteredOptions" :key="option.id" :value="option.name">{{ option.name }}</option>
                                                </select>
                                            </div>
                                            <button v-if="selectedLocation!==''" class="btn text-start mb-1" style="background-color: #535C72;color: white;" @click="clearLocation">Clear Selection</button>
                                        </div>


                                    </div> 
                                    <!-- End of right side elements -->

                                </div>
                                <!-- End of bootstrap row -->

                                </div>
                                <!-- End of modal body -->
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button v-if="!inEdit" type="button" @click="addReview" class="btn btn-primary">Submit Review</button>
                                    <button v-else type="button" @click="editReview" class="btn btn-primary">Update Review</button>
                                </div>
                            </div>
                        </div>
                    </div>
                <!-- END OF MODAL -->


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
                <!-- TODO  EDIT MODAL IF NOT DOING COMPONENT-->
                <div>
                    <div class="row" v-for="review in filteredReviews" v-bind:key="review._id">
                        <!-- profile photo -->
                        <div class="col-1">
                            <img :src=" 'data:image/jpeg;base64,' + (getPhotoFromReview(review) || defaultProfilePhoto)" alt="" class="profile-image">
                        </div>
                        <!-- user reviews -->
                        <div class="col-9">
                            <div class="row">
                                <div class="d-flex align-items-center text-start mb-2">
                                    @{{ getUsernameFromReview(review) }} rated {{ review['rating'] }} 
                                    <!-- star icon -->
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill me-5" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                    <!-- Insert Edit modal here -->

                                    <div v-if="review.userID['$oid'] === userID" class="ms-2 ml-auto">
                                        <button class="btn btn-warning me-1" @click="setUpdateID(review)" data-bs-toggle="modal" data-bs-target="#reviewModal">Edit</button>
                                        <button class="btn btn-danger ms-1" @click="setDeleteID(review)" data-bs-toggle="modal" data-bs-target="#deleteReview">Delete</button>
                                    </div>
                                </div>
                                <div class="text-start mb-3">
                                    {{ review['reviewDesc'] }}
                                </div>
                                <!-- flavour tag -->
                                <div class="text-start mb-1">
                                    <!-- flavor tag -->
                                        <span v-for="(tag, index) in review.flavorTag" :key="index" class="badge rounded-pill me-2" :style="{ backgroundColor: getTagColor(tag) }">{{ getTagName(tag) }}</span>
                                </div>
                                <div style="display: inline;" class="text-start">
                                    <!-- voting -->
                                    <svg v-if="!JSON.stringify(review.userVotes.upvotes).includes(JSON.stringify(userID))" @click="voteReview(review, 'upvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-up" viewBox="0 0 16 16">
                                        <path d="M3.204 11h9.592L8 5.519zm-.753-.659 4.796-5.48a1 1 0 0 1 1.506 0l4.796 5.48c.566.647.106 1.659-.753 1.659H3.204a1 1 0 0 1-.753-1.659"/>
                                    </svg>
                                    <svg v-else @click="voteReview(review, 'unupvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-up-fill" viewBox="0 0 16 16">
                                        <path d="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
                                    </svg>
                                    <span class="mx-2">{{ review.userVotes.upvotes.length - review.userVotes.downvotes.length }}</span>
                                    <svg v-if="!JSON.stringify(review.userVotes.downvotes).includes(JSON.stringify(userID))" @click="voteReview(review, 'downvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-down me-3" viewBox="0 0 16 16">
                                        <path d="M3.204 5h9.592L8 10.481zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659"/>
                                    </svg>
                                    <svg v-else @click="voteReview(review, 'undownvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-down-fill me-3" viewBox="0 0 16 16">
                                        <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                                    </svg>
                                    <a href="#" class="text-decoration-underline text-secondary">Detailed Review ></a>
                                </div>
                            </div>
                        </div>
                        <div class="col-2">
                            <div class="text-end">
                                <!-- review photo -->
                                <img :src=" 'data:image/jpeg;base64,' + (review['photo'] || defaultProfilePhoto)" alt="" class="review-image" style="width: 125px; height: 125px">
                            </div>
                        </div>
                        <!-- Delete review modal -->
                        <!-- <div v-if="checkUserID(review.userID)"> -->
                        <!-- <div v-if="review.userID['$oid'] === userID">
                            <button class="btn btn-danger" @click="setDeleteID(review)" data-bs-toggle="modal" data-bs-target="#deleteReview">Delete</button>
                        </div> -->
                        <div class="modal fade" id="deleteReview" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                
                                <!-- DELETE SUCCESS -->
                                <div class="text-success fst-italic fw-bold fs-3 modal-content" v-if='successDelete'>
                                    <span>Your review has successfully been deleted!</span>
                                    <div class="modal-footer">
                                        <button type="button" @click="reloadRoute" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                                <!-- DELETE ERROR -->
                                <div class="text-danger fst-italic fw-bold fs-3 modal-content" v-if="errorDelete"> 
                                    <div v-if="errorDeleteMessage" class = "row"> 
                                        <span >An error occurred while attempting to delete, please try again!</span>
                                        <br>
                                        <button class="btn primary-btn btn-sm" @click="reset">
                                            <span class="fs-5 fst-italic"> Retry your delete request here! </span>
                                        </button>
                                    </div>
                                    
                                    <span v-if="notExist">There is no review by you for this bottle listing!</span>
                                    <br>

                                
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>

                                <!-- DELETE IN PROGRESS MODAL -->
                                <div v-if="deletingReview" class="modal-content">
                                    <div class="modal-header" style="background-color: #535C72">
                                        <h5 class="modal-title" id="deleteReview" style="color: white;">Delete Review</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        Are you sure you want to delete your review?
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-danger" @click="deleteReview">Delete Review</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- END of delete review modal -->

                        <!-- review photo -->
                        <div class="col-2">

                        </div>
                    </div>
                </div>

                <hr>

                
            </div> <!-- end of producer information -->
            
            <!-- where to buy & where to try & 88 bamboo's review -->
            <div class="col-3">
                <!-- where to buy -->
                <div class="row">
                    <div class="square primary-square rounded p-3 mb-3">
                        <!-- header text -->
                        <div class="square-inline text-start">
                            <h4 class="mr-auto"> Where to Buy </h4>
                        </div>
                        <!-- body -->
                        <div class="text-start pt-2">
                            <!-- [function] where to buy -->
                            <div v-for="producer in producerListings" v-bind:key="producer._id">
                                <router-link :to="{ path: '/Producers/Profile-Page/' + producer.$oid }" class="reverse-clickable-text">
                                    <p> {{ getProducerName(producer) }} </p>
                                </router-link>
                            </div>
                        </div>
                        <div class="py-5"></div>
                    </div>
                </div>
                <!-- where to try -->
                <div class="row">
                    <div class="square primary-square rounded p-3 mb-3">
                        <!-- header text -->
                        <div class="square-inline text-start">
                            <h4 class="mr-auto"> Where to Try </h4>
                        </div>
                        <!-- body -->
                        <div class="text-start pt-2">
                            <!-- [function] where to try -->
                            <div v-for="venue in venueListings" v-bind:key="venue._id">
                                <router-link :to="{ path: '/Venues/Profile-Page/' + venue.$oid }" class="reverse-clickable-text">
                                    <p> {{ venue.venueName }} </p>
                                </router-link>
                            </div>
                        </div>
                        <div class="py-5"></div>
                    </div>
                </div>
                <!-- 88 bamboo's review -->
                <div class="row">
                    <div class="square secondary-square rounded p-3 mb-3">
                        <!-- header text -->
                        <div class="py-2 text-start">
                            <h4> 88 Bamboo's Review </h4>
                            <a :href="specified_listing['reviewLink']" class="text-left default-text-no-background">
                                {{ deepDiveLinkFormatted }}
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
    </div> <!-- end of your drinks shelf & brands you follow -->

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    // import ReviewModal from '@/components/EditReview.vue'
    
    export default {
        // setup(){

        // },
        // components:{ReviewModal},
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
                acctype:null,

                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                filteredReviews:[],

                // specified listing lisitng_id used for createReview
                listing_id: null,
                specified_listing: {},

                // specified producer
                producer_id: null,

                // where to buy
                producerListings: [],

                // where to try
                venueListings: [],

                // customization for drinkLists buttons
                // [TODO] get drink list of user, for now is hardcoded
                drinkList:  {
                                "haveTried": ["Harmony Collection Inspired by Intense Arabica"],
                                "wantToTry": ["Catnip Gin No. 2", "Five Farms Irish Cream Liqueur"]
                            },
                haveTried: false,
                wantToTry: false,

                // For creating review
                languages:[],
                selectedLanguage:"English",
                reviewDesc:"",
                rating: 5,
                colours: ["#FFFFFF", "#FEED97", "#FBE166", "#FAD74A", "#F5C84B", "#F8C139", "#E79E12", "#E07D1F", "#D55530", "#B63426", "#AA1F22", "#702C1C", "#4A1C0C", "#000000"],
                specialColours: {
                                    "red":['#FF0F0F', '#69140F'],
                                    "green":['#24FF00', '#074202'],
                                    "lightBlue":['#82E3E9', '#0A7E97'],
                                    "darkBlue":['#8F8DF3', '#051B6B'],
                                    "purple":['#CBA4E3', '#5B0E8A'],
                                    "pink":['#FDC1FE', '#AD1181'],
                                },
                selectedColour:"",
                image64: null,
                photo: null,
                observationTags: ["Beginner Friendly", "Recommended for Enthusiasts", "Good for Gifts", "Cool Packaging", "Acquired Taste", "Easy to Drink", "Good for Cocktails", "Good for Sipping", "Good for Highballs", "Unique Expression", "For My Worst Enemy", "Overhyped!", "More Complex Than Inception", "What Just Hit Me", "Is This Water?", "Try Once", "Daily Drinker","Sharp Like a Toothpick","Hot Like Hell", "Ticket to Funkytown", "Food Pairing Friendly", "Netflx & Chill", "Broke the Bank", "Smooth Criminal", "Grail"],
                selectedObservations:[],
                flavourTags: [],
                selectedFlavourTags:[],
                aroma:"",
                taste:"",
                finish:"",
                wouldRecommend:false,
                wouldBuyAgain:false,
                extendReview:true,
                locationOptions: [], // Your list of options
                locationSearchTerm: "",
                selectedLocation: "",
                selectedLocationId: "",
                extendObservation: false,
                loggedIn:false,
                userID: "defaultUser",
                reviewDescError:'',
                reviewResponseCode:'',
                addingReview: true,
                successSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                errorSubmission:false,

                // To delete review
                deleteID :null,
                successDelete:false,
                deletingReview:true,
                errorDelete:false,
                errorDeleteMessage:false,

                // To edit review
                inEdit:false,
                specificReview:[],
                
                // matched user
                matchedUser: {},

                deepDiveLinkFormatted: "",

                defaultProfilePhoto:  "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"
            };
        },
        mounted() {
            try {
                    // Get the query string parameters (listing ID) from the URL
                    this.listing_id = this.$route.params.id;
                    console.log(this.listing_id)
                    if (this.listing_id == null) {
                        // redirect to page
                        this.$router.push('/Users/Bottle-Listings');
                    }
                } 
                catch (error) {
                    console.error(error);
                }
            
            this.loadData();
            // Load local storage variables
            const accID = localStorage.getItem("88B_accID");
            if(accID !== null){
                this.userID = localStorage.getItem('88B_accID')
            }
            //     this.loggedIn = true
            // }
            const accType = localStorage.getItem("88B_accType");
            if(accType !==null){
                this.acctype = accType
            }
        },
        computed: {
            filteredOptions() {
            return this.locationOptions.filter(option =>
                option.name.toLowerCase().includes(this.locationSearchTerm.toLowerCase())
            );
            }
        },
        methods: {
            // fetch specific listing data
            created() {
                
            },

            // load data from database
            async loadData() {
                    // countries
                    // _id, originCountry
                        // try {
                        //         const response = await this.$axios.get('http://127.0.0.1:5000/getCountries');
                        //         this.countries = response.data;
                        //     } 
                        //     catch (error) {
                        //         console.error(error);
                        // }
                    // reviews
                    // _id, userID, reviewTarget, date, rating, reviewDesc, taggedUsers, reviewTitle, reviewType, flavorTag, photo
                        try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                            this.reviews = response.data;
                        }
                        catch (error) {
                            console.error(error);
                        }
                    // flavourTags
                    // _id, hexcode, familyTag, subtag, showbox
                    try {
                                const response = await this.$axios.get('http://127.0.0.1:5000/getFlavourTags');
                                this.flavourTags = response.data.map(item => {
                                    return { ...item, showBox: false }; // Add the showBox property with initial value of false
                                });
                            } 
                        catch (error) {
                            console.error(error);
                        }
                    // venues
                    // _id, venueName, venueDesc, originCountry, address, openingHours
                        try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getVenues');
                            this.venues = response.data;
                            this.locationOptions = response.data.map(item => ({name: item.venueName, id:item._id}));
                            // this.whereToTry(); // find where to try specified listing [RE-ENABLE WHEN VENUES HAVE MENU ATTRIBUTE]
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
                        this.producer_id = this.specified_listing.producerID.$oid // find specified producer
                        console.log(this.specified_listing)
                        this.whereToBuy(); // find where to buy specified listing
                        this.filteredReviews = this.getReviewsForListing(this.specified_listing);
                        this.specificReview = this.getLoggedUserReview();
                        this.formatDeepDiveLink();
                    } 
                    catch (error) {
                        console.error(error);
                    }
                // languages
                // _id, language
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getLanguages');
                        this.languages = response.data;
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
                // users
                // _id, username, displayName, choiceDrinks, drinkLists, modType, photo
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getUsers');
                        this.users = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                    }
                
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                // try {
                //         const response = await this.$axios.get('http://127.0.0.1:5000/getVenuesAPI');
                //         this.venuesAPI = response.data;
                //     } 
                //     catch (error) {
                //         console.error(error);
                //     }
                // drinkTypes
                // _id, drinkType, typeCategory
                    // try {
                    //     const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                    //     this.drinkTypes = response.data;
                    // } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // requestListings
                // _id, listingName, producerNew, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, sourceLink, brandRelation, reviewStatus, userID, photo
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getRequestListings');
                    //         this.requestListings = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getRequestEdits');
                    //         this.requestEdits = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // modRequests
                // _id, userID, drinkType, modDesc
                    // try {
                    //         const response = await this.$axios.get('http://127.0.0.1:5000/getModRequests');
                    //         this.modRequests = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
            },

            // view which producers have specified listing
            whereToBuy() {
                this.producerListings = this.listings
                    .filter(listing => listing["listingName"] == this.specified_listing["listingName"])
                    .map(listing => listing["producerID"]);
            },

            // view which venues have specified listing, sort by alphabetical order of venue name
            whereToTry() {
                this.venueListings = this.venues
                    .filter(venue => venue["menu"].includes(this.specified_listing._id["$oid"]))
                    .sort((a, b) => a["venueName"].localeCompare(b["venueName"]));
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
                    return review["reviewTarget"]['$oid'] == listing._id['$oid'];
                });
                return reviews;
            },

            getLoggedUserReview(){
                const specificReview = this.filteredReviews.filter((review) => {
                    return review["userID"]['$oid'] == this.userID;
                });
                if(specificReview.length!=0){
                    this.inEdit=true
                    this.selectedLanguage= specificReview[0].language
                    this.selectedColour= specificReview[0].colour
                    this.reviewDesc= specificReview[0].reviewDesc
                    this.wouldRecommend= specificReview[0].willRecommend
                    this.wouldBuyAgain= specificReview[0].wouldBuyAgain
                    this.aroma= specificReview[0].aroma
                    this.taste= specificReview[0].taste
                    this.finish= specificReview[0].finish
                    this.rating= specificReview[0].rating
                    this.selectedFlavourTags= specificReview[0].flavorTag
                    this.selectedObservations= specificReview[0].observationTag
                    this.image64= specificReview[0].photo
                    const selectedLocation = this.locationOptions.filter((location)=>{
                        return location['id']['$oid'] == specificReview[0].location['$oid']
                    })
                    this.selectedLocation = selectedLocation[0].name
                }

                return specificReview
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
            },

            displaySelectColour(colour){
                this.selectedColour = colour
            },
            // function to display submitted image
            onFileChange(event){
                const file = event.target.files[0];
                const reader = new FileReader();

                reader.onloadend = async () => {
                    const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
                    this.image64 = base64String;
                };
                reader.readAsDataURL(file);
            },

            // Function to add review
            addReview(){
                // let errorPhrase = "Your completion is incomplete"
                // form validation
                if(this.reviewDesc.length < 20){
                    this.reviewDescError ="Character count is less than 20, please write more for a more detailed review."
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                let createdDate = new Date().toISOString() + '+00:00';
                if (this.reviewDesc !== "") {
                    this.reviewDesc = this.reviewDesc.trim();
                }
                if (this.photo !== null) {
                    this.photo = this.photo.trim();
                }
                if (this.aroma !== "") {
                    this.aroma = this.aroma.trim();
                }
                if (this.taste !== "") {
                    this.taste = this.taste.trim();
                }
                if (this.finish !== "") {
                    this.finish = this.finish.trim();
                }
                let submitAPI = "http://127.0.0.1:5005/createReview"
                let submitData = {
                    "userID" : this.userID,
                    "reviewTarget" :this.listing_id,
                    "rating" : this.rating,
                    "reviewDesc": this.reviewDesc,
                    "reviewType": "Listing",
                    "flavorTag" : this.selectedFlavourTags,
                    "photo" : this.image64,
                    "colour" : this.selectedColour,
                    "language" : this.selectedLanguage,
                    "aroma" : this.aroma,
                    "taste" : this.taste,
                    "finish" : this.finish,
                    "location" :this.selectedLocationId,
                    "willRecommend": this.wouldRecommend,
                    "wouldBuyAgain": this.wouldBuyAgain,
                    "observationTag": this.selectedObservations,
                    "createdDate": createdDate,
                    "userVotes": {
                        "downvotes":[],
                        "upvotes":[]
                    }
                }
                this.writeReview(submitAPI, submitData)
                
            },

            editReview(){
                if(this.reviewDesc.length < 20){
                    this.reviewDescError ="Character count is less than 20, please write more for a more detailed review."
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                if (this.reviewDesc !== "") {
                    this.reviewDesc = this.reviewDesc.trim();
                }
                if (this.photo !== null) {
                    this.photo = this.photo.trim();
                }
                if (this.aroma !== "") {
                    this.aroma = this.aroma.trim();
                }
                if (this.taste !== "") {
                    this.taste = this.taste.trim();
                }
                if (this.finish !== "") {
                    this.finish = this.finish.trim();
                }
                let submitAPI = "http://127.0.0.1:5200/updateReview/" + this.specificReview[0]._id['$oid']
                let submitData = {
                    "userID" : this.userID,
                    "reviewTarget" :this.listing_id,
                    "rating" : this.rating,
                    "reviewDesc": this.reviewDesc,
                    "reviewType": "Listing",
                    "flavorTag" : this.selectedFlavourTags,
                    "photo" : this.image64,
                    "colour" : this.selectedColour,
                    "language" : this.selectedLanguage,
                    "aroma" : this.aroma,
                    "taste" : this.taste,
                    "finish" : this.finish,
                    "location" :this.selectedLocationId,
                    "willRecommend": this.wouldRecommend,
                    "wouldBuyAgain": this.wouldBuyAgain,
                    "observationTag": this.selectedObservations,
                    "createdDate": this.specificReview[0].createdDate
                }
                this.updateReview(submitAPI, submitData)
            },

            async updateReview(submitAPI, submitData){
                const response = await this.$axios.put(submitAPI, submitData)
                .then((response)=>{
                    this.reviewResponseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.reviewResponseCode = error.response.data.code
                });
                if(this.reviewResponseCode==200){
                    this.successSubmission=true; // Display success message
                    this.addingReview=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.addingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

            async writeReview(submitAPI, submitData){
                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    this.reviewResponseCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.reviewResponseCode = error.response.data.code
                });
                if(this.reviewResponseCode==201){
                    this.successSubmission=true; // Display success message
                    this.addingReview=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.addingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

            // Function to expand/contract the modal
            controlModal(){
                if(this.extendReview){
                    this.extendReview = false
                }
                else{
                    this.extendReview = true
                }
            },

            filterOptions(event) {
                const selectedOption = this.filteredOptions.find(option => option.name === event.target.value);
                this.selectedLocationId = selectedOption.id;
            },
            
            toggleBox(family) {
                let tempShowBox = family.showBox
                this.flavourTags.forEach(item => {
                    item.showBox = false;
                });
                family.showBox = !tempShowBox; // Toggle the visibility of the box
            },

            toggleObservations(){
                this.extendObservation = !this.extendObservation
            },

            toggleObservationSelection(observation) {
                const index = this.selectedObservations.indexOf(observation);
                if (index === -1) {
                    // Observation is not selected, so add it to the array
                    this.selectedObservations.push(observation);
                } else {
                    // Observation is selected, so remove it from the array
                    this.selectedObservations.splice(index, 1);
                }
            },

            toggleFlavourSelection(flavour, hexcode) {
                const index = this.selectedFlavourTags.indexOf(flavour+hexcode);
                if (index === -1) {
                    // Observation is not selected, so add it to the array
                    this.selectedFlavourTags.push(flavour+hexcode);
                } else {
                    // Observation is selected, so remove it from the array
                    this.selectedFlavourTags.splice(index, 1);
                }
            },

            clearColour(){
                this.selectedColour = ''
            },

            clearLocation(){
                this.selectedLocation = ''
            },

            clearPhoto(){
                this.image64 = null
                document.getElementById('reviewPhoto').value = '';
            },

            async deleteReview(){
                let deleteAPI = "http://127.0.0.1:5006/deleteReview/" + this.deleteID['$oid']
                console.log(this.deleteID)
                const response = await this.$axios.delete(deleteAPI)
                .then((response)=>{
                    this.deleteReviewCode = response.data.code
                })
                .catch((error)=>{
                    console.log(error);
                    this.deleteReviewCode = error.response.data.code
                });
                if(this.deleteReviewCode==200){
                    this.successDelete=true; // Display success message
                    this.deletingReview=false; // Hide submission in progress message
                }else{
                    this.errorDelete=true; // Display error message
                    this.deletingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.notExist = true // Display duplicate entry message
                    }else{
                        this.errorDeleteMessage = true // Display generic error message
                    }
                }
                return response
                
            },

            setDeleteID(review){
                this.deleteID = review._id
            },

            setUpdateID(review){
                this.updateID = review._id
            },

            async voteReview(review, vote){
                if (vote == "upvote") {
                    review.userVotes.upvotes.push(this.userID);
                    if (review.userVotes.downvotes.some(vote => JSON.stringify(vote) === JSON.stringify(this.userID))) {
                        review.userVotes.downvotes = review.userVotes.downvotes.filter(vote => JSON.stringify(vote) !== JSON.stringify(this.userID));
                    } 
                } else if (vote == "downvote") {
                    review.userVotes.downvotes.push(this.userID);
                    if (review.userVotes.upvotes.some(vote => JSON.stringify(vote) === JSON.stringify(this.userID))) {
                        review.userVotes.upvotes = review.userVotes.upvotes.filter(vote => JSON.stringify(vote) !== JSON.stringify(this.userID));
                    }
                } else if (vote == "unupvote") {
                    review.userVotes.upvotes = review.userVotes.upvotes.filter(vote => JSON.stringify(vote) !== JSON.stringify(this.userID));
                } else if (vote == "undownvote") {
                    review.userVotes.downvotes = review.userVotes.downvotes.filter(vote => JSON.stringify(vote) !== JSON.stringify(this.userID));
                }

                try {
                    const response = await this.$axios.post('http://127.0.0.1:5200/voteReview', 
                        {
                            reviewID: review._id,
                            userVotes: review.userVotes
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } catch (error) {
                    console.error(error);
                }
            },

            reloadRoute() {
                this.$router.go(); // Reloads the current route
            },

            checkUserID(review){
                console.log(review)
                console.log(this.userID)
            },
            getTagName(tag) {
            const tagParts = tag.split("#");
            return tagParts[0];
            },
            getTagColor(tag) {
                const tagParts = tag.split("#");
                console.log("#" + tagParts[1]);
                return "#" + tagParts[1];
            },

            formatDeepDiveLink() {
                let unformattedLink = this.specified_listing["reviewLink"];
                // extract segment after the last "/"
                const segment = unformattedLink.substring(unformattedLink.lastIndexOf("/") + 1);
                // split the segment by "-"
                const words = segment.split("-");
                // capitalize the first letter of each word
                const capitalizedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));
                // join the words back together with spaces
                this.deepDiveLinkFormatted = capitalizedWords.join(" ");
            }, 
        }
    };
</script>