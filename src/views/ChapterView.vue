<script lang="ts" setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ChapterNavigation from '../components/ChapterNavigation.vue'
import ReaderSettings from '@/components/ReaderSettings.vue'

const route = useRoute()
const router = useRouter()
const novelSlug = route.params.novelSlug
const chapterSlug = route.params.chapterSlug
const chapterNumber = Number(chapterSlug.split('-')[1])
const chapterData = ref(null)

async function getChapterInfo() {
  const res = await fetch('http://localhost:5000/novel/' + novelSlug + '/' + chapterSlug)
  chapterData.value = await res.json()
}

const fontSize = ref(null)
const lineHeight = ref(null)
const fontFamily = ref(null)

async function onChapterChange(e) {
  const newChapterSlug = 'chapter-' + String(e)
  console.log(newChapterSlug)
  console.log(novelSlug)
  router.push({
    name: 'Chapter',
    params: { novelSlug: novelSlug, chapterSlug: newChapterSlug },
    replace: true,
  })
}

async function changeFontSize(e) {
  fontSize.value = e
}

async function changeLineHeight(e) {
  lineHeight.value = e
}

async function changeFontFamily(e) {
  fontFamily.value = e
}

getChapterInfo()
</script>

<template>
  <div class="min-h-screen bg-background p-4 md:p-8" v-if="chapterData">
    <div class="mx-auto max-w-4xl">
      <div class="card w-auto bg-base-100 card-md shadow-sm mb-6">
        <div class="card-body p-6">
          <div class="flex items-center justify-between">
            <RouterLink :to="{ name: 'Novel', params: { novelSlug: novelSlug } }">
              <h1 class="text-xl font-semibold card-title">
                {{ chapterData.novel_title }}
              </h1>
            </RouterLink>

            <ReaderSettings
              v-on:changeFontSize="changeFontSize"
              v-on:changeLineHeight="changeLineHeight"
              v-on:changeFontFamily="changeFontFamily"
            />
          </div>
        </div>
        <ChapterNavigation
          v-on:chapterChange="onChapterChange"
          v-bind:chapterNumber="chapterNumber"
          v-bind:novelSlug="novelSlug"
        />
      </div>
      <div class="card w-auto bg-base-100 card-md shadow-sm flex justify-between">
        <div class="card-body">
          <div class="justify-start">
            <h2 class="mb-4 text-lg font-medium">{{ chapterData.title }}</h2>
          </div>
          <div class="prose max-w-none text-foreground">
            <p
              :class="`mb-4 text-${fontSize} leading-${lineHeight} font-${fontFamily}`"
              v-for="(para, index) in chapterData.body"
              v-bind:key="index"
            >
              {{ para }}
            </p>
          </div>
        </div>
      </div>

      <ChapterNavigation
        v-on:chapterChange="onChapterChange"
        v-bind:chapterNumber="chapterNumber"
        v-bind:novelSlug="novelSlug"
      />
    </div>
  </div>
</template>
