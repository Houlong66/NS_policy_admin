import axios from 'axios'
import { Loading, Message } from 'element-ui'

let loading

const request = axios.create({
  baseURL: process.env.VUE_APP_HOST + process.env.VUE_APP_API_URL,
  timeout: 10000 // 请求超时
})

request.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
request.defaults.headers.get['Content-Type'] = 'application/x-www-form-urlencoded'
request.defaults.transformRequest = [function (data) {
  let ret = ''
  for (let it in data) {
    ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
  }
  return ret
}]

request.interceptors.request.use(
  config => {
    // 这里可以添加一些自定义的config设置，如token
    // 添加Loading
    if (config.loading) {
      loading = Loading.service({
        lock: true,
        text: '加载中'
      })
    }
    return config
  },
  error => {
    // 这里处理一些请求出错的情况
    if (loading) loading.close()
    Promise.reject(error)
  }
)

request.interceptors.response.use(
  response => {
    if (loading) loading.close()
    const res = response.data
    // 这里处理一些response 正常放回时的逻辑
    return res
  },
  error => {
    if (loading) loading.close()
    Message({
      message: error.response.data.msg,
      type: 'error'
    })
    // 这列处理一些response出错的逻辑
    return Promise.reject(error)
  }
)

export default request