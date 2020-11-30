import api from '@/services/api'

export default {
  postCutest(payload) {
    //TODO : /cutestcat
    return api.post(`cutest/`, payload)
              .then(response => response.data)
  },
  getAllCats(){
    return api.get(`cat`)
              .then(response=>response.data)
  }
}