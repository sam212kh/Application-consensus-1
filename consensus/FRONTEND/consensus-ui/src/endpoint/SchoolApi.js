import Api from "@/endpoint/Api";

export default {
  getAll() {
    return Api.get("school");
  }
};
