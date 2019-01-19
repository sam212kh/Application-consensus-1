<template>
  <section class="container">
    <div class="row row-no-padding">
      <div class="col">
        <school-season v-bind:schoolId="schoolId"></school-season>
        <school-staff v-bind:schoolId="schoolId"></school-staff>
      </div>
    </div>
  </section>
</template>

<script>
import UtilMixin from "@/mixins/UtilMixin";
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import VuetableBootstrapMixin from "../../mixins/VuetableBootstrapMixin";
import bModal from "bootstrap-vue/es/components/modal/modal";
import SchoolStaff from "./SchoolStaff";
import SchoolSeason from "./season/SchoolSeason";

export default {
  name: "SchoolHome",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    SchoolStaff,
    SchoolSeason,
    VuetablePagination,
    "b-modal": bModal
  },
  data: function() {
    return {
      schoolId: this.$route.params.id
    };
  }
};
</script>

<style></style>
