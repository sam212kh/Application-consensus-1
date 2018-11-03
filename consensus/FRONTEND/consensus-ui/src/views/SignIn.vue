<template>
    <div class="signIn">
        <div class="container">
            <div class="login-form">
                <div class="row">
                    <div class="col-md-5 col-sm-5 col-xs-5 offset-3">
                        <div class="main-div">
                            <div class="panel">
                                <img id="profile-img" class="profile-img-card hidden-xs" src="images/avatar.png">
                                <h2>Sign in by your account</h2>
                            </div>
                            <form id="Login">
                                <div class="row">
                                    <div class="col-md-12 col-sm-12 col-xs-12">
                                        <div class="form-group">
                                            <input class="form-control" id="inputEmail" v-model="username"
                                                   placeholder="UserName or Email Address">
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-12 col-sm-12 col-xs-12">
                                        <div class="form-group">
                                            <input type="password" class="form-control" id="inputPassword"
                                                   v-model="password"
                                                   placeholder="Password">
                                        </div>
                                    </div>
                                </div>
                                <div class="forgot">
                                    <a href="reset.html">Forgot password?</a>
                                </div>
                                <button type="submit" class="btn btn-block btn-success" v-on:click="submit">
                                    Sign in
                                </button>
                                <hr/>
                                <div class="panel">
                                    <h2 class="margin-top-20">or sign in with Google account</h2>
                                </div>
                                <button type="submit" class="btn btn-block btn-primary">
                                    <i class="fa fa-google-plus"></i>
                                    Sign in with google
                                </button>
                                <hr/>
                                <div class="singup">
                                    <span>Not have an account?</span>
                                    <a href="SignUp.html">Create a new one</a>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>

    import SessionApi from "@/endpoint/SessionApi"

    export default {
        name: "SignIn",
        data: function () {
            return {
                username: '',
                password: ''
            }
        },
        methods:{
            submit: function(){
                if(this.username === '' || this.password === ''){
                    return;
                }

                let self =this;
                SessionApi.login(this.username, this.password).then(function(data){
                    self.$router.push('/');
                }, function(data){
                    console.log(data);
                });

            }
        }
    };
</script>

<style scoped>
    .signIn {
        background: -webkit-linear-gradient(left, #3931af, #00c6ff);
    }

    .form-heading {
        color: #fff;
        font-size: 23px;
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
