<script lang="ts" setup>
import { useRoute } from 'vue-router'
import { BookOpen, Bookmark } from 'lucide-vue-next'

const route = useRoute()

const props = defineProps({
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
          <!-- <div class="stat-figure text-primary">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              class="inline-block h-8 w-8 stroke-current"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
              ></path>
            </svg>
          </div> -->
          <div class="stat-title">Chapters</div>
          <div class="stat-value text-primary">1250</div>
          <!-- <div class="stat-desc">21% more than last month</div> -->
        </div>

        <div class="stat">
          <!-- <div class="stat-figure text-secondary">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              class="inline-block h-8 w-8 stroke-current"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 10V3L4 14h7v7l9-11h-7z"
              ></path>
            </svg>
          </div> -->
          <div class="stat-title">Page Views</div>
          <div class="stat-value text-secondary">1.2M</div>
          <!-- <div class="stat-desc">21% more than last month</div> -->
        </div>

        <div class="stat">
          <!-- <div class="stat-figure text-secondary">
            <div class="avatar online">
              <div class="w-16 rounded-full">
                <img
                  src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
                />
              </div>
            </div>
          </div> -->
          <div class="stat-title">Rating</div>
          <div class="stat-value text-accent">4.8/5</div>
          <!-- <div class="stat-desc text-secondary">31 tasks remaining</div> -->
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
        <a :href="path + '/chapter-1'">
          <button class="btn bg-blue-500 text-white">
            <BookOpen class="w-4 h-4" />
            Read First Chapter
          </button>
        </a>
        <button class="btn">
          <Bookmark class="w-4 h-4" />
          Bookmark
        </button>
      </div>
    </div>
  </div>
</template>
