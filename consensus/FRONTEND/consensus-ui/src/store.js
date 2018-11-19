import Vue from "vue";
import Vuex from "vuex";
import SessionApi from "@/endpoint/SessionApi";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentUser: {},
    currentSchool: {}
  },
  mutations: {
    currentUser: function(state, payload) {
      state.currentUser = payload.currentUser;
    }
  },
  actions: {
    checkSession: function(context) {
      return SessionApi.getUser().then(
        function(response) {
          context.commit({ type: "currentUser", currentUser: response.data });
        },
        function() {
          context.commit({ type: "currentUser", currentUser: {} });
        }
      );
    }
  },
  getters: {
    isStaffUser: function(state) {
      return true === state.currentUser.is_staff;
    },
    isSuperUser: function(state) {
      return true === state.currentUser.is_superuser;
    },
    isStaffOrSuperUser: function(state) {
      return (
        true === (state.currentUser.is_staff || state.currentUser.is_superuser)
      );
    },
    isLoadedUser: function(state) {
      return !!state.currentUser.id;
    }
  }
});
