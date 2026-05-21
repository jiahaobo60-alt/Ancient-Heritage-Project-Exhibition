<template>
  <div class="dashboard">
    <el-row :gutter="20" class="stats-row">
      <el-col :span="6">
        <el-card class="stat-card">
          <div class="stat-icon" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <el-icon><OfficeBuilding /></el-icon>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ stats.total_buildings }}</div>
            <div class="stat-label">古建筑总数</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <div class="stat-icon" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <el-icon><Calendar /></el-icon>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ stats.total_dynasties }}</div>
            <div class="stat-label">历史朝代</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <div class="stat-icon" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <el-icon><Location /></el-icon>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ stats.total_regions }}</div>
            <div class="stat-label">地理区域</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <div class="stat-icon" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <el-icon><Collection /></el-icon>
          </div>
          <div class="stat-info">
            <div class="stat-value">{{ stats.total_elements }}</div>
            <div class="stat-label">建筑元素</div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="charts-row">
      <el-col :span="12">
        <el-card>
          <template #header>
            <span>朝代分布</span>
          </template>
          <div ref="dynastyChart" style="height: 300px;"></div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card>
          <template #header>
            <span>屋顶形式分布</span>
          </template>
          <div ref="roofChart" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="charts-row">
      <el-col :span="12">
        <el-card>
          <template #header>
            <span>地域分布</span>
          </template>
          <div ref="regionChart" style="height: 300px;"></div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card>
          <template #header>
            <span>建筑分布地图</span>
          </template>
          <div ref="mapChart" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue'
import * as echarts from 'echarts'
import { dashboardApi } from '@/api'
import { OfficeBuilding, Calendar, Location, Collection } from '@element-plus/icons-vue'

const stats = reactive({
  total_buildings: 0,
  total_dynasties: 0,
  total_regions: 0,
  total_elements: 0
})

const dynastyChart = ref(null)
const roofChart = ref(null)
const regionChart = ref(null)
const mapChart = ref(null)

const loadStats = async () => {
  try {
    const res = await dashboardApi.getStats()
    stats.total_buildings = res.total_buildings || 0
    stats.total_dynasties = res.total_dynasties || 0
    stats.total_regions = res.total_regions || 0
    stats.total_elements = res.total_elements || 0
    
    // 渲染图表
    renderDynastyChart(res.dynasty_data || [])
    renderRoofChart(res.roof_data || [])
    renderRegionChart(res.region_data || [])
    renderMapChart(res.scatter_data || [])
  } catch (error) {
    console.error('加载统计数据失败:', error)
  }
}

const renderDynastyChart = (data) => {
  if (!dynastyChart.value) return
  const chart = echarts.init(dynastyChart.value)
  chart.setOption({
    tooltip: { trigger: 'item' },
    legend: { bottom: 0 },
    series: [{
      type: 'pie',
      radius: ['40%', '70%'],
      data: data.map((item, index) => ({
        name: item.name,
        value: item.value
      })),
      emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' } }
    }]
  })
}

const renderRoofChart = (data) => {
  if (!roofChart.value) return
  const chart = echarts.init(roofChart.value)
  chart.setOption({
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: data.map(d => d.name), axisLabel: { rotate: 30 } },
    yAxis: { type: 'value' },
    series: [{ type: 'bar', data: data.map(d => d.value), itemStyle: { color: '#5470c6' } }]
  })
}

const renderRegionChart = (data) => {
  if (!regionChart.value) return
  const chart = echarts.init(regionChart.value)
  chart.setOption({
    tooltip: { trigger: 'item' },
    series: [{
      type: 'pie',
      radius: ['40%', '70%'],
      data: data.slice(0, 10).map(item => ({ name: item.name, value: item.value }))
    }]
  })
}

const renderMapChart = (data) => {
  if (!mapChart.value) return
  const chart = echarts.init(mapChart.value)
  
  // 使用简单散点图代替地图（中国地图需要额外加载地图数据）
  chart.setOption({
    tooltip: { trigger: 'item', formatter: (p) => `${p.data.name}<br/>朝代: ${p.data.dynasty}` },
    geo: {
      map: 'china',
      roam: true,
      label: { show: false },
      itemStyle: { areaColor: '#e0e7ff', borderColor: '#c7d2fe' },
      emphasis: { label: { show: true }, itemStyle: { areaColor: '#a5b4fc' } }
    },
    series: [{
      type: 'scatter',
      coordinateSystem: 'geo',
      data: data.map(d => ({ name: d.bname, value: [d.lon, d.lat], dynasty: d.dynasty }))
    }]
  })
}

onMounted(() => {
  loadStats()
})
</script>

<style scoped>
.dashboard { padding: 20px; }
.stats-row { margin-bottom: 20px; }
.charts-row { margin-bottom: 20px; }
.stat-card { display: flex; align-items: center; padding: 20px; }
.stat-icon { width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 20px; }
.stat-icon .el-icon { font-size: 28px; color: white; }
.stat-value { font-size: 28px; font-weight: bold; color: #303133; }
.stat-label { font-size: 14px; color: #909399; margin-top: 4px; }
</style>
