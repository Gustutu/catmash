<template>
  <!DOCTYPE html>
  <section class="section">
    <div class="container">
      <h1 class="title">Hello World</h1>
      <p class="subtitle">My first website with <strong>Bulma</strong>!</p>
    </div>
    <div class="columns">
      <div class="column">
        <div class="container">
          <figure class="image is-128x128">
            <img
              class="is-rounded"
              src="/static/1dp"
            />
          </figure>
        </div>
      </div>
      <div class="column"></div>
      <figure class="image is-128x128">
        <img
          class="is-rounded"
          src="https://bulma.io/images/placeholders/128x128.png"
        />
      </figure>
    </div>
  </section>
</template>

<script>
import messageService from "./services/messageService";
export default {
  data() {
    return {
      cats: [],
    };
  },
  name: "App",

  created() {
    messageService.getCats().then((res) => {
      console.log(res);
      console.log("test");
      console.log(this.cats)
      this.cats.push(res[0]);
      this.cats.push(res[1])
    });
  },
};
</script>