<script setup>
import { cases } from "@/enums/literals";

defineProps({
    props: {}
})

</script>

<template>
    <div>
        <div class="flex justify-between">
            <div class="my-10">
                <h2 class="text-xl">Fälle</h2>
                <div v-for="item in cases">
                    {{ item }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Maskulinum</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(1, 7)">
                    {{ value }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Femininum</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(7, 13)">
                    {{ value }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Neutrum</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(13, 19)">
                    {{ value }}
                </div>
            </div>
            <div class="my-10">
                <h2 class="text-xl">Plural</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(19, 25)">
                    {{ value }}
                </div>
            </div>
        </div>
        <div class="flex space-x-28">
            <div>
                <h2 class="text-xl">Kurzform</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(25, 29)">
                    {{ value }}
                </div>
            </div>
            <div>
                <h2 class="text-xl">Steigerung</h2>
                <div v-for="([key, value]) in Object.entries(props).slice(29, 31)">
                    {{ value }}
                </div>
            </div>
        </div>
    </div>
</template>