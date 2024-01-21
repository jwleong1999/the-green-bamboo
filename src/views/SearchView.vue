<!-- Search page from navigation bar. Globally available, and should still use NavBar for new search queries. -->

<!-- WORK IN PROGRESS -->

<!-- CURRENT ISSUES:
1. While using NavBar does update URL query for search input, page does not reload to reflect change.
2. Search input is not retained when navigating back to previous pages. Potentially acceptable.
3. If multiple consecutive searches made, "Go Back" button returns to an older search instead of "real" previous page. Potentially acceptable. -->

<template>
    <NavBar />
    <h3>Search Results Placeholder:</h3>
    <p>{{ searchInput }}</p>
    <button type="button" class="btn btn-dark" @click="goBack">Go Back</button>
</template>

<script>
    import '../assets/global.css'
    import NavBar from '@/components/NavBar.vue'

    export default {
        name: "SearchView",
        components: {
            NavBar
        },
        data() {
            return {
                searchInput: this.$route.query.input
            }
        },
        methods: {
            goBack() {
                this.$router.go(-1)
            }
        }
    }
</script>