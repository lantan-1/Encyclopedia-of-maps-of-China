import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/index.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('@/views/login/LoginAndRegisterView.vue')
    },
    {
      path: '/index',
      name: 'index',
      component: () => import('@/views/index/IndexView.vue'),
      redirect: '/maps/china',
      children: [
        {
          path: '/maps/china',
          component: () => import('@/views/maps/ChinaView.vue')
        },
        {
          path: '/maps/hebei',
          component: () => import('@/views/maps/hebei/HeBeiView.vue')
        },
        {
          path: '/maps/henan',
          component: () => import('@/views/maps/henan/HeNanView.vue')
        },
        {
          path: '/maps/shandong',
          component: () => import('@/views/maps/shandong/ShanDongView.vue')
        },
        {
          path: '/maps/shanxi',
          component: () => import('@/views/maps/shanxi/ShanXiView.vue')
        },
        {
          path: '/knowledge',
          component: () => import('@/views/knowledge/KnowledgeView.vue')
        },
        {
          path: '/settings',
          component: () => import('@/views/settings/Settings.vue')
        },
        {
          path: '/others',
          component: () => import('@/views/others/Others.vue')
        },
        {
          path: '/user',
          component: () => import('@/views/user/UserView.vue')
        },
        {
          path: '/user/chgpwd',
          component: () => import('@/views/user/chgpwd/ChgPwdView.vue')
        },
        {
          path: '/user/destroy',
          component: () => import('@/views/user/destroy/DestroyView.vue')
        }
      ]
    }
  ]
})

// 登录访问拦截 => 默认是直接放行的
// 根据返回值决定，是放行还是拦截
// 返回值：
// 1. undefined / true  直接放行
// 2. false 拦回from的地址页面
// 3. 具体路径 或 路径对象  拦截到对应的地址
//    '/login'   { name: 'login' }
router.beforeEach((to) => {
  // 如果没有token, 且访问的是非登录页，拦截到登录，其他情况正常放行
  const useStore = useUserStore()
  if (!useStore.token && to.path !== '/') return '/'
  // if (useStore.token && to.path === '/') return '/index'
})

export default router
