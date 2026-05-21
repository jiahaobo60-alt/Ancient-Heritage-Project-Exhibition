<template>
  <div class="element-list">
    <el-card>
      <template #header>
        <div class="card-header">
          <span>建筑元素管理</span>
          <el-button type="primary" @click="handleCreate">
            <el-icon><Plus /></el-icon> 新增元素
          </el-button>
        </div>
      </template>
      
      <el-table :data="tableData" border stripe v-loading="loading">
        <el-table-column prop="eid" label="ID" width="80" />
        <el-table-column prop="ename" label="元素名称" min-width="150" />
        <el-table-column prop="category" label="类别" width="120" />
        <el-table-column prop="explanation" label="解释" min-width="300" show-overflow-tooltip />
        <el-table-column label="操作" width="180" fixed="right">
          <template #default="{ row }">
            <el-button size="small" type="primary" @click="handleEdit(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="700px" @close="resetForm">
      <el-form :model="formData" label-width="100px">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="元素名称" required>
              <el-input v-model="formData.ename" placeholder="如：七铺作斗拱" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="类别" required>
              <el-select v-model="formData.category" placeholder="选择类别" style="width: 100%">
                <el-option label="斗拱" value="斗拱" />
                <el-option label="屋顶" value="屋顶" />
                <el-option label="柱式" value="柱式" />
                <el-option label="装饰" value="装饰" />
                <el-option label="结构" value="结构" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="原文引用">
          <el-input v-model="formData.original_text" type="textarea" :rows="2" placeholder="梁思成《中国建筑史》原文引用" />
        </el-form-item>
        <el-form-item label="详细解释" required>
          <el-input v-model="formData.explanation" type="textarea" :rows="3" placeholder="请输入详细解释" />
        </el-form-item>
        <el-form-item label="结构说明">
          <el-input v-model="formData.structure_description" type="textarea" :rows="2" placeholder="请输入结构说明" />
        </el-form-item>
        <el-form-item label="功能说明">
          <el-input v-model="formData.function_description" type="textarea" :rows="2" placeholder="请输入功能说明" />
        </el-form-item>
        <el-form-item label="演变历史">
          <el-input v-model="formData.evolution" type="textarea" :rows="2" placeholder="请输入演变历史" />
        </el-form-item>
        <el-form-item label="示意图URL">
          <el-input v-model="formData.image_url" placeholder="请输入图片URL" />
        </el-form-item>
        <el-form-item label="结构图URL">
          <el-input v-model="formData.diagram_url" placeholder="请输入结构图URL" />
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
import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { elementApi } from '@/api'

const loading = ref(false)
const saving = ref(false)
const tableData = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)

const formData = reactive({
  ename: '',
  category: '',
  original_text: '',
  explanation: '',
  structure_description: '',
  function_description: '',
  evolution: '',
  image_url: '',
  diagram_url: ''
})

const dialogTitle = computed(() => isEdit.value ? '编辑元素' : '新增元素')

onMounted(() => fetchData())

async function fetchData() {
  loading.value = true
  try {
    const res = await elementApi.getAll({})
    tableData.value = res.results || []
  } catch (e) {
    ElMessage.error('加载失败')
  } finally {
    loading.value = false
  }
}

function handleCreate() {
  isEdit.value = false
  resetForm()
  dialogVisible.value = true
}

function handleEdit(row) {
  isEdit.value = true
  Object.assign(formData, row)
  dialogVisible.value = true
}

function resetForm() {
  Object.assign(formData, {
    ename: '', category: '', original_text: '', explanation: '',
    structure_description: '', function_description: '', evolution: '',
    image_url: '', diagram_url: ''
  })
}

async function handleSave() {
  if (!formData.ename || !formData.category || !formData.explanation) {
    ElMessage.warning('请填写必填项')
    return
  }
  saving.value = true
  try {
    if (isEdit.value) {
      await elementApi.update(formData.eid, formData)
      ElMessage.success('更新成功')
    } else {
      await elementApi.create(formData)
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
    await ElMessageBox.confirm(`确定删除「${row.ename}」吗？`, '删除确认', { type: 'warning' })
    await elementApi.delete(row.eid)
    ElMessage.success('删除成功')
    fetchData()
  } catch (e) {
    if (e !== 'cancel') ElMessage.error('删除失败')
  }
}
</script>

<style scoped>
.element-list { padding: 20px; }
.card-header { display: flex; justify-content: space-between; align-items: center; }
</style>
