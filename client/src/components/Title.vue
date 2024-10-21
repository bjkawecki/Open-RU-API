<script setup>

defineProps({
  title: String,
});
</script>

<template>
  <section class="flex justify-center my-5">
    <div class="w-full md:w-1/2">
      <h1 class="text-3xl font-medium tracking-tight text-gray-700 ps-1">
        {{ title }}
      </h1>
    </div>
  </section>
</template>
