<script setup>
import { RouterLink } from "vue-router";

</script>

<template>
    <div class="mt-5">
        <RouterLink to="/words"
            class="px-3 py-2.5 font-bold text-white bg-green-500 rounded hover:bg-green-600 active:bg-green-500">
            Zurück zur Liste
        </RouterLink>
    </div>
</template>