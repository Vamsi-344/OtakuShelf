<script lang="ts" setup>
import { ref } from 'vue'
import NovelCard from './NovelCard.vue'

const novels = ref(null)
async function fetchNovels() {
  const res = await fetch('http://localhost:5000/novels')
  const data = await res.json()
  novels.value = data['response']
}

fetchNovels()
</script>

<template>
  <div class="mx-auto max-w-7xl p-4">
    <h2 class="ml-4 mb-4 text-2xl font-bold">Trending Novels</h2>
    <!-- <pre v-if="novels">{{ novels }}</pre> -->
    <div v-if="novels" class="grid grid-cols-4 gap-4">
      <NovelCard
        v-for="(novel, index) in novels"
        v-bind:key="index"
        :title="`${novel.title}`"
        :slug="`${novel.slug}`"
        :image_url="`${novel.image_url}`"
      />
    </div>
  </div>
</template>
