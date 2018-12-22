<template>
  <section class="container">
    <div class="row row-no-padding justify-content-end">
      <div class="col-3">
        <button class="btn btn-block btn-info" v-on:click="goToAddSchool">
          <i class="fa fa-plus"></i> Add a new School
        </button>
      </div>
      <div class="col-3">
        <button class="btn btn-block btn-primary" v-on:click="goToAddSeason">
          <i class="fa fa-plus"></i> Add a new Season
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
          :row-class="onRowClass"
          class="school-table"
          detail-row-component="school-seasons"
          @vuetable:row-clicked="onRowClicked"
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
    <b-modal
      size="lg"
      centered
      ref="newSeasonModalRef"
      id="newSeasonModal"
      title="Add a new season"
      :header-bg-variant="'modal-header padding-10 background-light-silver'"
      :footer-bg-variant="
        'modal-footer padding-10 background-light-silver border-bottom-right-radius-10 border-bottom-left-radius-10'
      "
      :aria-required="false"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-body">
            <form>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Season Name</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="pick a name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Season Kind</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="pick a name"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Start Date</label>
                    <input
                      class="form-control"
                      data-date-format="dd/mm/yyyy"
                      id="startDate"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">End Date</label>
                    <input
                      class="form-control"
                      data-date-format="dd/mm/yyyy"
                      id="endDate"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >Application acceptance Start Date</label
                    >
                    <input
                      class="form-control"
                      data-date-format="dd/mm/yyyy"
                      id="appStartDate"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >Application acceptance End Date</label
                    >
                    <input
                      class="form-control"
                      data-date-format="dd/mm/yyyy"
                      id="appEndDate"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >School (amonge of registered schools)</label
                    >
                    <select class="form-control select">
                      <option>School num1</option>
                      <option>School num2</option>
                      <option>School num3</option>
                      <option>School num4</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">max size (1-200)</label>
                    <select class="form-control select">
                      <option>20</option>
                      <option>30</option>
                      <option>150</option>
                      <option>250</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-12 col-sm-12 col-xs-12">
                  <div class="form-group">
                    <label class="pull-left">More Info</label>
                    <input type="text" class="form-control" />
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div slot="modal-footer" class="w-100">
        <div class="row row-no-padding width-full">
          <div class="col-md-4 col-sm-4 col-xs-12">
            <button type="button" class="btn btn-success btn-block">
              <i class="glyphicon glyphicon-ok"></i> Submit Season
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
            >
              <i class="fa fa-close"></i> Cancel
            </button>
          </div>
        </div>
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
import schoolApi from "@/endpoint/SchoolApi";

export default {
  name: "SchoolHome",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination,
    "b-modal": bModal
  },
  created: function() {
    this.$eventsBus.$emit("header:title", "Schools");
    this.localData = schoolApi.getAll();
  },
  data: function() {
    return {
      selectedId: -1,
      localData: {},
      tableUrl: "/api/v1/school",
      tableFields: [
        {
          sortField: "full_name",
          name: "full_name",
          title: `<span class="icon is-small orange"><i class="fa fa-book color-gray"></i></span> Full Name`,
          titleClass: "text-left",
          dataClass: "text-left"
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
      schoolApi.delete(self.selectedSchoolForDelete).then(
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
    onRowClicked: function(data) {
      this.selectedId = data.id;
      this.$refs.vuetable.toggleDetailRow(data.id);
    },
    onRowClass: function(dataItem) {
      if (this.selectedId !== dataItem.id) {
        return "clickable";
      }
      return "bg-info text-light clickable";
    },
    goToAddSeason: function() {
      this.$refs.newSeasonModalRef.show();
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
