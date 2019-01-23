<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <a class="navbar-brand" href="#">{{ title }}</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse  justify-content-end"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav margin-right-10">
          <li class="nav-item margin-right-10">
            <a class="nav-link" href="#">
              <span class="notice">2</span> <i class="fa fa-bell"></i>
            </a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#" v-on:click="logout">
              <i class="fa fa-sign-out"></i> LogOut
            </a>
          </li>
          <li class="nav-item dropdown active">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              {{ fullName }}
            </a>
            <div
              class="dropdown-menu dropdown-menu-right"
              aria-labelledby="navbarDropdown"
            >
              <a class="dropdown-item" href="#">
                <i class="fa fa-user color-lightPink"></i>
                <span class="margin-left-10 color-gray">My Profile</span>
              </a>
              <a class="dropdown-item" href="#">
                <i class="fa fa-link color-lightPink"></i>
                <span class="margin-left-10 color-gray">Activity</span>
              </a>
              <a class="dropdown-item" href="#">
                <i class="fa fa-envelope color-lightPink"></i>
                <span class="margin-left-10 color-gray">Messages</span>
              </a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#" v-on:click="logout">
                <i class="fa fa-sign-out color-lightPink"></i>
                <span class="margin-left-10 color-gray">LogOut</span>
              </a>
            </div>
          </li>
        </ul>
        <div class="nav-pic"><img src="images/avatar.png" /></div>
      </div>
    </nav>
    <div class="content-header">
      <div class="row">
        <div class="col-md-12 col-sm-12 col-xs-12">
          <breadcrumb></breadcrumb>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import SessionApi from "@/endpoint/SessionApi";
import UtilMixin from "@/mixins/UtilMixin";
import Breadcrumb from "./Breadcrumb.vue";

export default {
  name: "MainHeader",
  mixins: [UtilMixin],
  components: {
    Breadcrumb
  },
  created: function() {
    this.$eventsBus.$on("header:title", this.onTitleChanged);
  },
  data: function() {
    return {
      pageList: [],
      items: [],
      title: "Home"
    };
  },
  computed: {
    fullName: function() {
      return (
        this.$store.state.currentUser.first_name +
        " " +
        this.$store.state.currentUser.last_name
      );
    }
  },
  methods: {
    logout: function() {
      let self = this;
      SessionApi.logout().then(
        function() {
          self.$router.push({ name: "signIn" });
        },
        function(error) {
          self.notifyDefaultServerError(error);
        }
      );
    },
    onTitleChanged: function(title) {
      if (this.pageList.indexOf(title) == -1) {
        this.pageList.push(title);
        this.items.push({ text: title, to: this.$route.path });
      } else {
        this.items.splice(this.pageList.indexOf(title) + 1, 2);
        this.pageList.splice(this.pageList.indexOf(title) + 1, 2);
      }
      this.title = title;
    }
  }
};
</script>
