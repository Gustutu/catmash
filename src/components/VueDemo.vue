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
      :to="{ name: 'messages' }"
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
    <router-view/>
    <div class="columns m-0 is-flex columns center" style="min-width: 100%">
      <div class="column center is-flex" style="background-color: #ecb8a5">
        <figure class="is-flex image center">
          <img
            v-on:click="selected(0)"
            class="image is-rounded"
            style="width: auto"
            v-bind:src="'/static/' + cats[0].id"
          />
        </figure>
      </div>

      <div class="column center is-flex" style="background-color: #e49ab0">
        <figure class="is-flex image center">
            <img
              v-on:click="selected(1)"
              class="image is-rounded"
              style="width: auto"
              v-bind:src="'/static/' + cats[1].id"
            />
        </figure>
      </div>
    </div>
  </div>
</template>




<script>
// TODO: use cat model
import messageService from "../services/messageService";
import Cat from "../models/cat";
export default {
  data() {
    return {
      cats: [],
    };
  },
  name: "App",
  methods: {
    selected: function (winner) {
      console.log(winner);
      var msg = new Object();
      msg.catsIds = [this.cats[0].id, this.cats[1].id];
      msg.winnerId = this.cats[winner].id;
      console.log(msg);
      messageService.postCutest(msg);
      this.cats = [];
      messageService.getCats().then((res) => {
        this.cats.push(res[0]);
        this.cats.push(res[1]);
      });
    },
  },

  created() {
    messageService.getCats().then((res) => {
      cats = res.map(cat => Cat.deserialize(cat));
      console.log("test");
      console.log(this.cats);

      this.cats.push(cats[0]);
      this.cats.push(cats[1]);
      console.log(this.cats[0].id);
    });
  },
};
</script>
