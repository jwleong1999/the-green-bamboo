<!-- User Form: Request for New Bottle Listing -->

<!--
    TODO:
    - Make accessible to only users within application
    - Consider if any duplicate submission has to be detected / prevented. Includes requests for bottles that already exist.
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
            }
        }
</script>