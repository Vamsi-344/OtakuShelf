<script lang="ts" setup></script>

<template>
  <div class="mx-auto max-w-7xl p-4 md:p-8">
    <div
      class="rounded-xl bg-gradient-to-r from-blue-900 to-blue-800 p-8 text-white bg-[url(/hero.png)]"
    >
      <div class="mx-auto max-w-3xl text-center">
        <h1 class="mb-4 text-4xl font-bold">Discover Amazing Light Novels</h1>
        <p class="mb-6 text-lg opacity-90">
          Explore thousands of light novels across various genres
        </p>
        <div class="relative">
          <!-- <input type="text" placeholder="Type here" class="input" /> -->
          <label class="input bg-neutral">
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
            <input
              type="search"
              class="grow"
              placeholder="Search for novels, authors, or genres..."
            />
            <kbd class="kbd kbd-sm bg-neutral border-neutral-100">⌘</kbd>
            <kbd class="kbd kbd-sm bg-neutral border-neutral-100">K</kbd>
          </label>
          <!-- <Input
            size="lg"
            placeholder="Search for novels, authors, or genres..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            startContent={<Icon icon="lucide:search" class="h-5 w-5 text-default-400" />}
            class="w-full max-w-xl bg-white"
          /> -->
        </div>
      </div>
    </div>
  </div>
  <!-- <div class="card bg-base-100 image-full shadow-sm">
    <figure>
      <img src="/cool.png" alt="Shoes" />
    </figure>
    <div class="card-body">
      <h2 class="card-title">Card Title</h2>
      <p>
        A card component has a figure, a body part, and inside body there are title and actions
        parts
      </p>
      <div class="card-actions justify-end">
        <button class="btn btn-primary">Buy Now</button>
      </div>
    </div>
  </div> -->
  <!-- <div class="hero bg-base-200 min-h-screen relative overflow-hidden">
    <div
      style="
        position: absolute;
        inset: 0;
        background-image: url('/hero.png');
        background-size: cover;
        background-position: center;
        opacity: 0.5;
        z-index: 0;
      "
    ></div>
    <div class="hero-content text-center relative z-10">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">Discover Your Next Obsession</h1>
        <p class="py-6">
          A dreamy bookshelf aesthetic with animated floating books, manga panels fading in/out, and
          maybe a character peeking from behind a shelf.
        </p>
        <button class="btn btn-primary m-2">Explore Now</button>
        <button class="btn btn-primary">Browse by Genre</button>
      </div>
    </div>
  </div> -->
</template>
