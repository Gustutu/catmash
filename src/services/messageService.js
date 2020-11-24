import api from '@/services/api'

export default {
  getCats() {
    return api.get(`cat/`)
              .then(response => response.data)
  },
  postCutest(payload) {
    return api.post(`cat/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`messages/${msgId}`)
              .then(response => response.data)
  }
}