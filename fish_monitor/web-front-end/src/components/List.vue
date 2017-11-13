<template lang="html">
  <div class="tank-list__wrapper">
    <div class="loading" v-if="loading">
      Loading...
    </div>
    <div class="tank-list">
      <div class="tank-list__item" v-for="tank in tanks">
        <div class="name">{{ tank.name }}</div>
        <div class="timestamp">Last updated: {{ tank.timestamp }}</div>
        <div class="stats">
          <div class="stat">
            <div class="stat__title">Water changed</div>
            <div class="stat__body stat__body--primary"><span class="days">{{ tank.lastChange }}</span> days ago</div>
          </div>
          <div class="stat">
            <div class="stat__title">Temperature</div>
            <div class="stat__body">{{ tank.last_temp }} °c</div>
          </div>
          <div class="stat">
            <div class="stat__title">pH</div>
            <div class="stat__body">{{ tank.last_ph }}</div>
          </div>
          <div class="stat">
            <div class="stat__title">Ammonia</div>
            <div class="stat__body">{{ tank.last_ammonia }}</div>
          </div>
        </div>
      </div>
      <div class="tank-list__item tank-list__item--create">
        create a tank
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Auth from './Auth'
import { map } from 'lodash'
import moment from 'moment'

export default {
  data () {
    return {
      loading: false,
      tanks: [],
      errorMessage: ''
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      this.loading = true
      const headers = { Authorization: `Token ${Auth.getToken()}` }
      axios({
        method: 'get',
        url: 'http://localhost:8000/tanks/',
        headers
      })
      .then((res) => {
        this.tanks = map(res.data, (tank) => {
          tank.timestamp = moment(tank.updated).format('dddd MMMM Do YYYY')
          tank.lastChange = moment(tank.last_water_change).diff(moment(), 'days')
          return tank
        })
        this.loading = false
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

.tank-list__wrapper {
  display: flex;
  justify-content: center;
}

.tank-list {
  display: flex;
  flex: 0 1 800px;
  flex-flow: column;
}

.tank-list__item {
  background: var(--white);
  margin-top: 30px;
  padding: 30px;
}

.tank-list__item .name {
  border-left: 5px solid var(--primary);
  color: var(--primary);
  font-size: 1.4rem;
  font-weight: 700;
  margin-left: -30px;
  padding-left: 25px;
}

.tank-list__item .timestamp {
  border-bottom: 1px solid var(--dark);
  display: inline-block;
  margin-top: 5px;
  padding-bottom: 5px;
}

.tank-list__item .stats {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.tank-list__item .stat {
  box-sizing: border-box;
}

.stat__title { text-align: center; }

.stat__body {
  color: var(--primary);
  font-size: 2rem;
  margin-top: 10px;
}

.stat__body .days { font-size: 2.5rem; }

.stat__body--primary {
  align-items: center;
  background: var(--primary);
  color: var(--white);
  display: flex;
  flex-flow: column;
  font-size: 1rem;
  padding: 20px;
}

</style>
