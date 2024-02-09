<!-- HTML -->
<template>
    <!-- navbar-->
    <NavBar />
    <SubmitListingNew mode = "power" />
    


</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    // import axios from 'axios'
    import NavBar from '@/components/NavBar.vue'
    import SubmitListingNew from '@/components/SubmitListingNew.vue'
    export default {
        components:{
            NavBar,
            SubmitListingNew
        },
        mounted() {
            if (localStorage.getItem('88B_accType') != "producer") {
                this.$router.push({path: '/login'});
            }
        },
    };
    
</script>


