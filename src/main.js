// Javascript file that kickstarts application. Imports root component, Bootstrap, and router, and mounts the app to the DOM.

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/global.css';

createApp(App).use(router).mount('#app')
