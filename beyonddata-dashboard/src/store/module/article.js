import { publishArticle } from '@/api/article'

export default {
  state: {
  },
  mutations: {
  },
  actions: {
    handlePublish ({ commit }, {title, articelBody, ownerId}) {
      console.log('store api: ' + title, articelBody, ownerId)
      return new Promise((resolve, reject) => {
        publishArticle({
          title,
          articelBody,
          ownerId
        }).then(res => {
          console.log(res)
          const data = res.data
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    }
  }
}