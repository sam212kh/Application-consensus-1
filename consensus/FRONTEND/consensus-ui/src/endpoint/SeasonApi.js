import Api from "@/endpoint/Api";

export default {
  getBySchoolId(schoolId) {
    return Api.get("season?school_id=" + schoolId);
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
