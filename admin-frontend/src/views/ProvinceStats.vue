<template>
  <div class="province-container">
    <!-- 顶部标题 -->
    <div class="page-header">
      <h2>省份古建筑统计</h2>
      <p class="subtitle">全国各省份古建筑数量分布</p>
    </div>

    <!-- TOP10卡片 -->
    <el-row :gutter="20" class="top-section">
      <el-col :span="24">
        <el-card class="top-card">
          <template #header>
            <div class="card-header">
              <span class="title">🏆 TOP 10 省份古建筑数量</span>
            </div>
          </template>
          <div class="top10-grid">
            <div v-for="(item, index) in top10List" :key="index" class="top-item" :class="'rank-' + (index + 1)">
              <div class="rank-badge">{{ index + 1 }}</div>
              <div class="province-name">{{ item.pname }}</div>
              <div class="building-count">{{ item.count }} 处</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 完整列表 -->
    <el-row :gutter="20">
      <el-col :span="24">
        <el-card class="list-card">
          <template #header>
            <div class="card-header">
              <span class="title">📊 完整省份统计数据</span>
              <span class="total">共 {{ provinceList.length }} 个省份</span>
            </div>
          </template>
          
          <el-table :data="provinceList" stripe style="width: 100%">
            <el-table-column prop="pid" label="编号" width="100" />
            <el-table-column prop="pname" label="省份" width="150">
              <template #default="{ row }">
                <span class="province-tag">{{ row.pname }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="count" label="古建筑数量">
              <template #default="{ row }">
                <div class="count-bar">
                  <div class="bar-fill" :style="{ width: (row.count / maxCount * 100) + '%' }"></div>
                  <span class="bar-text">{{ row.count }} 处</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="占比" width="120">
              <template #default="{ row }">
                {{ ((row.count / totalCount) * 100).toFixed(1) }}%
              </template>
            </el-table-column>
            <el-table-column label="排名" width="80">
              <template #default="{ row }">
                <el-tag :type="getRankType(row)" size="small">{{ getRank(row) }}</el-tag>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { provinceApi } from '@/api'
import { ElMessage } from 'element-plus'

const provinceList = ref([])

const top10List = computed(() => provinceList.value.slice(0, 10))
const maxCount = computed(() => Math.max(...provinceList.value.map(p => p.count), 1))
const totalCount = computed(() => provinceList.value.reduce((sum, p) => sum + p.count, 0))

const getRank = (row) => {
  const index = provinceList.value.findIndex(p => p.pid === row.pid)
  return index + 1
}

const getRankType = (row) => {
  const rank = getRank(row)
  if (rank === 1) return 'danger'
  if (rank <= 3) return 'warning'
  if (rank <= 10) return 'success'
  return 'info'
}

const fetchProvinceStats = async () => {
  try {
    const res = await provinceApi.getStats()
    provinceList.value = res.results || []
  } catch (error) {
    ElMessage.error('获取省份数据失败')
    console.error(error)
  }
}

onMounted(() => {
  fetchProvinceStats()
})
</script>

<style scoped>
.province-container {
  padding: 20px;
}

.page-header {
  margin-bottom: 24px;
}

.page-header h2 {
  margin: 0 0 8px 0;
  font-size: 24px;
  color: #333;
}

.subtitle {
  margin: 0;
  color: #666;
  font-size: 14px;
}

.top-section {
  margin-bottom: 20px;
}

.top-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.top-card :deep(.el-card__header) {
  background: rgba(255,255,255,0.1);
  border-color: rgba(255,255,255,0.2);
}

.top-card :deep(.el-card__body) {
  padding: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header .title {
  font-size: 16px;
  font-weight: 600;
}

.card-header .total {
  font-size: 14px;
  color: #666;
}

.top10-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 15px;
}

.top-item {
  background: rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 20px 15px;
  text-align: center;
  transition: all 0.3s;
  position: relative;
}

.top-item:hover {
  background: rgba(255,255,255,0.25);
  transform: translateY(-5px);
}

.rank-badge {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #ffd700;
  color: #333;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

.rank-1 .rank-badge { background: linear-gradient(135deg, #ffd700, #ff8c00); }
.rank-2 .rank-badge { background: linear-gradient(135deg, #c0c0c0, #808080); }
.rank-3 .rank-badge { background: linear-gradient(135deg, #cd7f32, #8b4513); }

.province-name {
  font-size: 16px;
  font-weight: 600;
  margin: 10px 0 5px;
}

.building-count {
  font-size: 20px;
  font-weight: bold;
  color: #ffd700;
}

.list-card {
  margin-top: 20px;
}

.province-tag {
  font-weight: 600;
  color: #409eff;
}

.count-bar {
  position: relative;
  height: 24px;
  background: #f0f0f0;
  border-radius: 12px;
  overflow: hidden;
}

.bar-fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: linear-gradient(90deg, #409eff, #67c23a);
  border-radius: 12px;
  transition: width 0.5s ease;
}

.bar-text {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 12px;
  font-weight: 600;
  color: #333;
}
</style>
