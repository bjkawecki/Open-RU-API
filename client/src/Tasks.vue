<script setup>
import { ref, onMounted } from "vue";

const name = ref("John");
const status = ref("active");
const tasks = ref(["Task 1", "Task 2", "Task 3"]);
const newTask = ref("");

const toggleStatus = () => {
    if (status.value === "active") {
        status.value = "pending";
    } else {
        status.value = "active";
    }
};

const addTask = () => {
    if (newTask.value.trim() !== "") {
        tasks.value.push(newTask.value);
        newTask.value = "";
    }
};

const deleteTask = (index) => {
    tasks.value.splice(index, 1);
};

onMounted(async () => {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos");
        const data = await response.json();
        tasks.value = data.slice(0, 5).map((task) => task.title);
    } catch (error) {
        console.log("Error fetching tasks");
    }
});
</script>

<template>
    <h1>{{ name }}</h1>
    <h2>Status: {{ status }}</h2>
    <br />
    <form @submit.prevent="addTask">
        <label for="newTask">Add Task</label>
        <input type="text" name="newTask" id="newTask" v-model="newTask">
        <button type="submit">Submit</button>
    </form>
    <br />

    <h3>Tasks</h3>
    <div>
        <ul>
            <li v-for="(task, index) in tasks" :key="task">
                <span>
                    {{ task }}
                </span>
                <button @click="deleteTask(index)">x</button>
            </li>
        </ul>
    </div>
    <br />
    <div>
        <button @click="toggleStatus">Change status</button>
    </div>
</template>
