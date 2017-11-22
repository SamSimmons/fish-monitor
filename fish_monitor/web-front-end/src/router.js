import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home'
import List from './components/List'
import Auth from './components/Auth'
import Dashboard from './components/Dashboard/index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
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
    },
    {
      path: '/tank/:id',
      name: 'Tank',
      component: Dashboard,
      before: (to, from, next) => {
        if (!Auth.loggedIn()) {
          next('/')
        }
        next()
      }
    }
  ]
})
