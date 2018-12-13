<template>
  <section class="container-fluid">
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-3 col-sm-3 col-xs-3 ">
        <button class="btn btn-block btn-primary" @click="showNewStaffModal();">
          <i class="fa fa-plus"></i> Add a new Staff
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 justify-content-start">
        <div class="boxing">
          <i class="fa fa-users"></i>
          <h4>Staffs</h4>
          <div class="info">
            <div class="left">
              <h6>School staffs : {{ school.total_staff_count }}</h6>
            </div>
            <div class="right"></div>
          </div>
        </div>
      </div>
    </div>
    <b-modal
      size="lg"
      centered
      ref="newStaffModalRef"
      id="newStaffModal"
      :hide-header="true"
      :hide-footer="true"
      :aria-required="false"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header padding-10 background-light-silver">
              <h6 class="modal-title" id="exampleModalLabel">
                Add a new staff in season 1
              </h6>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
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
                    <label for="inlineFormInputGroup">
                      Or search and add by username</label
                    >
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
                    <label for="inlineFormInputGroup">
                      Or search and add by email</label
                    >
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
            <div
              class="modal-footer padding-10 background-light-silver border-bottom-right-radius-10 border-bottom-left-radius-10"
            >
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
                  >
                    <i class="fa fa-close"></i> Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </b-modal>
  </section>
</template>

<script>
import SchoolApi from "../../endpoint/SchoolApi";
import bModal from "bootstrap-vue/es/components/modal/modal";

export default {
  name: "SchoolStaff",
  mixins: [],
  components: {
    "b-modal": bModal
  },
  props: {
    schoolId: {
      type: Number,
      required: true
    }
  },
  created: function() {
    let self = this;
    SchoolApi.get(this.schoolId).then(
      function(response) {
        self.school = response.data;
      },
      function(error) {
        self.notifyDefaultServerError(error);
        // Lets back if the current school could not be retrieved
        self.$router.back();
      }
    );
  },
  data: function() {
    return {
      school: {}
    };
  },
  methods: {
    showNewStaffModal: function() {
      this.$refs.newStaffModalRef.show();
    }
  }
};
</script>

<style></style>
