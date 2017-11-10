<template lang="html">
  <div class="home">
    <login v-show="!loggedIn" @submit="sendLogin" />
    <div v-show="loggedIn" >
      <button class="btn" v-on:click="logOut">Log out</button>
    </div>
    <div class="btn demo-link">view demo</div>
  </div>
</template>

<script>
import Login from './Login'
import Auth from './Auth'

export default {
  components: {
    Login
  },
  data () {
    return {
      loggedIn: Auth.loggedIn()
    }
  },
  methods: {
    sendLogin (creds) {
      console.log('creds', creds)
      Auth.login(creds, (err, response) => {
        if (err) {
          console.log('err', err)
        }
        console.log('res', response)
      })
    },
    logOut () {
      Auth.logout()
    }
  },
  created () {
    Auth.onChange = (loggedIn) => {
      this.loggedIn = loggedIn
    }
  }
}
</script>

<style lang="css">
.home {
  display: flex;
  flex-flow: column;
}


.demo-link {
  margin-top: 50px;
  padding: 10px;
}
</style>
