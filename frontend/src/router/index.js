import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListRemisiones from '@/components/Remisiones/ListRemisiones'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/remisiones',
      name: 'ListRemisiones',
      component: ListRemisiones
    }
  ],
  mode:'history'
})
