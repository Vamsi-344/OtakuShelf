<script lang="ts" setup>
import { ref, watch, computed } from 'vue'
import {
  ChevronsLeft,
  ChevronsRight,
  ChevronLeft,
  ChevronRight,
  Navigation,
  SendHorizontal,
} from 'lucide-vue-next'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const props = defineProps({
  novelSlug: String,
})

const jumpChapter = ref('')

const selectedTab = ref('chapters')

const items = ref([])
const total = ref(0)
const limit = 10
const page = ref(1)
const totalPages = ref(1)

const windowSize = 5

// const startPage = computed(() => Math.max(2, page.value - Math.floor(windowSize / 2)))
// const endPage = computed(() => Math.min(totalPages.value - 1, startPage.value + windowSize - 1))

// const visiblePages = computed(() => {
//   const pages = []
//   for (let i = startPage.value; i <= endPage.value; i++) {
//     pages.push(i)
//   }
//   return pages
// })
const startPage = computed(() => {
  if (totalPages.value <= windowSize + 2) return 2
  return Math.max(
    2,
    Math.min(page.value - Math.floor(windowSize / 2), totalPages.value - windowSize),
  )
})

const endPage = computed(() => {
  if (totalPages.value <= windowSize + 2) return totalPages.value - 1
  return Math.min(totalPages.value - 1, startPage.value + windowSize - 1)
})

const visiblePages = computed(() => {
  const pages = []
  for (let i = startPage.value; i <= endPage.value; i++) {
    pages.push(i)
  }
  return pages
})

const fetchItems = async () => {
  const skip = (page.value - 1) * limit
  const res = await fetch(
    `http://localhost:5000/chapters/${props.novelSlug}?skip=${skip}&limit=${limit}`,
  )
  const data = await res.json()
  items.value = data.chapters
  total.value = data.total
  totalPages.value = Math.ceil(total.value / limit)
}

function jumpToChapter() {
  console.log(jumpChapter)
  router.push({
    name: 'Chapter',
    params: { novelSlug: props.novelSlug, chapterSlug: 'chapter-' + jumpChapter.value },
  })
}

fetchItems()

watch(page, fetchItems)
</script>

<template>
  <div class="card bg-base-100 shadow-sm">
    <div class="p-4">
      <div class="tabs tabs-box w-52">
        <input
          type="radio"
          name="my_tabs_6"
          class="tab"
          aria-label="Chapters"
          value="chapters"
          v-model="selectedTab"
        />

        <input
          type="radio"
          name="my_tabs_6"
          class="tab"
          aria-label="Comments"
          value="comments"
          v-model="selectedTab"
        />
      </div>
    </div>
    <div class="card-body">
      <div v-if="selectedTab === 'chapters'">
        <label class="input">
          <Navigation class="w-4 h-4" />
          <!-- <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g
              stroke-linejoin="round"
              stroke-linecap="round"
              stroke-width="2.5"
              fill="none"
              stroke="currentColor"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.3-4.3"></path>
            </g>
          </svg> -->
          <input v-model="jumpChapter" @keyup.enter="jumpToChapter" placeholder="Jump to..." />
        </label>
        <button class="btn btn-ghost" type="submit" v-on:click="jumpToChapter">
          <SendHorizontal class="h-4 w-4" />
        </button>
        <div v-if="totalPages > 1" class="join mt-4 justify-center flex flex-wrap gap-1">
          <button class="join-item btn" :disabled="page === 1" @click="page = 1">
            <ChevronsLeft class="w-4 h-4" />
          </button>

          <button class="join-item btn" :disabled="page === 1" @click="page--">
            <ChevronLeft class="w-4 h-4" />
          </button>

          <button
            class="join-item btn"
            :class="{ 'btn-active btn-primary': page === 1 }"
            @click="page = 1"
          >
            1
          </button>

          <span v-if="startPage > 2" class="join-item btn btn-disabled">...</span>

          <button
            class="join-item btn"
            v-for="p in visiblePages"
            :key="p"
            :class="{ 'btn-active btn-primary': page === p }"
            @click="page = p"
          >
            {{ p }}
          </button>

          <span v-if="endPage < totalPages - 1" class="join-item btn btn-disabled">...</span>

          <button
            v-if="totalPages > 1"
            class="join-item btn"
            :class="{ 'btn-active btn-primary': page === totalPages }"
            @click="page = totalPages"
          >
            {{ totalPages }}
          </button>

          <button class="join-item btn" :disabled="page === totalPages" @click="page++">
            <ChevronRight class="w-4 h-4" />
          </button>

          <button class="join-item btn" :disabled="page === totalPages" @click="page = totalPages">
            <ChevronsRight class="w-4 h-4" />
          </button>
        </div>

        <ul class="list bg-base-100 rounded-box shadow-md mt-4">
          <li class="list-row" v-for="chapter in items" v-bind:key="chapter.slug">
            <div class="text-4xl font-thin opacity-30 tabular-nums">
              {{ chapter.chapter_number }}
            </div>
            <div class="list-col-grow">
              <div>{{ chapter.title }}</div>
              <div class="text-xs uppercase font-semibold opacity-60">
                Updated {{ chapter.updated_at.slice(0, 10) }}
              </div>
            </div>
            <RouterLink :to="route.fullPath + '/' + chapter.slug">
              <button class="btn btn-square btn-ghost w-auto p-2">
                Read <ChevronRight class="h-4 w-4" />
              </button>
            </RouterLink>
          </li>
        </ul>
      </div>
      <div v-else-if="selectedTab === 'comments'">
        <p class="text-center">Comments section coming soon...</p>
      </div>
    </div>
  </div>
</template>
