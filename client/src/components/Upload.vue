<script setup>
import { reactive, ref } from "vue";

const state = reactive({
    response: "",
    isLoading: false,
    error: ""
});

const file = ref();

function handleFileChange(e) {
    file.value = e.target.files[0];
    console.log(file.value);
}

const handleFileUpload = async () => {

    let formData = new FormData();
    formData.append("file", file.value);

    const config = {
        method: "POST",
        body: formData
    };
    try {
        const response = await fetch("/api/file/upload/", config);
        state.isLoading = true;
        state.response = await response.json();
    } catch (err) {
        if (err instanceof Error) {
            state.error = err.message;
        }
    } finally {
        state.isLoading = false;
    }
}


</script>
<template>
    <section class="flex justify-center">
        <div class="w-full md:w-1/2">
            <div class="max-w-xl">
                <form @submit.prevent="handleFileUpload">
                    <label class="block mb-2 text-sm font-medium text-gray-900"
                        for="file_input">JSON-Datei hochladen</label>
                    <input
                        class="block w-full text-sm text-gray-900 bg-gray-50 rounded border border-gray-300 file:cursor-pointer file:mr-5 file:py-1 file:px-3 file:bg-blue-500 file:text-white file:border-blue-500"
                        id="fileInput" type="file"
                        v-on:change="handleFileChange($event)" name="file" ref="file">
                    <button type="submit"
                        class="px-3 py-2 mt-2 bg-gray-300 rounded hover:bg-gray-400 active:bg-gray-300">Submit</button>
                </form>
            </div>
            <div v-if="state.isLoading">Lädt...</div>
            <div v-else-if="state.response">{{ state.response }}</div>
            <div v-else>{{ state.error }}</div>
        </div>
    </section>
</template>