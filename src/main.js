// Javascript file that kickstarts application. Imports root component, Bootstrap, and router, and mounts the app to the DOM.

// Import Axios
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/global.css';

// Set up Axios as a global property in Vue prototype
const app = createApp(App);
app.config.globalProperties.$axios = axios;

// Mount the app to the DOM
app.use(router).mount('#app');