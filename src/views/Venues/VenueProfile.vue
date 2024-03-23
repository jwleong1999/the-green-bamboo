<!-- Venue Profile Page -->
<!-- If venueID is not specified, display logged in venue's profile page. If not logged in as a venue, redirect to your own profile page / login. -->

<template>
    <NavBar />

    <!-- Main Content -->
    <div class="container pt-5">

        <!-- Display when data is still loading -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="dataLoaded == false">
            <span>Loading venue, please wait...</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <!-- Display when venue does not exist -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="venueExists == false || dataLoaded == null"> 
            <span>An error occurred while loading this page, please try again!</span>
            <br>
            <span class="text-danger-emphasis fw-normal">Are you sure that this venue exists?</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="this.$router.go(-1)">
                <span class="fs-5 fst-italic"> Return to previous page </span>
            </button>
            <router-link :to="'/'" class="mx-1">
                <button class="btn primary-btn btn-sm">
                    <span class="fs-5 fst-italic"> Go to Home page </span>
                </button>
            </router-link>
        </div>

        <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

        <div class="row" v-if="dataLoaded == true">

            <!-- ------- START Venue Information ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

            <!-- Venue Information -->
            <div class="col-9 no-margin">

                <!-- ------- START Header ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Header -->
                <div class="row">

                    <!-- ------- START Image ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Image -->
                    <div class="col-3 image-container">

                        <!-- [if] editing profile -->
                        <div v-if="editProfile" style="position: relative; text-align: center;">
                            <!-- image -->
                            <img :src="'data:image/jpeg;base64,' + (editProfilePhoto || defaultProfilePhoto)" 
                                alt="" style="width: 200px; height: 200px; z-index: 1; opacity: 50%">
                            <!-- change option -->
                            <label for="fileSelectPFP" class="btn primary-light-dropdown mt-3" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">Choose File</label>
                            <input id="fileSelectPFP" type="file" @change="handleFileSelectPFP" ref="fileInput" style="width: 0px; height: 0px;">
                            <!-- reset image option -->
                            <button class="btn primary-light-dropdown m-1" @click="editProfilePhoto = targetVenue['photo']">Revert</button>
                            <!-- remove image option -->
                            <button class="btn primary-light-dropdown m-1" @click="editProfilePhoto = ''">Remove</button>
                            
                        </div>

                        <!-- [else] not editing -->
                        <div v-else>
                            <img :src="'data:image/jpeg;base64,' + (targetVenue['photo'] || defaultProfilePhoto)" 
                                alt="" style="width: 200px; height: 200px; z-index: 1;">
                        </div>

                    </div>

                    <!-- ------- END Image / START Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Details -->
                    <div class="col-9 container text-start">

                        <div class="row">

                            <!-- Country -->
                            <div class="col-8">

                                <!-- [if] editing profile -->
                                <div v-if="editProfile">
                                    <label for="editCountryInput"> Country of Origin </label>
                                    <input type="text" class="form-control mb-3" id="editCountryInput" aria-describedby="originLocation" v-model="editCountry">
                                </div>

                                <!-- [else] not editing -->
                                <h5 v-else class="text-body-secondary">{{ targetVenue['originLocation'] }}</h5>

                            </div>

                            <!-- Claim Venue / Report Menu Inaccuracy / Edit Profile -->
                            <div class="col-4">
                                <!-- [if] not logged in as viewed venue -->
                                <div class="d-grid no-padding text-end" v-if="!selfView && !powerView">

                                    <!-- Claim Venue -->
                                    <p v-if="!targetVenue['claimStatus']" class="text-body-secondary no-margin text-decoration-underline fst-italic" @click="claimVenueAccount"> Claim This Business </p>
                                    <p v-else class="text-body-secondary no-margin fw-bold fst-italic"> Venue Claimed </p>

                                    <!-- Report Menu Inaccuracy (Opens Modal) -->
                                    <p v-if="loggedIn && targetVenue['claimStatus']" class="text-body-secondary no-margin text-decoration-underline fst-italic" data-bs-toggle="modal" data-bs-target="#inaccurateModal"> Report Menu Inaccuracy </p>
                                    <p v-if="!loggedIn && targetVenue['claimStatus']" class="text-body-secondary no-margin text-decoration-underline fst-italic" @click="this.$router.push('/login');"> Report Menu Inaccuracy </p>
                                </div>

                                <!-- [else] logged in as viewed venue -->
                                <div class="d-grid no-padding text-end" v-else>

                                    <!-- Edit Profile Toggle -->

                                    <!-- [if] not editing -->
                                    <button v-if="!editProfile" type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="editProfile = true">
                                        Edit Profile
                                    </button>
                                    <!-- [else] if editing -->
                                    <button v-else type="button" class="btn success-btn rounded-0 reverse-clickable-text" @click="saveProfileEdits">
                                        Save
                                    </button>
                                </div>
                            </div>

                            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->
                            <!-- modal for inaccurate listing request -->
                            <div class="modal fade" id="inaccurateModal" tabindex="-1" aria-labelledby="inaccurateModalLabel" aria-hidden="true" data-bs-backdrop="static">
                                <div class="modal-dialog modal-xl">

                                    <!-- Report Submission Successful -->
                                    <div class="text-success text-center fst-italic fw-bold fs-3 modal-content" v-if='reportSubmitSuccess'>
                                        <span>Your report has successfully been submitted!</span>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" @click="resetReport" data-bs-dismiss="modal">Close</button>
                                        </div>
                                    </div>

                                    <!-- Report Submission Error -->
                                    <div class="text-danger text-center fst-italic fw-bold fs-3 modal-content" v-if="reportSubmitError != null">

                                        <!-- Error: Generic -->
                                        <span v-if="reportSubmitError == 'error'">An error occurred while attempting to report, please try again!</span>
                                        <!-- Error: Duplicate Report -->
                                        <span v-if="reportSubmitError == 'dupe'">You've already submitted an inaccurate report for this bottle listing!</span>
                                        
                                        <div class="modal-footer">
                                            <button type="button" class="btn primary-btn" @click="retryReport">Retry</button>
                                            <button type="button" class="btn btn-secondary" @click="resetReport" data-bs-dismiss="modal">Clear & Close</button>
                                        </div>
                                        
                                    </div>

                                    <!-- Report Form -->
                                    <div v-if="reportFormView" class="modal-content" style="height: 450px;">
                                        <div class="modal-header" style="background-color: #535C72">
                                            <h1 class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Report Menu Inaccuracy</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">

                                            <!-- Select: Menu Section -->
                                            <p class='text-start mb-2 fw-bold'>Menu Section: <span class="text-danger">*</span></p>
                                            <div class="input-group">
                                                <select v-model="reportSection" class="form-select mw-100" @change="getReportSectionItems">
                                                    <option disabled value=''> (Select a section) </option>
                                                    <option v-for="(section, index) in detailedMenu" v-bind:key="index" v-bind:value="index">{{ section.sectionName }}</option>
                                                </select>
                                            </div>

                                            <!-- Select: Inaccurate Item -->
                                            <p class='text-start mb-2 fw-bold'>Inaccurate Item: <span class="text-danger">* <span v-if="reportItemNone">(Select 1)</span></span></p>
                                            <div class="input-group" v-if="reportSectionItems.length > 0">
                                                <select v-model="reportItem" class="form-select mw-100">
                                                    <option disabled value=''> (Select an item) </option>
                                                    <option v-for="item in reportSectionItems" v-bind:key="item.itemID" v-bind:value="item.itemID">{{ item.itemDetails.itemName }}</option>
                                                </select>
                                            </div>
                                            <!-- disabled if no valid items to select -->
                                            <div class="input-group" v-else>
                                                <select class="form-select mw-100" disabled>
                                                    <option selected>-</option>
                                                </select>
                                            </div>

                                            <!-- Text Input: Reason for Inaccuracy -->
                                            <div class = 'row justify-content-start mt-3'>
                                                <div class = "col-md-12">
                                                    <p class='text-start mb-2 fw-bold'>Report Reason: <span class="text-danger">* <span v-if="reportReasonNone">(Required)</span></span></p>
                                                    <textarea v-model="reportReason" class="form-control" id="reportReasonTextArea" rows="3" placeholder="Enter report reason / Describe inaccuracy and how to resolve your concern."></textarea>
                                                </div>
                                            </div>

                                        </div>

                                        <!-- end of modal body -->
                                        <div class="modal-footer">
                                            <div v-if="reportSubmitLoading" class="spinner-border" role="status">
                                                <span class="visually-hidden">Loading...</span>
                                            </div>
                                            <button type="button" @click="submitReport" class="btn btn-primary">Submit Report</button>
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        </div>
                                    </div>
                                </div>

                            </div>
                            <!-- END OF MODAL FOR INACCURATE REPORTING -->
                            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

                        </div>

                        <!-- ------- START Producer ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                        <!-- Producer -->
                        <div class="row">
                            <div class="col-12">
                                <!-- [if] editing -->
                                <div v-if="editProfile">
                                    <label for="venueNameInput"> Venue Name </label>
                                    <input type="text" class="form-control mb-3" id="venueNameInput" aria-describedby="venueName" v-model="editVenueName">
                                </div>
                                <!-- [else] not editing -->
                                <h3 v-else class="text-body-secondary"> <b> {{ targetVenue["venueName"] }} </b> </h3>
                            </div>
                        </div>

                        <!-- ------- END Producer / START Description ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                        <!-- Description -->
                        <div class="row">
                            <div class="col-12">
                                <!-- [if] editing -->
                                <div v-if="editProfile">
                                    <label for="venueDescInput"> Venue Description </label>
                                    <textarea type="text" class="form-control" id="venueDescInput" aria-describedby="venueDesc" v-model="editVenueDesc"></textarea>
                                </div>
                                <!-- [else] not editing -->
                                <p v-else class="text-body-secondary fs m-0"> {{ targetVenue["venueDesc"] }} </p>
                            </div>
                        </div>

                        <!-- ------- END Description ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    </div>

                    <!-- ------- END Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                </div>

                <!-- ------- END Header / START Content Buttons ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Content Buttons (Bar Overview / Bar Menu / Follow Venue) -->
                <div class="row mt-3">
                    <div class="col-8 d-flex justify-content-start">
                        <!-- Toggle Bar Overview -->
                        <button v-if="contentMode == 'overview'" class="btn primary-btn-outline-less-round mx-1" @click="contentMode = 'overview'"> Bar Overview </button>
                        <button v-else class="btn primary-btn-less-round mx-1" @click="contentMode = 'overview'"> Bar Overview </button>
                        <!-- Toggle Bar Menu -->
                        <button v-if="contentMode == 'menu'" class="btn primary-btn-outline-less-round mx-1" @click="contentMode = 'menu'"> Bar Menu </button>
                        <button v-else class="btn primary-btn-less-round mx-1" @click="contentMode = 'menu'"> Bar Menu </button>
                    </div>
                    <!-- Follow Venue -->
                    <div v-if="viewerType == 'user'" class="col-4 d-flex justify-content-end">
                        <button v-if="!userFollowing" class="btn primary-btn-less-round mx-1" @click="editFollow('follow')"> + Follow Venue </button>
                        <button v-else class="btn primary-btn-outline-less-round mx-1" @click="editFollow('unfollow')"> Following </button>
                    </div>
                </div>

                <hr>

                <!-- ------- END Content Buttons / START Bar Overview ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Bar Overview -->
                <div v-if="contentMode == 'overview'">

                    <!-- ------- START Latest Updates Header + Latest Update Information ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Latest Updates Header -->
                    <div class="row">
                        <div class="col-12">
                            <p class="text-start text-body-secondary fs-3 fw-bold m-0">Latest Updates from {{ targetVenue["venueName"] }}</p>
                            <p v-if="targetVenue['updates'].length > 0 && targetVenue['claimStatus']" class="text-start text-decoration-underline fs-5 m-0 pb-2">Posted on: {{ targetVenue["updates"][0].date }}</p>
                            <p v-if="!(targetVenue['updates'].length > 0) && targetVenue['claimStatus']" class="text-start fs-5 fst-italic m-0 pb-2">{{ targetVenue["venueName"] }} has not posted any updates!</p>
                        </div>
                    </div>

                    <!-- Latest Updates Lock Message (Venue Unclaimed) -->
                    <div class="row text-center py-2 mx-1" v-if="!targetVenue['claimStatus']" style="background-color:#DDC8A9;">
                        <p class="fs-3 fw-bold fst-italic mt-3" style="font-family: Radley, serif;">
                            Do you own this distillery?
                        </p>
                        <p> Sign up for a venue account to share your latest updates with your fans! </p>

                        <div class="col-lg-4 col-sm-3 col-2"></div>
                        <button type="submit" class="col-lg-4 col-sm-6 col-8 btn secondary-btn-border-thick mb-3" @click="claimVenueAccount"> Claim This Business </button>
                        <div class="col-lg-4 col-sm-3 col-2"></div>
                    </div>

                    <!-- Latest Update Information -->
                    <div class="row" v-if="targetVenue['updates'].length > 0 && targetVenue['claimStatus']">

                        <!-- Photo / Number of Likes -->
                        <div class="col-xl-2 col-md-3">
                            <img :src=" 'data:image/jpeg;base64,' + (targetVenue['updates'][0].photo || defaultProfilePhoto)" alt="" style="width: 128px; height: 128px;">

                            <div class="row pt-2">
                                <!-- Like Symbol -->
                                <div v-if="Array.isArray(targetVenue['updates'][0].likes) && viewerType !== null" class="col-6 text-end">
                                    <!-- [if] Liked -->
                                    <div v-if="targetVenue['updates'][0].likes.some(like => like['$oid'] == viewerID)" class="d-inline-block" @click="unlikeUpdates(targetVenue['updates'][0]._id['$oid'])">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="red" class="bi bi-heart-fill" viewBox="0 0 16 16">
                                            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                                        </svg>
                                    </div>
                                    <!-- [else] Not Liked -->
                                    <div v-else class="d-inline-block" @click="likeUpdates(targetVenue['updates'][0]._id['$oid'])">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                        </svg>
                                    </div>
                                </div>
                                <div v-else class="col-6 text-end">
                                    <div class="d-inline-block opacity-25">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                        </svg>
                                    </div>
                                </div>

                                <!-- Like Count -->
                                <div class="col-6 text-start">
                                    <p v-if="Array.isArray(targetVenue['updates'][0].likes)" class="text-body-secondary fs-5 m-0">{{ targetVenue['updates'][0].likes.length }}</p>
                                    <p v-else class="text-body-secondary fs-5 m-0">-</p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Description -->
                        <div class="col-xl-10 col-md-9">
                            <p class="text-start p-text-lg">{{ targetVenue['updates'][0].text }}</p>
                        </div>

                    </div>

                    <!-- ------- END Latest Updates Header + Latest Update Information / START Add Update ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Add Update -->
                    <div v-if="selfView" class="row pt-3">

                        <!-- Text Box / Options -->
                        <div class="input-group centered">

                            <!-- Text Box -->
                            <input class="search-bar form-control rounded fst-italic" type="text" placeholder="Say hi to your patrons!" v-model="newUpdateText">

                            <!-- Photo Upload -->
                            <label for="fileSelectUpdate" class="btn p-0 ms-2">
                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                                    <path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z"/>
                                    <path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/>
                                </svg>
                            </label>
                            <input id="fileSelectUpdate" type="file" @change="handleFileSelectUpdate" ref="fileInput" style="width: 0px; height: 0px;">

                            <!-- Submit Button -->
                            <button class="btn send-icon p-0 mx-1" @click="submitNewUpdate">
                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                    <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                </svg>
                            </button>

                        </div>

                        <!-- New Update Preview -->
                        <div v-if="newUpdateText.length > 0 || newUpdatePhoto" class="border border-secondary rounded mt-3">

                            <!-- Header / Clear Button -->
                            <div class="row my-2">
                                <div class="col-10">
                                    <p class="text-start text-body-secondary fs-5 fw-bold m-0">New Update Preview:</p>
                                </div>
                                <div class="col-2 d-flex justify-content-end align-items-center">
                                    <button type="button" class="btn-close" aria-label="Clear New Update Draft" @click="newUpdateText = ''; newUpdatePhoto = ''"></button>
                                </div>
                            </div>

                            <div class="row mb-3">
                                <!-- Photo / Clear Photo -->
                                <div class="col-xl-2 col-md-3">
                                    <div style="position: relative; text-align: center; width: 128px; height: 128px;">
                                        <img :src=" 'data:image/jpeg;base64,' + (newUpdatePhoto || defaultProfilePhoto)" alt="" style="width: 128px; height: 128px;">
                                        <button type="button" class="btn-close" @click="newUpdatePhoto = ''" style="position: absolute; top: 10%; left: 90%; transform: translate(-50%, -50%); z-index: 2;"></button>
                                    </div>
                                </div>
                                <!-- Description -->
                                <div class="col-xl-10 col-md-9">
                                    <p class="text-start p-text-lg">{{ newUpdateText }}</p>
                                </div>
                            </div>

                        </div>

                    </div>

                    <!-- ------- END Add Update / START View More Updates ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- View More Updates -->
                    <div class="row" v-if="targetVenue['claimStatus']">

                        <!-- Toggle Button -->
                        <button type="button" class="btn tertiary-text text-decoration-underline pt-2 no-margin border border-0" data-bs-toggle="collapse" data-bs-target="#collapseMoreUpdates" aria-expanded="false" aria-controls="collapseMoreUpdates" @click="showMoreUpdates = !showMoreUpdates;"> View <span v-if="showMoreUpdates">less</span><span v-else>more</span> </button>

                        <!-- More Updates Collapsible -->
                        <div class="collapse" id="collapseMoreUpdates" v-if="Array.isArray(targetVenue['updates'])">

                            <p v-if="targetVenue['updates'].length > 1" class="text-body-secondary fs-5 fw-bold m-0">Viewing {{ targetVenue['updates'].length -1 }} more updates</p>
                            <p v-else class="fs-5 fst-italic m-0">There are no more updates to view!</p>

                            <div v-for="updateMore in targetVenue['updates'].slice(1)" v-bind:key="updateMore._id">
                                <p class="text-start text-decoration-underline fs-5 m-0 pb-2">Posted on: {{ updateMore.date }}</p>

                                <!-- Update Information -->
                                <div class="row">

                                    <!-- Photo / Number of Likes -->
                                    <div class="col-xl-2 col-md-3">
                                        <img :src=" 'data:image/jpeg;base64,' + (updateMore.photo || defaultProfilePhoto)" alt="" style="width: 128px; height: 128px;">

                                        <div class="row pt-2">
                                            <!-- Like Symbol -->
                                            <div v-if="Array.isArray(updateMore.likes)" class="col-6 text-end">
                                                <!-- [if] Liked -->
                                                <div v-if="updateMore.likes.some(like => like['$oid'] == viewerID)" class="d-inline-block" @click="unlikeUpdates(updateMore._id['$oid'])">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="red" class="bi bi-heart-fill" viewBox="0 0 16 16">
                                                        <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                                                    </svg>
                                                </div>
                                                <!-- [else] Not Liked -->
                                                <div v-else class="d-inline-block" @click="likeUpdates(updateMore._id['$oid'])">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                                    </svg>
                                                </div>
                                            </div>
                                            <div v-else class="col-6 text-end">
                                                <div class="d-inline-block">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                                    </svg>
                                                </div>
                                            </div>

                                            <!-- Like Count -->
                                            <div class="col-6 text-start">
                                                <p v-if="Array.isArray(updateMore.likes)" class="text-body-secondary fs-5 m-0">{{ updateMore.likes.length }}</p>
                                                <p v-else class="text-body-secondary fs-5 m-0">-</p>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <!-- Description -->
                                    <div class="col-xl-10 col-md-9">
                                        <p class="text-start p-text-lg">{{ updateMore.text }}</p>
                                    </div>

                                </div>
                            </div>
                        </div>

                    </div>

                    <hr>

                    <!-- ------- END View More Updates / START View Sorted Listings ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- View Sorted Listings -->
                        <!-- 1: Most Popular (Highest Ratings) -->
                        <!-- 2: Most Discussed (Most Reviews) -->
                        <!-- 3: Recently Added (Newest) -->
                    <div v-for="sortedList in [mostPopular, mostDiscussed, recentlyAdded]" v-bind:key="sortedList">

                        <!-- Sorted Listing Titles -->
                        <p v-if="sortedList == mostPopular" class="text-start text-body-secondary fs-3 fw-bold m-0">Most Popular</p>
                        <p v-if="sortedList == mostDiscussed" class="text-start text-body-secondary fs-3 fw-bold m-0">Most Discussed</p>
                        <p v-if="sortedList == recentlyAdded" class="text-start text-body-secondary fs-3 fw-bold m-0">Recently Added</p>

                        <div class="container">
                            <div class="row">

                                <!-- Image Content -->
                                <div class="add-drink-photo-container image-container-150" v-for="drinkListing in sortedList" v-bind:key="drinkListing._id">

                                    <!-- Listing Photo + Link -->
                                    <router-link :to="{ path: '/listing/view/' + drinkListing._id.$oid }" class="default-text-no-background">
                                        <img :src=" 'data:image/jpeg;base64,' + (drinkListing.photo || defaultProfilePhoto)" class="add-drink-photo-background centered rounded"> 
                                    </router-link>
                                    
                                    <!-- Bookmark Icon -->
                                    <div v-if="viewerType == 'user'">
                                        <svg v-if="userBookmarks.includes(drinkListing._id['$oid'])" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bookmark-fill overlay-icon" viewBox="0 0 16 16"
                                            data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(drinkListing)">
                                            <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
                                        </svg>
                                        <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bookmark overlay-icon" viewBox="0 0 16 16"
                                            data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(drinkListing)">
                                            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                        </svg>
                                    </div>

                                </div>

                                <!-- Listing Name -->
                                <div class="add-drink-photo-container-text scrollable" v-for="drinkListing in sortedList" v-bind:key="drinkListing._id">
                                    <router-link :to="{ path: '/listing/view/' + drinkListing._id.$oid }" class="default-clickable-text">
                                        {{ drinkListing.listingName }}
                                    </router-link>
                                </div>
                                
                            </div>
                        </div>

                    </div>

                    <!-- ------- END View Sorted Listings ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                </div>

                <!-- ------- END Bar Overview / START Bar Menu ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Bar Menu -->
                <div v-if="contentMode == 'menu'">

                    <!-- ------- START Menu Lock Message (Venue Unclaimed) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Menu Lock Message (Venue Unclaimed) -->
                    <div class="row text-center py-2 mx-1" v-if="!targetVenue['claimStatus']" style="background-color:#DDC8A9;">
                        <p class="fs-3 fw-bold fst-italic mt-3" style="font-family: Radley, serif;">
                            Do you own this distillery?
                        </p>
                        <p> Sign up for a venue account to share your bar's menu with your fans! </p>

                        <div class="col-lg-4 col-sm-3 col-2"></div>
                        <button type="submit" class="col-lg-4 col-sm-6 col-8 btn secondary-btn-border-thick mb-3" @click="claimVenueAccount"> Claim This Business </button>
                        <div class="col-lg-4 col-sm-3 col-2"></div>
                    </div>

                    <!-- ------- END Menu Lock Message (Venue Unclaimed) / START Menu Header + Option Buttons ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Menu Header + Option Buttons -->
                    <div v-if="!editMenuMode && targetVenue['claimStatus']" class="row align-items-center pb-3">

                        <!-- Menu Header -->
                        <div class="col-8">
                            <p class="text-body-secondary text-start fs-4 m-0"><span class="fw-bold">{{ loadedListings.length }}</span> Drinks On The Menu</p>
                        </div>

                        <!-- Option Buttons -->
                        <div class="col-4 d-grid">
                            <div v-if="selfView" class="row">

                                <!-- Edit Menu -->
                                <div class="col-6 d-grid px-1">
                                    <button type="button" class="btn primary-btn-outline-thick rounded-0 reverse-clickable-text" @click="enableEditMenuMode"> Edit Menu </button>
                                </div>

                                <!-- Share Menu -->
                                <div class="col-6 d-grid px-1">
                                    <button type="button" class="btn primary-btn-outline-thick rounded-0 reverse-clickable-text" data-bs-toggle="modal" data-bs-target="#shareMenuModal"> Share Menu </button>

                                    <!-- Share Menu Modal (QR Code) -->
                                    <div class="modal fade" id="shareMenuModal" tabindex="-1" aria-labelledby="shareMenuModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h1 class="modal-title fs-5" id="shareMenuModalLabel"> Venue QR Code </h1>
                                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                </div>
                                                <div class="modal-body">
                                                    <div class="centered">
                                                        <qr-code v-bind:text="currentURL"></qr-code>
                                                    </div>
                                                    <div class="input-group pt-3">
                                                        <input type="text" class="form-control" aria-label="Link" aria-describedby="button-addon2" v-bind:value="currentURL" disabled>
                                                        <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="copyToClipboard(currentURL)">
                                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
                                                                <path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1z"/>
                                                                <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0z"/>
                                                            </svg>
                                                        </button>
                                                    </div>
                                                    <p class="text-start pt-2" v-if="clipboardItem"> 
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                                                            <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425z"/>
                                                        </svg>
                                                        Copied to clipboard!
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                </div>

                            </div>
                        </div>

                    </div>

                    <!-- ------- END Menu Header + Option Buttons / START Search + Edit Menu Options + Sort ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Search + Edit Menu Options + Sort -->
                    <div class="row align-items-center" v-if="!(editMenuMode && !editMenuDataLoaded) && targetVenue['claimStatus']">

                        <!-- Reset Search -->
                        <div v-if="!editMenuMode" class="col-1 p-0">
                            <button type="button" class="btn tertiary-btn" @click="searchMenuTerm = ''; searchMenu()">
                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-clockwise" viewBox="0 0 16 16">
                                    <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2z"/>
                                    <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466"/>
                                </svg>
                            </button>
                        </div>

                        <!-- Search Bar -->
                        <div v-if="!editMenuMode" class="col-9 p-0">
                            <input class="search-bar form-control rounded fst-italic" type="text" placeholder="Search menu" v-model="searchMenuTerm" @keyup.enter="searchMenu">
                        </div>

                        <!-- Edit Menu Options: Reset Section Order / Add New Section / Add Menu Item / Save Menu / Reset / Exit -->
                        <div v-if="editMenuMode" class="col-2 d-grid px-1">
                            <button type="button" class="btn secondary-btn-border-thick rounded-0 reverse-clickable-text px-0" @click="editMenu.sort((a, b) => (a.sectionOrder > b.sectionOrder) ? 1 : -1);"> Reset Section Order </button>
                        </div>
                        <div v-if="editMenuMode" class="col-2 d-grid px-1">
                            <button type="button" class="btn primary-btn-outline-thick rounded-0 reverse-clickable-text px-0" @click="addMenuSection"> Add New Section </button>
                        </div>
                        <div v-if="editMenuMode" class="col-2 d-grid px-1">
                            <button type="button" class="btn primary-btn-outline-thick rounded-0 reverse-clickable-text px-0" data-bs-toggle="modal" data-bs-target="#addMenuItemModal"> Add Menu Item </button>
                        </div>
                        <div v-if="editMenuMode" class="col-2 d-grid px-1">
                            <button type="button" class="btn success-btn rounded-0 reverse-clickable-text px-0" @click="updateMenu"> Save Menu </button>
                        </div>
                        <div v-if="editMenuMode" class="col-1 d-grid px-1">
                            <button type="button" class="btn secondary-btn-border-thick rounded-0 reverse-clickable-text px-0" @click="resetEditMenu"> Reset </button>
                        </div>
                        <div v-if="editMenuMode" class="col-1 d-grid px-1">
                            <button type="button" class="btn primary-btn-outline-thick rounded-0 reverse-clickable-text px-0" @click="editMenuMode = false"> Exit </button>
                        </div>

                        <!-- Sort Menu -->
                        <div class="col-2 me-0">
                            <div class="d-grid gap-2 dropdown">
                                <button class="btn primary-light-dropdown dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                    Sort{{ sortMenuTerm ? ': ' + sortMenuTerm : ' By...' }}
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="#" @click="sortMenu('')">(Default Order)</a></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li v-for="sortOption in sortMenuOptions" v-bind:key="sortOption">
                                        <a class="dropdown-item" href="#" @click="sortMenu(sortOption)">{{ sortOption }}</a>
                                    </li>
                                </ul>
                            </div>
                        </div>

                    </div>

                    <!-- ------- END Search + Edit Menu Options + Sort / START Menu View (Not Editing) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Menu View (Not Editing) -->
                    <div v-if="!editMenuMode && targetVenue['claimStatus']" class="container text-start scrollable-listings">

                        <!-- No Menu Sections to Show -->
                        <div v-if="searchMenuResults.length == 0" class="row my-4">
                            <p class="text-center fs-5 fst-italic m-0">No menu sections to show! Try clearing your search.</p>
                        </div>

                        <!-- Message about Expanding / Collapsing Sections -->
                        <div v-else class="row my-2">
                            <p class="text-start fw-bold fst-italic m-0">Click on each menu section's name to expand or hide its contents!</p>
                        </div>

                        <!-- Menu Sections -->
                        <div class="row mb-4" v-for="(menuSection, index) in searchMenuResults" v-bind:key="menuSection">

                            <!-- Section Name -->
                            <div class="col-12 d-grid">
                                <button type="button" class="btn secondary-btn-not-rounded fs-5 fw-bold text-start" data-bs-toggle="collapse" :data-bs-target="'#collapseMenuSection' + index" aria-expanded="true" :aria-controls="'collapseMenuSection' + index" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                    {{ menuSection.sectionName }}
                                </button>
                            </div>

                            <div class="collapse show" :id="'collapseMenuSection' + index">

                                <!-- No Section Contents to Show -->
                                <div v-if="menuSection.sectionMenu.length == 0" class="col-12 my-3">
                                    <p class="text-center fst-italic m-0">No menu items to show!</p>
                                </div>

                                <!-- Section Contents -->
                                <div class="col-12 my-3" v-for="sectionItem in menuSection.sectionMenu" v-bind:key="sectionItem.itemID">
                                    <div class="row">

                                        <!-- Item Image -->
                                        <div class="col-2 image-container text-center mx-auto">
                                            <router-link :to="{ path: '/listing/view/' + sectionItem.itemID['$oid'] }" class="default-text-no-background">
                                                <img :src=" 'data:image/jpeg;base64,' + (sectionItem.itemDetails['itemPhoto'] || defaultProfilePhoto)" style="width: 150px; height: 150px;">
                                            </router-link>
                                        </div>

                                        <!-- Item Information -->
                                        <div class="col-10">

                                            <!-- ------- START Item Info Header ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                            <!-- Item Info Header -->
                                            <div class="row">

                                                <!-- Item Name -->
                                                <div class="col-7">
                                                    <p class="fs-5 fw-bold text-start text-decoration-underline m-0" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">{{ sectionItem.itemDetails['itemName'] }}</p>
                                                </div>

                                                <!-- Bookmark: Have Tried -->
                                                <div v-if="viewerType == 'user'" class="col-2 pe-0">
                                                    <div v-html="checkDrinkLists(sectionItem.itemID['$oid']).buttons.haveTried" class="d-grid" @click="addToBookmarks('tried', sectionItem.itemID)"></div>
                                                </div>

                                                <!-- Bookmark: Want to Try -->
                                                <div v-if="viewerType == 'user'" class="col-2 ps-0">
                                                    <div v-html="checkDrinkLists(sectionItem.itemID['$oid']).buttons.wantToTry" class="d-grid" @click="addToBookmarks('want', sectionItem.itemID)"> </div>
                                                </div>

                                                <!-- Bookmark Icon -->
                                                <div v-if="viewerType == 'user'" class="col-1 text-end">
                                                    <svg v-if="userBookmarks.includes(sectionItem.itemID['$oid'])" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16"
                                                        data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(loadedListings.find(item => item._id['$oid'] === sectionItem.itemID['$oid']))">
                                                        <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
                                                    </svg>
                                                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16"
                                                        data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="populateBookmarkModal(loadedListings.find(item => item._id['$oid'] === sectionItem.itemID['$oid']))">
                                                        <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
                                                    </svg>
                                                </div>

                                            </div>

                                            <!-- ------- END Item Info Header / START Item Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->
                                            
                                            <!-- Item Details -->
                                            <div class="row">

                                                <!-- Item Producer / Drink Type / Type Category / ABV / Country / Description -->
                                                <div class="col-10">
                                                    <p class="text-start mb-1" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                                        <span v-if="sectionItem.itemDetails['itemProducer']">{{ sectionItem.itemDetails['itemProducer'] }} | </span>
                                                        <span v-if="sectionItem.itemDetails['itemType']">{{ sectionItem.itemDetails['itemType'] }} | </span>
                                                        <span v-if="sectionItem.itemDetails['itemTypeCategory']">{{ sectionItem.itemDetails['itemTypeCategory'] }} | </span>
                                                        <span v-if="sectionItem.itemDetails['itemABV']">{{ sectionItem.itemDetails['itemABV'] }} ABV | </span>
                                                        <span v-if="sectionItem.itemDetails['itemCountry']">{{ sectionItem.itemDetails['itemCountry'] }}</span>
                                                    </p>

                                                    <p class="text-start fst-italic mb-1" style="height: 50px; max-height: 50px; overflow-y: auto;">
                                                        <span v-if="sectionItem.itemDetails['itemDesc']">{{ sectionItem.itemDetails['itemDesc'] }}</span>
                                                    </p>
                                                </div>

                                                <!-- Item Rating -->
                                                <div class="col-2">
                                                    <p class="fs-3 fw-bold rating-text text-end">
                                                        {{ sectionItem.itemDetails['itemRating'] }}
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                        </svg>
                                                    </p>
                                                </div>

                                            </div>

                                            <!-- ------- END Item Details / START Item Menu Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                            <!-- Item Menu Details -->
                                            <div class="row">

                                                <!-- Item Price / Item Serving Type -->
                                                <div class="col-4">
                                                    <p class="text-start fs-5 fw-bold default-text-no-background">${{ sectionItem.itemPrice }} / {{ sectionItem.itemDetails.itemServingTypeName }}</p>
                                                </div>

                                                <!-- See User Reviews -->
                                                <div class="col-4">
                                                    <router-link :to="{ path: '/listing/view/' + sectionItem.itemID['$oid'] }">
                                                        <button type="button" class="btn primary-btn-outline-thick p-1 px-2"> See User Reviews </button>
                                                    </router-link>
                                                </div>

                                                <!-- Item Availability -->
                                                <div v-if="sectionItem.itemAvailability == false" class="col-4">
                                                    <p class="text-start fs-5 text-danger fw-bold fst-italic text-decoration-underline">Temporarily Unavailable</p>
                                                </div>

                                            </div>

                                            <!-- ------- END Item Menu Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                        </div>

                                    </div>
                                </div>
                                
                            </div>

                        </div>

                    </div>

                    <!-- ------- END Menu View (Not Editing) / START Menu View (Editing) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    <!-- Display when edit menu data is still loading -->
                    <div class="text-info-emphasis fst-italic fw-bold fs-5 my-5" v-if="editMenuMode && editMenuDataLoaded == false">
                        <span>Loading more data for menu edits, please wait...</span>
                        <br><br>
                        <div class="spinner-border" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                    
                    <!-- Menu View (Editing) -->
                    <div v-if="editMenuMode && editMenuDataLoaded" class="container text-start scrollable-listings">

                        <!-- No Menu Sections to Show -->
                        <div v-if="editMenu.length == 0" class="row my-4">
                            <p class="text-center fs-5 fst-italic m-0">No menu sections to show! Click "Add New Section" to get started.</p>
                        </div>

                        <!-- Message about Expanding / Collapsing Sections -->
                        <div v-else class="row my-2">
                            <p class="text-start fw-bold fst-italic m-0">
                                Click on each menu section's name to expand or hide its contents!
                            </p>
                        </div>

                        <!-- ------- START Menu Sections ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                        <!-- Menu Sections -->
                        <draggable v-model="editMenu" item-key="sectionOrder" @start="drag=true" @end="drag=false" v-bind="dragOptions">
                            <template #item="{element: menuSection}">

                                <div class="row mb-4">

                                    <!-- Section Name -->
                                    <div class="col-8 d-grid pe-0">
                                        <button type="button" class="btn secondary-btn-not-rounded rounded-end-0 fs-5 fw-bold text-start" data-bs-toggle="collapse" :data-bs-target="'#collapseEditMenuSection' + menuSection.sectionOrder" aria-expanded="true" :aria-controls="'collapseEditMenuSection' + menuSection.sectionOrder" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                            {{ menuSection.sectionName }}
                                        </button>
                                    </div>

                                    <!-- Reset Section Content Order -->
                                    <div class="col-2 d-grid p-0">
                                        <button type="button" class="btn secondary-btn-not-rounded rounded-0 px-0 text-end" @click="menuSection.sectionMenu.sort((a, b) => (a.itemOrder > b.itemOrder) ? 1 : -1);">
                                            (Reset Order)
                                        </button>
                                    </div>

                                    <!-- Edit Section Name -->
                                    <div class="col-1 d-grid p-0">
                                        <button type="button" class="btn secondary-btn-not-rounded rounded-0 px-0 text-end" data-bs-toggle="modal" data-bs-target="#renameMenuSectionModal" @click="populateRenameMenuSectionModal(menuSection.sectionOrder)">
                                            (Rename)
                                        </button>
                                    </div>

                                    <!-- Delete Section -->
                                    <div class="col-1 d-grid ps-0">
                                        <button type="button" class="btn secondary-btn-not-rounded rounded-start-0 px-0" @click="deleteMenuSection(menuSection.sectionOrder)">
                                            <svg xmlns='http://www.w3.org/2000/svg' width="20" height="20" fill='#f5f5f5' class="pb-1" viewBox='0 0 16 16'>
                                                <path d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/>
                                            </svg>
                                        </button>
                                    </div>

                                    <div class="collapse" :id="'collapseEditMenuSection' + menuSection.sectionOrder">

                                        <!-- No Section Contents to Show -->
                                        <div v-if="menuSection.sectionMenu.length == 0" class="col-12 my-3">
                                            <p class="text-center fst-italic m-0">No menu items to show! Search for a drink to add above.</p>
                                        </div>

                                        <!-- ------- START Section Contents ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                        <!-- Section Contents -->
                                        <draggable v-model="menuSection.sectionMenu" item-key="itemOrder" @start="drag=true" @end="drag=false" v-bind="dragOptions">
                                            <template #item="{element: menuItem}">

                                                <div class="col-12 my-3">
                                                    <div class="row">

                                                        <!-- Item Image -->
                                                        <div class="col-2 image-container text-center mx-auto">
                                                            <img :src=" 'data:image/jpeg;base64,' + (menuItem.itemDetails['itemPhoto'] || defaultProfilePhoto)" style="width: 150px; height: 150px;">
                                                        </div>

                                                        <!-- Item Information -->
                                                        <div class="col-10">

                                                            <!-- ------- START Item Info Header ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                                            <!-- Item Info Header -->
                                                            <div class="row">

                                                                <!-- Item Name -->
                                                                <div class="col-11">
                                                                    <p class="fs-5 fw-bold text-start text-decoration-underline m-0" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">{{ menuItem.itemDetails['itemName'] }}</p>
                                                                </div>

                                                                <!-- Remove Item From Menu Section -->
                                                                <div class="col-1 d-grid">
                                                                    <button type="button" class="btn-close" @click="deleteMenuItem(menuSection.sectionOrder, menuItem.itemOrder)"></button>
                                                                </div>

                                                            </div>

                                                            <!-- ------- END Item Info Header / START Item Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->
                                                            
                                                            <!-- Item Details -->
                                                            <div class="row">

                                                                <!-- Item Producer / Drink Type / Type Category / ABV / Country / Description -->
                                                                <div class="col-10">
                                                                    <p class="text-start mb-1" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                                                        <span v-if="menuItem.itemDetails['itemProducer']">{{ menuItem.itemDetails['itemProducer'] }} | </span>
                                                                        <span v-if="menuItem.itemDetails['itemType']">{{ menuItem.itemDetails['itemType'] }} | </span>
                                                                        <span v-if="menuItem.itemDetails['itemTypeCategory']">{{ menuItem.itemDetails['itemTypeCategory'] }} | </span>
                                                                        <span v-if="menuItem.itemDetails['itemABV']">{{ menuItem.itemDetails['itemABV'] }} ABV | </span>
                                                                        <span v-if="menuItem.itemDetails['itemCountry']">{{ menuItem.itemDetails['itemCountry'] }}</span>
                                                                    </p>

                                                                    <p class="text-start fst-italic mb-1" style="height: 50px; max-height: 50px; overflow-y: auto;">
                                                                        <span v-if="menuItem.itemDetails['itemDesc']">{{ menuItem.itemDetails['itemDesc'] }}</span>
                                                                    </p>
                                                                </div>

                                                                <!-- Item Rating -->
                                                                <div class="col-2">
                                                                    <p class="fs-3 fw-bold rating-text text-end">
                                                                        {{ menuItem.itemDetails['itemRating'] }}
                                                                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                                        </svg>
                                                                    </p>
                                                                </div>

                                                            </div>

                                                            <!-- ------- END Item Details / START Item Menu Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                                            <!-- Item Menu Details -->
                                                            <div class="row">

                                                                <!-- Toggle Item Availability -->
                                                                <div class="col-4">
                                                                    <div class="form-check form-switch form-check-inline">
                                                                        <input class="form-check-input" type="checkbox" role="switch"
                                                                        :id="'AvailCheck' + menuSection.sectionOrder + menuItem.itemOrder + menuItem.itemDetails.itemName"
                                                                        :name="'AvailCheck' + menuSection.sectionOrder + menuItem.itemOrder + menuItem.itemDetails.itemName"
                                                                        v-model="menuItem.itemAvailability">
                                                                        <label v-if="menuItem.itemAvailability" class="form-check-label text-success fst-italic" :for="'AvailCheck' + menuSection.sectionOrder + menuItem.itemOrder + menuItem.itemDetails.itemName">
                                                                            Item Available
                                                                        </label>
                                                                        <label v-if="!menuItem.itemAvailability" class="form-check-label text-danger fst-italic" :for="'AvailCheck' + menuSection.sectionOrder + menuItem.itemOrder + menuItem.itemDetails.itemName">
                                                                            Temporarily Unavailable
                                                                        </label>
                                                                    </div>
                                                                </div>

                                                                <!-- Edit Item Price -->
                                                                <div class="col-3">
                                                                    <div class="input-group">
                                                                        <span class="input-group-text fw-bold">$</span>
                                                                        <input type="number" class="form-control" v-model="menuItem.itemPrice" placeholder="0" min="0" step="0.01">
                                                                    </div>
                                                                </div>

                                                                <!-- Edit Item Serving Type -->
                                                                <div class="col-5">
                                                                    <div class="input-group">
                                                                        <span class="input-group-text fw-bold">/</span>
                                                                        <select class="form-select" v-model="menuItem.itemServingType">
                                                                            <option v-for="servingType in servingTypes" :key="servingType._id" :value="servingType._id">{{ servingType.servingType }}</option>
                                                                        </select>
                                                                    </div>
                                                                </div>
                                                                

                                                            </div>

                                                            <!-- ------- END Item Menu Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                                        </div>

                                                    </div>
                                                </div>

                                            </template>
                                        </draggable>

                                        <!-- ------- END Section Contents ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->
                                        
                                    </div>

                                </div>

                            </template>
                        </draggable>

                        <!-- ------- END Menu Sections / START Menu Item Modal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                        <!-- Add Menu Item Modal -->
                        <div class="modal fade" id="addMenuItemModal" tabindex="-1" aria-labelledby="addMenuItemModal" aria-hidden="true">
                            <div class="modal-dialog modal-xl">
                                <div class="modal-content">

                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="addMenuItemModalLabel">Add Menu Item</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>

                                    <!-- Modal Body -->
                                    <div class="modal-body">

                                        <!-- Note -->
                                        <p class="fst-italic text-primary-emphasis">All newly added menu items are:<br>- set as "Available" at $0 / serving<br>- set to appear last in your selected target section.<br>Please modify them to your own satisfaction later!</p>

                                        <!-- [input] bottle name -->
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Bottle Listing ID (Search by Name) <span class="text-danger">*</span></p>
                                            <input list="newMenuItemList" v-model="newMenuItemID" class="form-control" id="newMenuItemID" placeholder="Enter a Drink to Add to Menu" @change="updateNewMenuItemTarget">
                                            <datalist id="newMenuItemList">
                                                <option v-for="listing in allListings" :key="listing._id.$oid" :value="listing._id.$oid">
                                                    {{ listing.listingName }} (Producer: {{ listing.producerName }})
                                                </option>
                                            </datalist>
                                            <p v-show="newMenuItemID.length > 0" class="text-start mb-1 text-danger" id="newMenuItemTargetError"></p>
                                        </div>

                                        <!-- [input] target menu section -->
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Target Menu Section <span class="text-danger">*</span></p>
                                            <select class="form-select" aria-label="newMenuItemTargetSection" v-model="newMenuItemTargetSection" @change="updateNewMenuItemTargetSection">
                                                <option v-for="(menuSection, sectionIndex) in editMenu" v-bind:key="menuSection" v-bind:value="menuSection"> 
                                                    #{{ sectionIndex }}: {{ menuSection.sectionName }} 
                                                </option>
                                            </select>
                                            <p v-show="Object.keys(this.newMenuItemTargetSection).length !== 0" class="text-start mb-1 text-danger" id="newMenuItemTargetSectionError"></p>
                                            <p v-show="Object.keys(this.newMenuItemTargetSection).length !== 0" class="text-start mb-1 text-warning-emphasis fst-italic" id="newMenuItemTargetSectionNotice"></p>
                                        </div>

                                        <!-- ------- START Menu Item Preview ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                        <!-- Menu Item Preview -->
                                        <div v-if="Object.keys(this.newMenuItemTarget).length !== 0" class="col-12 my-3">
                                            <hr>
                                            <p class="text-secondary-emphasis fw-bold fst-italic">Menu Item Preview:</p>

                                            <div class="row">

                                                <!-- Item Image -->
                                                <div class="col-2 image-container text-center mx-auto">
                                                    <img :src=" 'data:image/jpeg;base64,' + ( newMenuItemTarget.photo || defaultProfilePhoto)" style="width: 150px; height: 150px;">
                                                </div>

                                                <!-- Item Information -->
                                                <div class="col-10">

                                                    <!-- Item Name -->
                                                    <div class="row">
                                                        <div class="col-7">
                                                            <p class="fs-5 fw-bold text-start text-decoration-underline m-0" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">{{ newMenuItemTarget.listingName }}</p>
                                                        </div>
                                                    </div>

                                                    <!-- Item Details -->
                                                    <div class="row">

                                                        <!-- Item Producer / Drink Type / Type Category / ABV / Country / Description -->
                                                        <div class="col-10">
                                                            <p class="text-start mb-1" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                                                <span v-if="newMenuItemTarget.producerName">{{ newMenuItemTarget.producerName }} | </span>
                                                                <span v-if="newMenuItemTarget.drinkType">{{ newMenuItemTarget.drinkType }} | </span>
                                                                <span v-if="newMenuItemTarget.typeCategory">{{ newMenuItemTarget.typeCategory }} | </span>
                                                                <span v-if="newMenuItemTarget.abv">{{ newMenuItemTarget.abv }} ABV | </span>
                                                                <span v-if="newMenuItemTarget.originCountry">{{ newMenuItemTarget.originCountry }}</span>
                                                            </p>

                                                            <p class="text-start fst-italic mb-1" style="height: 50px; max-height: 50px; overflow-y: auto;">
                                                                <span v-if="newMenuItemTarget.officialDesc">{{ newMenuItemTarget.officialDesc }}</span>
                                                            </p>
                                                        </div>

                                                        <!-- Item Rating -->
                                                        <div class="col-2">
                                                            <p class="fs-3 fw-bold rating-text text-end">
                                                                {{ newMenuItemTarget.avgRating }}
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                                                    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                                </svg>
                                                            </p>
                                                        </div>

                                                    </div>

                                                    <!-- Item Menu Details -->
                                                    <div class="row">

                                                        <!-- Item Price / Item Serving Type -->
                                                        <div class="col-4">
                                                            <p class="text-start fs-5 fw-bold default-text-no-background">$0 / Serving</p>
                                                        </div>

                                                        <!-- See User Reviews -->
                                                        <div class="col-4">
                                                            <button type="button" class="btn primary-btn-outline-thick p-1 px-2"> See User Reviews </button>
                                                        </div>

                                                    </div>

                                                </div>

                                            </div>
                                        </div>

                                        <!-- ------- END Menu Item Preview ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                                    </div>

                                    <!-- Modal Footer -->
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="newMenuItemTargetSection = {}; newMenuItemTarget = {} ; newMenuItemID = ''">Cancel</button>
                                        <button type="button" class="btn tertiary-btn rounded reverse-clickable-text" data-bs-dismiss="modal" @click="addMenuItem"
                                            v-bind:disabled="Object.keys(newMenuItemTargetSection).length === 0 || Object.keys(newMenuItemTarget).length === 0">
                                            Add Item
                                        </button>
                                    </div>

                                </div>
                            </div>
                        </div>

                        <!-- ------- END Menu Item Modal / START Rename Menu Section Modal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                        <!-- Rename Menu Section Modal -->
                        <div class="modal fade" id="renameMenuSectionModal" tabindex="-1" aria-labelledby="renameMenuSectionModal" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">

                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="renameMenuSectionModalLabel">Rename Menu Section</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>

                                    <!-- Modal Body -->
                                    <div class="modal-body">
                                        <label class="form-check-label" for="renameMenuSectionInput">Original Section Name: <span class="fw-bold fst-italic">{{ renameMenuSectionModalOld }}</span></label>
                                        <input id="renameMenuSectionInput" type="text" class="form-control" v-model="renameMenuSectionModalNew" placeholder="New Section Name">
                                    </div>

                                    <!-- Modal Footer -->
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="renameMenuSection">Save</button>
                                    </div>

                                </div>
                            </div>
                        </div>

                        <!-- ------- END Rename Menu Section Modal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                    </div>

                    <!-- ------- END Menu View (Editing) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                </div>

                <!-- ------- END Bar Menu ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

            </div>

            <!-- ------- END Venue Information / START Venue Sidebar ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

            <!-- Venue Sidebar -->
            <div class="col-3">

                <!-- ------- START View Analytics ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- View Analytics Button (Venue) -->
                <div v-if="selfView" class="row">
                    <router-link class="d-grid pb-3 text-decoration-none" :to="{ path: '/dashboard/venue' }">
                        <button type="button" class="btn secondary-btn-not-rounded rounded-0"> View My Analytics </button>
                    </router-link>
                </div>

                <!-- View Analytics Button (Admin) -->
                <div v-if="powerView" class="row">
                    <router-link class="d-grid pb-3 text-decoration-none" :to="{ path: '/dashboard/venue/' + targetVenue._id['$oid'] }">
                        <button type="button" class="btn secondary-btn-not-rounded rounded-0"> View Venue's Analytics </button>
                    </router-link>
                </div>

                <!-- ------- END View Analytics / START Q & A ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Q & A -->
                <div class="row">
                    <div class="col-12">
                        <div class="square primary-square rounded p-3 mb-3">

                            <!-- Header -->
                            <div class="square-inline text-start">

                                <!-- [if] Self Venue -->
                                <div v-if="selfView" class="mr-auto">
                                    <h4> Q&A for You! </h4>
                                    <router-link :to="{ path: '/Venues/VenuesQA/' + targetVenue._id['$oid'] }" class="default-text-no-background">
                                        <p class="reverse-text no-margin text-decoration-underline text-start pb-2"> View All </p>
                                    </router-link>
                                </div>

                                <!-- [else] -->
                                <h4 v-else class="mr-auto"> Q&As for {{ targetVenue["venueName"] }} </h4>

                            </div>

                            <!-- Buttons for Answered/Unanswered Questions -->
                            <div v-if="selfView" class="row text-center px-2">
                                <div class="col-6 d-grid gap-0 no-padding">
                                    <button type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="qaMode = 'answered'">
                                        Answered
                                    </button>
                                </div>
                                <div class="col-6 d-grid gap-0 no-padding">
                                    <button type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="qaMode = 'unanswered'">
                                        Unanswered
                                    </button>
                                </div>
                            </div>

                            <!-- Q & A Content -->
                            <div class="text-start pt-2 py-1">
                                <div class="carousel slide" id="carouselQA">
                                    <div class="carousel-inner px-4">

                                        <!-- [if] Self Venue -->
                                        <div v-if="selfView">

                                            <!-- Answered Questions -->
                                            <div v-if="qaMode == 'answered'">
                                                <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                                    <p class="fw-bold">Q: {{ qa["question"] }}</p>
                                                    <p> A: {{ qa["answer"] }} </p>
                                                </div>
                                            </div>

                                            <!-- Unanswered Questions -->
                                            <div v-if="qaMode == 'unanswered'">
                                                <div class="carousel-item" v-for="(qa, index) in unansweredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                                    <p class="fw-bold">Q: {{ qa["question"] }}</p>
                                                    <div class="input-group centered pt-2">
                                                        <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Respond to your fans' latest questions." v-model="qaAnswer"></textarea>
                                                        <div @click="sendAnswer(qa)" class="send-icon ps-1">
                                                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                            </svg>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                        </div>

                                        <!-- [else] Other Viewers -->
                                        <div v-else>

                                            <!-- Answered Questions -->
                                            <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa._id" v-bind:class="{ 'active': index === 0 }">
                                                <p class="fw-bold">Q: {{ qa["question"] }}</p>
                                                <p> A: {{ qa["answer"] }} </p>
                                                
                                                <!-- Ask Question -->
                                                <div class="input-group centered pt-2">
                                                    <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask a question!" v-model="qaQuestion"></textarea>
                                                    <div @click="sendQuestion" class="send-icon ps-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- If No Answered Questions -->
                                            <div v-if="answeredQuestions.length === 0">
                                                <!-- Ask Question -->
                                                <div class="input-group centered pt-2">
                                                    <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask a question!" v-model="qaQuestion"></textarea>
                                                    <div @click="sendQuestion" class="send-icon ps-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </div>

                                        </div>

                                    </div>

                                    <!-- Carousel Control Buttons -->
                                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselQA" data-bs-slide="prev">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Previous</span>
                                    </button>
                                    <button class="carousel-control-next" type="button" data-bs-target="#carouselQA" data-bs-slide="next">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Next</span>
                                    </button>

                                </div>
                            </div>

                        </div>
                    </div>
                </div>

                <!-- ------- END Q & A / START Map View ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Map View -->
                <div class="row">
                    <div class="col-12">
                        <div class="square secondary-square rounded p-3 mb-3">

                            <!-- Header -->
                            <h4 class="text-start"> Venue Location </h4>
                            <p class="text-start mb-1 fst-italic">{{ targetVenue["address"] }}</p>

                            <!-- Map -->
                            <GMapMap
                                :center="{lat: mapLat, lng: mapLong}"
                                :zoom="15"
                                map-type-id="terrain"
                                style="width: 100%; height: 200px"
                            >
                                <GMapMarker
                                    :key="index"
                                    v-for="(m, index) in mapMarkers"
                                    :position="m.position"
                                />
                            </GMapMap>

                        </div>
                    </div>
                </div>

                <!-- ------- END Map View / START Opening Hours + Reservation Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

                <!-- Opening Hours + Reservation Details -->
                <div class="row">
                    <div class="col-12">
                        <div class="square secondary-square rounded p-3 mb-3">

                            <!-- Header -->
                            <div class="square-inline text-start">
                                <h4 class="mr-auto"> Opening Hours and Reservation Details </h4>
                            </div>

                            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

                            <!-- Opening Hours -->
                            <div class="py-2 text-start">

                                <!-- Section Header -->
                                <div class="square-inline">
                                    <h5 class="mr-auto"> Opening Hours </h5>
                                </div>

                                <!-- Buttons -->
                                <div class="pb-1" v-if="selfView">
                                    <!-- [if] not editing -->
                                    <button v-if="!editOpeningHours" type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="editOpeningHours = true; checkOpeningHours()">
                                        Edit
                                    </button>
                                    
                                    <!-- [else] if editing -->
                                    <button v-if="editOpeningHours" type="button" class="btn success-btn rounded-0 reverse-clickable-text" @click="saveOpeningHours" :disabled="editOpeningHoursError">
                                        Save
                                    </button>
                                    <button v-if="editOpeningHours" type="button" class="btn secondary-btn rounded-0 reverse-clickable-text ms-1" @click="editOpeningHours = false">
                                        Cancel
                                    </button>
                                    <button v-if="editOpeningHours" type="button" class="btn btn-danger rounded-0 reverse-clickable-text ms-1" @click="newOpeningHours = JSON.parse(JSON.stringify(openingHours)); checkOpeningHours()">
                                        Reset
                                    </button>
                                </div>

                                <!-- Section Content (Edit Mode) -->
                                <div v-if="editOpeningHours">
                                    <div class="default-text-no-background" v-for = "(hours, day) in newOpeningHours" v-bind:key="day">
                                        <span class="fw-bold">{{ day }}: </span>
                                        <div class="pb-1">
                                            <div class="d-flex align-items-center">
                                                <input type="time" class="form-control" :id="day + 'start'" v-model="hours[0]" @change="checkOpeningHours">
                                                <span class="mx-2">-</span>
                                                <input type="time" class="form-control" :id="day + 'end'" v-model="hours[1]" @change="checkOpeningHours">
                                            </div>
                                            <!-- for error message -->
                                            <span :id="day + 'error'" class="text-danger ms-1 fst-italic d-none"></span>
                                        </div>
                                    </div>
                                </div>

                                <!-- Section Content (View Mode) -->
                                <div v-else>
                                    <div class="default-text-no-background" v-for = "(hours, day) in openingHours" v-bind:key="day">
                                        <span class="fw-bold">{{ day }}: </span>
                                        <p class="d-inline">{{ hours[0] }} - {{ hours[1] }}</p>
                                    </div>
                                </div>

                            </div>

                            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

                            <!-- Public Holidays -->
                            <div class="py-2 text-start">

                                <!-- Section Header -->
                                <div class="square-inline">
                                    <h5 class="mr-auto"> Public Holiday Information </h5>
                                </div>

                                <!-- Buttons -->
                                <div class="pb-1" v-if="selfView">
                                    <!-- [if] not editing -->
                                    <button v-if="!editPublicHolidays" type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="editPublicHolidays = true">
                                        Edit
                                    </button>
                                    
                                    <!-- [else] if editing -->
                                    <button v-if="editPublicHolidays" type="button" class="btn success-btn rounded-0 reverse-clickable-text" @click="savePublicHolidays">
                                        Save
                                    </button>
                                    <button v-if="editPublicHolidays" type="button" class="btn secondary-btn rounded-0 reverse-clickable-text ms-1" @click="editPublicHolidays = false">
                                        Cancel
                                    </button>
                                    <button v-if="editPublicHolidays" type="button" class="btn btn-danger rounded-0 reverse-clickable-text ms-1" @click="newPublicHolidays = targetVenue['publicHolidays']">
                                        Reset
                                    </button>
                                </div>

                                <!-- Section Content (Edit Mode) -->
                                <div v-if="editPublicHolidays">
                                    <textarea v-model="newPublicHolidays" class="form-control" id="publicHolidaysTextArea" rows="3" placeholder="Enter public holiday information"></textarea>
                                </div>

                                <!-- Section Content (View Mode) -->
                                <div v-else>
                                    <div class="text-body-secondary">
                                        <div v-if="targetVenue['publicHolidays'] == ''" class="fst-italic">
                                            No information about public holiday opening hours!
                                        </div>
                                        <div v-else>
                                            {{ targetVenue["publicHolidays"] }}
                                        </div>
                                    </div>
                                </div>
                                
                            </div>

                            <!-- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->
                            
                            <!-- Reservation Details -->
                            <div class="py-2 text-start">

                                <!-- Section Header -->
                                <div class="square-inline">
                                    <h5 class="mr-auto"> Reservation Details </h5>
                                </div>

                                <!-- Buttons -->
                                <div class="pb-1" v-if="selfView">
                                    <!-- [if] not editing -->
                                    <button v-if="!editReservationDetails" type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text" @click="editReservationDetails = true">
                                        Edit
                                    </button>
                                    
                                    <!-- [else] if editing -->
                                    <button v-if="editReservationDetails" type="button" class="btn success-btn rounded-0 reverse-clickable-text" @click="saveReservationDetails">
                                        Save
                                    </button>
                                    <button v-if="editReservationDetails" type="button" class="btn secondary-btn rounded-0 reverse-clickable-text ms-1" @click="editReservationDetails = false">
                                        Cancel
                                    </button>
                                    <button v-if="editReservationDetails" type="button" class="btn btn-danger rounded-0 reverse-clickable-text ms-1" @click="newReservationDetails = targetVenue['reservationDetails']">
                                        Reset
                                    </button>
                                </div>

                                <!-- Section Content (Edit Mode) -->
                                <div v-if="editReservationDetails">
                                    <textarea v-model="newReservationDetails" class="form-control" id="reservationDetailsTextArea" rows="3" placeholder="Enter reservation details"></textarea>
                                </div>

                                <!-- Section Content (View Mode) -->
                                <div v-else>
                                    <div class="text-body-secondary">
                                        <div v-if="targetVenue['reservationDetails'] == ''" class="fst-italic">
                                            No reservation details available!
                                        </div>
                                        <div v-else>
                                            {{ targetVenue["reservationDetails"] }}
                                        </div>
                                    </div>
                                </div>
                                
                            </div>

                        </div>
                    </div>
                </div>

                <!-- ------- END Opening Hours + Reservation Details ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

            </div>

            <!-- ------- END Venue Sidebar / START Bookmark Modal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

            <!-- Bookmark Modal -->
            <div v-if="viewerType == 'user'" class="modal fade" id="bookmarkModal" tabindex="-1" aria-labelledby="bookmarkModal" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">

                        <!-- Modal Header -->
                        <div class="modal-header">
                            <h1 class="text-start modal-title fs-5" id="bookmarkModalTitle">Save to List(s): {{ bookmarkModalTarget.listingName }}</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>

                        <!-- Modal Body -->
                        <div class="modal-body text-start">

                            <!-- Existing Lists -->
                            <div class="form-check" v-for="(listItems, listName) in userInfo.drinkLists" :key="listName">
                                <input class="form-check-input" type="checkbox" :value="listName" :id="listName" v-model="selectedBookmarkList">
                                <label class="form-check-label" :for="listName">{{ listName }}</label>
                            </div>

                            <!-- New List -->
                            <div class="form-check mt-3">
                                <input class="form-check-input" type="checkbox" value="saveToNewList" id="saveToNewList" v-model="saveToNewList">
                                <label class="form-check-label" for="saveToNewList">Create New List</label>

                                <!-- Input New List Name -->
                                <div v-if="saveToNewList">
                                    <div class="mt-2">New List Name</div>
                                    <input type="text" class="form-control" v-model="othersListName" placeholder="New List Name">
                                    <div v-if="othersListNameError" class="text-danger text-sm">
                                        *{{ othersListNameError }}
                                    </div>
                                </div>
                            </div>

                        </div>

                        <!-- Modal Footer -->
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" @click="bookmarkItem">Save Changes</button>
                        </div>

                    </div>
                </div>
            </div>

            <!-- ------- END Bookmark Modal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -->

        </div>
    </div>
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import draggable from 'vuedraggable';

    export default {
        name: 'profileVenue',
        components: {
            NavBar,
            draggable
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        data() {
            return {
                drag: false,
                // Info
                viewerID: localStorage.getItem('88B_accID'),
                viewerType: localStorage.getItem('88B_accType'),
                targetVenue: '',
                currentURL: window.location.href,

                // Data
                servingTypes: [],
                loadedListings: [],
                loadedProducers: [],
                mostPopular: [],
                mostDiscussed: [],
                recentlyAdded: [],
                answeredQuestions: [],
                unansweredQuestions: [],
                openingHours: {},
                detailedMenu: [],

                // flags
                dataLoaded: false,
                venueExists: null,
                contentMode: 'overview',
                qaMode: 'answered',
                loggedIn: false,
                selfView: false,
                powerView: false,
                editProfile: false,
                clipboardItem: false,

                // Editable fields
                editVenueName: '',
                editVenueDesc: '',
                editCountry: '',
                qaQuestion: '',
                qaAnswer: '',

                // Profile Photo
                editProfilePhoto: '',
                defaultProfilePhoto: '',

                // Updates
                newUpdateText: '',
                newUpdatePhoto: '',
                showMoreUpdates: false,

                // Map View
                mapLat: null,
                mapLong: null,
                mapMarkers: [],

                // Opening Hours + Public Holidays + Reservation Details
                editOpeningHours: false,
                editOpeningHoursError: false,
                newOpeningHours: {},
                editPublicHolidays: false,
                newPublicHolidays: "",
                editReservationDetails: false,
                newReservationDetails: "",

                // User Features
                userInfo: {},
                userFollowing: false,
                userBookmarks: [],
                bookmarkModalTarget: {},
                selectedBookmarkList: [],
                saveToNewList: false,
                othersListName: '',
                othersListNameError: '',

                // Search + Sort Menu
                searchMenuResults: [],
                searchMenuTerm: '',
                sortMenuTerm: '',
                sortMenuOptions: [
                    'Alphabetical (A-Z)',
                    'Alphabetical (Z-A)',
                    'Rating (Low to High)',
                    'Rating (High to Low)',
                    'Price (Low to High)',
                    'Price (High to Low)',
                ],

                // Menu Editing
                editMenuMode: false,
                editMenuDataLoaded: false,
                allListings: [],
                editMenu: [],
                newMenuItemID: '',
                newMenuItemTarget: {},
                newMenuItemTargetSection: {},
                renameMenuSectionModalTarget: {},
                renameMenuSectionModalOld: '',
                renameMenuSectionModalNew: '',

                // Report Menu Inaccuracy
                reportFormView: true,
                reportSubmitLoading: false,
                reportSubmitSuccess: false,
                reportSubmitError: null,
                reportSection: '',
                reportSectionItems: [],
                reportItem: '',
                reportReason: '',
                reportItemNone: false,
                reportReasonNone: false,
                reportResponseCode: null,
                
            }
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        computed: {
            dragOptions() {
                return {
                    animation: 350,
                    group: "menuSections",
                    disabled: false,
                    ghostClass: "ghost"
                };
            }
        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        mounted() {

            // Check if route params "venueID" is present
            if (this.$route.params.venueID != "" && this.$route.params.venueID != undefined) {
                this.targetVenue = this.$route.params.venueID;

                // If logged in as a venue, check if the venueID matches the logged in venue's ID
                if (this.viewerType == 'venue' && this.viewerID == this.targetVenue) {
                    this.selfView = true;
                }
            }
            // If no venueID is specified, display logged in venue's profile page
            else if (this.viewerType == 'venue') {
                this.targetVenue = this.viewerID;
                this.selfView = true;
                this.currentURL = this.currentURL + '/' + this.targetVenue;
            }
            // If not logged in as a venue, redirect to your own profile page / login
            else {
                this.$router.push('/login');
            }

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Obtain venue data
            if (this.targetVenue != "" && this.targetVenue != undefined) {
                this.getVenueData();
            }
            else {
                this.venueExists = false;
            }

        },
        // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        methods: {
            // Obtain venue data
            async getVenueData() {
                try {
                    const response = await this.$axios.get('http://127.0.0.1:5000/getVenue/' + this.targetVenue);

                    if (response != null && response.data != null && response.data != "" && !(Array.isArray(response.data) && response.data.length == 0)) {

                        this.targetVenue = response.data;

                        // Set editable data
                        this.editProfilePhoto = this.targetVenue["photo"];
                        this.editVenueName = this.targetVenue["venueName"];
                        this.editVenueDesc = this.targetVenue["venueDesc"];
                        this.editCountry = this.targetVenue["originLocation"];
                        this.newPublicHolidays = this.targetVenue["publicHolidays"];
                        this.newReservationDetails = this.targetVenue["reservationDetails"];

                        // Set questions and answers data
                        let qaData = this.targetVenue["questionsAnswers"];
                        if (qaData.length > 0) {
                            for (let qa in qaData) {
                                let answer = qaData[qa]["answer"];
                                if (answer != "") {
                                    this.answeredQuestions.push(qaData[qa]);
                                }
                                else {
                                    this.unansweredQuestions.push(qaData[qa]);
                                }
                            }
                        }

                        // Set and sort opening hours data
                        this.openingHours = this.targetVenue["openingHours"];
                        const dayOrder = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
                        const sortedOpeningHours = Object.fromEntries(
                            dayOrder
                                .filter(key => key in this.openingHours) // Filter keys that exist in this.openingHours
                                .map(key => [key, this.openingHours[key]]) // Map each key to its corresponding value
                        );
                        this.openingHours = sortedOpeningHours;
                        this.newOpeningHours = JSON.parse(JSON.stringify(this.openingHours));

                        // Set and sort menu data
                        this.detailedMenu = this.targetVenue["menu"];
                        this.detailedMenu.sort((a, b) => (a.sectionOrder > b.sectionOrder) ? 1 : -1); // Sort by section order
                        for (let section of this.detailedMenu) {
                            section.sectionMenu.sort((a, b) => (a.itemOrder > b.itemOrder) ? 1 : -1); // Sort by item order
                        }

                        // Format updates
                        if (this.targetVenue["updates"].length > 0) {
                            for (let update of this.targetVenue["updates"]) {
                                update.date = update.date['$date'].split('T')[0].split('-').reverse().join('/');
                            }
                        }

                        // Obtain servingTypes
                        const servingTypesResponse = await this.$axios.get('http://127.0.0.1:5000/getServingTypes');
                        this.servingTypes = servingTypesResponse.data;

                        // Obtain map data
                        const mapResponse = await this.$axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                            params: {
                                address: this.targetVenue["address"],
                                key: 'AIzaSyD5aukdDYDbnc8BKjFF_YjApx-fUe515Hs'
                            }
                        });
                        const { lat, lng } = mapResponse.data.results[0].geometry.location;
                        this.mapLat = lat;
                        this.mapLong = lng;
                        this.mapMarkers = [{ position: { lat, lng } }];

                        this.venueExists = true;
                        this.loadData();
                    }
                    else {
                        this.venueExists = false;
                    }
                }
                catch (error) {
                    this.dataLoaded = null;
                }
            },

            // Load other data
            async loadData() {

                // Get listing data for each item in menu
                try {

                    for (let section of this.detailedMenu) {
                        for (let item of section.sectionMenu) {

                            // Find item in loadedListings
                            let listingData = this.loadedListings.find(i => i._id['$oid'] == item.itemID['$oid']);

                            // If not found, get from server
                            if (listingData == undefined) {
                                let response = await this.$axios.get('http://127.0.0.1:5000/getListing/' + item.itemID['$oid']);
                                listingData = response.data;

                                if (Array.isArray(listingData) && listingData.length == 0) {
                                    // Remove item from section
                                    section.sectionMenu = section.sectionMenu.filter(i => i.itemID['$oid'] != item.itemID['$oid']);
                                }
                                // If found, obtain additional data and add to loadedListings
                                else if (listingData != null && listingData != "") {

                                    // Get reviews
                                    let reviewResponse = await this.$axios.get('http://127.0.0.1:5000/getReviewByTarget/' + item.itemID['$oid']);
                                    let reviewData = reviewResponse.data;

                                    if (Array.isArray(reviewData) && reviewData.length == 0) {
                                        listingData["reviews"] = [];
                                        listingData["avgRating"] = 0;
                                    }
                                    else if (reviewData != null && reviewData != "") {
                                        listingData["reviews"] = reviewData;
                                        listingData["avgRating"] = reviewData.reduce((a, b) => a + b.rating, 0) / reviewData.length;
                                    }
                                    else {
                                        // Error
                                        throw "Error: Unexpected response from server!";
                                    }

                                    // Find producer in loadedProducers
                                    let producerData = this.loadedProducers.find(p => p._id['$oid'] == listingData["producerID"]['$oid']);

                                    // If not found, get from server
                                    if (producerData == undefined) {
                                        let producerResponse = await this.$axios.get('http://127.0.0.1:5000/getProducer/' + listingData["producerID"]['$oid']);
                                        producerData = producerResponse.data;

                                        if (Array.isArray(producerData) && producerData.length == 0) {
                                            // Remove item from section
                                            section.sectionMenu = section.sectionMenu.filter(i => i.itemID['$oid'] != item.itemID['$oid']);
                                        }
                                        // If found, add to loadedProducers
                                        else if (producerData != null && producerData != "") {
                                            this.loadedProducers.push(producerData);
                                        }
                                        else {
                                            // Error
                                            throw "Error: Unexpected response from server!";
                                        }
                                    }

                                    // Set producer data (producerData should either be valid or [] here)
                                    if (!(Array.isArray(producerData) && producerData.length == 0)) {
                                        listingData["producerName"] = producerData["producerName"];

                                        // Add to loadedListings
                                        this.loadedListings.push(listingData);
                                    }
                                    else {
                                        listingData = [];
                                    }
                                    
                                }
                                else {
                                    // Error
                                    throw "Error: Unexpected response from server!";
                                }
                            }

                            // Set item data (listingData should either be valid or [] here)
                            if (!(Array.isArray(listingData) && listingData.length == 0)) {

                                item.itemDetails = {
                                    itemPhoto: listingData["photo"],
                                    itemName: listingData["listingName"],
                                    itemType: listingData["drinkType"],
                                    itemTypeCategory: listingData["typeCategory"],
                                    itemABV: listingData["abv"],
                                    itemCountry: listingData["originCountry"],
                                    itemDesc: listingData["officialDesc"],
                                    itemRating: listingData["avgRating"],
                                    itemProducer: listingData["producerName"]
                                };

                                // Get serving type name
                                let servingTypeData = this.servingTypes.find(s => s._id['$oid'] == item["itemServingType"]['$oid']);
                                if (servingTypeData != undefined) {
                                    item.itemDetails.itemServingTypeName = servingTypeData["servingType"];
                                }
                                else {
                                    item.itemDetails.itemServingTypeName = "(Unknown)";
                                }

                            }

                        }
                    }

                    // Obtain mostPopular listings
                    this.mostPopular = this.loadedListings.sort((a, b) => (a.avgRating < b.avgRating) ? 1 : -1).slice(0, 5);

                    // Obtain mostDiscussed listings
                    this.mostDiscussed = this.loadedListings.sort((a, b) => (a.reviews.length < b.reviews.length) ? 1 : -1).slice(0, 5);

                    // Obtain recentlyAdded listings
                    this.recentlyAdded = this.loadedListings.sort((a, b) => (Date.parse(a.addedDate) < Date.parse(b.addedDate)) ? 1 : -1).slice(0, 5);

                    // Set editMenu and searchMenuResults
                    this.resetEditMenu();
                    this.searchMenuResults = this.detailedMenu;
                    
                }
                catch (error) {
                    this.dataLoaded = null;
                }

                // Check if viewer is logged in
                if (this.viewerID != null && this.viewerID != "") {
                    this.loggedIn = true;

                    // Check if viewer is a user and get their data
                    if (this.viewerType == 'user') {
                        try {
                            const response = await this.$axios.get('http://127.0.0.1:5000/getUser/' + this.viewerID);
                            if (Array.isArray(response.data) && response.data.length == 0) {
                                throw "User not found!";
                            }
                            
                            else {
                                this.userInfo = response.data;

                                // Check if user is admin
                                if (this.userInfo.isAdmin == true) {
                                    this.powerView = true;
                                }

                                // Check if user is following venue
                                this.userFollowing = JSON.stringify(this.userInfo.followLists.venues).includes(JSON.stringify({$oid: this.targetVenue._id['$oid']}));

                                // Get user's bookmarks
                                for (let drinkList in this.userInfo.drinkLists) {
                                    for (let item of this.userInfo.drinkLists[drinkList].listItems) {
                                        this.userBookmarks.push(item[1]['$oid']);
                                    }
                                }
                                
                            }
                        }
                        catch (error) {
                            this.dataLoaded = null;
                        }
                    }
                }

                // Set data loaded flag
                if (this.dataLoaded != null) {
                    this.dataLoaded = true;
                }
            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            // Helper function to handle file selection for profile photo
            handleFileSelectPFP(event){
                try {
                    const file = event.target.files[0];
                    const reader = new FileReader;
                    
                    reader.onload = () => {
                        const base64String = reader.result.split(',')[1];
                        this.editProfilePhoto = base64String
                    };
                    
                    reader.readAsDataURL(file);
                }
                catch (error) {
                    // console.error(error);
                }
            },

            // Helper function to handle file selection for new update photo
            handleFileSelectUpdate(event){
                try {
                    const file = event.target.files[0];
                    const reader = new FileReader;
                    
                    reader.onload = () => {
                        const base64String = reader.result.split(',')[1];
                        this.newUpdatePhoto = base64String
                    };
                    
                    reader.readAsDataURL(file);
                }
                catch (error) {
                    // console.error(error);
                }
            },

            // Claim Venue Account
            claimVenueAccount() {
                let accountDetails = {
                    userID: this.$route.params.venueID,
                    businessType: "venue",
                    businessName: this.targetVenue.venueName,
                    businessDesc: this.targetVenue.venueDesc,
                    businessLink: this.$route.fullPath,
                    originCountry: this.targetVenue.originLocation,
                }
                this.$router.push({
                    path: '/BusinessSignup', 
                    query: accountDetails
                });
            },

            // Copy to Clipboard
            copyToClipboard(text) {
                navigator.clipboard.writeText(text)
                .then(() => {
                    this.clipboardItem = true;
                    setTimeout(() => {
                        this.clipboardItem = false;
                    }, 3000);
                })
                .catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            },

            // Search Menu
            searchMenu() {

                // Trim search term, set to lowercase. If empty, set searchMenuResults to detailedMenu
                this.searchMenuTerm = this.searchMenuTerm.trim().toLowerCase();
                if (this.searchMenuTerm == '') {
                    this.searchMenuResults = this.detailedMenu;
                }
                else {
                    // Reset searchMenuResults
                    this.searchMenuResults = [];

                    // Filter sections
                    for (let menuSection of this.detailedMenu) {

                        let menuSectionFiltered = {
                            sectionName: menuSection.sectionName,
                            sectionOrder: menuSection.sectionOrder,
                            sectionMenu: [],
                        };

                        // Retain sections that match search term
                        if (menuSection.sectionName.toLowerCase().includes(this.searchMenuTerm)) {
                            menuSectionFiltered.sectionMenu = menuSection.sectionMenu;
                        }
                        else {
                            // Filter items in sectionMenu (by name, type, type category, country, producer, serving type name)
                            menuSectionFiltered.sectionMenu = menuSection.sectionMenu.filter((item) => {
                                return (
                                    item.itemDetails.itemName.toLowerCase().includes(this.searchMenuTerm)
                                    || item.itemDetails.itemType.toLowerCase().includes(this.searchMenuTerm)
                                    || item.itemDetails.itemTypeCategory.toLowerCase().includes(this.searchMenuTerm)
                                    || item.itemDetails.itemCountry.toLowerCase().includes(this.searchMenuTerm)
                                    || item.itemDetails.itemProducer.toLowerCase().includes(this.searchMenuTerm)
                                    || item.itemDetails.itemServingTypeName.toLowerCase().includes(this.searchMenuTerm)
                                );
                            });
                        }

                        // Add section to searchMenuResults if it contains items
                        if (menuSectionFiltered.sectionMenu.length > 0) {
                            this.searchMenuResults.push(menuSectionFiltered);
                        }

                    }
                }

                // Sort searchMenuResults
                this.sortMenu(this.sortMenuTerm);

            },

            // Sort Menu
            sortMenu(sortTerm) {

                // Set sortMenuTerm
                this.sortMenuTerm = sortTerm;

                // Sort searchMenuResults
                if (this.searchMenuResults.length > 0) {
                    switch (sortTerm) {
                        case 'Alphabetical (A-Z)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemName > b.itemDetails.itemName) ? 1 : -1);
                                return s;
                            });
                            break;
                        case 'Alphabetical (Z-A)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemName < b.itemDetails.itemName) ? 1 : -1);
                                return s;
                            });
                            break;
                        case 'Rating (Low to High)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemRating > b.itemDetails.itemRating) ? 1 : -1);
                                return s;
                            });
                            break;
                        case 'Rating (High to Low)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemRating < b.itemDetails.itemRating) ? 1 : -1);
                                return s;
                            });
                            break;
                        case 'Price (Low to High)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemPrice < b.itemPrice) ? 1 : -1);
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemServingTypeName > b.itemDetails.itemServingTypeName) ? 1 : -1);
                                return s;
                            });
                            break;
                        case 'Price (High to Low)':
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemPrice > b.itemPrice) ? 1 : -1);
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemDetails.itemServingTypeName > b.itemDetails.itemServingTypeName) ? 1 : -1);
                                return s;
                            });
                            break;
                        // All other cases
                        default:
                            this.searchMenuResults = this.searchMenuResults.map(s => {
                                s.sectionMenu = s.sectionMenu.sort((a, b) => (a.itemOrder > b.itemOrder) ? 1 : -1);
                                return s;
                            });
                            break;
                    }
                }

            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Save Profile Edits
            async saveProfileEdits() {

                this.editProfile = false;

                try {
                    await this.$axios.post('http://127.0.0.1:5300/editDetails', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            image64: this.editProfilePhoto,
                            venueName: this.editVenueName,
                            venueDesc: this.editVenueDesc,
                            originLocation: this.editCountry,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                }
                catch (error) {
                    alert("An error occurred while attempting to save your changes, please try again!");
                    // console.error(error);
                }

                // Refresh page
                this.$router.go(0);
            },

            // Submit New Update
            async submitNewUpdate() {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/addUpdates', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            date: new Date().toISOString(),
                            text: this.newUpdateText,
                            image64: this.newUpdatePhoto,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } 
                catch (error) {
                    alert("An error occurred while attempting to submit, please try again!\nWe have tried to copy your update's text to your clipboard.");
                    // Copy update text to clipboard
                    this.copyToClipboard(this.newUpdateText);
                }

                // Refresh page
                this.$router.go(0);
            },

            // Send Answer to a Question
            async sendAnswer(qa) {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/sendAnswers', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            questionsAnswersID: qa._id['$oid'],
                            answer: this.qaAnswer,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                }
                catch (error) {
                    alert("An error occurred while attempting to send your answer, please try again!\nWe have tried to copy your answer's text to your clipboard.");
                    // Copy answer text to clipboard
                    this.copyToClipboard(this.qaAnswer);
                }

                // Refresh page
                this.$router.go(0);
            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Check Opening Hours
            checkOpeningHours() {

                // Reset error flag
                this.editOpeningHoursError = false;

                for (let day in this.newOpeningHours) {
                    // Get start and end time values
                    const startTimeValue = parseInt(this.newOpeningHours[day][0].replace(/:/g, ''));
                    const endTimeValue = parseInt(this.newOpeningHours[day][1].replace(/:/g, ''));
                    const errorElement = document.getElementById(day + 'error')

                    // Check if start time is before end time
                    if (startTimeValue >= endTimeValue) {
                        this.editOpeningHoursError = true;
                        if (errorElement) {
                            errorElement.classList.remove('d-none');
                            errorElement.innerText = "Start time must be before end time!";
                        }
                    }
                    else {
                        if (errorElement) {
                            errorElement.classList.add('d-none');
                            errorElement.innerText = "";
                        }
                    }
                }

            },
            
            // Update Opening Hours
            async saveOpeningHours() {

                this.editOpeningHours = false;

                try {
                    this.$axios.post('http://localhost:5300/editOpeningHours', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updatedOpeningHours: this.newOpeningHours,
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                }
                catch (error) {
                    alert("An error occurred while attempting to save your changes, please try again!");
                    // console.error(error);
                }

                // Refresh page
                this.$router.go(0);

            },

            // Update Public Holiday Information
            async savePublicHolidays() {

                this.editPublicHolidays = false;

                try {
                    this.$axios.post('http://localhost:5300/editPublicHolidays', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updatedPublicHolidays: this.newPublicHolidays,
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                }
                catch (error) {
                    alert("An error occurred while attempting to save your changes, please try again!");
                    // console.error(error);
                }

                // Refresh page
                this.$router.go(0);

            },

            // Update Reservation Details
            async saveReservationDetails() {

                this.editReservationDetails = false;

                try {
                    this.$axios.post('http://localhost:5300/editReservationDetails', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updatedReservationDetails: this.newReservationDetails,
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                }
                catch (error) {
                    alert("An error occurred while attempting to save your changes, please try again!");
                    // console.error(error);
                }

                // Refresh page
                this.$router.go(0);

            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Reset Edit Menu
            resetEditMenu() {
                this.editMenu = [];

                for (let section of this.detailedMenu) {
                    let sectionMenu = [];
                    for (let item of section.sectionMenu) {
                        sectionMenu.push(JSON.parse(JSON.stringify(item)));
                    }

                    this.editMenu.push({
                        sectionName: section.sectionName,
                        sectionOrder: section.sectionOrder,
                        sectionMenu: sectionMenu,
                    });
                }
            },
            
            // Add Menu Section
            addMenuSection() {
                this.editMenu.push({
                    sectionName: "New Section " + (this.editMenu.length + 1),
                    sectionOrder: this.editMenu.length,
                    sectionMenu: [],
                });
            },

            // Delete Menu Section
            deleteMenuSection(index) {
                // Remove section from editMenu
                this.editMenu = this.editMenu.filter(s => s.sectionOrder != index);
            },

            // Populate Rename Menu Section Modal
            populateRenameMenuSectionModal(index) {
                this.renameMenuSectionModalTarget = {
                    index: index,
                    data: JSON.parse(JSON.stringify(this.editMenu.find(s => s.sectionOrder == index))),
                }
                this.renameMenuSectionModalOld = this.renameMenuSectionModalTarget.data.sectionName;
                this.renameMenuSectionModalNew = this.renameMenuSectionModalTarget.data.sectionName;
            },

            // Rename Menu Section
            renameMenuSection() {
                this.renameMenuSectionModalTarget.data.sectionName = this.renameMenuSectionModalNew;
                this.editMenu = this.editMenu.map(s => s.sectionOrder == this.renameMenuSectionModalTarget.index ? this.renameMenuSectionModalTarget.data : s);
            },

            // Update New Menu Item Target
            updateNewMenuItemTarget() {

                // get error message element
                let newMenuItemTargetError = document.getElementById("newMenuItemTargetError");

                let itemData = this.allListings.find(i => i._id['$oid'] == this.newMenuItemID);
                if (itemData != undefined) {
                    this.newMenuItemTarget = itemData;
                    newMenuItemTargetError.innerText = "";

                    this.updateNewMenuItemTargetSection();
                }
                else {
                    this.newMenuItemTarget = {};
                    newMenuItemTargetError.innerText = "Please target a valid bottle listing!";
                }
            },

            // Update New Menu Item Target Section
            updateNewMenuItemTargetSection() {

                // get error + notice message element
                let newMenuItemTargetSectionError = document.getElementById("newMenuItemTargetSectionError");
                let newMenuItemTargetSectionNotice = document.getElementById("newMenuItemTargetSectionNotice");

                if (Object.keys(this.newMenuItemTargetSection).length !== 0) {

                    newMenuItemTargetSectionError.innerText = "";

                    // Check if item already exists in section
                    let itemExists = this.newMenuItemTargetSection.sectionMenu.find(i => i.itemID['$oid'] == this.newMenuItemID);
                    if (itemExists != undefined) {
                        newMenuItemTargetSectionNotice.innerText = "Are you sure you want to add a duplicate item to this section?"
                    }
                    else {
                        newMenuItemTargetSectionNotice.innerText = "";
                    }
                }
                else {
                    newMenuItemTargetSectionError.innerText = "Please select a valid menu section!";
                    newMenuItemTargetSectionNotice.innerText = "";
                }
            },

            // Add Menu Item
            addMenuItem() {
                    
                // Add item to section
                this.newMenuItemTargetSection.sectionMenu.push({
                    itemID: this.newMenuItemTarget['_id'],
                    itemOrder: this.newMenuItemTargetSection.sectionMenu.length,
                    itemPrice: 0,
                    itemServingType: this.servingTypes.find(s => s.servingType == "Serving")['_id'],
                    itemAvailability: true,
                    itemDetails: {
                        itemPhoto: this.newMenuItemTarget.photo,
                        itemName: this.newMenuItemTarget.listingName,
                        itemType: this.newMenuItemTarget.drinkType,
                        itemTypeCategory: this.newMenuItemTarget.typeCategory,
                        itemABV: this.newMenuItemTarget.abv,
                        itemCountry: this.newMenuItemTarget.originCountry,
                        itemDesc: this.newMenuItemTarget.officialDesc,
                        itemRating: this.newMenuItemTarget.avgRating,
                        itemProducer: this.newMenuItemTarget.producerName,
                        itemServingTypeName: "Serving",
                    }
                });

                // Reset newMenuItemID, newMenuItemTarget, newMenuItemTargetSection
                this.newMenuItemID = "";
                this.newMenuItemTarget = {};
                this.newMenuItemTargetSection = {};
            },

            // Delete Menu Item
            deleteMenuItem(sectionIndex, itemIndex) {
                // Find section
                let section = this.editMenu.find(s => s.sectionOrder == sectionIndex);

                // Remove item from section
                section.sectionMenu = section.sectionMenu.filter(i => i.itemOrder != itemIndex);
            },

            // Enable Edit Menu Mode
            async enableEditMenuMode() {
                this.editMenuMode = true;

                // If editMenuDataLoaded is false, load necessary additional data
                if (!this.editMenuDataLoaded) {

                    try {
                        // Obtain all listings
                        const listingResponse = await this.$axios.get('http://127.0.0.1:5000/getListings');
                        this.allListings = listingResponse.data;

                        // Obtain all reviews
                        let reviewResponse = await this.$axios.get('http://127.0.0.1:5000/getReviews');
                        let reviewData = reviewResponse.data;

                        // Obtain all producers
                        let producerResponse = await this.$axios.get('http://127.0.0.1:5000/getProducers');
                        this.loadedProducers = producerResponse.data;

                        // Get reviews + producer name for each listing
                        for (let listingData of this.allListings) {

                            // Get reviews
                            let listingReviews = reviewData.filter(r => r.reviewTarget['$oid'] == listingData._id['$oid']);

                            if (Array.isArray(listingReviews) && listingReviews.length == 0) {
                                listingData["reviews"] = [];
                                listingData["avgRating"] = 0;
                            }
                            else if (listingReviews != null && listingReviews != "") {
                                listingData["reviews"] = listingReviews;
                                listingData["avgRating"] = listingReviews.reduce((a, b) => a + b.rating, 0) / listingReviews.length;
                            }
                            else {
                                // Error
                                throw "Error: Unexpected response from server!";
                            }

                            // Find producer in loadedProducers
                            let producerData = this.loadedProducers.find(p => p._id['$oid'] == listingData["producerID"]['$oid']);

                            // If not found, remove item from valid listings
                            if (producerData == undefined) {
                                this.allListings = this.allListings.filter(i => i._id['$oid'] != listingData._id['$oid']);
                            }
                            // If found, set producer name
                            else {
                                listingData["producerName"] = producerData["producerName"];
                            }

                        }

                        // Set editMenuDataLoaded to true (prevent re-loading data on subsequent calls)
                        this.editMenuDataLoaded = true;
                    }
                    catch (error) {
                        alert("An error occurred while attempting to load extra data for menu editing, please try again!");
                        this.$router.go(0);
                    }
                }
            },

            // Update Menu
            async updateMenu() {

                this.editMenuMode = false;
                this.dataLoaded = false;

                // Update sectionOrder and itemOrder based on current ordering
                for (let sectionIndex in this.editMenu) {
                    this.editMenu[sectionIndex].sectionOrder = parseInt(sectionIndex);
                    for (let itemIndex in this.editMenu[sectionIndex].sectionMenu) {
                        this.editMenu[sectionIndex].sectionMenu[itemIndex].itemOrder = parseInt(itemIndex);
                    }
                }

                // Remove itemDetails from editMenu
                for (let section of this.editMenu) {
                    for (let item of section.sectionMenu) {
                        delete item.itemDetails;
                    }
                }

                try {
                    await this.$axios.post('http://127.0.0.1:5300/editMenu', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updatedMenu: this.editMenu,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                }
                catch (error) {
                    alert("An error occurred while attempting to save your changes. We apologise for the inconvenience. Please try again!");
                    // console.error(error);
                }

                // Refresh page
                this.$router.go(0);
            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Follow / Unfollow Venue
            async editFollow(action) {

                // Toggle Follow
                if (action == 'follow') {
                    this.userFollowing = true;
                }
                else if (action == 'unfollow') {
                    this.userFollowing = false;
                }

                try {
                    await this.$axios.post('http://127.0.0.1:5100/updateFollowLists', 
                        {
                            userID: this.viewerID,
                            action: action,
                            target: "venues",
                            followerID: this.targetVenue['_id']['$oid'],
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                }
                catch (error) {
                    // Reload page
                    this.$router.go(0);
                }
            },

            // Unlike Updates
            async unlikeUpdates(unlikeUpdateID) {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/unlikeUpdates', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updateID: unlikeUpdateID,
                            userID: this.viewerID,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } 
                catch (error) {
                    // console.error(error);
                }

                // Reload page
                this.$router.go(0);
            },

            // Like Updates
            async likeUpdates(likeUpdateID) {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/likeUpdates', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            updateID: likeUpdateID,
                            userID: this.viewerID,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } 
                catch (error) {
                    // console.error(error);
                }

                // Reload page
                this.$router.go(0);
            },

            // Send Question
            async sendQuestion() {
                try {
                    await this.$axios.post('http://127.0.0.1:5300/sendQuestions', 
                        {
                            venueID: this.targetVenue['_id']['$oid'],
                            question: this.qaQuestion,
                            answer: "",
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } 
                catch (error) {
                    alert("An error occurred while attempting to send your question, please try again!\nWe have tried to copy your question's text to your clipboard.");
                    // Copy answer text to clipboard
                    this.copyToClipboard(this.qaAnswer);
                }

                // Reload page
                this.$router.go(0);
            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // Report Menu Inaccuracy (Reset)
            resetReport() {
                this.reportSection = '';
                this.reportSectionItems = [];
                this.reportItem = '';
                this.reportReason = '';
                
                this.retryReport();
            },

            // Report Menu Inaccuracy (Retry)
            retryReport() {
                this.reportFormView = true;
                this.reportSubmitLoading = false;
                this.reportSubmitSuccess = false;
                this.reportSubmitError = null;
                this.reportItemNone = false;
                this.reportReasonNone = false;
                this.reportResponseCode = null;
            },

            // Report Menu Inaccuracy (Get Section Items)
            getReportSectionItems() {
                try {
                    this.reportItem = '';
                    if (this.reportSection !== '') {
                        this.reportSectionItems = this.detailedMenu[this.reportSection].sectionMenu;
                    }
                    else {
                        this.reportSectionItems = [];
                    }
                }
                catch (error) {
                    this.reportSectionItems = [];
                }
            },

            // Report Menu Inaccuracy (Submit)
            async submitReport() {
                try {
                    this.reportSubmitLoading = true;

                    // Reset error validation flags
                    this.reportItemNone = false;
                    this.reportReasonNone = false;

                    // Validate input
                    if (this.reportItem == '') {
                        this.reportItemNone = true;
                    }
                    if (this.reportReason.trim() == '') {
                        this.reportReasonNone = true;
                    }
                    if (this.reportItemNone || this.reportReasonNone) {
                        this.reportSubmitLoading = false;
                        return;
                    }

                    // Prepare data
                    let reportData = {
                        "userID": this.viewerID,
                        "venueID": this.targetVenue['_id']['$oid'],
                        "listingID": this.reportItem,
                        "inaccurateReason": "Menu Section: " + this.reportSection + "\nReason: " + this.reportReason,
                    }

                    // Send report
                    await this.$axios.post('http://localhost:5011/requestInaccuracy', reportData)
                    .then((response) => {
                        this.reportResponseCode = response.data.code;
                    })
                    .catch((error) => {
                        this.reportResponseCode = error.response.data.code;
                    });

                    this.reportFormView = false;
                    this.reportSubmitLoading = false;

                    // Handle response
                    if (this.reportResponseCode == 201) {
                        this.reportSubmitSuccess = true;
                    }
                    else if (this.reportResponseCode == 400) {
                        this.reportSubmitError = 'dupe';
                    }
                    else {
                        this.reportSubmitError = 'error';
                    }

                }
                catch (error) {
                    this.reportSubmitError = 'error';
                    this.reportSubmitLoading = false;
                    if (this.reportFormView) {
                        this.reportFormView = false;
                    }
                }
            },

            // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            // check if user has already added listing to shelf, add colour to button accordingly
            checkDrinkLists(listingID) {
                const haveTried = this.userInfo.drinkLists["Drinks I Have Tried"].listItems.some(item => item[1].$oid == listingID);
                const wantToTry = this.userInfo.drinkLists["Drinks I Want To Try"].listItems.some(item => item[1].$oid == listingID);

                const haveTriedButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${haveTried ? 'disabled' : ''}">
                    Have Tried
                </button>
                `;

                const wantToTryButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${wantToTry ? 'disabled' : ''}">
                    Want To Try
                </button>
                `;

                return {
                    buttons: {
                        haveTried: haveTriedButton,
                        wantToTry: wantToTryButton,
                    }
                }
            },

            // Add listing to user's drink lists
            async addToBookmarks(targetList, listingID){

                let submitAPI = "http://127.0.0.1:5070/addTo";

                if (targetList == "tried") {
                    submitAPI += "Tried/";

                    // Check if listing is already in "tried" list
                    if (this.userInfo.drinkLists["Drinks I Have Tried"].listItems.some(item => item[1].$oid == listingID['$oid'])) {
                        return;
                    }
                }
                else if (targetList == "want") {
                    submitAPI += "Want/";

                    // Check if listing is already in "want" list
                    if (this.userInfo.drinkLists["Drinks I Want To Try"].listItems.some(item => item[1].$oid == listingID['$oid'])) {
                        return;
                    }
                }
                
                let submitData = {
                    "date": new Date(),
                    "listingID": listingID,
                    "userID": this.viewerID,
                }

                try {
                    await this.$axios.put(submitAPI, submitData)
                }
                catch (error) {
                    alert("An error occurred while attempting to add to your bookmarks, please try again!");
                    // console.error(error);
                }

                // Reload page
                this.$router.go(0);
            },
            
            // Populate Bookmark Modal
            populateBookmarkModal(listingData) {

                this.bookmarkModalTarget = listingData;
                this.selectedBookmarkList = [];

                for (let drinkList in this.userInfo.drinkLists) {

                    // Check if listing is in list
                    if (this.userInfo.drinkLists[drinkList].listItems.some(item => item[1].$oid == listingData._id['$oid'])) {

                        // Add list to selectedBookmarkList if not already present
                        if (!this.selectedBookmarkList.includes(drinkList)) {
                            this.selectedBookmarkList.push(drinkList);
                        }
                    }
                }
                
            },

            // Bookmark Item
            async bookmarkItem() {

                let addListingID = this.bookmarkModalTarget._id;
                let userBookmarkData = this.userInfo.drinkLists;

                // Handle adding to new list
                if (this.saveToNewList) {
                    this.othersListName = this.othersListName.trim();

                    if (this.othersListName == "") {
                        this.othersListNameError = "Please enter a list name";
                        return;
                    } else if (userBookmarkData[this.othersListName]) {
                        this.othersListNameError = "List name already exists";
                        return;
                    } else {
                        this.othersListNameError = "";
                        userBookmarkData[this.othersListName] = {
                            listDesc: "",
                            listItems: [[new Date(), addListingID]],
                        };
                    }
                }

                // Handle modifying existing lists
                for (let drinkList in userBookmarkData) {

                    let itemExists = userBookmarkData[drinkList].listItems.some(item => item[1].$oid == addListingID['$oid'])

                    if (this.selectedBookmarkList.includes(drinkList)) {
                        if (!itemExists) {
                            userBookmarkData[drinkList].listItems.push([new Date(), addListingID]);
                        }
                    }
                    else {
                        if (itemExists) {
                            const index = userBookmarkData[drinkList].listItems.findIndex(item => item[1].$oid == addListingID['$oid']);
                            userBookmarkData[drinkList].listItems.splice(index, 1);
                        }
                    }

                }

                // Send updated bookmark data to server
                try {
                    await this.$axios.post('http://127.0.0.1:5100/updateBookmark', 
                        {
                            userID: this.viewerID,
                            bookmark: userBookmarkData,
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } catch (error) {
                    // console.error(error);
                }
                
                // Reload page
                this.$router.go(0);

            },

        }
    }
</script>

<style>
    .ghost {
    opacity: 0.5;
    background: #c8ebfb;
    }
</style>