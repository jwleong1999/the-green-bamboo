import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // ----------------- MAIN PAGES -----------------
  {
    // path: '/',
    // name: 'home',
    path: '/Users/Bottle-Listings',
    name: 'usersbottlelistings',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Users/BottleListings.vue')
  },
  {
    path: '/login',
    // name: 'login',
    name: 'loginpage',
    component: () => import('../views/LoginPage.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUpPage.vue')
  },
  {
    path: '/businessSignup',
    name: 'businesssignup',
    component: () => import('../views/BusinessSignUpPage.vue')
  },
  {
    path: '/search/:input?',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  // -------------------------------------------------------------------------------------
  
  // ----------------- PROFILE PAGES -----------------
  {
    // path: '/profile/user/:userID?',
    // name: 'profileuser',
    path: '/userprofile/:id?',
    name: 'userprofile',
    component: () => import('../views/UserProfile.vue')
  },
  {
    // path: '/profile/producer/:producerID?',
    // name: 'profileproducer',
    path: '/Producers/Profile-Page/:id',
    name: 'producersprofilepage',
    component: () => import('../views/Producers/ProducerProfile.vue')
  },
  {
    // path: '/profile/venue/:venueID?',
    // name: 'profilevenue',
    path: '/Venues/Profile-Page/:id',
    name: 'venuesprofilepage',
    component: () => import('../views/Venues/VenueProfile.vue')
  },
  // -------------------------------------------------------------------------------------

  // ----------------- LISTING PAGES -----------------
  {
    // path: '/listing/view/:listingID',
    // name: 'listingview',
    path: '/Producers/Bottle-Listings/:id',
    name: 'producersbottlelistings',
    component: () => import('../views/Producers/BottleListings.vue')
  },
  {
    // path: '/listing/create/:requestID?',
    // name: 'listingcreate',
    path: '/Producer/Producer-Create-Listing/:requestID?',
    name: 'producercreatelistings',
    component: () => import('../views/Producers/CreateListing.vue')
  },
  {
    // path: '/listing/edit/:listingID/:requestID?',
    // name: 'listingedit',
    path: '/Producer/Producer-Edit-Listing/:listingID/:requestID?',
    name: 'producerupdatelistingsdetails',
    component: () => import('../views/Producers/EditListing.vue')
  },
  // -------------------------------------------------------------------------------------
  
  // ----------------- REQUEST PAGES -----------------
  {
    // path: '/request/view',
    // name: 'requestview',
    path: '/producers/requests',
    name: 'producersrequests',
    component: () => import('../views/Producers/ViewRequests.vue')
  },
  {
    // path: '/request/new/:requestID?',
    // name: 'requestnew',
    path: '/Users/request/new/:requestID?',
    name: 'usersrequestlistingnew',
    component: () => import('../views/Users/RequestListingNew.vue')
  },
  {
    // path: '/request/modify/:mode/:listingID/:requestID?',
    // name: 'requestmodify',
    path: '/Users/request/modify/:mode/:listingID/:requestID?',
    name: 'usersrequestlistingmodify',
    component: () => import('../views/Users/RequestListingModify.vue')
  },

  // -------------------------------------------------------------------------------------

  // ----------------- Q&A PAGES -----------------
  {
    path: '/Producers/ProducersQA/:id',
    name: 'producersqanda',
    component: () => import('../views/Producers/ProducersQA.vue')
  },
  {
    path: '/Venues/VenuesQA/:id',
    name: 'venuessqanda',
    component: () => import('../views/Venues/VenuesQA.vue')
  },

  // -------------------------------------------------------------------------------------
  
  {
    // TO BE DELETED
    path: '/Producer/Producer-Edit-Listing',
    name: 'producerupdatelistings',
    component: () => import('../views/Producers/EditHome.vue')
  },
  {
    path: '/Venues/Add-Menu/:id',
    name: 'venuesaddmenu',
    component: () => import('../views/Venues/AddMenu.vue')
  },
  {
    // TO BE DELETED
    path: '/Venues/Bottle-Listings',
    name: 'venuesbottlelistings',
    component: () => import('../views/Venues/BottleListings.vue')
  },
  {
    // TO BE DELETED
    path: '/Producer/Producer-Listings',
    name: 'producerlistings',
    component: () => import('../views/Producers/ProducerListings.vue')
  },
  {
    // TO BE DELETED
    // path: '/test/home',
    // name: 'testhome',
    path: '/',
    name: 'home',
    component: () => import('../views/zToBeDeleted/HomeView.vue')
  },
  {
    // TO BE DELETED
    // path: '/test/about',
    // name: 'testabout',
    path: '/about',
    name: 'about',
    component: () => import('../views/zToBeDeleted/AboutView.vue')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
