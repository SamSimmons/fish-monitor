<template>
  <div id="app" class="app">
    <home />
  </div>
</template>

<script>

import Home from './components/Home'

export default {
  name: 'app',
  components: {
    Home
  },
  methods: {
  }
}
</script>

<style>
.app {
  --primary: #50C8BF;
  --white: #fff;
  --dark: #4F4F4F;
  --background: linear-gradient(30deg, #3C4069, #683F67);
  --sans: 'Lato', sans-serif;
  background: var(--background);
  color: var(--dark);
  font-family: var(--sans);
  min-height: 100vh;
}

body {
  padding: 0;
  margin: 0;
}

.btn {
  border: 2px solid var(--primary);
  background: none;
  color: var(--primary);
  cursor: pointer;
  display: inline-block;
  padding: 10px;
  text-transform: uppercase;
}
</style>
