<script setup>
import { RouterLink, useRoute } from 'vue-router';


const isActiveLink = (routePath) => {
    const route = useRoute();
    return route.path === routePath;

}

</script>

<template>
    <nav class="p-5 w-full font-semibold text-gray-200 bg-blue-500 shadow">
        <div class="flex justify-between items-end">
            <RouterLink to="/" class="text-xl no-underline">
                Wortschatz
            </RouterLink>
            <div class="items-center">
                <RouterLink to="search"
                    :class="[isActiveLink('/search') ? 'bg-blue-600' : 'hover:bg-blue-600', 'p-3', 'no-underline', 'rounded']">
                    Suche
                </RouterLink>
                <RouterLink to="words"
                    :class="[isActiveLink('/words') ? 'bg-blue-600' : 'hover:bg-blue-600', 'p-3', 'no-underline', 'rounded']">
                    Wörter
                </RouterLink>
                <RouterLink to="upload"
                    :class="[isActiveLink('/upload') ? 'bg-blue-600' : 'hover:bg-blue-600', 'p-3', 'no-underline', 'rounded']">
                    Upload
                </RouterLink>
            </div>
        </div>
    </nav>
</template>