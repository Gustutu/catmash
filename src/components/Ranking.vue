<template>
  <div style="max-height:100vh">
    <nav class="navbar" role="navigation" aria-label="main navigation" style="background-color: #ecb8a5">
      <div class="navbar-brand">
         
    <a class="navbar-item">
        <router-link
      :to="{ name: 'home' }"
      class="title bm-6"
    >
    Cat Mash
        </router-link>
    </a>

   
  
      </div>

      <div id="navbarBasicExample" class="navbar-menu"></div>
    </nav>
   <div class="table-container "  >
      <table class="table is-scrollable  center-table is-striped is-fullwidth ">
        <thead>
          <tr>
            <th>Rang</th>
            <th>Image</th>
            <th>Score</th>
          </tr>
        </thead>
        <tfoot>
          <tr>
            <th>Rang</th>
            <th>Image</th>
            <th>Score</th>
          </tr>
        </tfoot>
        <tbody>
          <tr v-for="(cat, index) in cats" :key="index">
            <td>
              {{ index + 1 }}
            </td>
            <td>
              <figure class="is-flex image center">
                <img
                  class="image is-rounded"
                  style="width: auto"
                  :src="'/static/' + cat.id"
                />
              </figure>
            </td>
            <td>
              {{ cat.score }}
            </td>
          </tr>
        </tbody>
      </table>
      </div>
  </div>
</template>

<script>
// import { mapState, mapActions } from "vuex";
import messageService from "../services/messageService";

export default {
  name: "Ranking",
  data() {
    return {
      cats: [],
    };
  },
  methods: {
    getAllCats: function () {
      messageService.getAllCats().then((res) => {
        this.cats = res;
        this.cats.sort((a, b) => b.score - a.score);
        console.log(this.cats);
      });
    },
  },
  created() {
    this.getAllCats();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}

.table {
  margin-left: auto;
  margin-right: auto;
}

.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}

.center-table th {
  text-align: center;
  vertical-align: middle;
}

.center-table td {
  text-align: center;
  vertical-align: middle;
}
img {
  width: 250px;
}

</style>
