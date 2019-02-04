import Api from "@/endpoint/Api";

export default {
  getBySchoolId(schoolId) {
    return Api.get(`school\\${schoolId}\\season`);
  },
  add(schoolId, season) {
    return Api.post(`school\\${schoolId}\\season`, season);
  },
  put(schoolId, season) {
    return Api.put(`school\\${schoolId}\\season\\${season.id}`, season);
  },
  delete(schoolId, season) {
    return Api.delete(`school\\${schoolId}\\season\\${season.id}`);
  }
};
