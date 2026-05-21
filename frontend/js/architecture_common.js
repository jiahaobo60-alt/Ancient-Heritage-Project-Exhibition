/**
 * 中国古建筑网站 - 通用交互功能
 * Architecture Common JS - Shared interactive functions
 */

// ==================== 全局配置 ====================
// 优先使用config.js中的BASE_URL（完整地址），否则使用相对路径
// 注意：config.js 必须在 architecture_common.js 之前加载

let CONFIG;

function initConfig() {
    const baseUrl = (typeof BASE_URL !== 'undefined' && BASE_URL) ? BASE_URL : '';
    CONFIG = {
        API_BASE_URL: baseUrl ? baseUrl + '/architecture' : '/architecture',
        BACKEND_BASE_URL: baseUrl || '',
        ITEMS_PER_PAGE: 9,
        ANIMATION_DURATION: 300
    };
    
    // 调试信息
    console.log('[Config] BASE_URL:', baseUrl);
    console.log('[Config] API_BASE_URL:', CONFIG.API_BASE_URL);
}

// 初始化配置
initConfig();

// ==================== 工具函数 ====================

/**
 * 防抖函数
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * 节流函数
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

/**
 * 格式化日期
 */
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * 显示加载动画
 */
function showLoading(containerId) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <p>正在加载...</p>
            </div>
        `;
    }
}

/**
 * 显示错误信息
 */
function showError(containerId, message) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="error-message">
                <span class="error-icon">⚠️</span>
                <p>${message}</p>
                <button onclick="location.reload()" class="retry-btn">重新加载</button>
            </div>
        `;
    }
}

/**
 * 显示空状态
 */
function showEmpty(containerId, message = '暂无数据') {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="empty-state">
                <span class="empty-icon">📭</span>
                <p>${message}</p>
            </div>
        `;
    }
}

// ==================== API 请求 ====================

/**
 * 通用API请求函数
 */
async function apiRequest(endpoint, options = {}) {
    const url = `${CONFIG.API_BASE_URL}${endpoint}`;
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    try {
        const response = await fetch(url, { ...defaultOptions, ...options });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API请求失败:', error);
        throw error;
    }
}

/**
 * 获取古建筑列表
 */
async function getBuildings(filters = {}) {
    const params = new URLSearchParams();
    Object.keys(filters).forEach(key => {
        if (filters[key]) {
            params.append(key, filters[key]);
        }
    });
    
    const queryString = params.toString();
    return await apiRequest(`/buildings/${queryString ? '?' + queryString : ''}`);
}

/**
 * 获取单个古建筑详情
 */
async function getBuildingDetail(id) {
    return await apiRequest(`/buildings/${id}/`);
}

/**
 * 获取朝代列表
 */
async function getDynasties() {
    return await apiRequest('/dynasties/');
}

/**
 * 获取地区列表
 */
async function getRegions() {
    return await apiRequest('/regions/');
}

/**
 * 获取建筑元素列表
 */
async function getElements(category = '') {
    const endpoint = category ? `/elements/?category=${category}` : '/elements/';
    return await apiRequest(endpoint);
}

/**
 * 渲染数据可视化案例参考网格
 * @param {string} containerId
 * @param {Array<{title, image, link}>} items
 */
function renderVizExamples(containerId, items) {
    const container = document.getElementById(containerId);
    if (!container) return;
    if (!items || items.length === 0) {
        container.innerHTML = '<p class="viz-caption">暂无示例</p>';
        return;
    }
    container.innerHTML = items.map(it => `
        <a class="viz-card" href="${it.link}" target="_blank" title="${it.title}">
            <img src="${it.image}" alt="${it.title}">
            <div class="viz-caption">${it.title}</div>
        </a>
    `).join('');
}

/**
 * 异步加载并渲染 viz_examples.json
 * @param {string} containerId
 * @param {string} dataUrl
 */
async function loadVizExamples(containerId = 'viz-examples-grid', dataUrl = './data/viz_examples.json') {
    const container = document.getElementById(containerId);
    
    // 先尝试从本地数据加载（更快，不产生404）
    try {
        const res = await fetch(dataUrl);
        if (res.ok) {
            const items = await res.json();
            renderVizExamples(containerId, items);
            
            // 后台尝试更新数据（静默失败）
            updateVizExamplesFromBackend();
            return;
        }
    } catch (e) {
        console.warn('本地数据加载失败，尝试后端 API', e);
    }

    // 如果本地数据失败，尝试后端 API
    try {
        const res = await fetch('/api/viz-examples/');
        if (res.ok) {
            const data = await res.json();
            const items = data.results || data;
            renderVizExamples(containerId, items);
        }
    } catch (e) {
        console.warn('后端 viz-examples API 不可用，使用备用数据', e);
        if (container) container.innerHTML = '<p class="viz-caption">暂无示例数据</p>';
    }
}

/**
 * 后台静默更新 viz-examples 数据
 */
async function updateVizExamplesFromBackend() {
    try {
        const res = await fetch('/api/viz-examples/');
        if (res.ok) {
            const data = await res.json();
            const items = data.results || data;
            // 静默更新，不重新渲染（除非数据有变化）
            console.log('[VizExamples] 后端数据已同步');
        }
    } catch (e) {
        // 静默失败，不影响用户体验
    }
}

// ==================== 模态框功能 ====================

/**
 * 打开模态框
 */
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // 添加动画效果
        setTimeout(() => {
            modal.classList.add('modal-active');
        }, 10);
    }
}

/**
 * 关闭模态框
 */
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('modal-active');
        
        setTimeout(() => {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }, CONFIG.ANIMATION_DURATION);
    }
}

/**
 * 初始化模态框关闭事件
 */
function initModalCloseEvents() {
    // 点击关闭按钮
    document.querySelectorAll('.modal-close').forEach(btn => {
        btn.addEventListener('click', function() {
            const modal = this.closest('.modal');
            if (modal) {
                closeModal(modal.id);
            }
        });
    });
    
    // 点击模态框外部关闭
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal(this.id);
            }
        });
    });
    
    // ESC键关闭
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal-active').forEach(modal => {
                closeModal(modal.id);
            });
        }
    });
}

// ==================== 搜索功能 ====================

/**
 * 初始化搜索框
 */
function initSearch(inputId, searchCallback, delay = 500) {
    const searchInput = document.getElementById(inputId);
    if (searchInput) {
        const debouncedSearch = debounce(searchCallback, delay);
        
        searchInput.addEventListener('input', function() {
            debouncedSearch(this.value);
        });
        
        // 回车搜索
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchCallback(this.value);
            }
        });
    }
}

// ==================== 分页功能 ====================

/**
 * 生成分页HTML
 */
function generatePagination(currentPage, totalPages, callback) {
    if (totalPages <= 1) return '';
    
    let html = '<div class="pagination">';
    
    // 上一页
    html += `<button class="page-btn ${currentPage === 1 ? 'disabled' : ''}" 
                     onclick="${currentPage > 1 ? callback + '(' + (currentPage - 1) + ')' : ''}">
                上一页
             </button>`;
    
    // 页码
    const maxVisible = 5;
    let startPage = Math.max(1, currentPage - Math.floor(maxVisible / 2));
    let endPage = Math.min(totalPages, startPage + maxVisible - 1);
    
    if (endPage - startPage < maxVisible - 1) {
        startPage = Math.max(1, endPage - maxVisible + 1);
    }
    
    if (startPage > 1) {
        html += `<button class="page-btn" onclick="${callback}(1)">1</button>`;
        if (startPage > 2) {
            html += '<span class="page-ellipsis">...</span>';
        }
    }
    
    for (let i = startPage; i <= endPage; i++) {
        html += `<button class="page-btn ${i === currentPage ? 'active' : ''}" 
                         onclick="${callback}(${i})">${i}</button>`;
    }
    
    if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
            html += '<span class="page-ellipsis">...</span>';
        }
        html += `<button class="page-btn" onclick="${callback}(${totalPages})">${totalPages}</button>`;
    }
    
    // 下一页
    html += `<button class="page-btn ${currentPage === totalPages ? 'disabled' : ''}" 
                     onclick="${currentPage < totalPages ? callback + '(' + (currentPage + 1) + ')' : ''}">
                下一页
             </button>`;
    
    html += '</div>';
    return html;
}

// ==================== 滚动动画 ====================

/**
 * 初始化滚动显示动画
 */
function initScrollAnimation() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

/**
 * 平滑滚动到指定元素
 */
function scrollToElement(elementId, offset = 80) {
    const element = document.getElementById(elementId);
    if (element) {
        const top = element.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({
            top: top,
            behavior: 'smooth'
        });
    }
}

// ==================== 本地存储 ====================

/**
 * 保存用户偏好
 */
function savePreference(key, value) {
    try {
        localStorage.setItem(`architecture_${key}`, JSON.stringify(value));
    } catch (e) {
        console.warn('无法保存偏好设置:', e);
    }
}

/**
 * 获取用户偏好
 */
function getPreference(key, defaultValue = null) {
    try {
        const value = localStorage.getItem(`architecture_${key}`);
        return value ? JSON.parse(value) : defaultValue;
    } catch (e) {
        return defaultValue;
    }
}

/**
 * 添加到浏览历史
 */
function addToHistory(type, id, title) {
    const history = getPreference('history', []);
    const newItem = { type, id, title, timestamp: Date.now() };
    
    // 去重并限制数量
    const filtered = history.filter(item => !(item.type === type && item.id === id));
    filtered.unshift(newItem);
    
    if (filtered.length > 50) {
        filtered.pop();
    }
    
    savePreference('history', filtered);
}

// ==================== 图片懒加载 ====================

/**
 * 初始化图片懒加载
 */
function initLazyLoad() {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                const src = img.dataset.src;
                
                if (src) {
                    // 创建临时图片对象预加载
                    const tempImg = new Image();
                    tempImg.onload = function() {
                        img.src = src;
                        img.classList.add('loaded');
                        observer.unobserve(img);
                    };
                    tempImg.onerror = function() {
                        // 加载失败时使用占位图
                        img.src = 'img/宫殿建筑-故宫太和殿/image_01.jpg';
                        img.classList.add('loaded');
                        observer.unobserve(img);
                    };
                    tempImg.src = src;
                }
            }
        });
    }, {
        rootMargin: '50px 0px', // 提前50px开始加载
        threshold: 0.1
    });
    
    document.querySelectorAll('img.lazy').forEach(img => {
        // 确保图片有固定的宽高，避免布局跳动
        if (!img.style.width && img.dataset.width) {
            img.style.width = img.dataset.width;
        }
        if (!img.style.height && img.dataset.height) {
            img.style.height = img.dataset.height;
        }
        imageObserver.observe(img);
    });
}

// ==================== 导航功能 ====================

/**
 * 初始化导航栏滚动效果
 */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        let lastScroll = 0;
        let ticking = false;
        
        function updateNavbar() {
            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 100) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
            
            lastScroll = currentScroll;
            ticking = false;
        }
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(updateNavbar);
                ticking = true;
            }
        });
    }
}

/**
 * 高亮当前页面导航
 */
function highlightCurrentNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index_architecture.html';
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href').includes(currentPage)) {
            link.classList.add('active');
        }
    });
}

// ==================== 初始化 ====================

document.addEventListener('DOMContentLoaded', function() {
    // 重新初始化配置（确保 config.js 已加载）
    initConfig();
    
    // 初始化模态框事件
    initModalCloseEvents();
    
    // 初始化滚动动画
    initScrollAnimation();
    
    // 初始化导航栏
    initNavbarScroll();
    
    // 高亮当前导航
    highlightCurrentNav();
    
    // 初始化图片懒加载
    initLazyLoad();

    // 加载数据可视化案例参考
    loadVizExamples('viz-examples-grid', './data/viz_examples.json');
});

// ==================== 导出 ====================
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        CONFIG,
        debounce,
        throttle,
        apiRequest,
        getBuildings,
        getBuildingDetail,
        getDynasties,
        getRegions,
        getElements,
        openModal,
        closeModal,
        showLoading,
        showError,
        showEmpty,
        generatePagination,
        scrollToElement,
        savePreference,
        getPreference,
        addToHistory,
        renderVizExamples,
        loadVizExamples
    };
}
