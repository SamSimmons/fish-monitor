<template lang="html">
  <div class="dashboard__container">
    <div class="dashboard__title">
      <div class="dashboard__subtitle">Temperature</div>
      <span class="dashboard__metric">{{ temperature }}</span>
    </div>
    <div class="dashboard__chart">
      <svg class="mini-temp-chart"></svg>
    </div>
  </div>
</template>

<script>
export default {
  props: ['temperature'],
  data () {
    return {

    }
  }
}
</script>

<style lang="css">
.mini-temp-chart {
  width: 100%;
}
</style>
