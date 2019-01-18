<template>
  <section class="container">
    <div class="row row-no-padding">
      <div class="col">
        <season v-bind:schoolId="schoolId"></season>
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
import schoolApi from "@/endpoint/SchoolApi";
import seasonApi from "@/endpoint/SeasonApi";
import SchoolStaff from "./SchoolStaff";
import Season from "./Season";

export default {
  name: "SchoolHome",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    SchoolStaff,
    Season,
    VuetablePagination,
    "b-modal": bModal
  },
  data: function() {
    return {
      schoolId: this.$route.params.id,
    }
  }
};
</script>

<style>
.school-table .vuetable-th-slot-actions {
  width: 200px;
  min-width: 200px;
}

.clickable {
  cursor: pointer;
}
</style>
