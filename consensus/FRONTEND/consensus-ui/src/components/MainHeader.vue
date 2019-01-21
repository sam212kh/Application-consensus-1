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
          <template>
            <b-breadcrumb :items="items" separator="chevron_right"/>
          </template>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import SessionApi from "@/endpoint/SessionApi";
import UtilMixin from "@/mixins/UtilMixin";




import bBreadcrumb from 'bootstrap-vue/es/components/breadcrumb/breadcrumb';




export default {
  name: "MainHeader",
  mixins: [UtilMixin],
  components: {
      bBreadcrumb
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
      if( this.pageList.indexOf(title) == -1  ){
          this.pageList.push(title);
          this.items.push({text:title,to:this.$route.path});
      }else{
        this.items.splice(this.pageList.indexOf(title)+1,2 )
        this.pageList.splice(this.pageList.indexOf(title)+1,2 )
      }
      this.title = title;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.breadcrumb{
  background: #eee;
  border-width: 1px;
  border-style: solid;
  border-color: #f5f5f5 #e5e5e5 #ccc;
  border-radius: 5px;
  box-shadow: 0 0 2px rgba(0,0,0,.2);
  overflow: hidden;
  width: 100%;
}

.breadcrumb-item{
  float: left;
}

.breadcrumb li{
  padding: .7em 1em .7em 2em;
  float: left;
  text-decoration: none;
  color: #444;
  position: relative;
  text-shadow: 0 1px 0 rgba(255,255,255,.5);
  background-color: #ddd;
  background-image: linear-gradient(to right, #f5f5f5, #ddd);
}

.breadcrumb li:first-child a{
  padding-left: 1em;
  border-radius: 5px 0 0 5px;
}



.breadcrumb-item a::after,
.breadcrumb-item a::before{
  content: "";
  position: absolute;
  top: 50%;
  margin-top: -1.5em;
  border-top: 1.5em solid transparent;
  border-bottom: 1.5em solid transparent;
  border-left: 1em solid;
  right: -1em;
}

.breadcrumb-item a::after{
  z-index: 2;
  border-left-color: #ddd;
}

.breadcrumb-item a::before{
  border-left-color: #ccc;
  right: -1.1em;
  z-index: 1;
}


.breadcrumb .active,
.breadcrumb .active:hover{
  font-weight: bold;
  background: none;
}

.breadcrumb .active::after,
.breadcrumb .active::before{
  content: normal;
}
</style>
