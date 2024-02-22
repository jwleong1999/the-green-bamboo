<!-- Form: Create New Bottle Listing -->

<template>
    <NavBar />
    <SubmitListingNew mode="power" />
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import SubmitListingNew from '@/components/SubmitListingNew.vue';

    export default {
        name: 'CreateListing',
        components: {
            NavBar,
            SubmitListingNew
        },
        mounted() {
            if (localStorage.getItem('88B_accType') != "producer") {
                alert("This page is only accessible to producers! Please log in as a producer to access this page.")
                this.$router.push({path: '/login'});
            }
        },
    };
</script>


