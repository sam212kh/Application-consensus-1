<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <a class="navbar-brand" href="#">Your Title</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse  justify-content-end" id="navbarSupportedContent">
        <ul class="navbar-nav margin-right-10">
          <li class="nav-item margin-right-10">
            <a class="nav-link" href="#">
              <span class="notice">2</span>
              <i class="fa fa-bell"></i>
            </a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#" v-on:click="logout">
              <i class="fa fa-sign-out"></i>
              LogOut
            </a>
          </li>
          <li class="nav-item dropdown active">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
               data-toggle="dropdown"
               aria-haspopup="true" aria-expanded="false">
              {{fullName}}
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
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
              <a class="dropdown-item" href="#">
                <i class="fa fa-sign-out color-lightPink"></i>
                <span class="margin-left-10 color-gray">LogOut</span>
              </a>
            </div>
          </li>
        </ul>
        <div class="nav-pic">
          <img src="images/avatar.png"/>
        </div>
      </div>
    </nav>
    <div class="content-header">
      <div class="row">
        <div class="col-md-12 col-sm-12 col-xs-12">
          <ol class="breadcrumb">
            <li class="active"><i class="fa fa-dashboard"></i> Home</li>
          </ol>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import SessionApi from "@/endpoint/SessionApi";

export default {
  name: "MainHeader",
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
        function(data) {
          console.log(data);
        }
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
