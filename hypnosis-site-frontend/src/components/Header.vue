<template>
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1">Guan Ling</el-menu-item>
  <el-submenu index="2">
    <template slot="title">Workspace</template>
    <el-menu-item index="2-1">item one</el-menu-item>
    <el-menu-item index="2-2">item two</el-menu-item>
    <el-menu-item index="2-3">item three</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">item four</template>
      <el-menu-item index="2-4-1">item one</el-menu-item>
      <el-menu-item index="2-4-2">item two</el-menu-item>
      <el-menu-item index="2-4-3">item three</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="3" disabled>Info</el-menu-item>
  <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">Orders</a></el-menu-item>
</el-menu>


</template>
<script>
  export default {
    name: "Header",
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style>
.el-menu-demo {
  top: 0;
  padding: 0 0 ;
}
</style>