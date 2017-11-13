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
import Login from './components/Login'
import Auth from './components/Auth'
import TankList from './components/List'

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

<style>
.app {
  --primary: #50C8BF;
  --white: #fff;
  --dark: #606060;
  --background: linear-gradient(30deg, #3C4069, #683F67);
  --sans: 'Lato', sans-serif;
  background: var(--background);
  color: var(--dark);
  font-family: var(--sans);
  min-height: 100vh;
}

body {
  padding: 0;
  margin: 0;
}

.btn {
  border: 2px solid var(--primary);
  background: none;
  color: var(--primary);
  cursor: pointer;
  display: inline-block;
  padding: 10px;
  text-transform: uppercase;
}

nav {
  display: flex;
  justify-content: flex-end;
}

nav .btn { margin: 15px; }

</style>
