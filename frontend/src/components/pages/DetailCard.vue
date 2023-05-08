<template>
  <div>
    <div v-if="loading">
      <default-spinner></default-spinner>
    </div>
    <div v-else>
      <div class="card">

        <img v-bind:src="item.image" class="card-img-top" />
        <div class="card-body">
          <h3 class="card-title">{{item.name}}</h3>
          <p class="card-text" style="width: 80%; margin: 40px 0 40px 0">
            {{item.description}}
          </p>
          <p>{{item.precious_metal.name_metal}}, {{item.precious_metal_sample.sample}}</p>
          <p style="font-weight: bold;font-size: 25px">{{item.price}} ₽</p>
          <a href="#" class="btn btn-primary">В корзину</a>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import DefaultSpinner from "@/components/ui/DefaultSpinner.vue";

export default {
  name: "DetailCard",
  components: {DefaultSpinner},
  data() {
    return {
      item: null,
      loading: true,
    }
  },
  mounted() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/Jewelery/${this.$route.params['id']}`
    })
        .then(response => (this.item = response.data))
        .finally(() => (this.loading = false))
  }

}
</script>

<style scoped>

.card {
  flex-direction: row;
  align-items: center;
  margin: 0 150px 0 150px;
}
.card-title {
  font-weight: bold;
}
.card img {
  width: 30%;
  border-top-right-radius: 0;
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-body{
  text-align: left;
  margin-left: 100px;
}
@media only screen and (max-width: 768px) {
  a {
    display: none;
  }
  .card-body {
    padding: 0.5em 1.2em;
  }
  .card-body .card-text {
    margin: 0;
  }
  .card img {
    width: 50%;
  }
}
@media only screen and (max-width: 1200px) {
  .card img {
    width: 40%;
  }
}

</style>