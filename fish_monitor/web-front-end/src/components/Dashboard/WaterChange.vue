<template lang="html">
  <div class="dashboard__container">
    <div class="dashboard__title">
      <div class="dashboard__subtitle">Water change due</div>
      <span class="dashboard__metric">{{ waterChanges.nextChange }}</span>
    </div>
    <div class="calendar">
      <div
        class="calendar__box"
        v-for="day in waterChanges.changeDates"
        :key="day.key"
        v-bind:class="{ 'calendar__box--full': day.changed }"
      >{{ day.date.format("DD/MM") }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['waterChanges'],
  data () {
    return {

    }
  }
}
</script>

<style lang="css">
</style>
