<template>
  <div class="literature-list">
    <el-card>
      <template #header>
        <div class="card-header">
          <span>文献资料管理</span>
          <el-button type="primary" @click="handleCreate">
            <el-icon><Plus /></el-icon> 新增文献
          </el-button>
        </div>
      </template>
      
      <el-table :data="tableData" border stripe v-loading="loading">
        <el-table-column prop="lid" label="ID" width="80" />
        <el-table-column prop="lname" label="文献名称" min-width="200" />
        <el-table-column prop="author" label="作者" width="120" />
        <el-table-column prop="dynasty" label="朝代" width="100" />
        <el-table-column prop="literature_type_display" label="类型" width="100" />
        <el-table-column prop="summary" label="摘要" min-width="200" show-overflow-tooltip />
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
            <el-form-item label="文献名称" required>
              <el-input v-model="formData.lname" placeholder="请输入文献名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="作者" required>
              <el-input v-model="formData.author" placeholder="请输入作者" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="朝代/时期">
              <el-input v-model="formData.dynasty" placeholder="如：唐代、民国" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="出版年份">
              <el-input-number v-model="formData.publish_year" :min="0" style="width: 100%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="文献类型">
              <el-select v-model="formData.literature_type" style="width: 100%">
                <el-option label="古代典籍" value="ancient" />
                <el-option label="现代著作" value="modern" />
                <el-option label="调查报告" value="survey" />
                <el-option label="教材" value="textbook" />
                <el-option label="文集" value="collection" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="出版社">
              <el-input v-model="formData.publisher" placeholder="请输入出版社" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="内容摘要" required>
          <el-input v-model="formData.summary" type="textarea" :rows="3" placeholder="请输入内容摘要" />
        </el-form-item>
        <el-form-item label="核心观点">
          <el-input v-model="formData.key_points" type="textarea" :rows="2" placeholder="请输入核心观点" />
        </el-form-item>
        <el-form-item label="学术贡献">
          <el-input v-model="formData.contributions" type="textarea" :rows="2" placeholder="请输入学术贡献" />
        </el-form-item>
        <el-form-item label="封面图片">
          <el-input v-model="formData.cover_image" placeholder="请输入封面图片URL" />
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
import { literatureApi } from '@/api'

const loading = ref(false)
const saving = ref(false)
const tableData = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)

const formData = reactive({
  lname: '',
  author: '',
  dynasty: '',
  publish_year: null,
  literature_type: 'modern',
  summary: '',
  key_points: '',
  contributions: '',
  publisher: '',
  edition: '',
  pages: null,
  cover_image: '',
  pdf_url: ''
})

const dialogTitle = computed(() => isEdit.value ? '编辑文献' : '新增文献')

onMounted(() => fetchData())

async function fetchData() {
  loading.value = true
  try {
    const res = await literatureApi.getAll({})
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
    lname: '', author: '', dynasty: '', publish_year: null,
    literature_type: 'modern', summary: '', key_points: '',
    contributions: '', publisher: '', edition: '', pages: null,
    cover_image: '', pdf_url: ''
  })
}

async function handleSave() {
  if (!formData.lname || !formData.author || !formData.summary) {
    ElMessage.warning('请填写必填项')
    return
  }
  saving.value = true
  try {
    if (isEdit.value) {
      await literatureApi.update(formData.lid, formData)
      ElMessage.success('更新成功')
    } else {
      await literatureApi.create(formData)
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
    await ElMessageBox.confirm(`确定删除「${row.lname}」吗？`, '删除确认', { type: 'warning' })
    await literatureApi.delete(row.lid)
    ElMessage.success('删除成功')
    fetchData()
  } catch (e) {
    if (e !== 'cancel') ElMessage.error('删除失败')
  }
}
</script>

<style scoped>
.literature-list { padding: 20px; }
.card-header { display: flex; justify-content: space-between; align-items: center; }
</style>
