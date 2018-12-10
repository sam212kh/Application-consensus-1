<template>
  <section class="container-fluid">
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-3 col-sm-3 col-xs-3">
        <button class="btn btn-block btn-success">
          <i class="glyphicon glyphicon-ok"></i> Submit a new application
        </button>
      </div>
      <div class="col-md-3 col-sm-3 col-xs-3 ">
        <button class="btn btn-block btn-primary">
          <i class="fa fa-plus"></i> Add a new Staff
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="boxing">
          <i class="fa fa-eye"></i>
          <h4>Applications Review</h4>
          <br />
          <div class="info">
            <div class="left">
              <h6>Reviewed : 27</h6>
              <h6>Scored : 4</h6>
            </div>
            <div class="right">3 new</div>
          </div>
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="boxing">
          <i class="fa fa-users"></i>
          <h4>Staffs</h4>
          <div class="info">
            <div class="left"><h6>School staffs : 8</h6></div>
            <div class="right"></div>
          </div>
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="boxing">
          <i class="fa fa-handshake-o"></i>
          <h4>Inrolled</h4>
          <div class="info">
            <div class="left"><h6>Student inrolled : 4</h6></div>
            <div class="right">1 new</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "SchoolSeason",
  mixins: [],
  components: {},
  created: function() {},
  data: function() {
    return {};
  },
  methods: {}
};
</script>

<style></style>
