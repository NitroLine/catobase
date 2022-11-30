<template>
  <el-card :body-style="{ padding: '0px' }">
    <img
        src="@/assets/cat.png"
        class="image"
    />
    <div style="padding: 14px">
      <span>{{cat.name}}</span>
      <div class="bottom">
        <time class="author">Придумал: {{cat.author}}</time>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  props: {
    cat:{
      type: Object,
      required: true,
    }
  },
  name: "CatCard",
}
</script>

<style scoped>
.image {
  max-width: 300px;
  display: block;
}
.author {
  font-size: 12px;
  color: #999;
}
</style>