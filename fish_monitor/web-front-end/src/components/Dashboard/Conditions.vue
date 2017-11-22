<template lang="html">
  <div class="dashboard__container">
    <div class="dashboard__title">
      <div class="dashboard__subtitle">Conditions</div>
      <span class="dashboard__metric">{{ conditions.conditionsStatus }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ['conditions'],
  data () {
    return {

    }
  }
}
</script>

<style lang="css">
</style>
