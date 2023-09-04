import Vue from 'vue'
import Vuex from 'vuex'
import Audio from './modules/Audio'
import product from './modules/products'
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        Audio,
        product
      }
    })