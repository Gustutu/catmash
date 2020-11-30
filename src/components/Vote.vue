<template>
  <div
    id="app"
    class="container centerall is-flex"
    style="
      display: flex;
      min-width: 100vw;
      min-height: 100vh;
      flex-wrap: nowrap;
    "
  >
    <h1
      class="title is-flex m-5"
      style="
        font-family: Comic Sans MS, cursive, sans-serif;
        text-align: center;
        position: absolute;
        display: block;
      "
    >
      CAT MASH
    </h1>

    <router-link
      :to="{ name: 'ranking' }"
      class="title bm-6"
      style="
        bottom: 10px;
        top-margin: auto;
        font-family: Comic Sans MS, cursive, sans-serif;
        text-align: center;
        position: absolute;
        display: block;
      "
    >
      Classement
    </router-link>
    <router-view />
    <div class="columns m-0 is-flex columns center" style="min-width: 100%">
      <div class="column center is-flex" style="background-color: #ecb8a5">
        <figure class="is-flex image center">
          <img
            v-on:click="selected(0)"
            class="image is-rounded"
            style="width: auto"
            v-bind:src="'/static/' + cat1.id"
          />
        </figure>
      </div>

      <div class="column center is-flex" style="background-color: #e49ab0">
        <figure class="is-flex image center">
          <img
            v-on:click="selected(1)"
            class="image is-rounded"
            style="width: auto"
            v-bind:src="'/static/' + cat2.id"
          />
        </figure>
      </div>
    </div>
  </div>
</template>




<script>
// TODO: use cat model
import messageService from "../services/messageService";
// import Cat from "../models/cat";
export default {
  data() {
    return {
      cat1: null,
      cat2: null,
      cats: [],
    };
  },
  name: "App",
  methods: {
    selected: function (winner) {
      console.log(winner);
      var msg = new Object();
      msg.catsIds = [this.cat1.id, this.cat2.id];
      if (winner == 0) {
        msg.winnerId = this.cat1.id;
      } else if (winner == 1) {
        msg.winnerId = this.cat2.id;
      }
      console.log(msg);
      messageService.postCutest(msg);
      var twoRandomDifferentCat = this.getTwoRandomDifferentCats();
      this.cat1 = twoRandomDifferentCat[0];
      this.cat2 = twoRandomDifferentCat[1];
    },
    getTwoRandomDifferentCats: function () {
      function getRandomDifferent(arr, last = undefined) {
        if (arr.length === 0) {
          return;
        } else if (arr.length === 1) {
          return arr[0];
        } else {
          let num = 0;
          do {
            num = Math.floor(Math.random() * arr.length);
          } while (arr[num] === last);
          return arr[num];
        }
      }

      var cat1 = getRandomDifferent(this.cats);
      var cat2 = getRandomDifferent(this.cats, cat1);
      console.log(cat1);
      return [cat1, cat2];
    },
  },

  created() {
    messageService.getAllCats().then((res) => {
      // cats = res.map(cat => Cat.deserialize(cat));
      console.log("test");
      this.cats = res;
      console.log(this.cats);
      var twoRandomDifferentCat = [];
    twoRandomDifferentCat = this.getTwoRandomDifferentCats();
    console.log(twoRandomDifferentCat);
    this.cat1 = twoRandomDifferentCat[0];
    this.cat2 = twoRandomDifferentCat[1];
    });
    
  },
};
</script>
