import Api from "@/endpoint/Api";

export default {
  getUser() {
    return Api.get("session");
  },
  login(username, password) {
    return Api.post("session", { username: username, password: password });
  },
  register(fields) {
    return Api.post("register/", fields);
  },
  logout() {
    return Api.delete("session");
  }
};
