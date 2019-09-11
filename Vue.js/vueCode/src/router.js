import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/nursing-assessment',
      name:'nursingAsswssment',
      component: () => import(/* webpackChunkName: "nursingAsswssment" */ './views/assessmentDoc/nursing-assessment.vue')
    },
    {
      path: '/measure',
      name: 'measure',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/careplan/measure.vue')
    },
    {
      path: '/nurseplan',
      name: 'nurseplan',
      component: () => import(/* webpackChunkName: "about" */ './views/careplan/nurseplan.vue')
    },
    {
      path: '/newplan',
      name: 'newplan',
      component: () => import(/* webpackChunkName: "about" */ './views/careplan/newExePlan.vue')
    }
  ]
})
