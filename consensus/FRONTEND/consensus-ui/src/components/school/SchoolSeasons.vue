<template>
  <table border="0">
    <thead>
      <tr>
        <th>Name</th>
        <th>Application</th>
        <th>score</th>
        <th>Enrolled</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="season in rowData.seasons" :key="season.id">
        <td class="clickable" v-on:click="gotoSeasonHome(season);">
          {{ season.full_name }}
        </td>
        <td>{{ season.application }}</td>
        <td>{{ season.scored }}</td>
        <td>{{ season.enrolled }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "SchoolSeasons",
  props: {
    rowData: {
      type: Object,
      required: true
    },
    rowIndex: {
      type: Number
    }
  },
  methods: {
    gotoSeasonHome: function(season) {
      this.$router.push({
        name: "school.detail",
        params: { school_id: this.rowData.id, season_id: season.id }
      });
    }
  }
};
</script>

<style scoped>
.clickable {
  color: #2185d0;
  cursor: pointer;
}
</style>
