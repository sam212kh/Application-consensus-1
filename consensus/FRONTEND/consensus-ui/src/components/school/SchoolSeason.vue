<template>
  <section class="container-fluid">
    <div class="row row-no-padding justify-content-end">
      <div class="col-md-3 col-sm-3 col-xs-3">
        <button
          class="btn btn-block btn-success"
          @click="showNewSeasonModal();"
        >
          <i class="glyphicon glyphicon-ok"></i> Submit a new application
        </button>
      </div>
    </div>
    <div class="row row-no-padding">
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="boxing">
          <i class="fa fa-eye"></i>
          <h5>Applications Review</h5>
          <br />
          <div class="info">
            <div class="left">
              <h6>Received : {{ season.application || 0 }}</h6>
              <h6>Scored : {{ season.scored || 0 }}</h6>
            </div>
            <div class="right">{{ season.new_application || 0 }} new</div>
          </div>
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="boxing">
          <i class="fa fa-handshake-o"></i>
          <h4>enrolled</h4>
          <div class="info">
            <div class="left">
              <h6>Student enrolled : {{ season.enrolled }}</h6>
            </div>
            <div class="right">{{ season.new_enrolled || 0 }} new</div>
          </div>
        </div>
      </div>
    </div>
    <b-modal
      size="lg"
      centered
      ref="newSeasonModalRef"
      id="newSeasonModal"
      :hide-header="true"
      :hide-footer="true"
      :aria-required="false"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header padding-10 background-light-silver">
              <h6 class="modal-title" id="exampleModalLabel">
                Register a new Season
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
            <div
              class="modal-footer padding-10 background-light-silver border-bottom-right-radius-10 border-bottom-left-radius-10"
            >
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
          </div>
        </div>
      </div>
    </b-modal>
  </section>
</template>

<script>
import SeasonApi from "../../endpoint/SeasonApi";
import bModal from "bootstrap-vue/es/components/modal/modal";

export default {
  name: "SchoolSeason",
  mixins: [],
  components: {
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
    let self = this;
    SeasonApi.get(this.seasonId).then(
      function(response) {
        self.season = response.data;
      },
      function(error) {
        self.notifyDefaultServerError(error);
        // Lets back if the current season could not be retrieved
        self.$router.back();
      }
    );
  },
  data: function() {
    return {
      season: {}
    };
  },
  methods: {
    showNewSeasonModal: function() {
      this.$refs.newSeasonModalRef.show();
    }
  }
};
</script>

<style></style>
