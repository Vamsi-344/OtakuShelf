<script lang="ts" setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const novelSlug = route.params.novelSlug
const novelInfo = ref(null)

async function fetchNovelInfo() {
  const res = await fetch('http://localhost:5000/novel/' + novelSlug)
  const data = await res.json()
  novelInfo.value = data['novel']
}

import { ArrowLeft } from 'lucide-vue-next'
import NovelDetails from '@/components/NovelDetails.vue'
import ChapterList from '@/components/ChapterList.vue'

fetchNovelInfo()
</script>

<template>
  <div class="mx-auto max-w-7xl p-4 md:p-8">
    <div class="mx-auto max-w-4l m-2">
      <RouterLink to="/">
        <div class="btn btn-ghost text-base-content">
          <ArrowLeft class="w-4 h-4" />
          Back to Home
        </div>
      </RouterLink>
    </div>

    <NovelDetails
      :title="`${novelInfo.title}`"
      :status="`${novelInfo.status}`"
      :author="`${novelInfo.author}`"
      :description="`${novelInfo.description}`"
      :slug="`${novelInfo.slug}`"
      :image_url="`${novelInfo.image_url}`"
      :path="route.path"
    />

    <ChapterList class="mt-4" :novelSlug="novelSlug" />
  </div>
</template>
