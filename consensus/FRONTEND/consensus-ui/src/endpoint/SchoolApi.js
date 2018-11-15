import Api from "@/endpoint/Api";

export default {
  getAll() {
    return Api.get("school");
  },
  add(school) {
    return Api.post("school", school);
  },
  delete(school) {
    return Api.delete("school/" + school.id);
  }
};
