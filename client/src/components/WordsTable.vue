<script setup>
import Spinner from "@/components/Spinner.vue";
import { wordClass } from "@/logic/literals";
import { onMounted, reactive } from "vue";
import { RouterLink } from "vue-router";

const state = reactive({
  jobs: [],
  isLoading: true,
  error: ""
});


onMounted(async () => {
  const config = {
    method: "GET",
    headers: { "content-type": "application/json" },
  };
  try {
    const Res = await fetch("/api/words/", config);
    state.words = await Res.json();
  } catch (err) {
    if (err instanceof Error) {
      state.error = err.message;
    }
  } finally {
    state.isLoading = false;
  }
});
</script>
<template>
  <section class="flex justify-center">
    <div class="flex-row w-full md:w-1/2">
      <div class="flex-row shadow">
        <div
          class="flex justify-around p-5 font-medium text-white uppercase bg-blue-500 border-b">
          <div>Russisch</div>
          <div>Wortart</div>
          <div>Deutsch</div>
        </div>
        <RouterLink :to="'words/' + word.id + '/'" v-for="word in state.words"
          :key="word.id" v-if="state.isLoading == false"
          class="flex p-5 text-center text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
          <div class="basis-1/3">{{ word.name_accent }}</div>
          <div class="basis-1/3">{{ wordClass[word.word_class] }}</div>
          <div class="basis-1/3">
            <div class="inline-flex" v-for="(translation, index) in word.translations"
              :key="translation">
              <div v-if="index">, {{ translation.name }}</div>
              <div v-else>
                {{ translation.name }}
              </div>
            </div>
          </div>
        </RouterLink>
        <div v-else="state.isLoading == true"
          class="flex justify-center p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
          <Spinner />
        </div>
      </div>
      <div v-if="state.error"
        class="flex justify-center p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
        {{ state.error }}</div>
    </div>
  </section>
</template>
