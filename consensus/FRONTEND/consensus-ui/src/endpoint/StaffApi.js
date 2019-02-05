import Api from "@/endpoint/Api";

export default {
  getBySchoolId(schoolId) {
    return Api.get(`school/${schoolId}/staff`);
  },
  add(schoolId, staff) {
    return Api.post(`school/${schoolId}/staff`, staff);
  },
  put(schoolId, staff) {
    return Api.put(`school/${schoolId}/staff/${staff.id}`, staff);
  },
  delete(schoolId, staff) {
    return Api.delete(`school/${schoolId}/staff/${staff.id}`);
  }
};
