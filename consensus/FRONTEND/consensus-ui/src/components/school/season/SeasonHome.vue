<template>
  <section class="container-fluid">
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-4 col-sm-4 col-xs-4">
        <button
          class="btn btn-block btn-success"
          @click="showNewApplicationModal()"
        >
          <i class="glyphicon glyphicon-ok"></i> Submit a new application
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div
          class="boxing"
          v-on:click="onApplicationBoxClick"
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
          v-on:click="onEnrolledBoxClick"
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

    <!-- Review Application -->
    <div class="row row-no-padding" v-if="applicationShown">
      <vuetable
        ref="vuetable"
        :api-mode="false"
        :data="reviewData"
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
              @click="reviewApplication(props.rowData)"
            >
              <span class="glyphicon glyphicon-pencil"></span></button
            >&nbsp;&nbsp;
          </div>
        </template>
        <template slot="decision_actions" scope="props">
          <div class="table-button-container">
            <button
              class="btn btn-success btn-sm"
              @click="acceptConfirmation(props.rowData)"
            >
              <span class="glyphicon glyphicon-check"></span></button
            >&nbsp;&nbsp;
            <button
              class="btn btn-outline-danger btn-sm"
              @click="rejectConfirmation(props.rowData)"
            >
              <span class="glyphicon glyphicon-trash"></span></button
            >&nbsp;&nbsp;
          </div>
        </template>
      </vuetable>
    </div>
    <!-- End Review Application -->

    <!-- Enrolled Application -->
    <div class="row row-no-padding" v-if="enrolledShown">
      <vuetable
        ref="vuetable"
        :api-mode="false"
        :data="enrolledData"
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
              @click="scoreBoxClick(props.rowData)"
            >
              <span class="fa fa-eye"></span></button
            >&nbsp;&nbsp;
          </div>
        </template>
      </vuetable>
    </div>
    <!-- End Enrolled Application -->

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
                    <input
                      type="text"
                      class="form-control"
                      v-model="newApp.first_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Last Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="newApp.last_name"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Birthday</label>
                    <input
                      type="date"
                      class="form-control"
                      v-model="newApp.date_of_birth"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Gender</label>
                    <select class="form-control" v-model="newApp.gender">
                      <option value="m">Male</option>
                      <option value="f">Female</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Email</label>
                    <input
                      type="email"
                      class="form-control"
                      v-model="newApp.email"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Phone Number</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="newApp.phone_number"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Info</label>
                    <textarea
                      class="form-control"
                      v-model="newApp.info"
                    ></textarea>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Educational Info</label>
                    <textarea
                      class="form-control"
                      v-model="newApp.educational_info"
                    ></textarea>
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
            <button
              v-on:click="submitApplication"
              type="button"
              class="btn btn-success btn-block"
            >
              <i class="glyphicon glyphicon-ok"></i> Add Application
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              @click="$refs.newApplicationModalRef.hide()"
            >
              <i class="fa fa-close"></i> Cancel
            </button>
          </div>
        </div>
      </div>
    </b-modal>

    <b-modal
      centered
      ref="confirmModalRef"
      id="confirmModal"
      :hide-header="true"
    >
      <p v-if="rejectConfirm" class="text-danger h6">
        Are you sure to reject this application?
      </p>
      <p v-if="acceptConfirm" class="text-danger h6">
        Are you sure to accept this application?
      </p>
      <div slot="modal-footer" class="w-100">
        <button
          type="button"
          class="btn btn-secondary float-left"
          @click="$refs.confirmModalRef.hide()"
        >
          <i class="la la-close"></i> Cancel
        </button>
        <button
          v-if="rejectConfirm"
          type="button"
          class="btn btn-danger float-right"
          @click="rejectApplication()"
        >
          <span v-show="rejectApplication">reject</span>
        </button>
        <button
          v-if="acceptConfirm"
          type="button"
          class="btn btn-success float-right"
          @click="acceptApplication()"
        >
          <span v-show="acceptApplication">Accept</span>
        </button>
      </div>
    </b-modal>

    <!-- review model -->
    <b-modal
      size="lg"
      centered
      ref="reviewAppModalRef"
      id="reviewAppModal"
      title="Review application"
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
                    <input
                      type="text"
                      class="form-control"
                      v-model="review.first_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Last Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="review.last_name"
                    />
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Phone number</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="review.phone_number"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Email</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="review.email"
                    />
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Birthday</label>
                    <input
                      type="date"
                      class="form-control"
                      v-model="review.date_of_birth"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Gender</label>
                    <select class="form-control" v-model="review.gender">
                      <option value="m">Male</option>
                      <option value="f">Female</option>
                    </select>
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Info</label>
                    <textarea
                      class="form-control"
                      v-model="newApp.info"
                    ></textarea>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Educational Info</label>
                    <textarea
                      class="form-control"
                      v-model="newApp.educational_info"
                    ></textarea>
                  </div>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-md-4 col-sm-4 col-xs-4">
                  <div class="form-group">
                    <label class="pull-left">Do score this Application</label>
                    <select class="form-control select" v-model="review.score">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6"></div>
              </div>
              <hr />
              <div class="row">
                <div class="col-md-12 col-sm-12 col-xs-12">
                  <div class="form-group">
                    <label class="pull-left">Comment</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="review.comment"
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
          <div v-if="!enrolledShown" class="col-md-4 col-sm-4 col-xs-12">
            <button
              v-on:click="updateReview"
              type="button"
              class="btn btn-success btn-block"
            >
              <i class="glyphicon glyphicon-ok"></i> Rate
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              @click="$refs.reviewAppModalRef.hide()"
            >
              <i class="fa fa-close"></i> Cancel
            </button>
          </div>
        </div>
      </div>
    </b-modal>
    <!-- end review model -->

    <!-- scores modal -->
    <b-modal centered ref="scoreModalRef" id="scoreModal" :hide-header="true">
      <!-- Scores -->
      <div class="row row-no-padding">
        <vuetable
          ref="vuetable"
          :api-mode="false"
          :data="scoreData"
          :fields="scoreTableFields"
          :css="css.table"
          class="application-table"
          :query-params="{
            sort: 'order_by',
            page: 'page',
            perPage: 'page_size'
          }"
          data-path="results"
          pagination-path="pagination"
        >
        </vuetable>
      </div>
      <!-- End Scores -->
    </b-modal>

    <!-- end scores modal -->
  </section>
</template>

<script>
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import bModal from "bootstrap-vue/es/components/modal/modal";
import utilMixin from "@/mixins/UtilMixin";
import vuetableBootstrapMixin from "../../../mixins/VuetableBootstrapMixin";
import applicationApi from "../../../endpoint/ApplicationApi";
import ApplicationStatus from "../model/ApplicationStatus";
import ScoresApi from "@/endpoint/ScoresApi";

let reviewActionField = {
  name: "__slot:review_actions",
  title: "review",
  titleClass: "text-left"
};
let decisionActionField = {
  name: "__slot:decision_actions",
  title: "decision",
  titleClass: "text-left"
};

export default {
  name: "SeasonHome",
  mixins: [utilMixin, vuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination,
    "b-modal": bModal
  },
  created: function() {
    this.$eventsBus.$emit("header:title", "School's season");
    this.schoolId = +this.$route.params.school_id;
    this.seasonId = +this.$route.params.season_id;
    this.reAssignData();
  },
  data: function() {
    return {
      schoolId: 0,
      seasonId: 0,
      season: {
        application: 0,
        applicationScored: 0,
        applicationEnrolled: 0,
        newEnrolled: 0,
        newApplication: 0
      },
      newApp: {},
      review: {},
      selectedApplication: {},
      selectedReview: null,
      selectedScore: null,
      applicationShown: false,
      enrolledShown: false,
      rejectConfirm: false,
      acceptConfirm: false,
      seasonData: {},
      scoreData: {},
      enrolledData: {},
      reviewData: {},
      reviewActionField: reviewActionField,
      decisionActionField: decisionActionField,
      scoreTableFields: [
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
          name: "score",
          title: "score",
          titleClass: "text-left",
          dataClass: "text-left"
        }
      ],
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
          name: "info",
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
        reviewActionField,
        decisionActionField
      ]
    };
  },
  methods: {
    showNewApplicationModal: function() {
      this.$refs.newApplicationModalRef.show();
    },
    reAssignData: function() {
      let self = this;
      self.reviewData = [];
      self.enrolledData = [];
      self.season.applicationScored = 0;
      self.season.applicationEnrolled = 0;
      self.season.newApplication = 0;
      self.season.newEnrolled = 0;
      applicationApi.getAll(this.seasonId).then(function(response) {
        self.seasonData = response.data;
        self.fragmentationApplication(response.data.results);
      });
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
          self.enrolledData.push(application);
        } else {
          self.reviewData.push(application);
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
    },
    onEnrolledBoxClick: function() {
      this.enrolledShown = !this.enrolledShown;
      this.applicationShown = false;
      this.decisionActionField.visible = !this.enrolledShown;
      this.$refs.vuetable && this.$refs.vuetable.normalizeFields();
    },
    scoreBoxClick: function() {
      this.scoreData = ScoresApi.getAll();
      this.$refs.scoreModalRef.show();
    },
    onApplicationBoxClick: function() {

      this.applicationShown = !this.applicationShown;
      this.enrolledShown = false;
      this.decisionActionField.visible = this.applicationShown;
      this.$refs.vuetable && this.$refs.vuetable.normalizeFields();
    },
    submitApplication: function() {
      let self = this;
      self.newApp.score = 0;
      self.newApp.status = "pending";
      self.newApp.created_date = new Date()
        .toJSON()
        .slice(0, 10)
        .replace(/-/g, "-");
      self.newApp.season =  self.seasonId;
      applicationApi.add(self.newApp).then(
        function() {
          self.notifySuccess("The application inserted");
          self.$refs.newApplicationModalRef.hide();
          self.reAssignData();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to add the new application"
          );
        }
      );
    },
    rejectConfirmation: function(application) {
      this.rejectConfirm = true;
      this.acceptConfirm = false;

      this.selectedApplication = application;
      this.$refs.confirmModalRef.show();
    },
    acceptConfirmation: function(application) {
      this.acceptConfirm = true;
      this.rejectConfirm = false;

      this.selectedApplication = application;
      this.$refs.confirmModalRef.show();
    },
    acceptApplication: function() {
      let self = this;
      this.selectedApplication.status = "enrolled";
      applicationApi.put(this.selectedApplication).then(
        function() {
          self.notifySuccess("The application accepted");
          self.$refs.confirmModalRef.hide();
          self.reAssignData();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to accepting the application"
          );
        }
      );
    },
    rejectApplication: function() {

      let self = this;
      this.selectedApplication.status = "reject";
      applicationApi.put(this.selectedApplication).then(
        function() {
          self.notifySuccess("The application rejected");
          self.$refs.confirmModalRef.hide();
          self.$refs.vuetable.refresh();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to rejecting the application"
          );
        }
      );
    },
    reviewApplication: function(application) {
      this.review = application;
      this.selectedReview = application;
      this.$refs.reviewAppModalRef.show();
    },
    updateReview: function() {
      let self = this;
      this.selectedReview.status = "scored";
      applicationApi.put(this.selectedReview).then(
        function() {
          self.notifySuccess("The application reviewed");
          self.$refs.reviewAppModalRef.hide();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to review the application"
          );
        }
      );
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
