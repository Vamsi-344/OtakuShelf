<script lang="ts" setup>
import NovelCard from './NovelCard.vue'
</script>

<template>
  <div class="mx-auto max-w-7xl p-4">
    <h2 class="ml-4 mb-4 text-2xl font-bold">Trending Novels</h2>
    <div class="grid grid-cols-3 gap-4">
      <NovelCard />
    </div>
  </div>
</template>
