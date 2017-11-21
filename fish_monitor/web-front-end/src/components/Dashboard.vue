<template lang="html">
  <div class="dashboard__wrapper">
    <div class="dashboard__name">Tank Name</div>
    <div class="dashboard__body">
      <div class="dashboard__container">
        <div class="dashboard__title">{{ temperature }}</div>
        <div class="dashboard__subtitle">Temperature</div>
      </div>
      <div class="dashboard__container">
        <div class="dashboard__title"> {{ nextChange }}</div>
        <div class="dashboard__subtitle">Water change due</div>
      </div>
      <div class="dashboard__container">
        <div class="dashboard__title">{{ lightValue }}</div>
        <div class="dashboard__subtitle">Lights</div>
      </div>
      <div class="dashboard__container">
        <div class="dashboard__title">{{ conditionsStatus }}</div>
        <div class="dashboard__subtitle">Conditions</div>
      </div>
    </div>
  </div>
</template>

<script>
import Auth from './Auth'
import moment from 'moment'
import axios from 'axios'

export default {
  data () {
    return {
      temperature: '',
      nextChange: '',
      lightValue: '',
      conditionsStatus: '',
      errorMessage: ''
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      const { id } = this.$route.params
      const headers = { Authorization: `Token ${Auth.getToken()}` }
      axios({
        method: 'get',
        url: `http://localhost:8000/tank/${id}/`,
        headers
      })
      .then((res) => {
        console.log(res.data)
        this.temperature = res.data.last_temp
        const { last_water_change: lastWaterChange, water_change_freq: freq } = res.data
        if (freq) {
          const lastChangeDate = moment(lastWaterChange)
          const dueChange = lastChangeDate.add(freq, 'days')
          if (dueChange < moment()) {
            this.nextChange = 'Now'
          }
          this.nextChange = dueChange.diff(moment(), 'days')
        }
      })
      .catch((err) => {
        if (err) {
          this.errorMessage = 'Something went wrong...'
        }
      })
    }
  }
}
</script>

<style lang="css">
</style>
