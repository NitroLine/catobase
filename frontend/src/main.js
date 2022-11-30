import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import {InfoFilled, Plus} from '@element-plus/icons-vue'
const app = createApp(App)

app.use(ElementPlus);
app.component('InfoFilled', InfoFilled);
app.component('PlusIcon', Plus);
app.mount('#app')