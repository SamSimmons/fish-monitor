<template lang="html">
  <div class="tank-list__wrapper">
    <div class="loading" v-if="loading">
      Loading...
    </div>
    <div class="tank-list">
      <list-item
        v-for="(tank, i) in tanks"
        v-bind:key="tank.name"
        v-bind:tank="tank"
      ></list-item>
      <create-tank></create-tank>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Auth from './Auth'
import { map } from 'lodash'
import moment from 'moment'
import ListItem from './ListItem'
import CreateTank from './CreateTank'

export default {
  components: {
    ListItem,
    CreateTank
  },
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


</style>
