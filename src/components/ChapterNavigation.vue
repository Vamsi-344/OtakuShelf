<script lang="ts" setup>
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'
import { ref, watch } from 'vue'

const props = defineProps({
  chapterNumber: Number,
  novelSlug: String,
})

const emits = defineEmits(['chapterChange'])

const chaptersList = ref([])

async function getChaptersList() {
  const res = await fetch('http://localhost:5000/chaptersList/' + props.novelSlug)
  const data = await res.json()
  chaptersList.value = data.chapters
}

const selectedChapter = ref(props.chapterNumber)

watch(
  () => props.chapterNumber,
  (newVal) => {
    selectedChapter.value = newVal
  },
)

async function chapterChange(toBeChapterNumber: number) {
  emits('chapterChange', toBeChapterNumber)
}

getChaptersList()
</script>

<template>
  <div className="flex flex-nowrap w-full items-center justify-between gap-4 overflow-x-auto">
    <div className="flex gap-2 items-end">
      <button
        class="btn btn-accent btn-xs sm:btn-sm md:btn-md m-3"
        :disabled="chapterNumber === 1"
        @click="chapterChange(chapterNumber - 1)"
      >
        <ChevronLeft class="h-4 w-4" />
        Previous
      </button>

      <button
        class="btn btn-accent btn-xs sm:btn-sm md:btn-md mb-3"
        :disabled="chapterNumber === chaptersList.length"
        @click="chapterChange(chapterNumber + 1)"
      >
        Next
        <ChevronRight class="h-4 w-4" />
      </button>
    </div>
    <div class="ml-72 mb-2">
      <fieldset class="fieldset">
        <legend class="fieldset-legend">Chapter</legend>
        <select
          class="select"
          v-model="selectedChapter"
          @change="chapterChange(Number(selectedChapter))"
        >
          <option
            v-if="chaptersList"
            v-for="(chapter, index) in chaptersList"
            v-bind:key="index"
            v-bind:value="index + 1"
            class="text-right"
          >
            {{ chapter.title }}
          </option>
        </select>
      </fieldset>
    </div>
  </div>
</template>
