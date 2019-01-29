import Api from "@/endpoint/Api";

export default {
  getAll(schoolId) {
    return Api.get("staff/"+schoolId);
  },
  add(schoolId,staff) {
    staff.school_id = schoolId;
    return Api.post("staff", staff);
  },
  put(staff) {
    return Api.put("staff/" + staff.id, staff);
  },
  delete(staff) {
    return Api.delete("staff/" + staff.id);
  }
};
