<template>
  <div class="school">
    <main-header></main-header>
    <router-view></router-view>
  </div>
</template>


<script>
// @ is an alias to /src
import MainHeader from "./MainHeader";

export default {
  name: "School",
  components: {
    MainHeader
  }
};
</script>


<style scoped>
.school {
  height: 100%;
}
</style>
