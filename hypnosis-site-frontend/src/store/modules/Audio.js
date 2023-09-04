import AudioService from "@/services/audio.service"
// import { ApiService } from "../../services/base.service";

//state
const state = {
    easehearts: []
}

//getters
const getters = {
    getEaseHearts: state => state.easehearts
}

//actions
const actions = {
    getAllEaseHearts({commit}, {code}){
        AudioService.getEaseHearts(easehearts => {
            console.log(easehearts, 'easehearts')
            if (easehearts.status == 6){
                return false
            }
            commit('setEaseHearts', easehearts.data.result)
        }, code)
        
    }
}

//mutations
const mutations = {
    setEaseHearts(state, easehearts) {
        state.easehearts = easehearts
    }
}


export default  {
    state,
    getters,
    actions,
    mutations
}