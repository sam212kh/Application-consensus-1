<template>
  <div id="app"><router-view /></div>
</template>

<script>
export default {
  name: "App",
  props: [],
  methods: {
    onSessionExpired: function() {
      this.$router.push({ name: "signIn" });
    }
  },
  watch: {
    "$store.state.currentUser": function() {
      if (!this.$store.getters.isLoadedUser) {
        this.$eventsBus.$emit("user:session-expired");
      }
    }
  },
  created: function() {
    this.$eventsBus.$on("user:session-expired", this.onSessionExpired);
  },
  destroyed: function() {
    this.$eventsBus.$off("user:session-expired", this.onSessionExpired);
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
