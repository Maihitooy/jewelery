<template>
  <div>
    <div v-if="loading">
      <default-spinner></default-spinner>
    </div>
    <div v-else>

      <div class="MyCards">
        <div v-for="category in categories" v-bind:key="category.id" class="MyCard">
          <div class="card">
            <div class="card_click" @click="$router.push(`/category/${category.id}`)">
              <img v-bind:src="category.image" class="card-img-top rounded-4" alt="Fissure in Sandstone"/>
            </div>
            <div class="card-body">
              <h5 class="card-title">{{category.name}}</h5>
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
  name: "CategoriesCards",
  components: {DefaultSpinner},
  data() {
    return {
      categories: [],
      loading: true,
    }
  },
  mounted() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/category/"
    })
        .then(response => response.data.forEach(category => this.categories.push(category)))
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

/*.card-img-top{*/
/*  bo*/
/*}*/

.card_click{
  cursor: pointer;
}

.card-body{
  padding: 0;
}
.card-title{
  margin-top: -60%;
  padding: 0;
  font-size: 40px;

  color: white;
}


</style>