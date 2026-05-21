# 营造中华 - Vue 管理后台

基于 Vue 3 + Element Plus + Vite 构建的古建筑数据管理后台。

## 项目结构

```
admin-frontend/
├── src/
│   ├── api/              # API 调用模块
│   │   └── index.js      # 古建筑、朝代、地域等 API
│   ├── router/           # 路由配置
│   │   └── index.js
│   ├── views/            # 页面组件
│   │   ├── Dashboard.vue      # 数据统计仪表盘
│   │   ├── BuildingList.vue   # 古建筑管理
│   │   ├── DynastyList.vue    # 朝代管理
│   │   ├── RegionList.vue    # 地域管理
│   │   ├── ElementList.vue   # 建筑元素
│   │   ├── LiteratureList.vue # 文献资料
│   │   └── UserList.vue      # 用户管理
│   ├── App.vue           # 主布局
│   └── main.js           # 入口文件
├── vite.config.js        # Vite 配置
└── package.json
```

## 快速启动

### 1. 启动后端 Django 服务

```bash
cd backend
python manage.py runserver 8000
```

### 2. 启动前端管理后台

```bash
cd admin-frontend
npm install
npm run dev
```

### 3. 访问

- **管理后台**: http://localhost:9527
- **后端API**: http://localhost:8000/api/

## 功能模块

| 模块 | 路径 | 功能 |
|------|------|------|
| 数据统计 | `/dashboard` | 建筑数量、朝代分布、屋顶形式、地图散点 |
| 古建筑管理 | `/buildings` | 增删改查、筛选、编辑弹窗 |
| 朝代管理 | `/dynasties` | 朝代数据维护 |
| 地域管理 | `/regions` | 地域数据维护 |
| 建筑元素 | `/elements` | 斗拱、屋顶等知识库 |
| 文献资料 | `/literatures` | 古建筑文献管理 |
| 用户管理 | `/users` | 用户数据（开发中）|

## API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/buildings/` | GET | 获取建筑列表 |
| `/api/dynasty/` | GET | 获取朝代列表 |
| `/api/region/` | GET | 获取地域列表 |
| `/api/structure_type/` | GET | 获取结构类型 |
| `/api/charts_data/` | GET | 获取图表数据 |
| `/api/elements/` | GET | 获取建筑元素 |

## 技术栈

- **Vue 3** - 渐进式 JavaScript 框架
- **Vite** - 下一代前端构建工具
- **Element Plus** - 基于 Vue 3 的组件库
- **Axios** - HTTP 请求库
- **ECharts** - 数据可视化图表
- **Vue Router** - Vue 路由管理
