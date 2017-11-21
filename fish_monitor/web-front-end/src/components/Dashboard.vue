<template lang="html">
  <div class="dashboard__wrapper">
    <div class="dashboard">
      <div class="dashboard__name">{{ name }}</div>
      <div class="dashboard__body">
        <div class="dashboard__container">
          <div class="dashboard__title">
            <div class="dashboard__subtitle">Temperature</div>
            <span class="dashboard__metric">{{ temperature }}</span>
          </div>
        </div>
        <div class="dashboard__container">
          <div class="dashboard__title">
            <div class="dashboard__subtitle">Water change due</div>
            <span class="dashboard__metric">{{ nextChange }}</span>
          </div>
        </div>
        <div class="dashboard__container">
          <div class="dashboard__title">
            <div class="dashboard__subtitle">Lights</div>
            <span class="dashboard__metric">{{ lightValue }}</span>
          </div>
        </div>
        <div class="dashboard__container">
          <div class="dashboard__title">
            <div class="dashboard__subtitle">Conditions</div>
            <span class="dashboard__metric">{{ conditionsStatus }}</span>
          </div>
        </div>
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
      name: '',
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
        this.name = res.data.name
        // check last recorded temp
        // TODO needs to use min, max temp and check that last temp was ok
        this.temperature = res.data.last_temp

        // check the time of the last water change, and check it against the due date
        const { last_water_change: lastWaterChange, water_change_freq: freq } = res.data
        if (freq) {
          const lastChangeDate = moment(lastWaterChange)
          const dueChange = lastChangeDate.add(freq, 'days')
          if (dueChange < moment()) {
            this.nextChange = 'Now'
          }
          this.nextChange = `${dueChange.diff(moment(), 'days')} days`

          // check whether light value is setup and available
          const { light_value: lights } = res.data
          if (lights) {
            this.lightValue = lights
          }

          // check the water conditions are within ok levels
          const {
            last_ammonia: ammonia,
            ammonia_max: ammoniaMax,
            last_ph: ph,
            ph_min: phMin,
            ph_max: phMax
          } = res.data

          // TODOneeds to check the unhappy path, ie where ammonia max and ph vals arent setup yet
          const phStatusOk = (ph >= phMin && ph <= phMax)
          const ammoniaStatusOk = (ammonia <= ammoniaMax)
          if (phStatusOk && ammoniaStatusOk) {
            this.conditionsStatus = 'ok'
          }
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

.dashboard {
  background: var(--white);
  display: flex;
  flex-flow: row wrap;
}

.dashboard__wrapper {
  padding: 15vh 10vw;
}

.dashboard__name {
  border-left: 5px solid var(--primary);
  color: var(--primary);
  flex: 1 1 100%;
  font-size: 1.5rem;
  font-weight: 700;
  margin-top: 20px;
  padding-left: 20px;
}

.dashboard__body {
  display: flex;
  flex: 1 1 100%;
  flex-flow: row wrap;
  padding: 10px 30px 30px;
}

.dashboard__container {
  border: 1px solid var(--primary-border);
  box-sizing: border-box;
  flex: 1 1 calc(50% - 40px);
  min-height: 200px;
  margin: 20px;
  padding: 10px;
  position: relative;
}

.dashboard__title {
  color: var(--primary);
  display: inline-block;
  font-size: 2rem;
  font-weight: 700;
  position: absolute;
  right: 10px;
  text-align: right;
  top: -12px;
}

.dashboard__subtitle {
  background: var(--white);
  font-size: 1.35rem;
  font-weight: 400;
  padding: 0 10px;
}

.dashboard__metric { padding-right: 10px; }
</style>
