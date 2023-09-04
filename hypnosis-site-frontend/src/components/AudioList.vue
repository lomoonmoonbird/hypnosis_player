<template>
  
  <v-app id="inspire">
      <v-layout row>
        <v-flex xs12 sm12 >
          <v-jumbotron  color="primary lighten-2">
              <v-container fill-height>
                <v-layout align-center>
                  <v-flex>
                    <h3 class="display-3">静心催眠</h3>
                    <p class="subheading">每周六晚八点至周日中午12点.</p>
                    <p class="subheading">静心共九节课，每周一节课，按顺序循环进行, 进行的课程为绿色边框的课程.</p>
                    <v-divider class="my-3"></v-divider>
                  </v-flex>
                  
                </v-layout>
              </v-container>
            </v-jumbotron>
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs8>
          <v-text-field
            v-model="code"
            label="密码"
            required
          ></v-text-field>
        </v-flex>
        <v-flex xs4>
          <v-btn color="success" @click="submitCode">提交</v-btn>
        </v-flex>
    </v-layout>
    <v-layout row>
      
      <v-flex xs12 sm12 >

            <template v-for="(item, index) in easehearts">
              <aplayer v-bind:class="{on_border: (item.status==2)}" :controls="true" :autoplay="false" :key="index" :music="{
                    title: item.title,
                    artist: item.author,
                    src: item.url,
                    pic: '',
                }"
                />
               
            </template>
      </v-flex>
    </v-layout>
  </v-app>
  
</template>

<script>
    import { mapGetters, mapActions } from 'vuex'
    import Aplayer from 'vue-aplayer'

    export default {
        name: "AudioList",
        components: {
          Aplayer
        },
        data: function () {
          return {
            code: ""
          }
        },
        methods: {
          submitCode(){
            if (!this.code){
              alert("请输入密码")
            }
            else{
                this.$store.dispatch('getAllEaseHearts', {code: this.code})
            }
          }
        },
        computed: mapGetters({
            easehearts: 'getEaseHearts'
            
        }),
        created () {
            // this.$store.dispatch('getAllEaseHearts')
     
        }
    }
</script>

<style scoped>
.aplayer {
  margin-left:0;
  margin-right: 0;
}
.on_border {
  border: 2px;
  border-style:solid;
    border-color:green;
}

.off_border {

}
</style>
