import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import NotFound from "@/views/NotFound.vue";
import SearchView from "@/views/SearchView.vue";
import WordsView from "@/views/WordsView.vue";
import WordView from "@/views/WordView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "start",
      component: HomeView,
    },
    {
      path: "/words",
      name: "words",
      component: WordsView,
    },
    {
      path: "/words/:id",
      name: "word",
      component: WordView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/:catchAll(.*)",
      name: "not_found",
      component: NotFound,
    },
  ],
});

export default router;
