import Api from "@/endpoint/Api";

export default {
  getUser() {
    return Api.get("session");
  },
  login(username, password) {
    return Api.put("session", { username: username, password: password });
  },
  signUp(fields) {
    return Api.post("session", fields);
  },
  logout() {
    return Api.delete("session");
  }
};
