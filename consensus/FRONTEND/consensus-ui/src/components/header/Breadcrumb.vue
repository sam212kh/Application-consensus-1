<template>
  <div class="breadcrumb">
    <ul>
      <li
        v-for="(breadcrumb, idx) in breadcrumbList"
        :key="idx"
        @click="routeTo(idx)"
        :class="{ linked: !!breadcrumb.link }"
      >
        {{ breadcrumb.name }}
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "Breadcrumb",
  data() {
    return {
      breadcrumbList: [],
      shouldBeAddedToNavigation: true
    };
  },
  mounted: function() {
    this.updateLinkList(this.$router.currentRoute);
  },
  watch: {
    $route(value) {
      this.updateLinkList(value);
    }
  },
  methods: {
    routeTo: function(pRouteTo) {
      let newRoute = this.breadcrumbList[pRouteTo].link;
      if (newRoute) {
        this.$router.push(newRoute);
      }
    },
    updateLinkList: function(newRoute) {
      let self = this;

      // Push home page as a default
      if (self.breadcrumbList.length === 0) {
        this.breadcrumbList.push({ name: "schools", link: "/" });
      }

      // If the new route already exists in the bread crumb list
      self.breadcrumbList.forEach(function(currentBreadcrumbItem, index) {
        if (currentBreadcrumbItem.name === newRoute.name) {
          self.shouldBeAddedToNavigation = false;
          // Truncate list from new route index
          self.breadcrumbList.splice(index + 1, self.breadcrumbList.length);
        }
      });

      // Push current route into the breadcrumb
      if (this.shouldBeAddedToNavigation) {
        this.breadcrumbList.push({ name: newRoute.name, link: newRoute.path });
      }

      this.shouldBeAddedToNavigation = true;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.breadcrumb ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.breadcrumb ul {
  background: #eee;
  border-width: 1px;
  border-style: solid;
  border-color: #f5f5f5 #e5e5e5 #ccc;
  border-radius: 5px;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  width: 100%;
}

.breadcrumb .linked {
  float: left;
}

.breadcrumb li {
  padding: 0.7em 1em 0.7em 2em;
  float: left;
  text-decoration: none;
  color: #444;
  position: relative;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
  background-color: #ddd;
  background-image: linear-gradient(to right, #f5f5f5, #ddd);
  margin: 0;
}

.breadcrumb li:first-child .linked {
  padding-left: 1em;
  border-radius: 5px 0 0 5px;
}

.breadcrumb .linked::after,
.breadcrumb .linked::before {
  content: "";
  position: absolute;
  top: 50%;
  margin-top: -1.5em;
  border-top: 1.5em solid transparent;
  border-bottom: 1.5em solid transparent;
  border-left: 1em solid;
  right: -1em;
}

.breadcrumb .linked::after {
  z-index: 2;
  border-left-color: #ddd;
}

.breadcrumb .linked::before {
  border-left-color: #ccc;
  right: -1.1em;
  z-index: 1;
}

.breadcrumb .active,
.breadcrumb .active:hover {
  font-weight: bold;
  background: none;
}

.breadcrumb .active::after,
.breadcrumb .active::before {
  content: normal;
}
</style>
