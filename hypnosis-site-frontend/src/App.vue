<template>
  <div id="app">
    <router-view></router-view> 

  </div>
</template>

<script>
import Layouts from "@/layouts/Layouts"

export default {
  name: 'App',
  components: {
    Layouts
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  
}

body {
  margin: 0 0 ;
  padding: 0 0 ;
}
</style>
