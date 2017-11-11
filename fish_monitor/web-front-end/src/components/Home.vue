<template lang="html">
  <div class="home">
    <login
      v-show="!loggedIn"
      @login="sendLogin"
      @register="sendRegistration"
    />
    <!--move nav into own component as soon as there's stuff to put in there  -->
    <nav v-show="loggedIn">
      <button class="btn" v-on:click="logOut">Log out</button>
    </nav>
    <dashboard v-show="loggedIn" />
  </div>
</template>

<script>
import Login from './Login'
import Auth from './Auth'
import Dashboard from './Dashboard'

export default {
  components: {
    Login,
    Dashboard
  },
  data () {
    return {
      loggedIn: Auth.loggedIn()
    }
  },
  methods: {
    sendLogin (creds) {
      Auth.login(creds, (err, res) => {
        if (err) { console.log('err', err) }
        console.log('res', res)
      })
    },
    sendRegistration (creds) {
      console.log('creds', creds)
      Auth.register(creds, (err, res) => {
        if (err) { console.log('err', err) }
        console.log('res', res)
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
nav {
  display: flex;
  justify-content: flex-end;
}

nav .btn { margin: 15px; }
</style>
