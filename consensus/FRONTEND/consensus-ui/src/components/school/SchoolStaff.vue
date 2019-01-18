<template>
  <section>
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-4 col-sm-4 col-xs-4 ">
        <button class="btn btn-block btn-primary" @click="showNewStaffModal();">
          <i class="fa fa-plus"></i> Add a new Staff
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 justify-content-start">
        <div
          class="boxing"
          v-on:click="staffShown = !staffShown;"
          v-bind:class="{ active: staffShown }"
        >
          <i class="fa fa-users"></i>
          <h4>Staffs</h4>
          <div class="info">
            <div class="left">
              <h6>
                School staffs :
                {{ localData.results ? localData.results.length : 0 }}
              </h6>
            </div>
            <div class="right"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-no-padding" v-if="staffShown">
      <vuetable
        ref="vuetable"
        :api-mode="false"
        :data="localData"
        :api-url="tableUrl"
        :fields="tableFields"
        :css="css.table"
        class="staff-table"
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
    <b-modal
      size="lg"
      centered
      ref="newStaffModalRef"
      id="newStaffModal"
      title="Add a new staff"
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
                      v-model="newStaff.first_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Last Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="newStaff.last_name"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">User Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="newStaff.user_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Email</label>
                    <input
                      type="email"
                      class="form-control"
                      v-model="newStaff.email"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Phone Number</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="newStaff.phone_number"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Password</label>
                    <input
                      type="password"
                      class="form-control"
                      v-model="newStaff.password"
                    />
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
              v-on:click="submitStaff"
              type="button"
              class="btn btn-success btn-block"
            >
              <i class="glyphicon glyphicon-ok"></i> Add Staff
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              @click="$refs.newStaffModalRef.hide();"
            >
              <i class="fa fa-close"></i> Cancel
            </button>
          </div>
        </div>
      </div>
    </b-modal>

    <b-modal
      size="lg"
      centered
      ref="editStaffModalRef"
      id="editStaffModal"
      title="Edit staff"
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
                      v-model="editStaff.first_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Last Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="editStaff.last_name"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">User Name</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="editStaff.user_name"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Email</label>
                    <input
                      type="email"
                      class="form-control"
                      v-model="editStaff.email"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Phone Number</label>
                    <input
                      type="text"
                      class="form-control"
                      v-model="editStaff.phone_number"
                    />
                  </div>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6">
                  <div class="form-group">
                    <label class="pull-left">Password</label>
                    <input
                      type="password"
                      class="form-control"
                      v-model="editStaff.password"
                    />
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
              v-on:click="updateStaff"
              type="button"
              class="btn btn-success btn-block"
            >
              <i class="glyphicon glyphicon-ok"></i> Update Staff
            </button>
          </div>
          <div class="col-md-3 col-sm-3 col-xs-12">
            <button
              type="button"
              class="btn btn-danger btn-block"
              data-dismiss="modal"
              @click="$refs.editStaffModalRef.hide();"
            >
              <i class="fa fa-close"></i> Cancel
            </button>
          </div>
        </div>
      </div>
    </b-modal>

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
          @click="deleteStaff();"
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
import staffApi from "../../endpoint/StaffApi";
import Vuetable from "vuetable-2/src/components/Vuetable";
import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
import bModal from "bootstrap-vue/es/components/modal/modal";
import utilMixin from "@/mixins/UtilMixin";
import vuetableBootstrapMixin from "../../mixins/VuetableBootstrapMixin";

export default {
  name: "SchoolStaff",
  mixins: [utilMixin, vuetableBootstrapMixin],
  components: {
    Vuetable,
    VuetablePagination,
    "b-modal": bModal
  },
  props: {
    schoolId: {
      required: true
    }
  },
  created: function() {
    this.localData = staffApi.getAll(this.schoolId);
  },
  data: function() {
    return {
      staffs: {},
      newStaff: {},
      editStaff: {},
      staffShown: false,
      selectedStaffForDelete: null,
      deletingRecord: false,
      localData: {},
      tableUrl: "/api/v1/staff",
      tableFields: [
        {
          sortField: "first_name",
          name: "first_name",
          title: `<span class="icon is-small orange"><i class="fa fa-book color-gray"></i></span> First Name`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "last_name",
          title: `<span class="icon is-small orange"><i class="fa fa-users color-gray"></i></span> Last Name`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "email",
          title: `<span class="icon is-small orange"><i class="fa fa-calendar color-gray"></i></span> Email`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "phone_number",
          title: `<span class="icon is-small orange"><i class="fa fa-send color-gray"></i></span> Phone Number`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        {
          name: "user_name",
          title: `<span class="icon is-small orange"><i class="fa fa-calendar color-gray"></i></span> User Name`,
          titleClass: "text-left",
          dataClass: "text-left"
        },
        "__slot:actions"
      ]
    };
  },
  methods: {
    showNewStaffModal: function() {
      this.$refs.newStaffModalRef.show();
    },
    showConfirmDeleteModal: function(staff) {
      this.selectedStaffForDelete = staff;
      this.$refs.confirmDeleteModalRef.show();
    },
    deleteStaff: function() {
      let self = this;
      self.deletingRecord = true;

      staffApi.delete(self.selectedStaffForDelete).then(
        function() {
          self.$refs.vuetable.refresh();
          self.deletingRecord = false;
          self.$refs.confirmDeleteModalRef.hide();
          self.notifySuccess("The staff deleted");
        },
        function() {
          self.deletingRecord = false;
          self.notifyError(
            "Some error happened when trying to delete the staff"
          );
        }
      );
    },
    editRow: function(staff) {
      this.editStaff = staff;
      this.$refs.editStaffModalRef.show();
    },
    updateStaff: function() {
      let self = this;
      staffApi.put(self.editStaff).then(
        function() {
          self.notifySuccess("The staff updated");
          self.$refs.editStaffModalRef.hide();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to update the staff"
          );
        }
      );
    },
    submitStaff: function() {
      let self = this;
      staffApi.add(self.newStaff).then(
        function() {
          self.notifySuccess("The staff inserted");
          self.$refs.newStaffModalRef.hide();
        },
        function() {
          self.notifyError(
            "Some error happened when trying to add the new staff"
          );
        }
      );
    }
  }
};
</script>

<style>
.staff-table {
  margin-top: 15px;
  margin-left: 15px;
  margin-right: 15px;
}
</style>
