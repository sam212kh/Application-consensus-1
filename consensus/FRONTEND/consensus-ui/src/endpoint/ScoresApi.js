export default {
  mockScore: {
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
        application_id: 17,
        staff_id: 12,
        first_name: "staff",
        last_name: "12",
        score_date: "2018-12-24",
        score: 4,
      },
      {
        id: 18,
        school_id: 12,
        application_id: 14,
        staff_id: 12,
        first_name: "staff",
        last_name: "11",
        score_date: "2018-12-22",
        score: 4,
      },
      {
        id: 18,
        school_id: 11,
        application_id: 17,
        staff_id: 12,
        first_name: "staff",
        last_name: "12",
        score_date: "2018-12-24",
        score: 4,
      },
      {
        id: 15,
        school_id: 12,
        application_id: 13,
        staff_id: 13,
        first_name: "staff",
        last_name: "13",
        score_date: "2018-12-20",
        score: 2,
      },
    ]
  },
  getAll() {
    return this.mockScore;
  },
  get(ScoreId) {
    for (let i = 0; i < this.mockScore.results.length; i++) {
      if (this.mockScore.results[i].id === +schoolId) {
        return Promise.resolve({
          status: 200,
          data: this.mockScore.results[i]
        });
      }
    }
    return Promise.resolve({
      status: 200,
      data: this.mockScore.results[0]
    });
  },
  add(score) {
    application.id = Math.floor(Math.random() * 10000 + 1);
    this.mockScore.results.push(score);
    return Promise.resolve({ status: 200 });
  },
  put(score) {
    return this.get(score.id).then(function(persistedScore) {
      Object.assign(persistedScore.data, application);
      return Promise.resolve({ status: 200 });
    });
  },
  delete(score) {
    let self = this;
    return this.get(score.id).then(function(persistedScore) {
      self.mockScore.results.splice(
        self.mockScore.results.indexOf(persistedScore.data),
        1
      );
      return Promise.resolve({ status: 200 });
    });
  }
};
