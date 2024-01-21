<!-- Default generated view by Vue CLI, should not be actively used in the final version. -->
<!-- Currently used as Component Testing PLAYGROUND. -->

<template>
  <NavBar />
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>

</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    NavBar
}
}
</script>
