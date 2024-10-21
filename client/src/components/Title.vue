<script setup>
import { defineProps } from 'vue';

defineProps({
    title: String
});
</script>

<template>
    <div className="flex justify-center my-10">
        <h1 class="text-xl">
            {{ title }}
        </h1>
    </div>
</template>