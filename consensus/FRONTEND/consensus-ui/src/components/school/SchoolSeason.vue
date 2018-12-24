<template>
  <section class="container-fluid">
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-4 col-sm-4 col-xs-4">
        <button
          class="btn btn-block btn-success"
          @click="showNewApplicationModal();"
        >
          <i class="glyphicon glyphicon-ok"></i> Submit a new application
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div
          class="boxing"
          v-on:click="
            applicationShown = !applicationShown;
            enrolledShown = false;
          "
          v-bind:class="{ active: applicationShown }"
        >
          <i class="fa fa-eye"></i>
          <h5>Applications Review</h5>
          <br />
          <div class="info">
            <div class="left">
              <h6>Received : {{ season.application }}</h6>
              <h6>Scored : {{ season.applicationScored }}</h6>
            </div>
            <div class="right">{{ season.newApplication }} new</div>
          </div>
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div
          class="boxing"
          v-on:click="
            enrolledShown = !enrolledShown;
            applicationShown = false;
          "
          v-bind:class="{ active: enrolledShown }"
        >
          <i class="fa fa-handshake-o"></i>
          <h4>enrolled</h4>
          <div class="info">
            <div class="left">
              <h6>Student enrolled : {{ season.applicationEnrolled }}</h6>
            </div>
            <div class="right">{{ season.newEnrolled }} new</div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-no-padding" v-if="applicationShown || enrolledShown">
      <vuetable
        ref="vuetable"
        :api-mode="false"
        :data="localData"
        :fields="tableFields"
        :css="css.table"
        class="application-table"
        :query-params="{
          sort: 'order_by',
          page: 'page',
          perPage: 'page_size'
        }"
        data-path="results"
        pagination-path="pagination"
        @vuetable:pagination-data="onPaginationData"
      >
        <template slot="review_actions" scope="props">
          <div class="table-button-container">
            <button
              class="btn btn-warning btn-sm"
              @click="reviewApplication(props.rowData);"
            >
              <span class="glyphicon glyphicon-pencil"></span> Review</button
            >&nbsp;&nbsp;
          </div>
        </template>
        <template slot="decision_actions" scope="props">
          <div class="table-button-container">
            <button
              class="btn btn-success btn-sm"
              @click="acceptApplication(props.rowData);"
            >
              <span class="glyphicon glyphicon-check"></span> Accept</button
            >&nbsp;&nbsp;
            <button
              class="btn btn-outline-success btn-sm"
              @click="rejectAppliction(props.rowData);"
            >
              <span class="glyphicon glyphicon-trash"></span> Reject</button
            >&nbsp;&nbsp;
          </div>
        </template>
      </vuetable>
    </div>
    <b-modal
      size="lg"
      centered
      ref="newApplicationModalRef"
      id="newAModal"
      title="Add a new application"
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
                    <label class="pull-left">First Name</label>
                    <input type="text" class="form-control" />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Last Name</label>
                    <input type="text" class="form-control" />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">User Name</label>
                    <input type="text" class="form-control" />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Email</label>
                    <input type="email" class="form-control" />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Phone Number</label>
                    <input type="text" class="form-control" />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Password</label>
                    <input type="email" class="form-control" />
                  </div>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <label> Or search and add by username</label>
                  <div class="input-group mb-2">
                    <div class="input-group-prepend">
                      <div class="input-group-text">
                        <i class="fa fa-search"></i>
                      </div>
                    </div>
                    <input type="text" class="form-control" />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <label> Or search and add by email</label>
                  <div class="input-group mb-2">
                    <div class="input-group-prepend">
                      <div class="input-group-text">
                        <i class="fa fa-search"></i>
                      </div>
                    </div>
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
              <i class="glyphicon glyphicon-ok"></i> Add Staff
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              @click="show = false;"
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
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import bModal from "bootstrap-vue/es/components/modal/modal";
import utilMixin from "@/mixins/UtilMixin";
import vuetableBootstrapMixin from "../../mixins/VuetableBootstrapMixin";
import applicationApi from "../../endpoint/ApplicationApi";
import ApplicationStatus from "./model/ApplicationStatus";

export default {
  name: "SchoolSeason",
  mixins: [utilMixin, vuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination,
    "b-modal": bModal
  },
  props: {
    schoolId: {
      type: Number,
      required: true
    },
    seasonId: {
      type: Number,
      required: true
    }
  },
  created: function() {
    this.localData = applicationApi.getAll(this.schoolId);

    this.fragmentationApplication(this.localData.results);
  },
  data: function() {
    return {
      season: {
        application: 0,
        applicationScored: 0,
        applicationEnrolled: 0,
        newEnrolled: 0,
        newApplication: 0
      },
      applicationShown: false,
      enrolledShown: false,
      selectedForDelete: null,
      deletingRecord: false,
      localData: {},
      tableFields: [
        {
          sortField: "first_name",
          name: "first_name",
          title: "First Name",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "last_name",
          title: "Last Name",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "date_of_birth",
          title: "Date of birth",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "gender",
          title: "Gender",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "email",
          title: "Email",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "phone_number",
          title: "Phone number",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "application_info",
          title: "Info",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "educational_info",
          title: "Educational Info",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "score",
          title: "Score",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "status",
          title: "Status",
          titleClass: "text-left",
          dataClass: "text-left"
        },
        "__slot:review_actions",
        "__slot:decision_actions"
      ]
    };
  },
  methods: {
    showNewApplicationModal: function() {
      this.$refs.newApplicationModalRef.show();
    },
    fragmentationApplication: function(applications) {
      let self = this;
      this.season.application = applications.length;
      self.season.applicationScored = self.season.applicationScored || 0;
      applications.forEach(function(application) {
        // Count scored applications
        if (application.score > 0) {
          self.season.applicationScored++;
        }

        // Count enrolled applications
        if (application.status === ApplicationStatus.Enrolled) {
          self.season.applicationEnrolled++;
        }

        // Count new(today) applications
        if (
          self.formatDate(application.created_date, "YYYY/MM/DD") ===
          self.formatDate(new Date(), "YYYY/MM/DD")
        ) {
          switch (application.status) {
            case ApplicationStatus.Enrolled:
              self.season.newEnrolled++;
              break;
            case ApplicationStatus.Scored:
            case ApplicationStatus.Pending:
              self.season.newApplication++;
              break;
          }
        }
      });
    }
  }
};
</script>

<style>
.application-table {
  margin-top: 15px;
  margin-left: 15px;
  margin-right: 15px;
}
</style>
