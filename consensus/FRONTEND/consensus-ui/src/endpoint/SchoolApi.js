export default {
  mockSchool: {
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
        full_name: "school_31",
        total_season_count: 3,
        total_application_count: 15,
        total_staff_count: 8,
        total_score_count: 7,
        total_enrolled_count: 11,
        seasons: [
          {
            id: 18,
            full_name: "season_1",
            application: 2,
            staff: 3,
            score: 4,
            enrolled: 2
          },
          {
            id: 12,
            full_name: "season_2",
            application: 5,
            staff: 1,
            score: 2,
            enrolled: 6
          },
          {
            id: 31,
            full_name: "season_3",
            application: 8,
            staff: 4,
            score: 1,
            enrolled: 3
          }
        ]
      },
      {
        id: 13,
        full_name: "school_100",
        total_season_count: 1,
        total_application_count: 11,
        total_staff_count: 4,
        total_score_count: 17,
        total_enrolled_count: 10,
        seasons: [
          {
            id: 18,
            full_name: "season_11",
            application: 2,
            staff: 3,
            score: 4,
            enrolled: 2
          },
          {
            id: 12,
            full_name: "season_12",
            application: 5,
            staff: 1,
            score: 2,
            enrolled: 6
          },
          {
            id: 31,
            full_name: "season_13",
            application: 8,
            staff: 4,
            score: 1,
            enrolled: 3
          }
        ]
      }
    ]
  },
  getAll() {
    return this.mockSchool;
    // return Api.get("school");
  },
  get(id) {
    for (let i = 0; i < this.mockSchool.results.length; i++) {
      if (this.mockSchool.results[i].id === id) {
        return Promise.resolve({
          status: 200,
          data: this.mockSchool.results[i]
        });
      }
    }
    // return Api.get("school/" + id);
  },
  add(school) {
    school.id = Math.random() * 10000 + 1;
    this.mockSchool.results.push(school);
    return Promise.resolve({ status: 200 });
    // return Api.post("school", school);
  },
  put(school) {
    Object.assign(this.get(school.id), school);
    return Promise.resolve({ status: 200 });
    // return Api.put("school/" + school.id, school);
  },
  delete(school) {
    let persistedSchool = this.get(school.id);
    this.mockSchool.results.splice(
      this.mockSchool.results.indexOf(persistedSchool),
      1
    );
    return Promise.resolve({ status: 200 });
    // return Api.delete("school/" + school.id);
  }
};
