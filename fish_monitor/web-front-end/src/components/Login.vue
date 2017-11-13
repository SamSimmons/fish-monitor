<template lang="html">
  <div class="login">
    <div class="login__container" v-show="!isRegistering">
      <div class="title-bar">
        <div class="title">LOGIN</div>
        <div class="subtitle" v-on:click="showRegister">or register</div>
      </div>
      <div class="field">
        <label for="username">Username:</label>
        <input type="text" name="username" defaultValue="" v-model="username">
      </div>
      <div class="field">
        <label for="password">Password:</label>
        <input type="password" name="password" defaultValue="" v-model="password" v-on:keyup.enter="submitLogin">
      </div>
      <button class="btn login__submit" v-on:click="submitLogin">GO</button>
      <div class="login__forgot">Forgot your password?</div>
    </div>
    <div class="login__container login__container--register" v-show="isRegistering">
      <div class="title-bar">
        <div class="title">REGISTER</div>
        <div class="subtitle" v-on:click="showLogin">or login</div>
      </div>
      <div class="field">
        <label for="username">Username:</label>
        <input type="text" name="username" defaultValue="" v-model="username">
      </div>
      <div class="field">
        <label for="email">Email:</label>
        <input type="text" name="email" defaultValue="" v-model="email">
      </div>
      <div class="field">
        <label for="password">Password:</label>
        <input type="password" name="password" defaultValue="" v-model="password">
      </div>
      <div class="field">
        <label for="repeat-password">Repeat Password:</label>
        <input type="password" name="repeat-password" defaultValue="" v-model="repeatPassword" v-on:keyup.enter="submitRegistration">
      </div>
      <div v-show="error" class="error-container">{{errorMessage}}</div>
      <button class="btn login__submit" v-on:click="submitRegistration">SIGN UP</button>
    </div>
    <div class="btn demo-link">view demo</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isRegistering: false,
      username: '',
      email: '',
      password: '',
      repeatPassword: '',
      error: false,
      errorMessage: ''
    }
  },
  methods: {
    showLogin () {
      this.isRegistering = false
    },
    showRegister () {
      this.username = ''
      this.password = ''
      this.isRegistering = true
    },
    submitLogin () {
      const username = this.username
      const password = this.password
      this.$emit('login', { username, password })
    },
    submitRegistration () {
      if (this.password !== this.repeatPassword) {
        this.error = true
        this.errorMessage = 'Passwords must match'
        return
      }
      this.error = false
      const username = this.username
      const email = this.email
      const password = this.password
      this.$emit('register', { username, email, password })
    }

  }
}
</script>

<style lang="css">

.login {
  align-items: center;
  display: flex;
  flex-flow: column;
  justify-content: center;
  min-height: 100vh;
}

.login__container {
  box-shadow: 3px 4px 3px 3px rgba(30, 30, 30, .2);
  background: var(--white);
  display: inline-flex;
  flex-flow: row wrap;
  padding: 30px 50px;
}

.login__container .subtitle {
  background: var(--primary);
  color: var(--white);
  cursor: pointer;
  font-size: .8rem;
  padding: 5px;
}

.login__forgot {
  cursor: pointer;
  font-size: .8rem;
  margin-top: 10px;
  opacity: .8;
}

.login__submit { margin-top: 30px; }

.title {
  font-size: 1.4rem;
  font-weight: 700;
}

.field {
  display: flex;
  flex-flow: column;
  margin-top: 15px;
}

.field input {
  border: 0;
  border-bottom: 1px solid var(--dark);
  background: var(--white);
  color: var(--dark);
}

.login__container {
  display: flex;
  flex-flow: column;
}

.title-bar {
  display: flex;
  justify-content: space-between;
  margin-left: -50px;
  margin-right: -50px;
  color: var(--primary);
  border-left: 5px solid var(--primary);
  padding-left: 40px;
}

.login__container--register {
  background: var(--primary);
  color: var(--white);
}

.login__container--register .subtitle {
  background: var(--white);
  color: var(--primary);
}

.login__container--register .title-bar {
  color: var(--white);
  border-left: 5px solid var(--white);
}

.login__container--register input {
  background: var(--primary);
  border-bottom: 1px solid var(--white);
  color: var(--white);
}

.login__container--register .btn {
    color: var(--white);
    border-color: var(--white);
}

.demo-link { margin-top: 30px; }

</style>
