<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
    <el-aside width="220px" class="sidebar">
      <div class="logo">
        <el-icon :size="24"><OfficeBuilding /></el-icon>
        <span>营造中华管理后台</span>
      </div>
      <el-menu
        :default-active="$route.path"
        router
        background-color="#304156"
        text-color="#bfcbd9"
        active-text-color="#409EFF"
      >
        <el-menu-item index="/dashboard">
          <el-icon><DataAnalysis /></el-icon>
          <span>数据统计</span>
        </el-menu-item>
        <el-menu-item index="/buildings">
          <el-icon><OfficeBuilding /></el-icon>
          <span>古建筑管理</span>
        </el-menu-item>
        <el-menu-item index="/dynasties">
          <el-icon><Calendar /></el-icon>
          <span>朝代管理</span>
        </el-menu-item>
        <el-menu-item index="/regions">
          <el-icon><Location /></el-icon>
          <span>地域管理</span>
        </el-menu-item>
        <el-menu-item index="/provinces">
          <el-icon><PieChart /></el-icon>
          <span>省份统计</span>
        </el-menu-item>
        <el-menu-item index="/elements">
          <el-icon><Grid /></el-icon>
          <span>建筑元素</span>
        </el-menu-item>
        <el-menu-item index="/literatures">
          <el-icon><Document /></el-icon>
          <span>文献资料</span>
        </el-menu-item>
        <el-menu-item index="/users">
          <el-icon><User /></el-icon>
          <span>用户管理</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <!-- 顶部导航 -->
      <el-header class="header">
        <div class="header-left">
          <span class="page-title">{{ pageTitle }}</span>
        </div>
        <div class="header-right">
          <el-dropdown>
            <span class="user-info">
              <el-icon><UserFilled /></el-icon>
              管理员
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人中心</el-dropdown-item>
                <el-dropdown-item divided>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 主内容区 -->
      <el-main class="main-content">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const pageTitle = computed(() => {
  const titles = {
    '/dashboard': '数据统计',
    '/buildings': '古建筑管理',
    '/dynasties': '朝代管理',
    '/regions': '地域管理',
    '/provinces': '省份统计',
    '/elements': '建筑元素',
    '/literatures': '文献资料',
    '/users': '用户管理',
  }
  return titles[route.path] || '管理后台'
})
</script>

<style scoped>
.layout-container {
  height: 100vh;
}

.sidebar {
  background-color: #304156;
  overflow-x: hidden;
}

.logo {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 20px;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  border-bottom: 1px solid #3d4a5c;
}

.logo span {
  margin-left: 10px;
}

.header {
  background: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
}

.header-left {
  font-size: 18px;
  font-weight: 500;
}

.user-info {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: #606266;
}

.user-info:hover {
  color: #409EFF;
}

.main-content {
  background-color: #f0f2f5;
  padding: 20px;
}
</style>
