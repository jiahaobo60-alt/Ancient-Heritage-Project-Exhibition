import axios from 'axios'

const API_BASE = 'http://127.0.0.1:8000'

const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
api.interceptors.request.use(
  config => {
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

// ========== 仪表盘统计 ==========
export const dashboardApi = {
  getStats: () => api.get('/architecture/dashboard_stats/'),
  getChartsData: () => api.get('/architecture/charts_data/'),
}

// ========== 古建筑 API (完整CRUD) ==========
export const buildingApi = {
  // 获取列表
  getAll: (params) => api.get('/architecture/buildings/', { params }),
  
  // 获取详情
  getById: (bid) => api.get(`/architecture/building/${bid}/`),
  
  // 创建
  create: (data) => api.post('/architecture/buildings/', data),
  
  // 更新
  update: (bid, data) => api.put(`/architecture/buildings/${bid}/`, data),
  
  // 删除
  delete: (bid) => api.delete(`/architecture/buildings/${bid}/`),
  
  // 筛选
  getByDynasty: (dynasty_id) => api.get('/architecture/buildings_by_dynasty/', { params: { dynasty_id } }),
  getByRegion: (region_id) => api.get('/architecture/buildings_by_region/', { params: { region_id } }),
  
  // 统计
  getRoofDistribution: () => api.get('/architecture/roof_type_distribution/'),
  
  // 导出
  exportAll: () => api.get('/architecture/export_all/'),
}

// ========== 朝代 API (完整CRUD) ==========
export const dynastyApi = {
  getAll: () => api.get('/architecture/dynasty/'),
  getById: (id) => api.get(`/architecture/dynasty/${id}/`),
  create: (data) => api.post('/architecture/dynasty/', data),
  update: (id, data) => api.put(`/architecture/dynasty/${id}/`, data),
  delete: (id) => api.delete(`/architecture/dynasty/${id}/`),
}

// ========== 地域 API (完整CRUD) ==========
export const regionApi = {
  getAll: () => api.get('/architecture/region/'),
  getById: (id) => api.get(`/architecture/region/${id}/`),
  create: (data) => api.post('/architecture/region/', data),
  update: (id, data) => api.put(`/architecture/region/${id}/`, data),
  delete: (id) => api.delete(`/architecture/region/${id}/`),
}

// ========== 省份统计 API ==========
export const provinceApi = {
  getStats: () => api.get('/architecture/province_stats/'),
}

// ========== 结构类型 API (完整CRUD) ==========
export const structureTypeApi = {
  getAll: () => api.get('/architecture/structure_type/'),
  getById: (id) => api.get(`/architecture/structure_type/${id}/`),
  create: (data) => api.post('/architecture/structure_type/', data),
  update: (id, data) => api.put(`/architecture/structure_type/${id}/`, data),
  delete: (id) => api.delete(`/architecture/structure_type/${id}/`),
}

// ========== 建筑元素 API (完整CRUD) ==========
export const elementApi = {
  getAll: (params) => api.get('/architecture/elements/', { params }),
  getById: (eid) => api.get(`/architecture/elements/${eid}/`),
  create: (data) => api.post('/architecture/elements/', data),
  update: (eid, data) => api.put(`/architecture/elements/${eid}/`, data),
  delete: (eid) => api.delete(`/architecture/elements/${eid}/`),
}

// ========== 文献资料 API (完整CRUD) ==========
export const literatureApi = {
  getAll: (params) => api.get('/architecture/literatures/', { params }),
  getById: (lid) => api.get(`/architecture/literatures/${lid}/`),
  create: (data) => api.post('/architecture/literatures/', data),
  update: (lid, data) => api.put(`/architecture/literatures/${lid}/`, data),
  delete: (lid) => api.delete(`/architecture/literatures/${lid}/`),
}

// ========== 用户 API ==========
export const userApi = {
  login: (data) => api.post('/architecture/login/', data),
  register: (data) => api.post('/architecture/register/', data),
}

export default api
