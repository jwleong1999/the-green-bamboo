<!-- Component for drinks display. Used in all profile pages. -->

<template>
    <h3 class="text-body-secondary text-start pt-4"> 
        <b> {{ displayName }} </b> 
    </h3>
    <div class="container">
        <div class="row ">
            <div v-for="(listing, index) in listingArr" :key="index" class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-2 align-items-center" :style="{ display: 'flex', flexDirection: 'column', width: columnWidth }">
                <div class="drink-photo-container-row image-container-150">
                    <router-link :to="{ path: '/Producers/Bottle-Listings/' + listing._id.$oid }" class="default-text-no-background">
                        <img v-if="listing.photo != ''" :src=" 'data:image/jpeg;base64,' + (listing.photo)" class="add-drink-photo-background centered rounded"> 
                        <img v-else src="../../Images/Drinks/Placeholder.png" class="add-drink-photo-background centered rounded">
                    </router-link>
                    
                    <BookmarkIcon 
                        v-if="user" 
                        :user="user" 
                        :listing="listing" 
                        :overlay="true"
                        size="20"
                        @icon-clicked="handleIconClick" />

                </div>
                <router-link :to="{ path: '/Producers/Bottle-Listings/' + listing._id.$oid }" class="default-clickable-text scrollable mt-3 mx-2" style="text-align: center">
                    {{ listing.listingName }}
                </router-link>
            </div>
        </div>
    </div>

</template>

<script>
import BookmarkIcon from '@/components/BookmarkIcon.vue';

    export default {
        name: "ListingRowDisplay",
        components: {
            BookmarkIcon,
            // BookmarkModal,
        },
        props: {
            displayName: String,
            listingArr: Array,
            user: Object,
            listing: Object,
            columnWidth: {
                type: String,
                default: '175px'
            }
},
        methods: {
            handleIconClick(data) {
                this.$emit('icon-clicked', data);
            },

        }
    }
</script>