<template>
  <div class="building-list">
    <el-card>
      <template #header>
        <div class="header-actions">
          <span>古建筑管理</span>
          <el-button type="primary" @click="openCreateDialog">
            <el-icon><Plus /></el-icon> 新增建筑
          </el-button>
        </div>
      </template>

      <!-- 筛选表单 -->
      <el-form :inline="true" class="filter-form">
        <el-form-item label="建筑名称">
          <el-input v-model="filters.search" placeholder="搜索建筑名称" clearable @clear="loadBuildings" @keyup.enter="loadBuildings" />
        </el-form-item>
        <el-form-item label="朝代">
          <el-select v-model="filters.dynasty" placeholder="选择朝代" clearable @change="loadBuildings">
            <el-option v-for="d in dynasties" :key="d.did" :label="d.dname" :value="d.did" />
          </el-select>
        </el-form-item>
        <el-form-item label="地域">
          <el-select v-model="filters.region" placeholder="选择地域" clearable @change="loadBuildings">
            <el-option v-for="r in regions" :key="r.rid" :label="r.rname" :value="r.rid" />
          </el-select>
        </el-form-item>
        <el-form-item label="类型">
          <el-select v-model="filters.type" placeholder="选择类型" clearable @change="loadBuildings">
            <el-option v-for="t in structureTypes" :key="t.tid" :label="t.tname" :value="t.tid" />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="loadBuildings">查询</el-button>
          <el-button @click="resetFilters">重置</el-button>
        </el-form-item>
      </el-form>

      <!-- 数据表格 -->
      <el-table :data="buildings" v-loading="loading" stripe border>
        <el-table-column prop="bid" label="ID" width="80" />
        <el-table-column prop="bname" label="建筑名称" min-width="150" />
        <el-table-column prop="dynasty_name" label="朝代" width="100" />
        <el-table-column prop="region_name" label="地域" width="100" />
        <el-table-column prop="structure_type_name" label="结构类型" width="120" />
        <el-table-column prop="roof_type" label="屋顶形式" width="120" />
        <el-table-column prop="address" label="地址" min-width="150" show-overflow-tooltip />
        <el-table-column label="操作" width="180" fixed="right">
          <template #default="{ row }">
            <el-button size="small" type="primary" @click="openEditDialog(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页 -->
      <div class="pagination-wrapper">
        <el-pagination
          v-model:current-page="pagination.page"
          :page-size="pagination.size"
          :total="pagination.total"
          layout="total, prev, pager, next"
          @current-change="loadBuildings"
        />
      </div>
    </el-card>

    <!-- 创建/编辑弹窗 -->
    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="800px" @close="resetForm">
      <el-form :model="form" :rules="rules" ref="formRef" label-width="100px">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="建筑名称" prop="bname">
              <el-input v-model="form.bname" placeholder="请输入建筑名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="所属朝代" prop="dynasty_id">
              <el-select v-model="form.dynasty_id" placeholder="选择朝代" style="width: 100%">
                <el-option v-for="d in dynasties" :key="d.did" :label="d.dname" :value="d.did" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="所属地域" prop="region_id">
              <el-select v-model="form.region_id" placeholder="选择地域" style="width: 100%">
                <el-option v-for="r in regions" :key="r.rid" :label="r.rname" :value="r.rid" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="结构类型" prop="structure_type_id">
              <el-select v-model="form.structure_type_id" placeholder="选择类型" style="width: 100%">
                <el-option v-for="t in structureTypes" :key="t.tid" :label="t.tname" :value="t.tid" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="屋顶形式">
              <el-input v-model="form.roof_type" placeholder="如：庑殿顶、歇山顶" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="斗拱样式">
              <el-input v-model="form.dougong_style" placeholder="如：七铺作" />
            </el-form-item>
          </el-col>
        </el-row>
        
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="经度">
              <el-input-number v-model="form.longitude" :precision="6" :step="0.1" style="width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="纬度">
              <el-input-number v-model="form.latitude" :precision="6" :step="0.1" style="width: 100%" />
            </el-form-item>
          </el-col>
        </el-row>
        
        <el-form-item label="详细地址">
          <el-input v-model="form.address" placeholder="请输入详细地址" />
        </el-form-item>
        
        <el-form-item label="图片URL">
          <el-input v-model="form.image_url" placeholder="请输入图片URL" />
        </el-form-item>
        
        <el-form-item label="建筑简介">
          <el-input v-model="form.introduction" type="textarea" :rows="3" placeholder="请输入建筑简介" />
        </el-form-item>
        
        <el-form-item label="历史价值">
          <el-input v-model="form.historical_value" type="textarea" :rows="2" placeholder="请输入历史价值" />
        </el-form-item>
        
        <el-form-item label="建筑特色">
          <el-input v-model="form.architectural_features" type="textarea" :rows="2" placeholder="请输入建筑特色" />
        </el-form-item>
        
        <el-form-item label="梁思成评价">
          <el-input v-model="form.liang_sicheng_note" type="textarea" :rows="2" placeholder="请输入梁思成先生对该建筑的评述" />
        </el-form-item>
      </el-form>
      
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit" :loading="submitting">
          {{ isEdit ? '更新' : '创建' }}
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { buildingApi, dynastyApi, regionApi, structureTypeApi } from '@/api'

const buildings = ref([])
const dynasties = ref([])
const regions = ref([])
const structureTypes = ref([])
const loading = ref(false)
const submitting = ref(false)

const filters = reactive({ search: '', dynasty: null, region: null, type: null })
const pagination = reactive({ page: 1, size: 20, total: 0 })

const dialogVisible = ref(false)
const isEdit = ref(false)
const editingId = ref(null)
const formRef = ref(null)

const form = reactive({
  bname: '',
  dynasty_id: null,
  region_id: null,
  structure_type_id: null,
  roof_type: '',
  dougong_style: '',
  longitude: 0,
  latitude: 0,
  address: '',
  image_url: '',
  introduction: '',
  historical_value: '',
  architectural_features: '',
  liang_sicheng_note: ''
})

const rules = {
  bname: [{ required: true, message: '请输入建筑名称', trigger: 'blur' }],
  dynasty_id: [{ required: true, message: '请选择朝代', trigger: 'change' }],
  region_id: [{ required: true, message: '请选择地域', trigger: 'change' }],
  structure_type_id: [{ required: true, message: '请选择结构类型', trigger: 'change' }]
}

const dialogTitle = computed(() => isEdit.value ? '编辑建筑' : '新增建筑')

const loadBuildings = async () => {
  loading.value = true
  try {
    const params = {
      page: pagination.page,
      search: filters.search || undefined,
      dynasty: filters.dynasty || undefined,
      region: filters.region || undefined,
      type: filters.type || undefined
    }
    const res = await buildingApi.getAll(params)
    buildings.value = res.results || []
    pagination.total = res.total || 0
  } catch (error) {
    ElMessage.error('加载数据失败')
  } finally {
    loading.value = false
  }
}

const loadOptions = async () => {
  try {
    const [dynastyRes, regionRes, typeRes] = await Promise.all([
      dynastyApi.getAll(),
      regionApi.getAll(),
      structureTypeApi.getAll()
    ])
    dynasties.value = dynastyRes.results || []
    regions.value = regionRes.results || []
    structureTypes.value = typeRes.results || []
  } catch (error) {
    console.error('加载选项失败:', error)
  }
}

const resetFilters = () => {
  filters.search = ''
  filters.dynasty = null
  filters.region = null
  filters.type = null
  pagination.page = 1
  loadBuildings()
}

const openCreateDialog = () => {
  isEdit.value = false
  editingId.value = null
  resetForm()
  dialogVisible.value = true
}

const openEditDialog = (row) => {
  isEdit.value = true
  editingId.value = row.bid
  Object.assign(form, {
    bname: row.bname,
    dynasty_id: row.dynasty_id,
    region_id: row.region_id,
    structure_type_id: row.structure_type_id,
    roof_type: row.roof_type || '',
    dougong_style: row.dougong_style || '',
    longitude: row.longitude || 0,
    latitude: row.latitude || 0,
    address: row.address || '',
    image_url: row.image_url || '',
    introduction: row.introduction || '',
    historical_value: row.historical_value || '',
    architectural_features: row.architectural_features || '',
    liang_sicheng_note: row.liang_sicheng_note || ''
  })
  dialogVisible.value = true
}

const resetForm = () => {
  Object.assign(form, {
    bname: '', dynasty_id: null, region_id: null, structure_type_id: null,
    roof_type: '', dougong_style: '', longitude: 0, latitude: 0,
    address: '', image_url: '', introduction: '', historical_value: '',
    architectural_features: '', liang_sicheng_note: ''
  })
  formRef.value?.resetFields()
}

const handleSubmit = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return
  
  submitting.value = true
  try {
    if (isEdit.value) {
      await buildingApi.update(editingId.value, form)
      ElMessage.success('更新成功')
    } else {
      await buildingApi.create(form)
      ElMessage.success('创建成功')
    }
    dialogVisible.value = false
    loadBuildings()
  } catch (error) {
    ElMessage.error(error.message || '操作失败')
  } finally {
    submitting.value = false
  }
}

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm(`确定删除「${row.bname}」吗？`, '删除确认', {
      type: 'warning'
    })
    await buildingApi.delete(row.bid)
    ElMessage.success('删除成功')
    loadBuildings()
  } catch (error) {
    if (error !== 'cancel') ElMessage.error('删除失败')
  }
}

onMounted(() => {
  loadBuildings()
  loadOptions()
})
</script>

<style scoped>
.building-list { padding: 20px; }
.header-actions { display: flex; justify-content: space-between; align-items: center; }
.filter-form { margin-bottom: 20px; }
.pagination-wrapper { margin-top: 20px; display: flex; justify-content: flex-end; }
</style>
