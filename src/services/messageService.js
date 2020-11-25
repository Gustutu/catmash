import api from '@/services/api'

export default {
  getCats() {
    //TODO : /tworandomcats
    return api.get(`cat/1`)
              .then(response => response.data)
  },
  postCutest(payload) {
    //TODO : /cutestcat
    return api.post(`cat/`, payload)
              .then(response => response.data)
  },
  getAllCats(){
    return api.get(`cat`)
              .then(response=>response.data)
  }
}