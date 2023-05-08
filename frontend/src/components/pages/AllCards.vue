<template>
  <div>
    <div v-if="loading">
      <default-spinner></default-spinner>
    </div>
    <div v-else>
      <div class="MyCards">
        <div v-for="item in items" v-bind:key="item.id" class="MyCard">
          <div class="card">
            <div class="card_click" @click="$router.push(`/card/${item.id}`)">
              <img v-bind:src="item.image" class="card-img-top" alt="Fissure in Sandstone"/>
            </div>
            <div class="card-body">
              <h5 class="card-title">{{item.name}}</h5>
              <p class="card-text">{{item.price}} ₽</p>
              <a href="" class="btn btn-primary">Купить</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DefaultSpinner from "@/components/ui/DefaultSpinner.vue";

export default {
  name: "AllCards",
  components: {DefaultSpinner},
  data() {
    return {
      items: [],
      loading: true,
    }
  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/Jewelery/'
    })
        .then(response => response.data.forEach(item => this.items.push(item)))
        .finally(() => (this.loading = false))
  }
}
</script>

<style scoped>
@import '~mdb-ui-kit/css/mdb.min.css';
.MyCards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.MyCard {
  height: 10%;
  flex: 0 1 calc(100% / 4 - 20px * 2);
  margin: 20px;
}

.card_click{
  cursor: pointer;
}

</style>