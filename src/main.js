// Javascript file that kickstarts application. Imports root component, Bootstrap, and router, and mounts the app to the DOM.

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

createApp(App).use(router).mount('#app')
