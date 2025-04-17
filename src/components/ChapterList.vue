<script lang="ts" setup>
import { ref } from 'vue'
import { ChevronRight } from 'lucide-vue-next'
import { useRoute } from 'vue-router'

const route = useRoute()

defineProps({
  chapters: Array,
})

const selectedTab = ref('chapters')
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
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
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
          </svg>
          <input type="search" class="grow" placeholder="Search chapters..." />
        </label>
        <ul class="list bg-base-100 rounded-box shadow-md mt-4">
          <!-- <li class="p-4 pb-2 text-xs opacity-60 tracking-wide">Most played songs this week</li> -->

          <li class="list-row" v-for="chapter in chapters" v-bind:key="chapter.slug">
            <div class="text-4xl font-thin opacity-30 tabular-nums">
              {{ chapter.chapter_number }}
            </div>
            <!-- <div>
              <img
                class="size-10 rounded-box"
                src="https://img.daisyui.com/images/profile/demo/1@94.webp"
              />
            </div> -->
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
