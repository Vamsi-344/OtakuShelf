<script lang="ts" setup>
const props = defineProps({
  title: String,
  slug: String,
  image_url: String,
})
import { Star } from 'lucide-vue-next'
</script>

<template>
  <div>
    <a :href="`/novel/${slug}`">
      <div class="card bg-base-100 w-76 h-96 shadow-sm">
        <figure>
          <img :src="`${image_url}`" alt="Devil's Son-in-law" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">{{ title }}</h2>
          <div class="card-actions justify-between">
            <p class="text-md">Isekai</p>
            <Star />
          </div>
        </div>
      </div>
    </a>
  </div>
</template>
