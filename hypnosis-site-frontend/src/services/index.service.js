import {ApiService} from './base.service'
import { url } from '@/config/url.config'

export default {
    getArticle()  {
        return ApiService.get(url.index)
    }
}

