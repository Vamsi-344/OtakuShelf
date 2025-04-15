<script lang="ts" setup>
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'
</script>

<template>
  <div className="flex flex-wrap items-center justify-between gap-4">
    <div className="flex gap-2 items-end">
      <button class="btn btn-accent btn-xs sm:btn-sm md:btn-md m-3">
        <ChevronLeft class="h-4 w-4" />
        Previous
        <!-- <Icon icon="lucide:chevron-left" class="h-4 w-4" /> -->
      </button>
      <button class="btn btn-accent btn-xs sm:btn-sm md:btn-md mb-3">
        Next
        <ChevronRight class="h-4 w-4" />
        <!-- <Icon icon="lucide:chevron-right" class="h-4 w-4" /> -->
      </button>
    </div>
    <fieldset class="fieldset">
      <legend class="fieldset-legend">Chapter</legend>
      <select class="select">
        <option disabled selected>Pick a chapter</option>
        <option>Chapter 1: The Storm</option>
        <option>Chapter 2: New Beginnings</option>
        <option>Chapter 3: The Forest</option>
        <option>Chapter 4: First Contact</option>
        <option>Chapter 5: Evolution</option>
      </select>
      <!-- <span class="fieldset-label">Optional</span> -->
    </fieldset>
  </div>
</template>
