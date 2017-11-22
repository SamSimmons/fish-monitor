<template lang="html">
  <div class="dashboard__wrapper">
    <div class="dashboard">
      <div class="dashboard__name">{{ name }}</div>
      <div class="dashboard__body">
        <temperature :temperature="temperature"></temperature>
        <water-change :water-changes="waterChanges"></water-change>
        <lights :lights="lights"></lights>
        <conditions :conditions="conditions"></conditions>
      </div>
    </div>
  </div>
</template>

<script>
import Auth from '../Auth'
import moment from 'moment'
import axios from 'axios'
import { find } from 'lodash'
import WaterChange from './WaterChange'
import Temperature from './Temperature'
import Lights from './Lights'
import Conditions from './Conditions'

export default {
  components: {
    WaterChange,
    Temperature,
    Lights,
    Conditions
  },
  data () {
    return {
      name: '',
      temperature: '',
      lights: {
        lightValue: ''
      },
      conditions: {
        conditionsStatus: ''
      },
      waterChanges: {
        changeDates: [],
        nextChange: '',
        error: ''
      },
      errorMessage: ''
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    getMatchingDates (waterChanges) {
      const possibleDates = []
      for (let i = 14; i > 0; i--) {
        possibleDates.push({
          date: moment().subtract(i, 'd'),
          changed: false,
          key: `calendar-date-${i}`
        })
      }
      waterChanges.forEach((change) => {
        const matchingDate = find(possibleDates, (d) => d.date.isSame(moment(change.modified_date), 'day'))
        if (matchingDate) {
          matchingDate.changed = true
        }
      })
      return possibleDates
    },
    updateWaterChanges (tank, changes) {
      const { last_water_change: lastWaterChange, water_change_freq: freq } = tank
      if (freq) {
        const lastChangeDate = moment(lastWaterChange)
        const dueChange = lastChangeDate.add(freq, 'days')
        const diff = dueChange.diff(moment(), 'days')

        let nextChange = `${diff} ${diff > 1 ? 'days' : 'day'}`
        if (dueChange < moment()) {
          nextChange = 'Now'
        }

        const changeDates = this.getMatchingDates(changes)
        return {
          nextChange,
          changeDates
        }
      }
      return {
        error: 'Water Changes not setup'
      }
    },
    updateTemperature (tank) {
      // check last recorded temp
      // TODO needs to use min, max temp and check that last temp was ok
      return tank.last_temp
    },
    updateLights (tank) {
      // check whether light value is setup and available
      const { light_value: lights } = tank
      if (lights) {
        return lights
      }
      return ''
    },
    updateConditions (tank) {
      // check the water conditions are within ok levels
      const {
        last_ammonia: ammonia,
        ammonia_max: ammoniaMax,
        last_ph: ph,
        ph_min: phMin,
        ph_max: phMax
      } = tank

      // TODOneeds to check the unhappy path, ie where ammonia max and ph vals arent setup yet
      const phStatusOk = (ph >= phMin && ph <= phMax)
      const ammoniaStatusOk = (ammonia <= ammoniaMax)
      if (phStatusOk && ammoniaStatusOk) {
        return { conditionsStatus: 'ok' }
      }
      return {
        conditionsStatus: 'ALERT'
      }
    },
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
        const { tank, changes } = res.data
        this.name = tank.name
        this.temperature = this.updateTemperature(tank)
        this.waterChanges = this.updateWaterChanges(tank, changes)
        this.lights = this.updateLights(tank)
        this.conditions = this.updateConditions(tank)
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
  align-items: center;
  border: 1px solid var(--primary-border);
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  flex: 1 1 calc(50% - 40px);
  min-height: 200px;
  margin: 20px;
  padding: 60px 10px 10px;
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

.calendar {
  display: flex;
  flex-flow: row wrap;
  width: calc(7 * 35px);
}

.calendar__box {
  border: 1px solid var(--primary);
  box-sizing: border-box;
  color: var(--white);
  flex: 0 1 35px;
  font-size: .7rem;
  line-height: 35px;
  height: 35px;
  text-align: center;
}

.calendar__box:hover { color: var(--primary); }

.calendar__box--full {
  background: var(--primary);
  color: var(--primary);
}

.calendar__box--full:hover { color: var(--white); }
</style>
