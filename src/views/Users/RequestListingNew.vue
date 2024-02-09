<!-- User Form: Request for New Bottle Listing -->

<!--
    TODO:
    - [Access Control] Make accessible to only users within application
-->

<template>
    <NavBar />
    <SubmitListingNew mode="user" />
</template>

<script>
    import NavBar from '@/components/NavBar.vue';
    import SubmitListingNew from '@/components/SubmitListingNew.vue';

        export default {
            name: 'RequestListingNew',
            components: {
                NavBar,
                SubmitListingNew
            },
            mounted() {
                if (localStorage.getItem('88B_accType') != "user") {
                    this.$router.push({path: '/login'});
                }
            },
        }
</script>