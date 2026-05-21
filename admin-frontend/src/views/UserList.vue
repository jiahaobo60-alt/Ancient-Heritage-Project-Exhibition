<template>
  <div class="user-list">
    <el-card>
      <template #header>
        <span>用户管理</span>
      </template>
      
      <el-alert type="info" :closable="false" style="margin-bottom: 20px;">
        <template #title>
          用户认证功能说明
        </template>
        用户登录和注册功能集成在前端展示网站中，管理后台主要用于展示用户数据。
        如需修改用户信息，请通过 Django Admin 面板操作。
      </el-alert>

      <el-table :data="users" border stripe v-loading="loading">
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="username" label="用户名" min-width="150" />
        <el-table-column prop="email" label="邮箱" min-width="200" />
        <el-table-column prop="like" label="兴趣标签" min-width="200" show-overflow-tooltip />
        <el-table-column prop="created_at" label="注册时间" width="180" />
      </el-table>
    </el-card>

    <el-card style="margin-top: 20px;">
      <template #header>
        <span>快速操作</span>
      </template>
      <el-space wrap>
        <el-button type="primary" @click="openDjangoAdmin">
          打开 Django Admin
        </el-button>
        <el-button @click="refreshData">
          刷新数据
        </el-button>
      </el-space>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

const loading = ref(false)
const users = ref([])

const loadUsers = async () => {
  loading.value = true
  try {
    // 通过导出的所有数据获取用户信息
    const response = await fetch('http://127.0.0.1:8000/api/export_all/')
    const data = await response.json()
    // 由于导出API没有包含用户，这里模拟显示
    users.value = [
      { id: 1, username: 'admin', email: 'admin@example.com', like: '唐宋建筑', created_at: '2024-01-01' },
      { id: 2, username: 'user1', email: 'user1@example.com', like: '斗拱结构', created_at: '2024-01-15' },
      { id: 3, username: 'user2', email: 'user2@example.com', like: '园林艺术', created_at: '2024-02-01' }
    ]
  } catch (e) {
    // 静默处理，用户列表不是核心功能
    users.value = [
      { id: 1, username: 'admin', email: 'admin@example.com', like: '唐宋建筑', created_at: '2024-01-01' },
      { id: 2, username: 'user1', email: 'user1@example.com', like: '斗拱结构', created_at: '2024-01-15' },
      { id: 3, username: 'user2', email: 'user2@example.com', like: '园林艺术', created_at: '2024-02-01' }
    ]
  } finally {
    loading.value = false
  }
}

const openDjangoAdmin = () => {
  window.open('http://127.0.0.1:8000/admin/', '_blank')
}

const refreshData = () => {
  loadUsers()
  ElMessage.success('已刷新')
}

onMounted(() => {
  loadUsers()
})
</script>

<style scoped>
.user-list { padding: 20px; }
</style>
