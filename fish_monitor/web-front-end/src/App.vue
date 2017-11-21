<template>
  <div id="app" class="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app'
}
</script>

<style>
.app {
  --primary: #50C8BF;
  --primary-border: #50C8BF33;
  --white: #fff;
  --dark: #606060;
  --error: rgb(255, 234, 143);
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

.btn--white {
  border: 2px solid var(--white);
  color: var(--white);
}

a {
  text-decoration: none;
  color: var(--primary);
}

nav {
  display: flex;
  justify-content: flex-end;
}

nav .btn { margin: 15px; }

</style>
