<template>
    <div class="common-layout dark  ">
   <el-container>
   <el-header>Котобаза
    <el-button class="ml-4" plain @click="openInfo">
      <el-icon color="#409EFC"  :size="20">
    <InfoFilled />
  </el-icon>
  </el-button>
   <el-button  plain @click="openAdd" :icon="Plus">
      Придумай новое
  </el-button>
  </el-header>
      <el-main v-loading="loading">
        <h4>Классные имена с котобазы (целых {{totalCount}}):</h4>
        <el-space class="demo-input-size">
        <el-input
            v-model="searchBy"
            class="w-50 m-2 sort"
            placeholder="Поиск.."
            :suffix-icon="Search"
        />
        <el-select v-model="sortBy" class="m-2 sort" placeholder="Сортировка">
        <el-option
            v-for="item in sortOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
        </el-select>
        </el-space>
        <div class="contenter" >
          <el-space wrap direction="horizontal">
            <CatCard v-for="cat of sortedNames" :key="cat.id" :cat="cat" />
          </el-space>
        </div>

      </el-main>
      <el-footer>
        <el-space wrap>
        <p>Версия фронтэнда: {{appVersion }}</p>
        <p>Версия бекэнда: {{backendVersion }}</p>
        <p>Номер реплики: {{replicaVersion }}</p>
      </el-space>
      </el-footer>

    </el-container>
  <el-dialog
    v-model="dialogVisible"

    title="Придумал классное имя?"

    :before-close="handleClose"
  >
    <span>Прояви фантазию</span>
  <el-form
    status-icon
    v-loading="modalLoading"
    label-position="top"
    class="demo-ruleForm"
  >
    <span class="error-text">{{modalError}}</span>
    <el-form-item label="Имя для кошки" prop="name">
      <el-input v-model="newName" type="text" />
    </el-form-item>
    <el-form-item label="Кто придумал" prop="author">
      <el-input v-model="newAuthor" type="text"/>
    </el-form-item>
  </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Отмена</el-button>
        <el-button type="primary" @click="addNewName" :disabled="modalLoading">
          Добавить
        </el-button>
      </span>
    </template>
  </el-dialog>
  </div>
</template>
<script setup>
import { Plus, Search } from '@element-plus/icons-vue'
</script>
<script>
import { ElMessageBox } from 'element-plus';
import {version} from '../package.json'
import CatCard from "@/components/CatCard";
import {getAPI} from "@/params";

export default {
  name: 'App',
  components: {
    CatCard,
  },
  data(){
    return {
      appVersion: version,
      replicaVersion: "Unknown",
      backendVersion: "Unknown",
      dialogVisible: false,
      modalLoading: false,
      names: [],
      loading: true,
      totalCount: 0,
      modalError: "",
      newName: "",
      newAuthor: "",
      sortBy: "name_id",
      searchBy: "",
      sortOptions: [
        {
          value: 'name_id',
          label: 'Стандартная',
        },
        {
          value: 'name',
          label: 'По имени',
        },
        {
          value: 'author',
          label: 'По автору',
        },
      ]
    }
  },
  mounted(){
    this.getBackendData().catch((err)=> console.error(err))
    this.getList().catch((err)=> console.error(err))
  },
  computed: {
    sortedNames(){
      return this.searchingNames.sort((a, b) => {
        return ('' + a[this.sortBy]).localeCompare(b[this.sortBy]);
      })
    },
    searchingNames(){
      return this.names.filter((item) => item.name.toLowerCase().includes(this.searchBy.toLowerCase()) || item.author.toLowerCase().includes(this.searchBy.toLowerCase()))
    }
  },
  methods:{
    openInfo(){
      ElMessageBox({
        title: 'FAQ (ЧЗХ?)',
        message: "Что это? Это база данных, со списком имён для кошек.",
      })
    },
    openAdd(){
      this.dialogVisible = true;
    },
    async getBackendData(){
      const resp = await fetch(`${getAPI()}/api/info`);
      const data = await resp.json();
      console.log(data)
      this.replicaVersion = data.replica_id;
      this.backendVersion = data.backend_version;
    },
    async getList(){
      const resp = await fetch(`${getAPI()}/api/cats`);
      const data = await resp.json();
      console.log(data)
      this.names = data.cat_names;
      this.totalCount = data.count;
      this.loading = false;
    },
    handleClose(done){
      if (this.newName !== "" || this.newAuthor !== ""){
        ElMessageBox.confirm('Вы правда ничено не придумали?', {
          confirmButtonText: 'Да',
          cancelButtonText: 'Погодите.',})
            .then(() => {
              done()
            })
            .catch(() => {
            })
      }else{
        done()
      }

    },
    async addNewName(){
      if (this.newName === ""){
        this.modalError = "Введите имя."
        return;
      }
      if (this.newAuthor === ""){
        this.modalError = "Введите имя автора."
        return;
      }
      this.modalError = "";
      this.modalLoading = true;
      fetch(`${getAPI()}/api/cats`, {
        body: JSON.stringify({
          name: this.newName,
          author: this.newAuthor
        }),
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }).then(async (resp) => {
        if (!resp.ok){
          this.modalError = resp.statusMessage;
          this.modalLoading = false;
          return;
        }
        const data = await resp.json();
        this.names.push({
          id: data.created_id,
          name: this.newName,
          author: this.newAuthor,
        })
        this.newName = ""
        this.newAuthor = ""
        this.replicaVersion = data.replica_id;
        this.backendVersion = data.backend_version;
        this.modalLoading = false;
        this.dialogVisible = false;
      }).catch((err) => {
        this.modalError = String(err);
        this.modalLoading = false;
      })
    },
  },
}
</script>

<style>
.dialog-footer button:first-child {
  margin-right: 10px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding:0;
  margin:0;
  color: #2c3e50;
}
.contenter{

  margin-right: 50px;
  margin-left: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.ml-4{
  margin-left: 4px;
}
.el-form{
  padding: 15px;
}
.sort{
  margin-bottom: 20px;
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
  min-height: calc(100vh - 110px);
}
.error-text{
  color: red;
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
