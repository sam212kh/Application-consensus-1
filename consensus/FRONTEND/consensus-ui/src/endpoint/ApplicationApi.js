import Api from "@/endpoint/Api";

export default {
  getBySeasonId(seasonId) {
    return Api.get("application?season_id=" + seasonId);
  },
  add(application) {
    return Api.post("application", application);
  },
  put(application) {
    return Api.put("application/" + application.id, application);
  },
  delete(application) {
    return Api.delete("application/" + application.id);
  }
};
