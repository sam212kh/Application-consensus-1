export default {
  mixins: [],
  data: function() {
    return {
      tablePerPage: 10,
      tableFiltering: {},
      pageSizeOptions: [5, 10, 15, 25, 50, 100, 200, 0],
      tableHTTPOptions: {},
      css: {
        table: {
          tableClass: "table table-striped table-bordered",
          ascendingIcon: "glyphicon glyphicon-chevron-up",
          descendingIcon: "glyphicon glyphicon-chevron-down",
          handleIcon: "glyphicon glyphicon-menu-hamburger"
        },
        pagination: {
          infoClass: "pull-left",
          wrapperClass: "vuetable-pagination pull-right",
          activeClass: "btn-primary",
          disabledClass: "disabled",
          pageClass: "btn btn-border",
          linkClass: "btn btn-border",
          icons: {
            first: "",
            prev: "",
            next: "",
            last: ""
          }
        }
      }
    };
  },
  watch: {
    tablePerPage: function() {
      this.$nextTick(function() {
        this.$refs.vuetable.refresh();
      });
    },
    tableFiltering: {
      handler: function() {
        this.$nextTick(function() {
          this.$refs.vuetable.refresh();
        });
      },
      deep: true
    }
  },
  methods: {
    getSortParam: function(sortOrder) {
      if (!sortOrder || sortOrder.field === "") {
        return "";
      }
      return sortOrder
        .map(function(sort) {
          return (
            (sort.direction === "desc" ? "" : "-") +
            (sort.sortField || sort.field)
          );
        })
        .join(",");
    },
    onPaginationData: function(paginationData) {
      paginationData.from =
        (paginationData.current_page - 1) * paginationData.page_size + 1;
      paginationData.to = Math.min(
        paginationData.current_page * paginationData.page_size,
        paginationData.total
      );
      if (this.$refs.pagination) {
        this.$refs.pagination.setPaginationData(paginationData);
      }
      if (this.$refs.paginationInfo) {
        this.$refs.paginationInfo.setPaginationData(paginationData);
      }
    },
    onChangePage: function(page) {
      if (this.$refs.vuetable) {
        this.$refs.vuetable.changePage(page);
      }
    },
    OnLoadErrorData: function(response) {
      this.showDefaultServerError(response);
    },
    OnLoadedData: function() {
      this.loadingOverlay = false;
    },
    OnLoadingData: function() {
      this.loadingOverlay = true;
    }
  }
};
