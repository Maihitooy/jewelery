<template>
  <div class="app">
    <AllCards></AllCards>
    <DetailCard></DetailCard>
  </div>
</template>

<script>


import AllCards from "@/components/pages/AllCards.vue";
import DetailCard from "@/components/pages/DetailCard.vue";

export default {
  name: 'App',
  components: {DetailCard, AllCards},
}
</script>

<style>
</style>
