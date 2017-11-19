<template>
  <div id="app" class="app">
    <div class="home">
      <login
        v-if="!loggedIn"
        @login="sendLogin"
        @register="sendRegistration"
      />
      <!--move nav into own component as soon as there's stuff to put in there  -->
      <nav v-show="loggedIn">
        <button class="btn" v-on:click="logOut">Log out</button>
      </nav>
      <tank-list v-if="loggedIn" />
    </div>
  </div>
</template>

<script>
import Login from './Login'
import Auth from './Auth'
import TankList from './List'

export default {
  name: 'app',
  components: {
    Login,
    TankList
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

<style></style>
