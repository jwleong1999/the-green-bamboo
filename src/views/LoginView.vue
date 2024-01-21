<!-- Log In / Sign Up page. Should be able to handle all account types and both login / sign up functions. -->

<!-- WORK IN PROGRESS -->

<template>
    <NavBar />
    <h3>Log In / Sign Up Placeholder Page</h3>
    <button type="button" class="btn btn-dark" @click="goBack">Go Back</button>
</template>

<script>
    import NavBar from '@/components/NavBar.vue'

    export default {
        name: "LoginView",
        components: {
            NavBar
        },
        methods: {
            goBack() {
                this.$router.go(-1)
            }
        }
    }
</script>