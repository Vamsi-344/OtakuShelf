<script lang="ts" setup>
import { Settings } from 'lucide-vue-next'

const emits = defineEmits(['changeFontSize', 'changeLineHeight', 'changeFontFamily'])

async function changeFontSize(size: string) {
  emits('changeFontSize', size)
}

async function changeLineHeight(size: string) {
  emits('changeLineHeight', size)
}

async function changeFontFamily(family: string) {
  emits('changeFontFamily', family)
}
</script>

<template>
  <details class="dropdown dropdown-end">
    <summary class="btn m-1">
      <Settings class="h-5 w-5" />
    </summary>
    <ul class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
      <li>
        Font Size
        <div class="mt-2 flex gap-2">
          <div class="btn btn-sm" v-on:click="changeFontSize('base')">A</div>
          <div class="btn btn-sm" v-on:click="changeFontSize('lg')">AA</div>
          <div class="btn btn-sm" v-on:click="changeFontSize('xl')">AAA</div>
        </div>
      </li>
      <li>
        Line Height
        <!-- Check the tailwind class names with their size https://v3.tailwindcss.com/docs/line-height -->
        <div class="mt-2 flex gap-2">
          <div class="btn btn-sm" v-on:click="changeLineHeight('normal')">1.5</div>
          <div class="btn btn-sm" v-on:click="changeLineHeight('relaxed')">1.625</div>
          <div class="btn btn-sm" v-on:click="changeLineHeight('loose')">2</div>
        </div>
      </li>
      <li>
        Font Family
        <div class="mt-2 flex gap-2">
          <div class="btn btn-sm" v-on:click="changeFontFamily('sans')">sans</div>
          <div class="btn btn-sm" v-on:click="changeFontFamily('serif')">serif</div>
        </div>
      </li>
    </ul>
  </details>
</template>
