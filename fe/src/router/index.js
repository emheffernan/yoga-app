import Vue from 'vue'
import Router from 'vue-router'
import YogaApp from '@/components/YogaApp'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'YogaApp',
      component: YogaApp
    }
  ]
})
