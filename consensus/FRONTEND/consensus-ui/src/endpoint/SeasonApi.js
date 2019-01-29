import Api from "@/endpoint/Api";

export default {
  getAll(schoolId) {
    return Api.get("season/"+schoolId);
  },
  add(season) {
    return Api.post("season", season);
  },
  put(season) {
    return Api.put("season/" + season.id, season);
  },
  delete(season) {
    return Api.delete("season/" + season.id);
  }
};
