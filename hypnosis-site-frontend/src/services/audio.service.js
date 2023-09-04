import {ApiService} from './base.service'
import { url } from '@/config/url.config'

export default  {
    getEaseHearts(cb, code)  {

         ApiService.getWithParam(url.audio, {code:code}).then((data)=>{cb(data.data)})
    }
}

