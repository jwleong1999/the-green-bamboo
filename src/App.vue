<!-- Root Component File. -->

<template>
  <!-- Temporary page navigation, to be removed eventually. -->
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/Login">LoginPage</router-link> |
    <router-link to="/about">About</router-link>
    <br>
    <router-link to="/Users/Bottle-Listings">(Users) Bottle Listings</router-link> |
    <router-link to="/Users/request/new">(Users) Request Listing [New]</router-link> |
    <router-link to="/Users/request/modify/edit">(Users) Request Listing [Modify]</router-link> |
    <router-link to="/Users/request/modify/duplicate">(Users) Request Listing [Duplicate]</router-link> |
    <router-link to="/userprofile">User Profile</router-link>
    <br>
    <router-link to="/Producers/Bottle-Listings">(Producers) Bottle Listings</router-link> |
    <router-link to="/Producers/Profile-Page">(Producers) Profile Page </router-link> |
    <router-link to="/Producer/Producer-Listings">(Producers) Listings </router-link> |
    <router-link to="/Producer/Producer-Create-Listing">(Producers) Create Listings</router-link> |
    <router-link to="/Producer/Producer-Edit-Listing">(Producers) Edit Listings</router-link> |
    <router-link to="/producers/requests">(Producers) View Requests</router-link>
  </nav>
  <hr style="margin: 0;">
  <router-view/>
</template>

<style>
/* Styling from App.vue */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>