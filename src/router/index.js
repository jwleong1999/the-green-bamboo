import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/Users/Bottle-Listings',
    name: 'usersbottlelistings',
    component: () => import(/* webpackChunkName: "about" */ '../views/Users/BottleListings.vue')
  }, 
  {
    path: '/Producers/Bottle-Listings',
    name: 'producersbottlelistings',
    component: () => import(/* webpackChunkName: "about" */ '../views/Producers/BottleListings.vue')
  },  
  {
    path: '/userprofile',
    name: 'userprofile',
    component: () => import(/* webpackChunkName: "about" */ '../views/UserProfile.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
