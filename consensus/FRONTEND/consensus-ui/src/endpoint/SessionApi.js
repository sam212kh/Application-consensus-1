import Api from "@/endpoint/Api";

export default {
  getUser() {
    return Api.get("session");
  },
  login(username, password) {
    return Api.post("session", { username: username, password: password });
  },
  logout() {
    return Api.delete("session");
  }
};
