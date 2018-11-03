import Vue from "vue";
import axios from "axios";

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
Vue.prototype.$eventsBus = new Vue();

/****************************************
 ****************** App *****************
 ****************************************/

axios.defaults.baseURL = "/api/v1";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true; // allow to pass cookie in cross origin

Vue.prototype.$http = axios;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
