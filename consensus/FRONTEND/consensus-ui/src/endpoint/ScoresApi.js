import Api from "@/endpoint/Api";

export default {
  getByApplicationId(applicationId) {
    return Api.get(`application/${applicationId}/score`);
  },
  add(applicationId, score) {
    return Api.post(`application/${applicationId}/score`, score);
  },
  put(applicationId, score) {
    return Api.put(`application/${applicationId}/score/` + score.id, score);
  },
  delete(applicationId, score) {
    return Api.delete(`application/${applicationId}/score/` + score.id);
  }
};
