import axios from 'axios'

export default {
  login (creds, cb) {
    const { email, password } = creds
    if (localStorage.token) {
      if (cb) { cb(null, true) }
      this.onChange(true)
      return
    }
    axios.post('http://localhost:8000/api-token-auth/', {
      username: email,
      password
    })
    .then((res) => {
      console.log('hey got a response', res)
    })
    .catch(cb)
  },

  getToken () {
    return localStorage.token
  },

  logout (cb) {
    delete localStorage.token
    if (cb) {
      cb()
    }
    this.onChange(false)
  },

  loggedIn () {
    return !!localStorage.token
  },

  onChange () {}
}
