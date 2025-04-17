<script lang="ts" setup>
import { BookOpen, Bookmark } from 'lucide-vue-next'

defineProps({
  title: String,
  slug: String,
  image_url: String,
  status: String,
  description: String,
  author: String,
  path: String,
})
</script>

<template>
  <div class="card lg:card-side bg-base-100 shadow-sm">
    <figure class="min-w-[320px] m-4 mr-0 rounded-md">
      <img class="h-full w-full rounded-lg object-cover" :src="`${image_url}`" alt="Novel Image" />
    </figure>
    <div class="card-body ml-0">
      <h1 class="card-title">
        <strong>{{ title }}</strong>
      </h1>
      <p>
        {{ status }}<br /><span class="text-base-content/60">By {{ author }}</span
        ><br />Ecchi• Xuanhuan • Action • Harem • Comedy • Mature • Slice of life • Fantasy •
        Adventure
      </p>
      <div class="stats shadow">
        <div class="stat">
          <div class="stat-title">Chapters</div>
          <div class="stat-value text-primary">1250</div>
        </div>

        <div class="stat">
          <div class="stat-title">Page Views</div>
          <div class="stat-value text-secondary">1.2M</div>
        </div>

        <div class="stat">
          <div class="stat-title">Rating</div>
          <div class="stat-value text-accent">4.8/5</div>
        </div>

        <div class="stat">
          <div class="stat-title">Bookmarks</div>
          <div class="stat-value">45.2K</div>
        </div>
      </div>
      <h2><strong>Synopsis</strong></h2>
      <p>
        {{ description }}
      </p>
      <div class="card-actions">
        <RouterLink :to="path + '/chapter-1'">
          <button class="btn bg-blue-500 text-white">
            <BookOpen class="w-4 h-4" />
            Read First Chapter
          </button>
        </RouterLink>
        <button class="btn">
          <Bookmark class="w-4 h-4" />
          Bookmark
        </button>
      </div>
    </div>
  </div>
</template>
