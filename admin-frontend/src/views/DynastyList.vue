<template>
  <div class="dynasty-list">
    <el-card>
      <template #header>
        <div class="card-header">
          <span>朝代管理</span>
          <el-button type="primary" @click="handleCreate">
            <el-icon><Plus /></el-icon> 新增朝代
          </el-button>
        </div>
      </template>
      
      <el-table :data="tableData" border stripe v-loading="loading">
        <el-table-column prop="did" label="ID" width="100" />
        <el-table-column prop="dname" label="朝代名称" min-width="150" />
        <el-table-column prop="period" label="时期" min-width="200" />
        <el-table-column prop="description" label="简介" min-width="300" show-overflow-tooltip />
        <el-table-column label="操作" width="180" fixed="right">
          <template #default="{ row }">
            <el-button size="small" type="primary" @click="handleEdit(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="500px">
      <el-form :model="formData" label-width="100px">
        <el-form-item label="朝代名称" required>
          <el-input v-model="formData.dname" placeholder="请输入朝代名称" />
        </el-form-item>
        <el-form-item label="时期">
          <el-input v-model="formData.period" placeholder="如：公元前206年-公元220年" />
        </el-form-item>
        <el-form-item label="简介">
          <el-input v-model="formData.description" type="textarea" :rows="4" placeholder="请输入朝代简介" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSave" :loading="saving">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { dynastyApi } from '@/api'

const loading = ref(false)
const saving = ref(false)
const tableData = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)

const formData = reactive({
  dname: '',
  period: '',
  description: ''
})

const dialogTitle = computed(() => isEdit.value ? '编辑朝代' : '新增朝代')

import { computed } from 'vue'

onMounted(() => fetchData())

async function fetchData() {
  loading.value = true
  try {
    const res = await dynastyApi.getAll()
    tableData.value = res.results || []
  } catch (e) {
    ElMessage.error('加载失败')
  } finally {
    loading.value = false
  }
}

function handleCreate() {
  isEdit.value = false
  Object.assign(formData, { dname: '', period: '', description: '' })
  dialogVisible.value = true
}

function handleEdit(row) {
  isEdit.value = true
  Object.assign(formData, row)
  dialogVisible.value = true
}

async function handleSave() {
  if (!formData.dname) {
    ElMessage.warning('请输入朝代名称')
    return
  }
  saving.value = true
  try {
    if (isEdit.value) {
      await dynastyApi.update(formData.did, formData)
      ElMessage.success('更新成功')
    } else {
      await dynastyApi.create(formData)
      ElMessage.success('创建成功')
    }
    dialogVisible.value = false
    fetchData()
  } catch (e) {
    ElMessage.error('操作失败')
  } finally {
    saving.value = false
  }
}

async function handleDelete(row) {
  try {
    await ElMessageBox.confirm(`确定删除「${row.dname}」吗？`, '删除确认', { type: 'warning' })
    await dynastyApi.delete(row.did)
    ElMessage.success('删除成功')
    fetchData()
  } catch (e) {
    if (e !== 'cancel') ElMessage.error('删除失败')
  }
}
</script>

<style scoped>
.dynasty-list { padding: 20px; }
.card-header { display: flex; justify-content: space-between; align-items: center; }
</style>
