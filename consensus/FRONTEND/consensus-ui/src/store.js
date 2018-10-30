import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentUser: {}
  },
  mutations: {},
  actions: {},
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
