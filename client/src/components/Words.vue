<script setup>
import Spinner from "@/components/Spinner.vue";
import { onMounted, ref } from "vue";
import { RouterLink } from 'vue-router';

const is_loading = ref(true);
const error = ref("");
const words = ref([]);
const words_2 = ref([
    {
        "name": "большой",
        "name_accent": "большо́й",
        "word_class": "adjective",
        "translations": [
            {
                "name": "groß"
            },
            {
                "name": "dick"
            }
        ],
        "props": {
            "props_type": "adjective",
            "is_gradable": true
        }
    }
]);

onMounted(async () => {
    const config = {
        method: "GET",
        headers: { "content-type": "application/json" },
    };
    try {
        const Res = await fetch(`http://localhost:4000/${"words/"}`, config);
        words.value = await Res.json();
    } catch (error) {
        if (error instanceof Error) {
            error.value = error.message;
        }
    } finally {
        is_loading.value = false;
    }
});
</script>
<template>
    <section class="flex justify-center text-left">
        <div class="flex-row px-5 w-full md:w-1/2">
            <div class="flex-row shadow">
                <div class="flex justify-around p-5 font-medium text-white uppercase bg-blue-500 border-b">
                    <div>Russisch</div>
                    <div>Wortart</div>
                    <div>Deutsch</div>
                </div>
                <RouterLink :to="'words/' + word.id" v-for="word in words" :key="word.id"
                    class="flex p-5 text-center text-gray-700 bg-gray-50 border-b hover:bg-blue-100">
                    <div class="basis-1/3">{{ word.name_accent }}</div>
                    <div class="basis-1/3">{{ word.word_class }}</div>
                    <div class="basis-1/3">
                        <div class="inline-flex" v-for="(translation, index) in word.translations" :key="translation">
                            <div v-if="index">
                                , {{ translation.name }}
                            </div>
                            <div v-else>
                                {{ translation.name }}
                            </div>
                        </div>
                    </div>
                </RouterLink>
            </div>
            <div v-if="is_loading == true" class="flex justify-center p-5 text-gray-700">
                <Spinner />
            </div>
            <div v-else>{{ error }}</div>
        </div>
    </section>
</template>
