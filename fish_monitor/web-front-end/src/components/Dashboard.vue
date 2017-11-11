<template lang="html">
  <div class="dashboard">
    <div class="loading" v-if="loading">
      Loading...
    </div>
    <div class="">
      dashboard
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Auth from './Auth'

export default {
  data () {
    return {
      loading: false
    }
  },
  created () {
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
        console.log('tanks response', res)
        this.loading = false
      })
      .catch((err) => {
        console.log('bad stuff', err)
      })
    }
  }
}
</script>

<style lang="css">
</style>
