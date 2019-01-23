<template>
  <div class="breadcrumb">
    <ul>
      <li
        v-for="(breadcrumb, idx) in breadcrumbList"
        :key="idx"
        @click="routeTo(idx)"
        :class="{'linked': !! breadcrumb.link}"
        >
        {{breadcrumb.name}}
      </li>
    </ul>
  </div>
</template>
<script>

export default {
  name: "Breadcrumb",
  data() {
    return {
      breadcrumbList:[],
    }
  },
  created: function() {
    this.updateList();
  },
  mounted: function() {
    this.updateList()
  },
  watch: { '$route' () { this.updateList() } },
  methods: {
    routeTo: function(pRouteTo){
      if( this.breadcrumbList[pRouteTo].link ) this.$router.push(this.breadcrumbList[pRouteTo].link)
    },
    updateList: function() {
      this.breadcrumbList = this.$route.meta.breadcrumb
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.breadcrumb ul{
  list-style: none;
  padding: 0;
  margin: 0
}
.breadcrumb ul{
  background: #eee;
  border-width: 1px;
  border-style: solid;
  border-color: #f5f5f5 #e5e5e5 #ccc;
  border-radius: 5px;
  box-shadow: 0 0 2px rgba(0,0,0,.2);
  overflow: hidden;
  width: 100%;
}

.breadcrumb .linked{
  float: left;
}

.breadcrumb li{
  padding: .7em 1em .7em 2em;
  float: left;
  text-decoration: none;
  color: #444;
  position: relative;
  text-shadow: 0 1px 0 rgba(255,255,255,.5);
  background-color: #ddd;
  background-image: linear-gradient(to right, #f5f5f5, #ddd);
  margin: 0
}

.breadcrumb li:first-child .linked{
  padding-left: 1em;
  border-radius: 5px 0 0 5px;
}



.breadcrumb .linked::after,
.breadcrumb .linked::before{
  content: "";
  position: absolute;
  top: 50%;
  margin-top: -1.5em;
  border-top: 1.5em solid transparent;
  border-bottom: 1.5em solid transparent;
  border-left: 1em solid;
  right: -1em;
}

.breadcrumb .linked::after{
  z-index: 2;
  border-left-color: #ddd;
}

.breadcrumb .linked::before{
  border-left-color: #ccc;
  right: -1.1em;
  z-index: 1;
}


.breadcrumb .active,
.breadcrumb .active:hover{
  font-weight: bold;
  background: none;
}

.breadcrumb .active::after,
.breadcrumb .active::before{
  content: normal;
}
</style>
