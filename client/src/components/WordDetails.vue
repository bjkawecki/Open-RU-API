<script setup>
import BackButton from "@/components/BackButton.vue";
import Spinner from "@/components/Spinner.vue";
import { wordClass } from "@/logic/literals";
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const jobId = route.params.id;
const state = reactive({
    word: {},
    isLoading: true,
    error: ""
});

onMounted(async () => {
    const config = {
        method: "GET",
        headers: { "content-type": "application/json" },
    };
    try {
        const Res = await fetch(`/api/words/${jobId}`, config);
        state.word = await Res.json();
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
    <section class="flex justify-center my-5">
        <div v-if="state.isLoading == false"
            class="flex-row p-5 w-full bg-gray-100 shadow md:w-1/2">
            <div>
                Wort: {{ state.word.name_accent }}
            </div>
            <div>
                Wortart: {{ wordClass[state.word.word_class] }}
            </div>
            <div>
                Übersetzung: <div class="inline-flex"
                    v-for="(translation, index) in state.word.translations"
                    :key="translation">
                    <div v-if="index">, {{ translation.name }}</div>
                    <div v-else>
                        {{ translation.name }}
                    </div>
                </div>
            </div>
            <BackButton />
        </div>
        <div v-else class="flex w-full text-gray-700 md:w-1/2">
            <Spinner />
        </div>
        <div v-if="state.error">{{ state.error }}</div>
    </section>
</template>