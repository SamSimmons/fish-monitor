<template lang="html">
  <div class="login">
    <div class="login__container" v-show="!isRegistering">
      <div class="title-bar">
        <div class="title">LOGIN</div>
        <div class="subtitle" v-on:click="showRegister">or register</div>
      </div>
      <div class="field">
        <label for="email">Email:</label>
        <input type="text" name="email" defaultValue="" v-model="email">
      </div>
      <div class="field">
        <label for="password">Password:</label>
        <input type="password" name="password" defaultValue="" v-model="password">
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
        <label for="email">Email:</label>
        <input type="text" name="email" defaultValue="" v-model="email">
      </div>
      <div class="field">
        <label for="password">Password:</label>
        <input type="password" name="password" defaultValue="" v-model="password">
      </div>
      <div class="field">
        <label for="repeat-password">Repeat Password:</label>
        <input type="password" name="repeat-password" defaultValue="" v-model="repeatPassword">
      </div>
      <button class="btn login__submit">SIGN UP</button>
    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      isRegistering: false,
      email: '',
      password: '',
      repeatPassword: ''
    }
  },
  methods: {
    showLogin () {
      this.isRegistering = false
    },
    showRegister () {
      this.isRegistering = true
    },
    submitLogin () {
      const email = this.email
      const password = this.password
      this.$emit('submit', { email, password })
    }

  }
}
</script>

<style lang="css">

.login {
  box-shadow: 3px 4px 3px 3px rgba(30, 30, 30, .2);
}

.login__container {
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
}

.login__container {
  display: flex;
  flex-flow: column;
  flex: 1 1 100%;
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

</style>
