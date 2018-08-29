import axios from '@/libs/api.request'

export const login = ({ userName, password }) => {
  const data = {
    username: userName,
    password: password
  }
  return axios.request({
    url: 'http://45.76.77.76:9900/auth/token/create/',
    data,
    method: 'post'
  })
}

export const getUserInfo = (token) => {
  return axios.request({
    url: 'http://45.76.77.76:9900/auth/me',
    // headers: {
    //   Authorization: 'Token ' + token
    // },
    method: 'get'
  })
}

export const logout = (token) => {
  return axios.request({
    url: 'http://45.76.77.76:9900/auth/token/destroy/',
    method: 'post'
  })
}
