<template>
  <section class="container">
    <div class="row row-no-padding">
      <div class="col-md-10 col-sm-10 col-xs-12 offset-1">
        <div class="main-div">
          <h6 class="modal-title">Register a New School</h6>
          <hr />
          <form>
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
                  <select class="form-control select">
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
                  />
                </div>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">Country</label>
                  <select class="form-control select">
                    <option>US</option>
                    <option>United kingdom</option>
                    <option>Canada</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">State</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">City</label>
                  <select class="form-control select">
                    <option>Seattle</option>
                    <option>Boston</option>
                    <option>Austin</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6 col-sm-6 col-xs-6">
                <div class="form-group">
                  <label class="pull-left">Zipcode</label>
                  <select class="form-control select">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                  </select>
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
                  />
                </div>
              </div>
            </div>
            <hr />
            <div class="row row-no-padding width-full">
              <div class="col-md-4 col-sm-4 col-xs-12">
                <button
                  type="button"
                  class="btn btn-success btn-block"
                  v-on:click="addSchool"
                >
                  <i class="glyphicon glyphicon-ok"></i> Submit School
                </button>
              </div>
              <div class="col-md-3 col-sm-3 col-xs-12">
                <button
                  type="button"
                  class="btn btn-danger btn-block"
                  data-dismiss="modal"
                  v-on:click="cancel"
                >
                  <i class="fa fa-close"></i> Cancel
                </button>
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

export default {
  name: "AddSchool",
  mixins: [UtilMixin],
  components: {},
  created: function() {},
  data: function() {
    return {
      school: {}
    };
  },
  methods: {
    addSchool: function() {
      let self = this;
      SchoolApi.add(this.school).then(
        function() {
          self.$router.back();
        },
        function(error) {
          self.notifyDefaultServerError(error);
        }
      );
    },
    cancel: function() {
      this.$router.back();
    }
  }
};
</script>
