import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Login from '@/components/Login';
import 'bootstrap/dist/css/bootstrap.min.css'
//import '@/assets/css/main.css'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
