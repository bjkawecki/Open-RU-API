<script setup></script>
<template>
    <section class="flex justify-center">
        <div class="w-full md:w-1/2">
            <div class="max-w-xl">
                <label class="block mb-2 text-sm font-medium text-gray-900"
                    for="file_input">JSON-Datei hochladen</label>
                <input
                    class="block w-full text-sm text-gray-900 bg-gray-50 rounded border border-gray-300 file:cursor-pointer file:mr-5 file:py-1 file:px-3 file:bg-blue-500 file:text-white file:border-blue-500"
                    id="file_input" type="file">
            </div>
        </div>
    </section>
</template>