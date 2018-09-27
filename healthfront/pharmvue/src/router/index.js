import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Index from '@/components/Index'

Vue.use(Router)

export default new Router({
	mode: "history",
  routes: [
  	{
      path: '/',
      name: 'Index',
      component: Index
    },

    {
      path: '/Home',
      name: 'Home',
      component: Home
    }
  ]
})
