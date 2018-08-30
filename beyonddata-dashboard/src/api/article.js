import axios from '@/libs/api.request'

export const publishArticle = ({title, articelBody, ownerId}) => {
	console.log('api: ' + title, articelBody, ownerId)
	const data = {
	    'article_title': title,
	    'content': articelBody,
	    'owner': ownerId,
	    'publish_time': new Date(),
	    'save_time': new Date(),
	    'is_published': true,
	    'is_draft': false
  	}
  	return axios.request({
	    url: 'http://45.76.77.76:9900/articles/',
	    data,
	    method: 'post'
  	})
}