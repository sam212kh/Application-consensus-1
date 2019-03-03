<template>
  <div class="signUp">
    <div class="container">
      <div class="singup-form">
        <div class="row">
          <div class="col-md-6 col-sm-6 col-xs-6 offset-3">
            <div class="main-div">
              <div class="panel">
                <h2>Sign up your account</h2>
                <br />
              </div>
              <form id="Login" @submit.prevent="submit">
                <div class="row">
                  <div class="col-md-6 col-sm-6 col-xs-6">
                    <div class="form-group">
                      <label class="pull-left">First Name</label>
                      <input
                        type="text"
                        class="form-control"
                        v-model="registerFields.first_name"
                        placeholder="put your first name"
                      />
                    </div>
                  </div>
                  <div class="col-md-6 col-sm-6 col-xs-6">
                    <div class="form-group">
                      <label class="pull-left">Last Name</label>
                      <input
                        type="text"
                        class="form-control"
                        v-model="registerFields.last_name"
                        placeholder="put your last name"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12 col-sm-12 col-xs-12">
                    <div class="form-group">
                      <label class="pull-left">User Name</label>
                      <input
                        type="text"
                        class="form-control"
                        v-model="registerFields.username"
                        placeholder="pick a username"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12 col-sm-12 col-xs-12">
                    <div class="form-group">
                      <label class="pull-left">Email</label>
                      <input
                        type="email"
                        class="form-control"
                        v-model="registerFields.email"
                        placeholder="yourmail@example.com"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-6 col-sm-6 col-xs-6">
                    <div class="form-group">
                      <label class="pull-left">Country</label>
                      <select
                        class="form-control select"
                        v-model="registerFields.country"
                      >
                        <option>USA</option>
                        <option>UK</option>
                      </select>
                    </div>
                  </div>
                  <div class="col-md-6 col-sm-6 col-xs-6">
                    <div class="form-group">
                      <label class="pull-left">City</label>
                      <select
                        class="form-control select"
                        v-model="registerFields.city"
                      >
                        <option>California</option>
                        <option>Colorado</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12 col-sm-12 col-xs-12">
                    <div class="form-group">
                      <label class="pull-left">Phone Number</label>
                      <input
                        type="text"
                        class="form-control"
                        v-model="registerFields.phone_number"
                        placeholder="Write down your phone number"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12 col-sm-12 col-xs-12">
                    <div class="form-group">
                      <label class="pull-left">Password</label>
                      <input
                        type="password"
                        class="form-control"
                        v-model="registerFields.password"
                        placeholder="Create a password"
                      />
                      <p class="text-left color-gray">
                        Make sure it's at least 7 characters, including a
                        number, and a lowercase letter.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12 col-sm-12 col-xs-12">
                    <div class="form-group">
                      <div
                        id="recaptcha"
                        class="g-recaptcha"
                        data-sitekey="6Lcz5mwUAAAAAApZlebKWHYLt_Gx3w6CkPfBGPyq"
                      ></div>
                    </div>
                  </div>
                </div>
                <button type="submit" class="btn btn-block btn-success">
                  Sign up
                </button>
                <hr />
                <div class="panel">
                  <h2 class="margin-top-20">or sign up with Google account</h2>
                </div>
                <button type="submit" class="btn btn-block btn-primary">
                  <i class="fa fa-google-plus"></i>
                  Sign up with google
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SessionApi from "@/endpoint/SessionApi";
import UtilMixin from "@/mixins/UtilMixin";

export default {
  name: "SignUp",
  mixins: [UtilMixin],
  created: function() {
    this.addReCaptchaScriptTag();
  },
  data: function() {
    return {
      registerFields: {}
    };
  },
  methods: {
    submit: function() {
      if (
        this.registerFields.username === "" ||
        this.registerFields.password === ""
      ) {
        this.notifyError("please fill all required fields");
        return;
      }

      let self = this;
      SessionApi.signUp(this.registerFields).then(
        function() {
          self.$router.push("/");
        },
        function(error) {
          self.notifyDefaultServerError(error);
        }
      );
    },
    addReCaptchaScriptTag: function() {
      let recaptcha = document.createElement("script");
      recaptcha.setAttribute("src", "https://www.google.com/recaptcha/api.js");
      document.head.appendChild(recaptcha);
    }
  }
};
</script>

<style scoped>
.signUp {
  background: -webkit-linear-gradient(left, #3931af, #00c6ff);
}

.panel h2 {
  color: #444444;
  font-size: 18px;
  margin: 0 0 8px 0;
}

.panel p {
  color: #777777;
  font-size: 14px;
  margin-bottom: 30px;
  line-height: 24px;
}

.login-form .form-control {
  background: #f7f7f7 none repeat scroll 0 0;
  border: 1px solid #d4d4d4;
  border-radius: 4px;
  font-size: 14px;
  height: 50px;
  line-height: 50px;
}

.login-form .form-control.select {
  height: 45px !important;
}

.main-div {
  background: #ffffff none repeat scroll 0 0;
  border-radius: 12px;
  margin: 10px auto 30px;
  padding: 20px 50px 20px 50px;
}

.login-form .form-group {
  margin-bottom: 10px;
}

.login-form {
  text-align: center;
}

.forgot a {
  color: #777777;
  font-size: 14px;
  text-decoration: underline;
}

.forgot {
  text-align: left;
  margin-bottom: 15px;
}

.singup span {
  color: #777777;
  font-size: 14px;
}

.singup a {
  margin-left: 10px;
}

.botto-text {
  color: #ffffff;
  font-size: 14px;
  margin: auto;
}

.back {
  text-align: left;
  margin-top: 10px;
}

.back a {
  color: #444444;
  font-size: 13px;
  text-decoration: none;
}

.profile-img-card {
  width: 96px;
  height: 96px;
  margin: 0 auto 10px;
  display: block;
  -moz-border-radius: 50%;
  -webkit-border-radius: 50%;
  border-radius: 50%;
}

.margin-top-20 {
  margin-top: 20px !important;
}

.color-gray {
  color: gray;
}

@media (max-width: 768px) {
  .main-div {
    padding: 20px;
  }
}
</style>
