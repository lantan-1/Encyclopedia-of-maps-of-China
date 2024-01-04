import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from '@/stores/index.js'
import BaiduMap from 'vue-baidu-map-3x'
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import * as echarts from 'echarts'


const app = createApp(App)
app.use(ElementPlus, {
  locale: zhCn
})
app.use(pinia)
app.use(router)
app.use(BaiduMap, {
  // ak 是在百度地图开发者平台申请的密钥 详见 http://lbsyun.baidu.com/apiconsole/key */
  ak: 'meufeI6CmevY5CgYNUBZKjnVjayDdETx'
  // v:'2.0',  // 默认使用3.0
  // type: 'WebGL' // ||API 默认API  (使用此模式 BMap=BMapGL)
})
app.config.globalProperties.$echarts = echarts
app.mount('#app')