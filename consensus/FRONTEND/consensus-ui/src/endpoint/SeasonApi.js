export default {
  mockSeason: {
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
      full_name: "season_11",
      application: 7,
      scored: 4,
      enrolled: 2
    },
    {
      id: 12,
      school_id: 12,
      full_name: "season_12",
      application: 9,
      scored: 2,
      enrolled: 6
    },
    {
      id: 31,
      school_id: 13,
      full_name: "season_13",
      application: 6,
      scored: 1,
      enrolled: 3
    }
    ]
  },
  getAll() {
    return this.mockSeason;
  },
  get(seasonId) {
    for (let i = 0; i < this.mockSeason.results.length; i++) {
      if (this.mockSeason.results[i].id === +seasonId) {
        return Promise.resolve({
          status: 200,
          data: this.mockSeason.results[i]
        });
      }
    }
    return Promise.resolve({
      status: 200,
      data: this.mockSeason.results[0]
    });
  },
  add(schoolId, season) {
    season.id = Math.floor(Math.random() * 10000 + 1);
    season.school_id = schoolId;
    this.mockSeason.results.push(season);
    return Promise.resolve({ status: 200, data: season });
  },
  put(season) {
    return this.get(season.id).then(function(persistedSeason) {
      Object.assign(persistedSeason, season);
      return Promise.resolve({ status: 200 });
    });
  },
  delete(season) {
    let self = this;
    return this.get(season.id).then(function(persistedSeason) {
      self.mockSeason.results.splice(self.mockSeason.indexOf(persistedSeason), 1);
      return Promise.resolve({ status: 200 });
    });
  }
};
