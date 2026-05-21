# 修复总结 - 404错误和echarts-wordcloud错误

## 问题描述
根据用户截图，页面出现以下错误：
1. **404错误** - 请求 `/architecture/b...` 和 `/architecture/r...` 资源失败
2. **echarts-wordcloud错误** - `echarts.graphic.setTextStyle is not a function`

## 根本原因分析

### 1. 404错误原因
- `architecture_common.js` 中的 `API_BASE_URL` 配置逻辑有问题
- 当 `BASE_URL` 未正确定义时，会向错误的路径发起请求
- `loadVizExamples` 函数优先请求 `/api/viz-examples/` ，如果后端未启动会产生404

### 2. echarts-wordcloud错误原因
- `time.html` 使用了本地的 `js/echarts-wordcloud.js`
- 该版本与 `echarts-5.4.2` 不兼容
- echarts 5.x 的 API 已变更，`setTextStyle` 方法不存在

## 修复内容

### 修复 1: architecture_common.js
**文件**: `frontend/js/architecture_common.js`

**修改内容**:
1. 将 `CONFIG` 从常量改为变量
2. 添加 `initConfig()` 函数动态初始化配置
3. 在 `DOMContentLoaded` 时重新调用 `initConfig()` 确保 `BASE_URL` 已加载
4. 修改 `loadVizExamples()` 函数：
   - 优先从本地数据加载（避免404）
   - 后台静默更新后端数据
   - 更优雅的错误处理，不输出大量错误信息

### 修复 2: time.html
**文件**: `frontend/time.html`

**修改内容**:
1. 修改 echarts-wordcloud 加载方式：
   ```html
   <!-- 原代码 -->
   <script src="js/echarts-wordcloud.js"></script>
   
   <!-- 修复后 -->
   <script src="https://cdn.jsdelivr.net/npm/echarts-wordcloud@2.1.0/dist/echarts-wordcloud.min.js"></script>
   ```

2. 修复 API 请求路径：
   - `loadData()` 函数中的3个请求
   - `updateWordcloud()` 函数中的1个请求
   - 统一使用动态 URL 拼接，兼容有/无 `BASE_URL` 的情况

### 修复 3: 3d_architecture.html
**文件**: `frontend/3d_architecture.html`

**修改内容**:
调整脚本加载顺序，确保 `config.js` 在 `architecture_common.js` 之前加载：
```html
<!-- 原顺序 (错误) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="js/config.js"></script>
<script src="js/architecture_common.js"></script>

<!-- 修复后 (正确) -->
<script src="js/config.js"></script>
<script src="js/architecture_common.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

## 测试建议

1. **测试 404 错误**:
   - 打开 `time.html`，检查控制台是否还有404错误
   - 打开 `3d_architecture.html`，检查控制台是否还有404错误

2. **测试 echarts-wordcloud**:
   - 打开 `time.html`
   - 点击不同朝代，检查词云图是否正常显示
   - 检查控制台是否还有 `setTextStyle` 错误

3. **测试 API 请求**:
   - 如果后端未启动，页面应该正常使用本地数据，不产生404错误
   - 如果后端已启动，数据应该从后端 API 获取

## 后续优化建议

1. **统一 API 请求处理**: 建议创建一个统一的 API 请求包装函数，自动处理错误和降级逻辑

2. **移除本地 echarts-wordcloud.js**: 既然已经使用 CDN 版本，可以删除本地的 `js/echarts-wordcloud.js` 文件

3. **添加配置验证**: 在页面加载时验证 `BASE_URL` 是否正确配置

## 修复时间
2026-05-03
