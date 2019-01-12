import Vue from "vue";
import EventBus from "./event-bus";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import SchoolSeasons from "./components/school/SchoolSeasons";

Vue.config.productionTip = false;
Vue.prototype.$eventsBus = EventBus;

/****************************************
 ****************** App *****************
 ****************************************/

Vue.component("school-seasons", SchoolSeasons);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
