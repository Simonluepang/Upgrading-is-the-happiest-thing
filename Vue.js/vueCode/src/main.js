import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/layui/css/layui.css';
import '@/assets/layui/css/modules/laydate/default/laydate.css';
import '@/assets/layui/layui.all.js';
import './styles/index.scss' 

layui.config({
  // dir: '/layui/', //layui.js 所在路径（注意，如果是script单独引入layui.js，无需设定该参数。），一般情况下可以无视
  version: true ,//一般用于更新模块缓存，默认不开启。设为true即让浏览器不缓存。也可以设为一个固定的值，如：201610
  debug: true //用于开启调试模式，默认false，如果设为true，则JS模块的节点会保留在页面
});

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
