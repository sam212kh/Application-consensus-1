export default {
  mockApplication: {
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
        id: 18,
        school_id: 12,
        first_name: "application_18",
        last_name: "11",
        date_of_birth: "2000-12-20",
        gender: "Male",
        email: "application_11@gmail.com",
        phone_number: "01818181818",
        info: "my info",
        educational_info: "my education",
        score: 4,
        created_date: "2018-12-24",
        status: "scored"
      },
      {
        id: 13,
        school_id: 12,
        first_name: "application_13",
        last_name: "13",
        date_of_birth: "2000-10-21",
        gender: "Male",
        email: "application_13@gmail.com",
        phone_number: "013131313131313",
        info: "my info",
        educational_info: "my education",
        score: 2,
        created_date: "2018-12-24",
        status: "scored"
      },
      {
        id: 15,
        school_id: 11,
        first_name: "application_15",
        last_name: "13",
        date_of_birth: "2000-10-21",
        gender: "Male",
        email: "application_15@gmail.com",
        phone_number: "0151515151515",
        info: "my info",
        educational_info: "my education",
        score: 5,
        created_date: "2018-12-22",
        status: "scored"
      },
      {
        id: 16,
        school_id: 11,
        first_name: "application_15",
        last_name: "13",
        date_of_birth: "2000-10-21",
        gender: "Male",
        email: "application_15@gmail.com",
        phone_number: "0151515151515",
        info: "my info",
        educational_info: "my education",
        score: 0,
        created_date: "2018-12-22",
        status: "pending"
      },
      {
        id: 17,
        school_id: 11,
        first_name: "application_17",
        last_name: "13",
        date_of_birth: "2000-10-22",
        gender: "Male",
        email: "application_17@gmail.com",
        phone_number: "0171717171717",
        info: "my info",
        educational_info: "my education",
        score: 5,
        created_date: "2018-12-24",
        status: "enrolled"
      }
    ]
  },
  getAll() {
    return this.mockApplication;
  },
  get(schoolId) {
    for (let i = 0; i < this.mockApplication.length; i++) {
      if (this.mockApplication[i].school_id === +schoolId) {
        return Promise.resolve({
          status: 200,
          data: this.mockApplication[i]
        });
      }
    }
    return Promise.resolve({
      status: 200,
      data: this.mockApplication[0]
    });
  },
  add(season) {
    season.id = Math.random() * 10000 + 1;
    this.mockApplication.push(season);
    return Promise.resolve({ status: 200 });
  },
  put(season) {
    Object.assign(this.get(season.id), season);
    return Promise.resolve({ status: 200 });
  },
  delete(season) {
    let persistedSeason = this.get(season.id);
    this.mockApplication.splice(
      this.mockApplication.indexOf(persistedSeason),
      1
    );
    return Promise.resolve({ status: 200 });
  }
};
