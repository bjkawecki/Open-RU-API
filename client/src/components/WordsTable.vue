<script setup>
import Spinner from "@/components/Spinner.vue";
import { wordClass } from "@/enums/word";
import { onMounted, reactive } from "vue";
import { RouterLink } from "vue-router";

const state = reactive({
  words: {},
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
  <section class="flex justify-center mb-10">
    <div class="flex-row w-full md:w-1/2">
      <div class="flex-row shadow">
        <div class="flex p-5 font-medium text-white uppercase bg-blue-500 border-b">
          <div class="basis-1/12"></div>
          <div class="basis-1/4">Russisch</div>
          <div class="basis-1/4">Wortart</div>
          <div class="">Deutsch</div>
        </div>
        <RouterLink :to="'words/' + word.id + '/'" v-for="(word, index) in state.words"
          :key="word.id" v-if="(state.isLoading == false) && state.words.length"
          class="flex p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100 active:bg-blue-200">
          <div class="basis-1/12">{{ index + 1 }}</div>
          <div class="basis-1/4">{{ word.name_accent }}</div>
          <div class="basis-1/4">{{ wordClass[word.word_class] }}</div>
          <div class="">
            <div class="inline-flex" v-for="(translation, index) in word.translations"
              :key="translation">
              <div v-if="index">, {{ translation.name }}</div>
              <div v-else>
                {{ translation.name }}
              </div>
            </div>
          </div>
        </RouterLink>
        <div v-else-if="state.isLoading == true"
          class="flex justify-center p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
          <Spinner />
        </div>
        <div v-else class="flex justify-center p-5 text-gray-700 bg-gray-50 border-b">
          Keine Einträge.
        </div>
      </div>
      <div v-if="state.error"
        class="flex justify-center p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
        {{ state.error }}</div>
    </div>
  </section>
</template>
