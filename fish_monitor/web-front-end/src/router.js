import Vue from 'vue'
import Router from 'vue-router'
import App from './App'
import List from './components/List'
import Auth from './components/Auth'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'App',
      component: App
    },
    {
      path: '/list',
      name: 'List',
      component: List,
      before: (to, from, next) => {
        if (!Auth.loggedIn()) {
          next('/')
        }
        next()
      }
    }
  ]
})
