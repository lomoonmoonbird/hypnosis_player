import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/layouts/Layouts'),
      children: [
        {
          path: '',
          name: 'home',
          component: () => import("@/views/Home")
        },
        {
          path: '/article',
          name: 'article',
          component: () => import("@/components/Article")
        },
        {
          path: '/easeheart',
          name: 'easeheart',
          component: () => import("@/views/EaseHeart")
        }
      ]
    },
    {
      path: '/chat',
      name: 'chatroom',
      component: ()=>import("@/components/ChatRoom")
    },
    {
      path: '/test',
      name: 'test',
      component: () => import("@/components/test")
    }
    
  ]
})
