<script setup>
import { cases } from "@/enums/word";

defineProps({
    props: {}
})

</script>

<template>
    <div>
        <div class="flex space-x-20">
            <div class="my-10">
                <h2 class="text-xl">Fälle</h2>
                <div v-for="item in cases">
                    {{ item }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Singular</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(6, 12)">
                    {{ value }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Plural</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(12, 18)">
                    {{ value }}
                </div>
            </div>
        </div>
    </div>
</template>