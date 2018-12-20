export default {
  mockSeason: [
    {
      id: 18,
      full_name: "season_11",
      application: 7,
      scored: 4,
      enrolled: 2,
      new_application: 1,
      new_enrolled: 2
    },
    {
      id: 12,
      full_name: "season_12",
      application: 9,
      scored: 2,
      enrolled: 6,
      new_application: 1,
      new_enrolled: 2
    },
    {
      id: 31,
      full_name: "season_13",
      application: 6,
      scored: 1,
      enrolled: 3,
      new_application: 1,
      new_enrolled: 2
    }
  ],
  getAll() {
    return this.mockSeason;
  },
  get(id) {
    for (let i = 0; i < this.mockSeason.length; i++) {
      if (this.mockSeason[i].id === +id) {
        return Promise.resolve({
          status: 200,
          data: this.mockSeason[i]
        });
      }
    }
     return Promise.resolve({
          status: 200,
          data: this.mockSeason[0]
        });
  },
  add(season) {
    season.id = Math.random() * 10000 + 1;
    this.mockSeason.push(season);
    return Promise.resolve({ status: 200 });
  },
  put(season) {
    Object.assign(this.get(season.id), season);
    return Promise.resolve({ status: 200 });
  },
  delete(season) {
    let persistedSeason = this.get(season.id);
    this.mockSeason.splice(this.mockSeason.indexOf(persistedSeason), 1);
    return Promise.resolve({ status: 200 });
  }
};
