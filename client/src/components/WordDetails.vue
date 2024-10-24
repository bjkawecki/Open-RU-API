<script setup>
import BackButton from "@/components/BackButton.vue";
import AdjectiveProps from "@/components/props/AdjectiveProps.vue";
import Spinner from "@/components/Spinner.vue";
import { wordClass } from "@/enums/word";
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import SubstantiveProps from "./props/SubstantiveProps.vue";

const route = useRoute();
const jobId = route.params.id;
const state = reactive({
    word: {},
    props: {},
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
        const word = await Res.json();
        const { props, ...wordBase } = word;
        state.props = word.props;
        state.word = wordBase;
        console.table(state.word);
        console.table(state.props);

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
            class="flex flex-col justify-center w-full md:w-1/2">
            <div class="flex-row p-5 bg-gray-100 shadow">
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
                <div v-if="state.word.level">Stufe: {{ state.word.level }}</div>
                <div v-if="state.word.topic">Thema: {{ state.word.topic }}</div>
                <AdjectiveProps v-if="state.props?.props_type === 'adjective'"
                    :props=state.props />
                <SubstantiveProps v-if="state.props?.props_type === 'substantive'"
                    :props=state.props />

            </div>
            <BackButton />
        </div>
        <div v-else class="flex w-full text-gray-700 md:w-1/2">
            <Spinner />
        </div>
        <div v-if="state.error">{{ state.error }}</div>
    </section>
</template>