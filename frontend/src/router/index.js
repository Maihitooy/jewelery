import {createRouter, createWebHistory} from "vue-router";
import DetailCard from "@/components/pages/DetailCard.vue";
import AllCards from "@/components/pages/AllCards.vue";
import CategoriesCards from "@/components/pages/CategoriesCards.vue";
import DetailCategoriesCard from "@/components/pages/DetailCategoriesCard.vue";


const routes = [
  {
    path: '/card/:id',
    component: DetailCard
  },

  {
    path: '/',
    component: AllCards
  },

  {
    path: '/categories',
    component: CategoriesCards
  },
  {
    path: '/category/:id',
    component: DetailCategoriesCard
  },
]

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL)
})

export default router;