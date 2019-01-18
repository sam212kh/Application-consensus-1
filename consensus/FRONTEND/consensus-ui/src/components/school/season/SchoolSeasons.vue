<template>
  <table border="0">
    <thead>
      <tr>
        <th>Name</th>
        <th>Application</th>
        <th>score</th>
        <th>Enrolled</th>
        <th>#</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="season in rowData.seasons" :key="season.id">
        <td>
          {{ season.full_name }}
        </td>
        <td>{{ season.application || 0 }}</td>
        <td>{{ season.scored || 0 }}</td>
        <td>{{ season.enrolled || 0 }}</td>
        <td>
          <router-link
            class="btn btn-info btn-sm"
            :to="{ name: 'season.home', params: { school_id: rowData.id, season_id: season.id } }"
          >
            <span class="fa fa-eye"></span>
          </router-link>
        </td>
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
  }
};
</script>

<style scoped>
</style>
