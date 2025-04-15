<script lang="ts" setup>
const categories = [
  'Isekai',
  'Fantasy',
  'Action',
  'Romance',
  'Comedy',
  'Drama',
  'Slice of Life',
  'Adventure',
]
</script>

<template>
  <div class="mx-auto max-w-7xl pr-4 pl-4">
    <h2 class="ml-4 mb-4 text-2xl font-bold">Categories</h2>
    <button class="btn ml-4 m-1" v-for="category in categories" v-bind:key="category">
      {{ category }}
    </button>
  </div>
</template>
