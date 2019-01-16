import Vue from "vue";
import Router from "vue-router";
import Home from "./components/school/Home";
import SchoolHome from "./components/school/SchoolHome";
import SchoolSubmit from "./components/school/SchoolSubmit";
import SchoolDetail from "./components/school/SchoolDetail";
import School from "./components/school/School.vue";
import SignIn from "./components/SignIn.vue";
import store from "./store.js";

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      redirect: "/home"
    },
    {
      path: "/",
      component: School,
      beforeEnter: (to, from, next) => {
        store.dispatch("checkSession").then(function() {
          if (store.getters.isLoadedUser) {
            next();
          }
        });
        //TODO: should be handle dispatch promise failed
      },
      children: [
        { path: "/" },
        {
          path: "home",
          name: "home",
          component: Home
        },
      ]
    },
    {
      path: "/school",
      component: School,
      beforeEnter: (to, from, next) => {
        store.dispatch("checkSession").then(function() {
          if (store.getters.isLoadedUser) {
            next();
          }
        });
        //TODO: should be handle dispatch promise failed
      },
      children: [
        { path: "/school/", redirect: "home" },
        {
          path: ":id/view",
          name: "school.view",
          component: SchoolHome
        },
        {
          path: "add",
          name: "school.add",
          component: SchoolSubmit
        },
        {
          path: ":id/edit",
          name: "school.edit",
          component: SchoolSubmit
        },
        {
          path: ":school_id/season/:season_id",
          name: "school.detail",
          component: SchoolDetail
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
