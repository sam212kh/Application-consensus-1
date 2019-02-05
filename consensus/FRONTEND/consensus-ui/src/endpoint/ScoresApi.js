import Api from "@/endpoint/Api";

export default {
  getByApplicationId(applicationId) {
    return Api.get(`application/${applicationId}/score`);
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
