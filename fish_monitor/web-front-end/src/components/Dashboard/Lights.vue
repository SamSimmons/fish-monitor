<template lang="html">
  <div class="dashboard__container">
    <div class="dashboard__title">
      <div class="dashboard__subtitle">Lights</div>
      <span class="dashboard__metric">{{ lights.lightValue }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ['lights'],
  data () {
    return {

    }
  }
}
</script>

<style lang="css">
</style>
