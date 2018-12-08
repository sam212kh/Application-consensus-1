<template>
  <section class="container">
    <div class="row row-no-padding justify-content-end">
      <div class="col-3">
        <button class="btn btn-block btn-info" v-on:click="goToAddSchool">
          <i class="fa fa-plus"></i> Add a new School
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col">
        <vuetable
          ref="vuetable"
          :api-mode="false"
          :data="localData"
          :api-url="tableUrl"
          :fields="tableFields"
          :css="css.table"
          class="school-table"
          detail-row-component="school-detail-home"
          @vuetable:cell-clicked="onCellClicked"
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
                @click="showConfirmDeleteModal(props.rowData);"
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
    <b-modal
      centered
      ref="confirmDeleteModalRef"
      id="confirmDeleteModal"
      :hide-header="true"
    >
      <p class="text-danger h6">Are you sure to delete this record?</p>
      <div slot="modal-footer" class="w-100">
        <button
          type="button"
          class="btn btn-secondary float-left"
          @click="$refs.confirmDeleteModalRef.hide();"
        >
          <i class="la la-close"></i> Cancel
        </button>
        <button
          type="button"
          class="btn btn-danger float-right"
          :disabled="deletingRecord"
          @click="deleteSchool();"
        >
          <i
            :class="deletingRecord ? 'la la-spin la-spinner' : 'la la-trash'"
          ></i>
          <span v-show="!deletingRecord">Delete</span>
          <span v-show="deletingRecord">Deleting</span>
        </button>
      </div>
    </b-modal>
  </section>
</template>

<script>
import UtilMixin from "@/mixins/UtilMixin";
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import VuetableBootstrapMixin from "../../mixins/VuetableBootstrapMixin";
import bModal from "bootstrap-vue/es/components/modal/modal";
import SchoolApi from "@/endpoint/SchoolApi";

export default {
  name: "SchoolHome",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination,
    "b-modal": bModal
  },
  created: function() {
    this.localData = SchoolApi.getAll();
  },
  data: function() {
    return {
      localData: {},
      tableUrl: "/api/v1/school",
      tableFields: [
        {
          sortField: "full_name",
          name: "full_name",
          title: `<span class="icon is-small orange"><i class="fa fa-book color-gray"></i></span> School`,
          titleClass: "text-left",
          dataClass: "text-left clickable"
        },
        {
          name: "total_staff_count",
          title: `<span class="icon is-small orange"><i class="fa fa-users color-gray"></i></span> Staff`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "total_season_count",
          title: `<span class="icon is-small orange"><i class="fa fa-calendar color-gray"></i></span> Season`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "total_application_count",
          title: `<span class="icon is-small orange"><i class="fa fa-send color-gray"></i></span> Application`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "total_score_count",
          title: `<span class="icon is-small orange"><i class="fa fa-handshake-o color-gray"></i></span> Enrolled`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "total_enrolled_count",
          title: `<span class="icon is-small orange"><i class="fa fa-calendar color-gray"></i></span> Season`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        "__slot:actions"
      ],
      schools: [],
      selectedSchoolForDelete: null,
      deletingRecord: false
    };
  },
  methods: {
    goToAddSchool: function() {
      this.$router.push({ name: "school.add" });
    },
    showConfirmDeleteModal: function(school) {
      this.selectedSchoolForDelete = school;
      this.$refs.confirmDeleteModalRef.show();
    },
    deleteSchool: function() {
      let self = this;
      self.deletingRecord = true;
      SchoolApi.delete(self.selectedSchoolForDelete).then(
        function() {
          self.$refs.vuetable.refresh();
          self.deletingRecord = false;
          self.$refs.confirmDeleteModalRef.hide();
          self.notifySuccess("The school deleted");
        },
        function() {
          self.deletingRecord = false;
          self.notifyError(
            "Some error happened when trying to delete the school"
          );
        }
      );
    },
    editRow: function(school) {
      this.$router.push({ name: "school.edit", params: { id: school.id } });
    },
    onCellClicked: function(data) {
      this.$refs.vuetable.toggleDetailRow(data.id);
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
  color: #2185d0;
  cursor: pointer;
}
</style>
