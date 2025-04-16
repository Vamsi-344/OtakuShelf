<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  chapters: Array,
})

const itemsPerPage = 50
const currentPage = ref(1)

// // You'd fetch this from FastAPI or preload it via prop or static JSON
// const chapters = ref([
//   { title: 'Chapter 1' },
//   { title: 'Chapter 2' },
//   // ...
//   { title: 'Chapter 1430' },
// ])
console.log(props.chapters.length)
const totalPages = computed(() => Math.ceil(props.chapters.length / itemsPerPage))

const paginatedChapters = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return props.chapters.slice(start, start + itemsPerPage)
})
</script>

<template>
  <div>
    <table class="table w-full">
      <thead>
        <tr>
          <th>#</th>
          <th>Chapter</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(chapter, index) in paginatedChapters" :key="index">
          <td>{{ index + 1 + (currentPage - 1) * itemsPerPage }}</td>
          <td>{{ chapter.title }}</td>
        </tr>
      </tbody>
    </table>

    <div class="join mt-4">
      <button class="join-item btn" :disabled="currentPage === 1" @click="currentPage--">«</button>
      <button
        v-for="page in totalPages"
        :key="page"
        class="join-item btn"
        :class="{ 'btn-active': currentPage === page }"
        @click="currentPage = page"
      >
        {{ page }}
      </button>
      <button class="join-item btn" :disabled="currentPage === totalPages" @click="currentPage++">
        »
      </button>
    </div>
  </div>
</template>
