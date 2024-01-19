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
    path: '/userprofile',
    name: 'userprofile',
    component: () => import(/* webpackChunkName: "about" */ '../views/UserProfile.vue')
  },
  {
    path: '/Producer/Producer-Listings',
    name: 'producerbottlelistings',
    component: () => import(/* webpackChunkName: "about" */ '../views/Producer/ProducerListings.vue')
  },  
  {
    path: '/Producer/Producer-Create-Listing',
    name: 'producercreatelistings',
    component: () => import(/* webpackChunkName: "about" */ '../views/Producer/CreateListing.vue')
  },  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
