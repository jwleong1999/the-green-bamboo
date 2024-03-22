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

            <!-- Title -->
            <div class="col-12">
                <div class="d-grid gap-2">
                    <p class="fw-bold fs-1 m-0">Admin Dashboard</p>
                </div>
            </div>

            <nav>
                <div class="nav nav-tabs justify-content-center" id="nav-tab" role="tablist">
                    <button class="nav-link active w-25" id="nav-tag-tab" data-bs-toggle="tab" data-bs-target="#nav-tag" type="button" role="tab" aria-controls="nav-tag" aria-selected="true"> Tag Controls </button>
                    <button class="nav-link w-25" id="nav-moderator-tab" data-bs-toggle="tab" data-bs-target="#nav-moderator" type="button" role="tab" aria-controls="nav-moderator" aria-selected="false"> Moderators </button>
                    <button class="nav-link w-25" id="nav-business-tab" data-bs-toggle="tab" data-bs-target="#nav-business" type="button" role="tab" aria-controls="nav-business" aria-selected="false"> Business Accounts </button>
                </div>
            </nav>

            <!-- content in navtabs -->
            <div class="tab-content" id="nav-tabContent">
            
                <!-- tag controls navtab -->
                <div class="tab-pane fade show active" id="nav-tag" role="tabpanel" aria-labelledby="nav-tag-tab">
                    
                    <div class="row text-center">
                        <div class="col-12">
                            <h3><b>Tag Controls</b></h3>
                        </div>
                    </div>
                    <div>
                        <p class="gap-1">
                            <!-- Open a modal prompting to edit or add tags -->
                            <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#observationModal">
                                Action Tags
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
                                        <h1 v-if="selectingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Action Tag Control</h1>
                                        <h1 v-if="addingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Add Action Tag</h1>
                                        <h1 v-if="editingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Edit Action Tag</h1>
                                        <h1 v-if="deletingObservation" class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Delete Action Tag</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>

                                    <!-- Modal for success and error message -->
                                    <div v-if="successUpdateObservation" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>Action tags have successfully been updated!</span>
                                    </div>

                                    <div v-if="successCreateObservation" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>Action tags have successfully been created!</span>
                                    </div>

                                    <div v-if="updatingObservation" class="modal-body text-center text-primary fst-italic fw-bold fs-3">
                                        <span>Action tags are being updated!</span>
                                    </div>

                                    <div v-if="submittingObservation" class="modal-body text-center text-primary fst-italic fw-bold fs-3">
                                        <span>Action tags are being added!</span>
                                    </div>

                                    <div v-if="errorUpdateObservation" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span v-if="invalidTag"> The Action tag you are trying to update does not exist</span>
                                        <span v-if="errorMessage">An error occurred updating the action tags. Please try again.</span>
                                    </div>

                                    <div v-if="errorCreateObservation" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span v-if="duplicateTag"> The Action tag you are trying to create already exists!</span>
                                        <span v-if="errorMessage">An error occurred updating the Action tags. Please try again.</span>
                                    </div>

                                    <div v-if="successDeleteObservation" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>Action tag have successfully been deleted!</span>
                                    </div>
                                    <div v-if="errorDeletingObservation" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span v-if="notExistObservation"> The action tag you are trying to delete does not exist!</span>
                                        <span v-if="errorDeleteObservation">An error occurred deleting the action tag. Please try again.</span>
                                    </div>

                                    <!-- Modal body for selecting mode for observation operations -->
                                    <div v-if="selectingObservation" class="modal-body">
                                        <button class="btn btn-warning reverse-clickable-text text-dark" @click="addObservation" type="button">
                                            Add Action Tags
                                        </button> 

                                        <button class="btn btn-primary mx-1 reverse-clickable-text" @click="editObservation" type="button">
                                            Edit Action Tags
                                        </button>

                                        <button class="btn btn-danger mx-1 reverse-clickable-text" @click="deleteObservations" type="button">
                                            Delete Action Tags
                                        </button>
                                    </div>
                                    <!-- Modal body for adding observation -->
                                    <div v-if="addingObservation" class="modal-body">
                                        <input v-model="newObservation" type="text" class="form-control">
                                        <p v-if="newObservation ==''" class='text-danger text-start mb-2 fw-bold'>Action Tag cannot be empty</p>
                                    </div>
                                    <!-- Modal body for editing observation -->
                                    <div v-if="editingObservation" class="modal-body">
                                        <div class="row">
                                            <div v-for="tag in editedObservationTags" class="mb-2 col-md-6"  v-bind:key="tag._id">
                                                <input v-model="tag.observationTag" type="text" class="form-control">
                                                <p v-if="tag.observationTag==''" class='text-danger text-start mb-2 fw-bold'>Action Tag cannot be empty</p>
                                            </div>
                                        </div>
                                        <p class='text-danger text-center mb-2 fw-bold' v-if="nothingChanged">There is no changed action tag</p>
                                    </div>

                                    <div v-if="deletingObservation" class="modal-body">
                                        <div class="row">
                                            <div v-for="tag in observationTags" class="mb-2 col-md-4"  v-bind:key="tag._id">
                                                <button @click="deleteObservation(tag._id, tag.observationTag)" type="button" class="btn btn-danger" style="width: 150px; height: 60px;">{{ tag.observationTag }}</button>
                                            </div>
                                        </div>
                                        <div v-if="observationToDelete!=''">
                                            <div class="row">
                                                <span class='text-danger mb-2 fw-bold'>Are you sure you want to delete [{{ observationToDelete.observationTag }}]?</span>
                                            </div>
                                            
                                            <button @click="confirmDeleteTag" type="button" class="btn btn-danger mx-1">Confirm Delete</button>
                                            <button @click="resetDeleteTag" type="button" class="btn tertiary-btn reverse-clickable-text">No, do not delete</button>
                                        </div>
                                    </div>

                                    <div class="modal-footer">
                                        <button v-if="selectingObservation" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button v-if="!selectingObservation" @click="resetObservation" type="button" class="btn btn-secondary">Return</button>
                                        <button v-if="editingObservation" @click="updateObservation" type="button" class="btn btn-primary">Save Updates</button>
                                        <button v-if="addingObservation" @click="createNewObservation" type="button" class="btn btn-primary">Add Tag</button>
                                        <button v-if="successUpdateObservation || errorUpdateObservation || errorCreateObservation || successCreateObservation || successDeleteObservation || errorDeleteObservation" @click="resetErrors" type="button" data-bs-dismiss="modal" class="btn btn-secondary">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- end of modal-->
                    </div>
                </div>

                <!-- moderator navtab -->
                <div class="tab-pane fade" id="nav-moderator" role="tabpanel" aria-labelledby="nav-moderator-tab">
                    <!-- mod addition and removal -->
                    <div>
                        <div class="row text-center">
                            <div class="col-12">
                                <h3><b>Manage Moderators</b></h3>
                            </div>
                        </div>
                        <div>
                            <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#addModeratorModal">
                                Add a moderator
                            </button>      
                            <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#removeModeratorModal">
                                Remove a moderator
                            </button>      
                        </div>

                        <!-- Mod addition modal -->
                        <div class="modal fade" id="addModeratorModal" data-bs-backdrop="static" tabindex="-1" aria-labelledby="addModeratorLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header" style="background-color: #535C72">
                                        <h1 class="modal-title fs-5" id="addModeratorLabel" style="color: white;">Add Moderator</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="resetAddMod"></button>
                                    </div>

                                    <!-- Success add mod modal body -->
                                    <div v-if="successAddMod" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>User has successfully been added as moderator!</span>
                                    </div>
                                    <!-- Error add mod modal body -->
                                    <div v-if="errorAddMod" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span>There is an error adding user as moderator, please try again!</span>
                                    </div>
                                    <!-- Initial select user to promote -->
                                    <div v-if="!confirmModerator && !(successAddMod||errorAddMod)" class="modal-body">
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose user to promote to a moderator: <span class="text-danger">*</span></p>
                                            <input list="users" v-model="promotedUser" class="form-control" id="promotedUser" placeholder="Enter username" v-on:change="updateUsername">
                                            <datalist id="users">
                                                <option v-for="user in users" :key="user._id.$oid" :value="user.username">
                                                    {{user.username}}
                                                </option>
                                            </datalist>
                                            <p v-show="promotedUser.length > 0" class="text-start mb-1 text-danger" id="usernameError"></p>
                                        </div>
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose drink type user can moderate: <span class="text-danger">*</span></p>
                                            <div v-if="selectedPromotedUser!=null" >
                                                <p v-html="formattedPromotedModTypes" class="text-start mb-1"></p>
                                            </div>
                                            <input list="addableDrinkType" v-model="promotedType" class="form-control" id="promotedType" placeholder="Enter drink type" v-on:change="updateDrinkType">
                                            <datalist id="addableDrinkType">
                                                <option v-for="drinkType in addableDrinkType" :key="drinkType._id.$oid" :value="drinkType.drinkType">
                                                    {{drinkType.drinkType}}
                                                </option>
                                            </datalist>
                                            <p v-show="promotedType.length > 0" class="text-start mb-1 text-danger" id="promotedTypeError"></p>
                                        </div>
                                        <p class="text-start mb-1 text-danger" id="alreadyModError"></p>
                                    </div>

                                    <!-- confirm mod to promote -->
                                    <div v-if="confirmModerator && !(successAddMod||errorAddMod)" class="modal-body">
                                        <p class="text-start mb-1"> Do you really want to add <strong>{{ promotedUser }}</strong> as a moderator for <strong>{{ promotedType }}</strong>? <span class="text-danger">*</span></p>
                                    </div>

                                    <!-- Initial select mod to promote footer -->
                                    <div v-if="!confirmModerator && !(successAddMod||errorAddMod)" class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" @click="addModerator" class="btn btn-primary">Add Moderator</button>
                                    </div>

                                    <!-- confirm mod to promote footer -->
                                    <div v-if="confirmModerator && !(successAddMod||errorAddMod)" class="modal-footer">
                                        <button type="button" @click="selectPromotedUser" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="confirmAddModerator" class="btn btn-primary">Confirm Moderator</button>
                                    </div>

                                    <!-- successaddmod and erroraddmod footer -->
                                    <div v-if="successAddMod||errorAddMod" class="modal-footer">
                                        <button type="button" @click="selectPromotedUser" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="resetAddMod" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Mod removal modal -->

                        <div class="modal fade" id="removeModeratorModal" data-bs-backdrop="static" tabindex="-1" aria-labelledby="addModeratorLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header" style="background-color: #535C72">
                                        <h1 class="modal-title fs-5" id="removeModeratorLabel" style="color: white;">Remove Moderator</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="resetRemoveMod"></button>
                                    </div>
                                    <!-- Success remove mod modal body -->
                                    <div v-if="successRemoveMod" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>User has successfully been removed as moderator!</span>
                                    </div>
                                    <!-- Error remove mod modal body -->
                                    <div v-if="errorRemoveMod" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span>There is an error removing user as moderator, please try again!</span>
                                    </div>

                                    <!-- Initial select remove mod modal body -->
                                    <div v-if="!confirmRemoveModerator && !(successRemoveMod||errorRemoveMod)" class="modal-body">
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose user to remove as moderator: <span class="text-danger">*</span></p>
                                            <input list="moderators" v-model="removeMod" class="form-control" id="removeMod" placeholder="Enter username" v-on:change="updateModUsername">
                                            <datalist id="moderators">
                                                <option v-for="user in moderators" :key="user._id.$oid" :value="user.username">
                                                    {{user.username}}
                                                </option>
                                            </datalist>
                                            <p v-show="removeMod.length > 0" class="text-start mb-1 text-danger" id="modUsernameError"></p>
                                        </div>
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose drink type to remove moderator rights from: <span class="text-danger">*</span></p>
                                            <div v-if="selectedRemoveMod!=null" >
                                                <p v-html="formattedRemoveModTypes" class="text-start mb-1"></p>
                                            </div>
                                            <input list="removableDrinkType" v-model="removedType" class="form-control" id="removedType" placeholder="Enter drink type" v-on:change="updateRemovedDrinkType">
                                            <datalist id="removableDrinkType">
                                                <option v-for="drinkType in removableDrinkType" :key="drinkType._id.$oid" :value="drinkType.drinkType">
                                                    {{drinkType.drinkType}}
                                                </option>
                                            </datalist>
                                            <p v-show="removedType.length > 0" class="text-start mb-1 text-danger" id="removedTypeError"></p>
                                        </div>
                                        <p class="text-start mb-1 text-danger" id="notModError"></p>
                                    </div>

                                    <!-- confirm mod to promote -->
                                    <div v-if="confirmRemoveModerator && !(successRemoveMod||errorRemoveMod)" class="modal-body">
                                        <p class="text-start mb-1"> Do you really want to remove <strong>{{ removeMod }}</strong> as a moderator for <strong>{{ removedType }}</strong>? <span class="text-danger">*</span></p>
                                    </div>
                                    <!-- Initial select mod to remove footer -->
                                    <div v-if="!confirmRemoveModerator && !(successRemoveMod||errorRemoveMod)" class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" @click="removeModerator" class="btn btn-primary">Remove Moderator</button>
                                    </div>
                                    <!-- confirm mod to remove footer -->
                                    <div v-if="confirmRemoveModerator && !(successRemoveMod||errorRemoveMod)" class="modal-footer">
                                        <button type="button" @click="selectRemoveMod" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="confirmDowngradeModerator" class="btn btn-primary">Confirm Moderator</button>
                                    </div>

                                    <!-- successremovemod and errorremovemod footer -->
                                    <div v-if="successRemoveMod||errorRemoveMod" class="modal-footer">
                                        <button type="button" @click="selectRemoveMod" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="resetRemoveMod" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>


                    </div>
                    <!-- mod addition and removal end -->

                    <hr>

                    <!-- mod request -->
                    <div>
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
                    </div>
                    <!-- mod request end -->
                </div>

                <!-- business navtab -->
                <div class="tab-pane fade" id="nav-business" role="tabpanel" aria-labelledby="nav-business-tab">
                    <!-- add business -->
                    <div>
                        <div class="row text-center">
                            <div class="col-12">
                                <h3><b>Add Businesses</b></h3>
                            </div>
                        </div>
                        <div>
                            <p class="gap-1">
                                <!-- Open a modal prompting to edit or add tags -->
                                <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" data-bs-toggle="modal" data-bs-target="#addBusinessModal" @click="resetAddBusinessModal">
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
                                    <div class="modal-body text-start" v-if="createBusinessSuccess">
                                        <div class="alert alert-success" role="alert">
                                            Business account created successfully. 
                                            <br>
                                            Please save login details below.
                                            <br>
                                            <span class="text-danger">*This is the only time you can access the password. You cannot recover them later.</span>
                                            <br><br>
                                            <span v-if="businessType == 'producer'">Producer account: <b>{{ businessName }}</b></span>
                                            <!-- <span v-if="businessType == 'venue'">Venue account: {{ businessName }}</span> -->
                                            <br>
                                            Temporary password: <b>{{ tempPassword }}</b>
                                        </div>
                                    </div>
                                    <div class="modal-body text-start" v-else-if="createBusinessError != '' ">
                                        <div class="alert alert-danger" role="alert">{{createBusinessError}}</div>
                                    </div>
                                    <div class="modal-body text-start" v-else>
                                        <div>
                                            <div class="mb-2 fw-bold">
                                                Profile Type
                                            </div>
                                            <div class="mb-4">
                                                <div class="form-check form-check-inline">
                                                        <input class="form-check-input" type="radio" id="inlineCheckbox1" v-model="businessType" value="producer" name="business">
                                                    <label class="form-check-label text-start" for="inlineCheckbox1">Brand/Producer</label>
                                                </div>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" type="radio" id="inlineCheckbox2" v-model="businessType" value="venue" name="business">
                                                    <label class="form-check-label text-start" for="inlineCheckbox2">Venue</label>
                                                </div>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mb-2 fw-bold">
                                                Name
                                            </div>
                                            <div class="mb-4">
                                                <input type="text" class="form-control" v-model="businessName">
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mb-2 fw-bold">
                                                Description
                                            </div>
                                            <div class="mb-4">
                                                <input type="text" class="form-control" v-model="businessDesc">
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mb-2 fw-bold">
                                                Country
                                            </div>
                                            <div class="mb-4">
                                                <div class="input-group">
                                                    <select class="form-select" id="countrySelect" v-model="businessCountry">
                                                        <option v-for="country in countries" :key="country" :value="country.originCountry">
                                                            {{ country.originCountry }}
                                                        </option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="mb-2 fw-bold">
                                                Claim Status
                                            </div>
                                            <div class="mb-4">
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" type="radio" id="claimed" v-model="businessClaimStatus" value="true" name="claim">
                                                    <label class="form-check-label text-start" for="claimed">Claimed</label>
                                                </div>
                                                <div class="form-check form-check-inline">
                                                    <input class="form-check-input" type="radio" id="unclaimed" v-model="businessClaimStatus" value="false" name="claim">
                                                    <label class="form-check-label text-start" for="unclaimed">Unclaimed</label>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="alert alert-danger" role="alert" v-if="addBizError != '' ">{{addBizError}}</div>
                                    </div>

                                    
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button v-if="!createBusinessSuccess && createBusinessError == ''" type="button" class="btn btn-primary" @click="createBusiness">Save changes</button>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            <!-- add business modal end -->
                        </div>
                    </div>
                    <!-- add business end -->

                    <hr>

                    <!-- business account request -->
                    <div>
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
                                        <span class="fw-bold">Business Information</span>
                                        <hr>
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
                                        </ul>
                                        <hr>
                                        <span class="fw-bold">Requestor Information</span>
                                        <hr>
                                        <ul class="list-group list-group-flush text-start">
                                            <li class="list-group-item"><span class="fw-bold">First Name: </span> {{ request.firstName }} </li>
                                            <li class="list-group-item"><span class="fw-bold">Last Name: </span> {{ request.lastName }} </li>
                                            <li class="list-group-item"><span class="fw-bold">Email: </span> {{ request.email }} </li>
                                            <li class="list-group-item"><span class="fw-bold">Relationship: </span> {{ request.relationship }} </li>
                                            <li class="list-group-item"><span class="fw-bold">Price Plan: </span> {{ request.pricing }} </li>


                                        </ul>
                                        </div>
                                        <div class="card-footer">
                                            <button v-if="checkBusinessExist(request.businessLink)" class="btn btn-success btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'approve')" data-bs-toggle="modal" data-bs-target="#addBusinessModal">Approve</button>
                                            <button v-else class="btn btn-primary btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'add')" data-bs-toggle="modal" data-bs-target="#addBusinessModal">Add</button>
                                            <button class="btn btn-danger btn-sm mx-3 my-1" type="button" style="width: 75px;" @click="reviewAccountRequest(request, 'reject')">Reject</button>
                                        </div>
                                    </div>
                                </div>
                                        
                                
                            </div>
                            <div v-else>
                                No New Business Account Request
                            </div>
                        </div>
                    </div>
                    <!-- business account request end -->
                </div>

            </div>
            <!-- navtabs end -->
            
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
                    drinkTypes: [],

                    editedObservationTags: [],
                    pendingModRequests: [],
                    pendingAccountRequests: [],
                    moderators:[],

                    observationToDelete:'',
                    
                    //User 
                    user: null,
                    users: [],
                    promotedUser:'',
                    selectedPromotedUser:null,
                    promotedType:'',
                    selectedPromotedType:null,
                    removeMod:'',
                    selectedRemoveMod:null,
                    removedType:'',
                    selectedRemoveType:null,
                    removableDrinkType:[],
                    addableDrinkType:[],

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
                    deletingObservation:false,
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
                    errorDeletingObservation:false,
                    errorDeleteObservation:false,
                    successDeleteObservation:false,
                    notExistObservation:false,

                    confirmModerator:false,
                    successAddMod:false,
                    errorAddMod:false,
                    confirmRemoveModerator:false,
                    successRemoveMod:false,
                    errorRemoveMod:false,


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
                    createBusinessError: "",
                    createBusinessSuccess: false,

                }
            },
            computed: {
                formattedPromotedModTypes() {
                    // Join the modType array elements with commas and spaces
                    if(this.selectedPromotedUser.modType.length === 0){
                        return "This user is currently not a moderator!"
                    }
                    else{
                        return "This use is currently a moderator for <b>" + this.selectedPromotedUser.modType.join(', ') +"</b>!";
                    }
                },
                formattedRemoveModTypes() {
                    // Join the modType array elements with commas and spaces
                    if(this.selectedRemoveMod.modType.length === 0){
                        return "This user is currently not a moderator!"
                    }
                    else{
                        return "This use is currently a moderator for <b>" + this.selectedRemoveMod.modType.join(', ') +"</b>!";
                    }
                },
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
                        this.moderators = this.users.filter(user => user.modType.length>=1);
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
                    // drinkType
                    try {
                        const response = await this.$axios.get('http://127.0.0.1:5000/getDrinkTypes');
                        this.drinkTypes = response.data;
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
                    this.deletingObservation=false
                },

                editObservation(){
                    this.addingObservation=false
                    this.editingObservation=true
                    this.selectingObservation=false
                    this.deletingObservation =false
                },

                deleteObservations(){
                    this.addingObservation=false
                    this.editingObservation=false
                    this.selectingObservation=false
                    this.deletingObservation= true
                },

                resetObservation(){
                    this.editingObservation=false
                    this.addingObservation=false
                    this.selectingObservation=true
                    this.updatingObservation = false
                    this.deletingObservation =false
                    this.submittingObservation =false
                    this.deletingObservation =false
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
                    this.errorDeletingObservation = false
                    this.errorDeleteObservation = false
                    this.successDeleteObservation = false
                    this.notExistObservation = false
                },

                createNewObservation(){
                    if(this.newObservation==""){
                        alert('Please fill in the observation tag')
                        return null
                    }
                    this.submittingObservation=true
                    this.addingObservation=false
                    let submitAPI = "http://127.0.0.1:5053/createObservationTag"
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

                deleteObservation(tagId,tag){
                    // alert(tagId.$oid)
                    this.observationToDelete = {"tagId":tagId, "observationTag":tag}
                },
                async confirmDeleteTag(){
                    let responseCode = ''
                    let deleteAPI = "http://127.0.0.1:5052/deleteObservationTag/" + this.observationToDelete.tagId.$oid
                    const response = await this.$axios.delete(deleteAPI)
                    .then((response)=>{
                        responseCode = response.data.code
                    })
                    .catch((error)=>{
                        console.error(error);
                        responseCode = error.response.data.code
                    });
                    if(responseCode==200){
                        this.successDeleteObservation=true; // Display success message
                        this.deletingObservation=false; // Hide submission in progress message
                        let observationToRemove = this.observationTags.findIndex(obj => obj._id.$oid === this.observationToDelete.tagId.$oid);
                        if (observationToRemove !== -1) {
                            this.observationTags.splice(observationToRemove, 1);
                        }
                    }else{
                        this.errorDeletingObservation=true; // Display error message
                        this.deletingObservation=false; // Hide submission in progress message
                        if(responseCode==400){
                            this.notExistObservation = true // Display duplicate entry message
                        }else{
                            this.errorDeleteObservation = true // Display generic error message
                        }
                    }
                    this.observationToDelete = ''
                    return response
                },
                resetDeleteTag(){
                    this.observationToDelete=''
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
                            await this.$axios.post('http://127.0.0.1:5100/updateModType', 
                                {
                                    userID: userID,
                                    newModType: newModType,
                                }, {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            });
                        } catch (error) {
                            console.error(error);
                        }
                    }
                    
                    // update mod request db
                    try {
                        await this.$axios.post('http://127.0.0.1:5101/updateModRequest', 
                            {
                                requestID: requestID,
                                reviewStatus: false,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
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
                        this.businessType = request.businessType;
                        this.businessName = request.businessName;
                        this.tempPassword = hashPassword(request.businessName).toString();
                        this.tempPassword = this.tempPassword.replace(/-/g, '');
                        const hashedPassword = hashPassword(request.businessName, this.tempPassword);

                        const newBusinessData = {
                            businessName: request.businessName,
                            businessDesc: request.businessDesc,
                            country: request.country,
                            hashedPassword: hashedPassword,
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

                                if (response.data.code == 201) {
                                    this.createBusinessSuccess = true;
                                } 

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

                                if (response.data.code == 201) {
                                    this.createBusinessSuccess = true;
                                } 

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
                        const createSuccess = await this.createBusiness();
                        if (!createSuccess) {
                            return;
                        }
                    }

                    // update review status
                    try {
                        await this.$axios.post('http://127.0.0.1:5031/updateAccountRequest', 
                            {
                                requestID: requestID,
                                reviewStatus: false,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
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
                        if (this.businessClaimStatus == "true") {
                            this.tempPassword = hashPassword(this.businessName).toString();
                            this.tempPassword = this.tempPassword.replace(/-/g, '');
                        } else {
                            this.tempPassword = "admin1234";
                        }
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
                            try {
                                const response = await this.$axios.post('http://127.0.0.1:5031/createProducerAccount', 
                                    {
                                        newBusinessData
                                    }, {
                                    headers: {
                                        'Content-Type': 'application/json'
                                    }
                                });

                                if (response.data.code == 201) {
                                    this.createBusinessSuccess = true;
                                    return true
                                } 
                            } catch (error) {
                                console.error(error);
                                if (error.response.data.code == 400) {
                                    this.createBusinessError = "Business name already exists";
                                    return false;
                                }
                            }
                        }
                    }
                }, 
                // reset when add a business button is clicked
                resetAddBusinessModal() {
                        this.businessType = "";
                        this.businessName = "";
                        this.businessDesc = "";
                        this.businessCountry = "";
                        this.businessClaimStatus = "";
                        this.tempPassword = "";
                        this.createBusinessSuccess = false;
                        this.createBusinessError = "";
                },

                updateUsername(){
                    // get error message element
                    let usernameError = document.getElementById("usernameError")
                    // find listing based on bottle name
                    let user = this.users.find(user => user.username === this.promotedUser)
                    if (user) {
                        this.selectedPromotedUser = user
                        usernameError.innerHTML = ""
                        let currentMod = user.modType
                        this.addableDrinkType = this.drinkTypes.filter(drinkType=>{
                            return !currentMod.includes(drinkType.drinkType);
                        })
                    }
                    else {
                        this.selectedPromotedUser = null
                        this.addableDrinkType= []
                        console.log(this.addableDrinkType)
                        usernameError.innerHTML = "Please enter a valid username"
                    }
                },
                updateModUsername(){
                    // get error message element
                    let usernameError = document.getElementById("modUsernameError")
                    // find listing based on bottle name
                    let user = this.moderators.find(user => user.username === this.removeMod)
                    if (user) {
                        this.selectedRemoveMod = user
                        usernameError.innerHTML = ""
                        let currentMod = user.modType
                        this.removableDrinkType = this.drinkTypes.filter(drinkType=>{
                            return currentMod.includes(drinkType.drinkType);
                        })
                    }
                    else {
                        this.selectedRemoveMod = null
                        this.removableDrinkType = []
                        console.log(this.removableDrinkType)
                        usernameError.innerHTML = "Please enter a valid username"
                    }
                },

                updateDrinkType(){
                    // get error message element
                    let promotedTypeError = document.getElementById("promotedTypeError")
                    // find listing based on bottle name
                    let drinkType = this.drinkTypes.find(drinkType => drinkType.drinkType === this.promotedType)
                    if (drinkType) {
                        this.selectedPromotedType = drinkType
                        promotedTypeError.innerHTML = ""
                    }
                    else {
                        this.selectedPromotedType = null
                        promotedTypeError.innerHTML = "Please enter a valid drink type"
                    }
                },
                updateRemovedDrinkType(){
                    // get error message element
                    let removedTypeError = document.getElementById("removedTypeError")
                    // find listing based on bottle name
                    let drinkType = this.drinkTypes.find(drinkType => drinkType.drinkType === this.removedType)
                    if (drinkType) {
                        this.selectedRemoveType = drinkType
                        removedTypeError.innerHTML = ""
                    }
                    else {
                        this.selectedRemoveType = null
                        removedTypeError.innerHTML = "Please enter a valid drink type"
                    }
                },

                addModerator(){
                    let errorMessage = ''
                    if(this.selectedPromotedUser == null){
                        errorMessage+="Please enter a valid username!\n"
                    }
                    if(this.selectedPromotedType == null){
                        errorMessage+="Please enter a valid drink type!\n"
                    }
                    if(errorMessage!=''){
                        alert(errorMessage)
                        return null
                    }
                    let alreadyModError = document.getElementById("alreadyModError")
                    if(this.selectedPromotedUser.modType.includes(this.selectedPromotedType.drinkType)){
                        alreadyModError.innerHTML = "This user is already a moderator for this drink type"
                        return null
                    }else{
                        alreadyModError.innerHTML = ""
                    }
                    this.confirmModerator = true
                    
                },
                removeModerator(){
                    let errorMessage = ''
                    if(this.selectedRemoveMod == null){
                        errorMessage+="Please enter a valid username!\n"
                    }
                    if(this.selectedRemoveType == null){
                        errorMessage+="Please enter a valid drink type!\n"
                    }
                    if(errorMessage!=''){
                        alert(errorMessage)
                        return null
                    }
                    let notModError = document.getElementById("notModError")
                    if(!this.selectedRemoveMod.modType.includes(this.selectedRemoveType.drinkType)){
                        notModError.innerHTML = "This user is not a moderator for this drink type"
                        return null
                    }else{
                        notModError.innerHTML = ""
                    }
                    this.confirmRemoveModerator = true
                    
                },

                async confirmAddModerator(){
                    try {
                        await this.$axios.post('http://127.0.0.1:5100/updateModType', 
                            {
                                userID: this.selectedPromotedUser._id.$oid,
                                newModType: this.selectedPromotedType.drinkType,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }).then(response => {
                            // Handle the response here
                            if(response.data.code == 201){
                                this.successAddMod = true
                                this.confirmModerator = false
                                this.selectedPromotedUser.modType.push(this.selectedPromotedType.drinkType)
                            }
                        });
                    } catch (error) {
                        console.error(error);
                        this.errorAddMod = true
                        this.confirmModerator = false
                    }
                },
                async confirmDowngradeModerator(){
                    try {
                        await this.$axios.post('http://127.0.0.1:5100/removeModType', 
                            {
                                userID: this.selectedRemoveMod._id.$oid,
                                removeModType: this.selectedRemoveType.drinkType,
                            }, {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }).then(response => {
                            // Handle the response here
                            if(response.data.code == 201){
                                this.successRemoveMod = true
                                this.confirmRemoveModerator = false
                                let modToDowngrade = this.selectedRemoveMod.modType.findIndex(obj => obj === this.selectedRemoveType.drinkType);
                                if (modToDowngrade !== -1) {
                                    this.selectedRemoveMod.modType.splice(modToDowngrade, 1);
                                }
                            }
                        });
                    } catch (error) {
                        console.error(error);
                        this.errorRemoveMod = true
                        this.confirmRemoveModerator = false
                    }
                },

                selectPromotedUser(){
                    this.confirmModerator=false
                    this.successAddMod = false
                    this.errorAddMod = false
                },
                selectRemoveMod(){
                    this.confirmRemoveModerator=false
                    this.successRemoveMod = false
                    this.errorRemoveMod = false
                },
                resetAddMod(){
                    this.confirmModerator=false
                    this.selectedPromotedType = null
                    this.selectedPromotedUser = null
                    this.promotedType=''
                    this.promotedUser=''
                    this.successAddMod = false
                    this.errorAddMod = false
                },
                resetRemoveMod(){
                    this.confirmRemoveModerator=false
                    this.selectedRemoveType = null
                    this.selectedRemoveMod = null
                    this.removedType=''
                    this.removeMod=''
                    this.successRemoveMod = false
                    this.errorRemoveMod = false
                }
            }
        }
</script>