<template>
  <div>
    <div class="MyCards">
      <div v-for="item in items" v-bind:key="item.id" class="MyCard">
        <div class="card">
          <img v-bind:src="item.image" class="card-img-top" alt="Fissure in Sandstone"/>
          <div class="card-body">
            <h5 class="card-title">{{item.name}}</h5>
            <p class="card-text">{{item.price}} ₽</p>
            <a href="" class="btn btn-primary">Купить</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AllCards",
  data() {
    return {
      items: [],
    }
  },
  methods: {
    async request_database() {
      (await axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/Jewelery/'
      })).data.forEach(item => {
        this.items.push(item)
      })
    }
  },
  mounted() {
    this.request_database()
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

</style>