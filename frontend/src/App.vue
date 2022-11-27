<template>
    <div class="common-layout dark  ">
    <el-container>
      <el-header>Котобаза  <el-button plain @click="open">
      <el-icon color="#409EFC"  :size="20">
    <InfoFilled />
  </el-icon></el-button>
  </el-header>
      <el-main>Main</el-main>
      <el-footer>Версия фронтэнда: {{appVersion }}</el-footer>
    </el-container>

  </div>
</template>

<script>
import { ElMessageBox } from 'element-plus';
import {version} from '../package.json'
export default {
  name: 'App',
  components: {

  },
  data(){
    return {
      appVersion: version,
    }
  },
  methods:{
    open(){
      ElMessageBox({
        title: 'ЧЗХ?',
        message: "Это база данных, со списком имён для кошек.",
      })
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding:0;
  margin:0;
  color: #2c3e50;
}
.common-layout .el-header {
  position: relative;
  background-color: var(--el-color-primary);
  color: var(--el-text-color-primary);
  text-align: left;
  padding-top: 10px;
  font-size: 28px;
  font-weight: 800;
}
.common-layout .el-header .el-button {
  float: right;
  margin-top: 5px;
}
.common-layout .el-main {
  min-height: calc(100vh - 90px);
}
.common-layout .el-footer {
  text-align: right;
}
</style>

<style>
body{
  padding: 0;
  margin: 0;
}
</style>
