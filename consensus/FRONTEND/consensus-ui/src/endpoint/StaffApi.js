import Api from "@/endpoint/Api";

export default {
  getBySchoolId(schoolId) {
    return Api.get("staff?school_id=" + schoolId);
  },
  add(staff) {
    return Api.post("staff", staff);
  },
  put(staff) {
    return Api.put("staff/" + staff.id, staff);
  },
  delete(staff) {
    return Api.delete("staff/" + staff.id);
  }
};
