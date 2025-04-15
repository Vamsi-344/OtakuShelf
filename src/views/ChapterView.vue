<script lang="ts" setup>
import ChapterNavigation from '../components/ChapterNavigation.vue'
import ReaderSettings from '@/components/ReaderSettings.vue'
</script>

<template>
  <div class="min-h-screen bg-background p-4 md:p-8">
    <div class="mx-auto max-w-4xl">
      <div class="card w-auto bg-base-100 card-md shadow-sm mb-6">
        <div class="card-body p-6">
          <div class="flex items-center justify-between">
            <h1 class="text-xl font-semibold card-title">
              That Time I Got Reincarnated as a Slime
            </h1>
            <ReaderSettings />
          </div>
        </div>
        <ChapterNavigation />
      </div>
      <div class="card w-auto bg-base-100 card-md shadow-sm flex justify-between">
        <div class="card-body">
          <div class="justify-start">
            <h2 class="mb-4 text-lg font-medium">Chapter 1: The Storm</h2>
          </div>
          <div class="prose max-w-none text-foreground">
            <p class="mb-4">
              The wind howled through the ancient trees, their branches creaking under the force of
              the approaching storm. I had always known that my life would change, but I never
              expected it to happen like this. The day had started normally enough - I went to work,
              attended the usual meetings, and was heading home when everything went sideways.
            </p>
            <p class="mb-4">
              "Watch out!" someone screamed, but it was too late. The last thing I saw was a flash
              of steel and then... darkness. When I opened my eyes again, something was different. I
              couldn't move my arms or legs - in fact, I couldn't feel them at all. That's when I
              realized: I had been reincarnated as a slime.
            </p>
            <p class="mb-4">
              Now, you might think being a slime would be terrible, and honestly, I thought so too
              at first. But as I soon discovered, being a slime had its own unique advantages. For
              one thing, I could absorb almost anything and gain its properties. For another, I was
              practically immortal - at least when it came to conventional weapons.
            </p>
          </div>
          <!-- <p>
            A card component has a figure, a body part, and inside body there are title and actions
            parts
          </p> -->
          <!-- <div class="justify-end card-actions">
            <button class="btn btn-primary">Buy Now</button>
          </div> -->
        </div>
      </div>

      <ChapterNavigation />
    </div>
  </div>
  <!-- <div class="min-h-screen bg-background p-4 md:p-8">
    <div class="mx-auto max-w-4xl">
      <Card class="mb-6">
        <div class="p-4 md:p-6">
          <div class="mb-6 flex items-center justify-between">
            <h1 class="text-xl font-semibold">That Time I Got Reincarnated as a Slime</h1>
            <ReaderSettings
              fontSize="{fontSize}"
              setFontSize="{setFontSize}"
              lineHeight="{lineHeight}"
              setLineHeight="{setLineHeight}"
              fontFamily="{fontFamily}"
              setFontFamily="{setFontFamily}"
            />
          </div>
          <ChapterNavigation />
        </div>
      </Card>

      <Card class="mb-6 b-1">
        <div class="p-4 md:p-6">
          <h2 class="mb-4 text-lg font-medium">Chapter 1: The Storm</h2>
          <div style="{contentStyle}" class="prose max-w-none text-foreground">
            <p class="mb-4">
              The wind howled through the ancient trees, their branches creaking under the force of
              the approaching storm. I had always known that my life would change, but I never
              expected it to happen like this. The day had started normally enough - I went to work,
              attended the usual meetings, and was heading home when everything went sideways.
            </p>
            <p class="mb-4">
              "Watch out!" someone screamed, but it was too late. The last thing I saw was a flash
              of steel and then... darkness. When I opened my eyes again, something was different. I
              couldn't move my arms or legs - in fact, I couldn't feel them at all. That's when I
              realized: I had been reincarnated as a slime.
            </p>
            <p class="mb-4">
              Now, you might think being a slime would be terrible, and honestly, I thought so too
              at first. But as I soon discovered, being a slime had its own unique advantages. For
              one thing, I could absorb almost anything and gain its properties. For another, I was
              practically immortal - at least when it came to conventional weapons.
            </p>
          </div>
        </div>
      </Card>

      <ChapterNavigation />
    </div>
  </div> -->
</template>
