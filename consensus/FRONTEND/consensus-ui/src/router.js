import Vue from "vue";
import Router from "vue-router";
import Home from "./components/Home";
import SchoolHome from "./components/school/SchoolHome";
import SchoolSubmit from "./components/school/SchoolSubmit";
import SeasonHome from "./components/school/season/SeasonHome";
import Schools from "./components/school/Schools.vue";
import SignIn from "./components/SignIn.vue";

import store from "./store.js";

import VueBreadcrumbs from 'vue-breadcrumbs'

Vue.use(VueBreadcrumbs)

Vue.use(VueBreadcrumbs, {
  template: '<nav class="breadcrumb" v-if="$breadcrumbs.length"> ' +
    '<router-link class="breadcrumb-item" v-for="(crumb, key) in $breadcrumbs" :to="linkProp(crumb)" :key="key">{{ crumb | crumbText }}</router-link> ' +
    '</nav>'
});

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: Home,

      beforeEnter: (to, from, next) => {
        store.dispatch("checkSession").then(function() {
          if (store.getters.isLoadedUser) {
            next();
          }
        });
        //TODO: should be handle dispatch promise failed
      },
      children: [
        {
          path: "",
          name: "schools",
          component: Schools,
          meta:{
            breadcrumb: [
              {name:'Schools', link:'/'}
            ]
          },
        },
        {
          path: "/school/:id/home",
          name: "school.home",
          component: SchoolHome,
          meta:{
            breadcrumb: [
              {name:'Schools', link:'/'},
              {name:'School home'}
            ]
          },
        },
        {
          path: "/add",
          name: "school.add",
          component: SchoolSubmit,
          meta:{
            breadcrumb: [
              {name:'Schools', link:'/'},
              {name:'New School'}
            ]
          }
        },
        {
          path: "/:id/edit",
          name: "school.edit",
          component: SchoolSubmit,
          meta:{
            breadcrumb: [
              {name:'Schools', link:'/'},
              {name:'Edit School'}
            ]
          }
        },
        {
          path: "/:school_id/season/:season_id",
          name: "season.home",
          component: SeasonHome,
          meta:{
            breadcrumb: [
              {name: 'Schools', link:'/'},
              {name: 'School', link: '/'},
              {name: "School's season"}
            ]
          }
        }
      ]
    },
    {
      path: "/singIn",
      name: "signIn",
      component: SignIn
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./components/About.vue")
    }
  ]
});
