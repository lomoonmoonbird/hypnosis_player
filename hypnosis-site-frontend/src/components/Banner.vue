<template>
  <v-app id="inspire">
    <v-carousel>
      <v-carousel-item v-for="(item,i) in items" v-bind:src="item.src" :key="i"></v-carousel-item>
    </v-carousel>
  </v-app>
</template>

<script>

    export default {
      name: "Banner",
      data () {
        return {
          items: [
            {
              src: 'http://7xilr2.com1.z0.glb.clouddn.com//guanling/book/WechatIMG88.jpeg'
            },
            {
              src: 'http://7xilr2.com1.z0.glb.clouddn.com//guanling/book/b2.jpeg'
            }
          ]
        }
      }
  }
</script>

<style scoped>
/* img {
  height:100%;
  width: 100px;
  border-image-repeat: stretch
} */
.application--wrap {
  min-height: 100px;
}

@media screen and (max-width: 760px) {
   /* img {
    height: 20px;
    border-image-repeat: stretch
  } */
}
</style>

