import Vue from 'vue'
import Router from 'vue-router'
import Vote from '@/components/Vote'
import Ranking from '@/components/Ranking'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Vote
    },
    {
      path: '/ranking',
      name: 'ranking',
      component: Ranking
    }
  ]
})
