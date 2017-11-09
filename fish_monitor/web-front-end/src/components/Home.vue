<template lang="html">
  <div class="home">
    <login />
    <div class="btn demo-link">view demo</div>
  </div>
</template>

<script>
import Login from './Login'

export default {
  components: {
    Login
  }
}
</script>

<style lang="css">
.home {
  display: flex;
  flex-flow: column;
}


.demo-link {
  margin-top: 50px;
  padding: 10px;
}
</style>
