<template>
  <div class="container-fluid school.detail">
    <div class="row-no-padding">
      <div class="col">
        <school-staff v-bind:schoolId="schoolId"></school-staff>
      </div>
    </div>
    <div class="row-no-padding">
      <div class="col"><h1 /></div>
    </div>
    <div class="row-no-padding">
      <div class="col">
        <school-season
          :school-id="schoolId"
          :season-id="seasonId"
        ></school-season>
      </div>
    </div>
  </div>
</template>

<script>
import SchoolStaff from "./SchoolStaff";
import SchoolSeason from "./SchoolSeason";

export default {
  name: "SchoolDetail",
  mixins: [],
  components: {
    SchoolStaff,
    SchoolSeason
  },
  created: function() {
    this.$eventsBus.$emit("header:title", "School's season");
    this.schoolId = +this.$route.params.school_id;
    this.seasonId = +this.$route.params.season_id;
  },
  data: function() {
    return {
      schoolId: 0,
      seasonId: 0
    };
  },
  methods: {}
};
</script>

<style scoped>
school.detail {
  height: 100%;
}
</style>
