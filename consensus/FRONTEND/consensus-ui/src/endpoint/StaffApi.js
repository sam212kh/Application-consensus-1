export default {
  mockStaff: {
    pagination: {
      next_url: null,
      previous_url: null,
      current_page: 1,
      next_page: null,
      previous_page: null,
      first_page: 1,
      last_page: 1,
      page_size: 10,
      total: 1
    },
    results: [
      {
        id: 12,
        school_id: 12,
        first_name: "staff 1",
        last_name: "one",
        email: "staff1@gmail.com",
        phone_number: "09121111111",
        user_name: "staff_1"
      },
      {
        id: 13,
        school_id: 12,
        first_name: "staff 2",
        last_name: "two",
        email: "staff2@gmail.com",
        phone_number: "09122222222",
        user_name: "staff_2"
      },
      {
        id: 14,
        school_id: 13,
        first_name: "staff 3",
        last_name: "three",
        email: "staff3@gmail.com",
        phone_number: "09133333333",
        user_name: "staff_3"
      }
    ]
  },
  getAll() {
    return this.mockStaff;
    // return Api.get("staff", schoolId);
  },
  get(id) {
    for (let i = 0; i < this.mockStaff.results.length; i++) {
      if (this.mockStaff.results[i].id === +id) {
        return Promise.resolve({
          status: 200,
          data: this.mockStaff.results[i]
        });
      }
    }
    // return Api.get("staff/" + schoolshowConfirmDeleteModalshowConfirmDeleteModalshowConfirmDeleteModalshowConfirmDeleteModalId);
  },
  add(staff) {
    staff.id = Math.random() * 10000 + 1;
    this.mockStaff.results.push(staff);
    return Promise.resolve({ status: 200 });
    // return Api.post("staff", staff);
  },
  put(staff) {
    Object.assign(this.get(staff.id), staff);
    return Promise.resolve({ status: 200 });
    // return Api.put("staff/" + staff.id, staff);
  },
  delete(staff) {
    let persistedStaff = this.get(staff.id);
    var indexof = -1;
    for (let i = 0; i < this.mockStaff.results.length; i++) {
      if (this.mockStaff.results[i].id === staff.id) {
          indexof = i;
      }
    }
    this.mockStaff.results.splice(indexof,1);
    return Promise.resolve({ status: 200 });
    // return Api.delete("staff/" + staff.id);
  }
};
