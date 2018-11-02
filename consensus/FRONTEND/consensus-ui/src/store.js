import Vue from "vue";
import Vuex from "vuex";
import SessionApi from "@/endpoint/SessionApi"


Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        currentUser: {}
    },
    mutations: {
        currentUser: function (state, payload) {
            state.currrentUser = payload.currentUser;
        }
    },
    actions: {
        isLogin: function (context) {
            return SessionApi.login().then(
                function (response) {
                    context.commit({type: 'currentUser', currentUser: response.data});
                },
                function (error) {
                    context.commit({type: 'currentUser', currentUser: {}});
                });
        }
    },
    getters: {
        isStaffUser: function (state) {
            return true === state.currentUser.is_staff;
        },
        isSuperUser: function (state) {
            return true === state.currentUser.is_superuser;
        },
        isStaffOrSuperUser: function (state) {
            return (
                true === (state.currentUser.is_staff || state.currentUser.is_superuser)
            );
        },
        isLoadedUser: function (state) {
            return !!state.currentUser.id;
        }
    }
});
