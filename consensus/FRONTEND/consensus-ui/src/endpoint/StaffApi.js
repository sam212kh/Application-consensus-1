import Api from "@/endpoint/Api";
import SessionApi from "@/endpoint/SessionApi";


export default {
  getAll(schoolId) {
    return Api.get("staff?id=" + schoolId);
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
