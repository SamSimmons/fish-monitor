import axios from 'axios'

export default {
  login (creds, cb) {
    const { username, password } = creds
    if (localStorage.token) {
      if (cb) { cb(null, true) }
      this.onChange(true)
      return
    }
    axios.post('http://localhost:8000/api-token-auth/', {
      username,
      password
    })
    .then((res) => {
      localStorage.token = res.data.token
      this.onChange(true)
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
