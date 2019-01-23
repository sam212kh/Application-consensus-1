import Vue from "vue";
import Router from "vue-router";
import Home from "./components/Home";
import SchoolHome from "./components/school/SchoolHome";
import SchoolSubmit from "./components/school/SchoolSubmit";
import SeasonHome from "./components/school/season/SeasonHome";
import Schools from "./components/school/Schools.vue";
import SignIn from "./components/SignIn.vue";

import store from "./store.js";



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
          component: Schools
        },
        {
          path: "/school/:id/home",
          name: "school.home",
          component: SchoolHome
        },
        {
          path: "/school/add",
          name: "school.add",
          component: SchoolSubmit
        },
        {
          path: "/school/:id/edit",
          name: "school.edit",
          component: SchoolSubmit
        },
        {
          path: "/school/:school_id/season/:season_id",
          name: "season.home",
          component: SeasonHome
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
