<script lang="ts" setup>
import { Settings } from 'lucide-vue-next'
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
          <div class="btn btn-sm">A</div>
          <div class="btn btn-sm">AA</div>
          <div class="btn btn-sm">AAA</div>
        </div>
      </li>
      <li>
        Line Height
        <div class="mt-2 flex gap-2">
          <div class="btn btn-sm">1.6</div>
          <div class="btn btn-sm">1.8</div>
          <div class="btn btn-sm">2.0</div>
        </div>
      </li>
      <li>
        Font Family
        <div class="mt-2 flex gap-2">
          <div class="btn btn-sm">sans</div>
          <div class="btn btn-sm">serif</div>
          <!-- <div class="btn btn-sm">2.0</div> -->
        </div>
      </li>
      <!-- <li><a>Item 1</a></li>
      <li><a>Item 2</a></li> -->
    </ul>
  </details>
  <!-- <Dropdown>
      <DropdownTrigger>
        <Button variant="light" isIconOnly>
          <Icon icon="lucide:settings" className="h-5 w-5" />
        </Button>
      </DropdownTrigger>
      <DropdownMenu aria-label="Reading Settings">
        <DropdownItem key="font-size" className="font-semibold">
          Font Size
          <div className="mt-2 flex gap-2">
            <Button
              size="sm"
              variant={fontSize === "small" ? "solid" : "light"}
              onPress={() => setFontSize("small")}
            >
              A
            </Button>
            <Button
              size="sm"
              variant={fontSize === "medium" ? "solid" : "light"}
              onPress={() => setFontSize("medium")}
            >
              A
            </Button>
            <Button
              size="sm"
              variant={fontSize === "large" ? "solid" : "light"}
              onPress={() => setFontSize("large")}
            >
              A
            </Button>
          </div>
        </DropdownItem>
        <DropdownItem key="line-height" className="font-semibold">
          Line Height
          <div className="mt-2 flex gap-2">
            <Button
              size="sm"
              variant={lineHeight === "1.6" ? "solid" : "light"}
              onPress={() => setLineHeight("1.6")}
            >
              1.6
            </Button>
            <Button
              size="sm"
              variant={lineHeight === "1.8" ? "solid" : "light"}
              onPress={() => setLineHeight("1.8")}
            >
              1.8
            </Button>
            <Button
              size="sm"
              variant={lineHeight === "2" ? "solid" : "light"}
              onPress={() => setLineHeight("2")}
            >
              2.0
            </Button>
          </div>
        </DropdownItem>
        <DropdownItem key="font-family" className="font-semibold">
          Font Family
          <div className="mt-2 flex gap-2">
            <Button
              size="sm"
              variant={fontFamily === "serif" ? "solid" : "light"}
              onPress={() => setFontFamily("serif")}
            >
              Serif
            </Button>
            <Button
              size="sm"
              variant={fontFamily === "sans" ? "solid" : "light"}
              onPress={() => setFontFamily("sans")}
            >
              Sans
            </Button>
          </div>
        </DropdownItem>
      </DropdownMenu>
    </Dropdown> -->
</template>
