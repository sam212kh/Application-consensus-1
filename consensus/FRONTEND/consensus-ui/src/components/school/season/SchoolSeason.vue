<template>
  <section>
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-4 col-sm-4 col-xs-4 ">
        <button class="btn btn-block btn-primary" v-on:click="addSeason">
          <i class="fa fa-plus"></i> Add a new Season
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 justify-content-start">
        <div
          class="boxing"
          v-on:click="seasonShown = !seasonShown"
          v-bind:class="{ active: seasonShown }"
        >
          <i class="fa fa-eye"></i>
          <h4>Season</h4>
          <div class="info">
            <div class="left">
              <h6>
                School Season :
                {{ seasonData.results ? seasonData.results.length : 0 }}
              </h6>
            </div>
            <div class="right"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-no-padding" v-if="seasonShown">
      <vuetable
        ref="vuetable"
        :api-mode="false"
        :data="seasonData"
        :fields="tableFields"
        :css="css.table"
        class="school-table"
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
              @click="editRow(props.rowData)"
            >
              <span class="glyphicon glyphicon-pencil"></span></button
            >&nbsp;
            <button
              class="btn btn-danger btn-sm"
              @click="showConfirmDeleteModal(props.rowData)"
            >
              <span class="glyphicon glyphicon-trash"></span></button
            >&nbsp;
            <router-link
              class="btn btn-info btn-sm"
              :to="{
                name: 'season.home',
                params: { school_id: schoolId, season_id: props.rowData.id }
              }"
            >
              <span class="fa fa-eye"></span>
            </router-link>
          </div>
        </template>
      </vuetable>
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
          @click="$refs.confirmDeleteModalRef.hide()"
        >
          <i class="la la-close"></i> Cancel
        </button>
        <button
          type="button"
          class="btn btn-danger float-right"
          :disabled="deletingRecord"
          @click="deleteSeason()"
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
                      v-model="selectedSeason.full_name"
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
                      v-model="selectedSeason.kind"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Start Date</label>
                    <dateTime
                      v-model="selectedSeason.start_date"
                      :config="{ timepicker: false }"
                      comparator="date"
                    ></dateTime>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">End Date</label>
                    <dateTime
                      v-model="selectedSeason.end_date"
                      :config="{ timepicker: false }"
                      comparator="date"
                    ></dateTime>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >Application acceptance Start Date</label
                    >
                    <dateTime
                      v-model="selectedSeason.acceptance_start_date"
                    ></dateTime>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >Application acceptance End Date</label
                    >
                    <dateTime
                      v-model="selectedSeason.acceptance_end_date"
                    ></dateTime>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left"
                      >School (among of registered schools)</label
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
                    <label class="pull-left">max size (1-250)</label>
                    <select
                      class="form-control select"
                      v-model="selectedSeason.max_size"
                    >
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
                    <input
                      type="text"
                      class="form-control"
                      v-model="selectedSeason.more_info"
                    />
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
            <button
              type="button"
              class="btn btn-success btn-block"
              v-on:click="submitSeason"
            >
              <i class="glyphicon glyphicon-ok"></i> Submit Season
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              v-on:click="$refs.newSeasonModalRef.hide()"
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
import VuetableBootstrapMixin from "@/mixins/VuetableBootstrapMixin";
import bModal from "bootstrap-vue/es/components/modal/modal";
import seasonApi from "@/endpoint/SeasonApi";
import dateTime from "../../dateTimePicker/DateTimePicker";

export default {
  name: "SchoolSeason",
  mixins: [UtilMixin, VuetableBootstrapMixin],
  components: {
    Vuetable,
    dateTime,
    VuetablePagination,
    "b-modal": bModal
  },
  props: {
    schoolId: {
      required: true
    }
  },
  created: function() {
    this.$eventsBus.$emit("header:title", "School");
    let self = this;
    seasonApi.getBySchoolId(this.schoolId).then(function(response) {
      self.seasonData = response.data;
    });
  },
  data: function() {
    return {
      seasonData: {},
      tableFields: [
        {
          sortField: "Name",
          name: "full_name",
          title: `<span class="icon is-small orange"><i class="fa fa-book color-gray"></i></span> Name`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          sortField: "Application",
          name: "application",
          title: `<span class="icon is-small orange"><i class="fa fa-send color-gray"></i></span> Application`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "scored",
          title: `<span class="icon is-small orange"><i class="fa fa-handshake-o color-gray"></i></span> Scored`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "enrolled",
          title: `<span class="icon is-small orange"><i class="fa fa-handshake-o color-gray"></i></span> Enrolled`,
          titleClass: "text-left",
          dataClass: "text-left"
        },

        "__slot:actions"
      ],
      selectedSeason: {},
      deletingRecord: false,
      seasonShown: false
    };
  },
  methods: {
    showConfirmDeleteModal: function(season) {
      this.selectedSeason = season;
      this.$refs.confirmDeleteModalRef.show();
    },
    deleteSeason: function() {
      let self = this;
      self.deletingRecord = true;
      seasonApi.delete(this.schoolId, self.selectedSeason).then(
        function() {
          self.deletingRecord = false;
          self.$refs.confirmDeleteModalRef.hide();
          self.seasonData.results.splice(
            self.seasonData.results.indexOf(self.selectedSeason),
            1
          );
          self.$refs.vuetable.refresh();
          self.notifySuccess("The school deleted");
        },
        function() {
          self.deletingRecord = false;
          self.notifyError(
            "Some error happened when trying to delete the season"
          );
        }
      );
    },
    editRow: function(season) {
      this.selectedSeason = season;
      this.$refs.newSeasonModalRef.show();
    },
    addSeason: function() {
      this.selectedSeason = {};
      this.$refs.newSeasonModalRef.show();
    },
    submitSeason: function() {
      let self = this;
      if (!this.selectedSeason.id) {
        this.selectedSeason.school = this.schoolId;
        seasonApi.add(this.schoolId, this.selectedSeason).then(
          function(resp) {
            self.notifySuccess("The season inserted");
            self.$refs.newSeasonModalRef.hide();
            self.seasonData.results.push(resp.data);
          },
          function() {
            self.notifyError(
              "Some error happened when trying to add the new season"
            );
          }
        );
      } else {
        seasonApi.put(this.schoolId, this.selectedSeason).then(
          function() {
            self.notifySuccess("The season updated");
            self.$refs.newSeasonModalRef.hide();
          },
          function() {
            self.notifyError(
              "Some error happened when trying to update the new season"
            );
          }
        );
      }
    }
  }
};
</script>

<style>
.school-table {
  margin-top: 15px;
  margin-left: 15px;
  margin-right: 15px;
}
</style>
