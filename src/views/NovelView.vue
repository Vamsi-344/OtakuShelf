<script lang="ts" setup>
import { ArrowLeft } from 'lucide-vue-next'
import NovelDetails from '@/components/NovelDetails.vue'
import ChapterList from '@/components/ChapterList.vue'
</script>

<template>
  <div class="mx-auto max-w-7xl p-4 md:p-8">
    <div class="mx-auto max-w-4l m-2">
      <a href="/">
        <div class="btn btn-ghost text-base-content">
          <ArrowLeft class="w-4 h-4" />
          Back to Home
        </div>
      </a>
    </div>
    <NovelDetails />
    <ChapterList class="mt-4" />
  </div>
</template>
