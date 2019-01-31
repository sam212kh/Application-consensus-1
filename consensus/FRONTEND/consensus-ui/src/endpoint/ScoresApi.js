import Api from "@/endpoint/Api";

export default {
  getAll(applicationId) {
    return Api.get("score/" + applicationId);
  },
  add(score) {
    return Api.post("score", score);
  },
  put(score) {
    return Api.put("score/" + score.id, score);
  },
  delete(score) {
    return Api.delete("score/" + score.id);
  }
};
