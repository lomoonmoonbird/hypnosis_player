<template>
  <el-row>
  <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
    <el-card :body-style="{ padding: '0px' }">
      <img src="http://a.hiphotos.baidu.com/image/h%3D300/sign=3e99e2c2067b020813c939e152d8f25f/14ce36d3d539b6006a6cc5d0e550352ac65cb733.jpg" class="image">
      <div style="padding: 14px;">
        <span>Yummy hamburger</span>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <el-button type="text" class="button">Operating button</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
</template>

<script>
export default {
    name: "Cards",
    data() {
        return {
            currentDate: new Date()
        };
    }
}
</script>

<style scoped>

  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>

