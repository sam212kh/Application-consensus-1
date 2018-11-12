<template>
  <section class="container-fluid">
    <div class="row row-no-padding">
      <div class="col-md-9 col-sm-9 col-xs-9"></div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <button class="btn btn-block btn-info">
          <i class="fa fa-plus"></i> Add a new School
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col">
        <vuetable
          ref="vuetable"
          :api-url="tableUrl"
          :fields="tableFields"
          :css="css"
          data-path="results"
        ></vuetable>
      </div>
    </div>
  </section>
</template>

<script>
import UtilMixin from "@/mixins/UtilMixin";
import Vuetable from "vuetable-2/src/components/Vuetable";

export default {
  name: "Home",
  mixins: [UtilMixin],
  components: {
    Vuetable
  },
  created: function() {},
  data: function() {
    return {
      tableUrl: "api/v1/school",
      tableFields: [
        {
          sortField: "full_name",
          name: "full_name",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          sortField: "phone_number",
          name: "phone_number",
          titleClass: "text-left",
          dataClass: "text-left"
        }
      ],
      css: {
        tableClass: "table table-striped table-bordered",
        ascendingIcon: "glyphicon glyphicon-chevron-up",
        descendingIcon: "glyphicon glyphicon-chevron-down",
        handleIcon: "glyphicon glyphicon-menu-hamburger"
      },
      schools: []
    };
  }
};
</script>
