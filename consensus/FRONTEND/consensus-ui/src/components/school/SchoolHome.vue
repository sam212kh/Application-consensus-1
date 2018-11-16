<template>
  <section class="container-fluid">
    <div class="row row-no-padding">
      <div class="col-md-9 col-sm-9 col-xs-9"></div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <button class="btn btn-block btn-info" v-on:click="goToAddSchool">
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
          :css="css.table"
          :query-params="{
            sort: 'order_by',
            page: 'page',
            perPage: 'page_size'
          }"
          data-path="results"
          pagination-path="pagination"
          @vuetable:pagination-data="onPaginationData"
        >
          <template slot="actions" scope="props">
            <div class="table-button-container">
              <button
                class="btn btn-warning btn-sm"
                @click="editRow(props.rowData);"
              >
                <span class="glyphicon glyphicon-pencil"></span> Edit</button
              >&nbsp;&nbsp;
              <button
                class="btn btn-danger btn-sm"
                @click="deleteRow(props.rowData);"
              >
                <span class="glyphicon glyphicon-trash"></span> Delete</button
              >&nbsp;&nbsp;
            </div>
          </template>
        </vuetable>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col">
        <vuetable-pagination
          ref="pagination"
          :css="css.pagination"
          @vuetable-pagination:change-page="onChangePage"
        ></vuetable-pagination>
      </div>
    </div>
  </section>
</template>

<script>
import UtilMixin from "@/mixins/UtilMixin";
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import VuetableBootstrapMixin from "../../mixins/VuetableBootstrapMixin";
import SchoolApi from "@/endpoint/SchoolApi";

export default {
  name: "Home",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination
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
        },
        "__slot:actions"
      ],
      schools: []
    };
  },
  methods: {
    goToAddSchool: function() {
      this.$store.commit("currentSchool", {});
      this.$router.push({ name: "school.submit" });
    },
    deleteRow: function(school) {
      let self = this;
      SchoolApi.delete(school).then(
        function() {
          self.$refs.vuetable.refresh();
          self.notifySuccess("The school deleted");
        },
        function() {
          self.notifyError(
            "Some error happened when trying to delete the school"
          );
        }
      );
    },
    editRow: function(school) {
      this.$store.commit("currentSchool", school);
      this.$router.push({ name: "school.submit" });
    }
  }
};
</script>
