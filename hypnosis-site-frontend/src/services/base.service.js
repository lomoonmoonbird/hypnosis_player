import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import {API_URL} from '@/config/url.config'

export const ApiService = {
    init() {
        Vue.use(VueAxios, axios)
        Vue.axios.defaults.baseURL = API_URL
    },

    get (resource, slug = '') {
        return Vue.axios
          .get(`${resource}`)
        //   .then((data) => {
        //       console.log('data', data.data)
        //       return data.data
        //   })
          .catch((error) => {
            throw new Error(`[RWV] ApiService ${error}`)
          })
      },

    getWithParam(resource,  params={}) {
      console.log(params, "params")
      return Vue.axios
        .get(`${resource}`, {params:params})

        .catch((error) => {
          throw new Error(`[RWV] ApiService ${error}`)
        })
    },
}

