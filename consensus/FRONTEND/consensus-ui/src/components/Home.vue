<template>
  <div class="home">
    <main-header></main-header>
    <router-view></router-view>
  </div>
</template>

<script>
// @ is an alias to /src
import MainHeader from "./MainHeader";

export default {
  name: "Home",
  components: {
    MainHeader
  }
};
</script>

<style scoped>
.home {
  height: 100%;
}
</style>
