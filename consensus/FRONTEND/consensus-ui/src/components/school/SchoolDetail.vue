<template>
  <div class="school.detail">
    <school-staff v-bind:schoolId="schoolId"></school-staff>
    <school-season
      v-bind:schoolId="schoolId"
      :seasonId="seasonId"
    ></school-season>
  </div>
</template>

<script>
import SchoolSeason from "./SchoolSeason";
import SchoolStaff from "./SchoolStaff";

export default {
  name: "SchoolDetail",
  mixins: [],
  components: {
    SchoolSeason,
    SchoolStaff
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
