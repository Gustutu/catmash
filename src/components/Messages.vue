<template>
  <div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>Rang</th>
          <th>Image</th>
          <th>Score</th>
        </tr>
      </thead>
    </table>
  </div>
</template>

<script>
// import { mapState, mapActions } from "vuex";
import messageService from "../services/messageService";

export default {
  name: "Messages",
  data() {
    return {
      cats: [],
    };
  },
  methods: {
    getAllCats:function(){
        messageService.getCats().then((res) => {
        this.cats=res
        console.log(this.cats)
      });
    }
  },
  created() {
    this.getAllCats()
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
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

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}
</style>
