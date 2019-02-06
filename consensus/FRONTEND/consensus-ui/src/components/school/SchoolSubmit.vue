<template>
  <section class="container">
    <div class="row row-no-padding">
      <div class="col-md-10 col-sm-10 col-xs-12 offset-1">
        <div class="main-div">
          <h6 class="modal-title">Register a New School</h6>
          <hr />
          <form @submit.prevent="submitSchool">
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">School Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="pic a name"
                    v-model="school.full_name"
                  />
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">Grade</label>
                  <select class="form-control select" v-model="school.grade">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">School Phone Number</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="put your school phone number"
                    v-model="school.phone_number"
                  />
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">School Email</label>
                  <input
                    type="email"
                    class="form-control"
                    placeholder="put your school email"
                    v-model="school.email"
                  />
                </div>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">Country</label>
                  <select class="form-control select" v-model="school.country">
                    <option>US</option>
                    <option>United kingdom</option>
                    <option>Canada</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">State</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="school.state"
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">City</label>
                  <select class="form-control select" v-model="school.city">
                    <option>Seattle</option>
                    <option>Boston</option>
                    <option>Austin</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">Zipcode</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="school.zip_code"
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="form-group">
                  <label class="pull-left">Address</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="write down your school address"
                    v-model="school.address"
                  />
                </div>
              </div>
            </div>
            <hr />
            <div class="row row-no-padding width-full">
              <div class="col-md-4 col-sm-4 col-xs-12">
                <button
                  type="Submit"
                  class="btn btn-success btn-block"
                  >
                  <i class="glyphicon glyphicon-ok"></i> Submit School
                </button>
              </div>
              <div class="col-md-3 col-sm-3 col-xs-12">
                <router-link
                  class="btn btn-block btn-danger"
                  :to="{ name: 'schools' }"
                >
                  <i class="fa fa-close"></i> Cancel
                </router-link>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import UtilMixin from "@/mixins/UtilMixin";
import SchoolApi from "../../endpoint/SchoolApi";
import SessionApi from "@/endpoint/SessionApi";

export default {
  name: "SubmitSchool",
  mixins: [UtilMixin],
  components: {},
  data: function() {
    return {
      school: {}
    };
  },
  created: function() {
    this.$eventsBus.$emit("header:title", "Add school");
    if (this.$route.params.id) {
      this.$eventsBus.$emit("header:title", "Edit school");
      // Retrieve current school when the school's id passed
      let self = this;
      SchoolApi.get(this.$route.params.id).then(
        function(response) {
          self.school = response.data;
        },
        function(error) {
          self.notifyDefaultServerError(error);
          // Lets back if the current school could not be retrieved
          self.$router.back();
        }
      );
    }
  },
  destroyed: function() {},
  methods: {
    submitSchool: function() {
      // If current school should be edit
      let request;
      if (this.school.id && this.school.id > 0) {
        request = SchoolApi.put(this.school);
      } else {
        request = SchoolApi.add(this.school);
      }

      // Use the same actions for both(add/edit) responses
      let self = this;
      request.then(
        function() {
          self.notifyDefaultServerSuccess({});
          self.$router.back();
        },
        function(error) {
          self.notifyDefaultServerError(error);
        }
      );
    }
  }
};
</script>
