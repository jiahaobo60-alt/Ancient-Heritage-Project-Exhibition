/**
 * 页面切换过渡动画系统 - Page Transition System
 * 提供中国传统古建筑主题的页面切换效果
 * 
 * 效果类型：
 * 1. scroll - 卷轴展开效果（默认）
 * 2. flip - 翻书效果
 * 3. fade - 淡入淡出
 * 4. slide - 滑动效果
 * 
 * @version 1.0
 * @date 2026-03-25
 */

class PageTransitionSystem {
    constructor(options = {}) {
        this.options = {
            type: 'scroll',      // 过渡类型: scroll, flip, fade, slide
            duration: 600,       // 过渡时长(ms)
            easing: 'cubic-bezier(0.4, 0, 0.2, 1)',  // 缓动函数
            background: 'linear-gradient(135deg, #8B4513 0%, #6B3410 100%)',  // 过渡背景
            ...options
        };
        
        this.isTransitioning = false;
        this.init();
    }

    /* ==================== 初始化 ==================== */
    init() {
        this.injectStyles();
        this.bindEvents();
        this.createTransitionLayer();
    }

    /* ==================== 注入CSS样式 ==================== */
    injectStyles() {
        if (document.getElementById('page-transition-styles')) return;

        const styles = `
            /* 页面切换基础样式 */
            .page-transition-layer {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 9999;
                pointer-events: none;
                opacity: 0;
                visibility: hidden;
            }

            .page-transition-layer.active {
                pointer-events: all;
                opacity: 1;
                visibility: visible;
            }

            /* 卷轴效果 */
            .transition-scroll .scroll-left,
            .transition-scroll .scroll-right {
                position: absolute;
                top: 0;
                width: 50%;
                height: 100%;
                background: var(--transition-bg);
                transition: transform var(--transition-duration) var(--transition-easing);
            }

            .transition-scroll .scroll-left {
                left: 0;
                transform: translateX(0);
                border-right: 2px solid var(--pattern-secondary);
            }

            .transition-scroll .scroll-right {
                right: 0;
                transform: translateX(0);
                border-left: 2px solid var(--pattern-secondary);
            }

            .transition-scroll.active .scroll-left {
                transform: translateX(-100%);
            }

            .transition-scroll.active .scroll-right {
                transform: translateX(100%);
            }

            /* 卷轴装饰 */
            .transition-scroll .scroll-left::before,
            .transition-scroll .scroll-right::before {
                content: '';
                position: absolute;
                top: 0;
                width: 20px;
                height: 100%;
                background: linear-gradient(to bottom, #D4A574, #8B4513);
            }

            .transition-scroll .scroll-left::before {
                right: -20px;
            }

            .transition-scroll .scroll-right::before {
                left: -20px;
            }

            /* 翻页效果 */
            .transition-flip {
                perspective: 1000px;
                transform-style: preserve-3d;
            }

            .transition-flip .flip-page {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: var(--transition-bg);
                transform-origin: left center;
                transform: rotateY(0deg);
                transition: transform var(--transition-duration) var(--transition-easing);
                backface-visibility: hidden;
            }

            .transition-flip.active .flip-page {
                transform: rotateY(-180deg);
            }

            /* 翻页背面 */
            .transition-flip .flip-back {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: var(--transition-bg);
                transform-origin: left center;
                transform: rotateY(180deg);
                backface-visibility: hidden;
            }

            /* 淡入淡出 */
            .transition-fade {
                background: var(--transition-bg);
                transition: opacity var(--transition-duration) var(--transition-easing);
            }

            .transition-fade.active {
                opacity: 0;
            }

            /* 滑动效果 */
            .transition-slide .slide-content {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: var(--transition-bg);
                transform: translateX(0);
                transition: transform var(--transition-duration) var(--transition-easing);
            }

            .transition-slide.active .slide-content {
                transform: translateX(-100%);
            }

            /* 页面内容动画 */
            body.page-transitioning {
                overflow: hidden;
            }

            .page-content {
                transition: opacity 0.3s ease;
            }

            .page-content.transitioning-out {
                opacity: 0.3;
            }

            .page-content.transitioning-in {
                opacity: 1;
            }

            /* 加载图标 */
            .transition-loading {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 60px;
                height: 60px;
                opacity: 0;
                transition: opacity 0.3s ease;
            }

            .transition-loading.active {
                opacity: 1;
            }

            .loading-icon {
                width: 100%;
                height: 100%;
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M20,80 L30,60 L70,60 L80,80 L80,85 L20,85 Z' fill='%23D4A574'/%3E%3Cpath d='M25,60 L35,40 L65,40 L75,60 L25,60 Z' fill='%238B4513'/%3E%3Cpath d='M30,40 L40,30 L60,30 L70,40 L30,40 Z' fill='%23D4A574'/%3E%3C/svg%3E") center/contain no-repeat;
                animation: loadingRotate 1.5s ease-in-out infinite;
            }

            @keyframes loadingRotate {
                0%, 100% { transform: rotate(0deg); }
                50% { transform: rotate(10deg); }
            }

            /* 响应式 */
            @media (max-width: 768px) {
                .transition-scroll .scroll-left,
                .transition-scroll .scroll-right {
                    width: 100%;
                }
                
                .transition-scroll .scroll-left::before,
                .transition-scroll .scroll-right::before {
                    display: none;
                }
            }
        `;

        const styleElement = document.createElement('style');
        styleElement.id = 'page-transition-styles';
        styleElement.textContent = styles;
        document.head.appendChild(styleElement);
    }

    /* ==================== 创建过渡层 ==================== */
    createTransitionLayer() {
        const layer = document.createElement('div');
        layer.className = `page-transition-layer transition-${this.options.type}`;
        layer.id = 'page-transition-layer';

        // 设置CSS变量
        layer.style.setProperty('--transition-duration', `${this.options.duration}ms`);
        layer.style.setProperty('--transition-easing', this.options.easing);
        layer.style.setProperty('--transition-bg', this.options.background);
        layer.style.setProperty('--pattern-secondary', '#D4A574');

        // 根据过渡类型创建内容
        switch (this.options.type) {
            case 'scroll':
                layer.innerHTML = `
                    <div class="scroll-left"></div>
                    <div class="scroll-right"></div>
                `;
                break;
            
            case 'flip':
                layer.innerHTML = `
                    <div class="flip-page"></div>
                    <div class="flip-back"></div>
                `;
                break;
            
            case 'fade':
                // 简单背景即可
                break;
            
            case 'slide':
                layer.innerHTML = `
                    <div class="slide-content"></div>
                `;
                break;
        }

        // 添加加载图标
        const loading = document.createElement('div');
        loading.className = 'transition-loading';
        loading.innerHTML = '<div class="loading-icon"></div>';
        layer.appendChild(loading);

        document.body.appendChild(layer);
    }

    /* ==================== 绑定事件 ==================== */
    bindEvents() {
        // 监听所有导航链接
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a[href]');
            if (link && this.isInternalLink(link.href)) {
                e.preventDefault();
                this.navigate(link.href);
            }
        });

        // 监听浏览器前进后退
        window.addEventListener('popstate', () => {
            this.reloadWithTransition();
        });
    }

    /* ==================== 判断是否为内部链接 ==================== */
    isInternalLink(href) {
        const currentOrigin = window.location.origin;
        return href.startsWith(currentOrigin) || href.startsWith('/') || href.startsWith('./') || !href.includes('://');
    }

    /* ==================== 导航到指定页面 ==================== */
    navigate(url) {
        if (this.isTransitioning) return;
        this.isTransitioning = true;

        // 显示加载图标
        document.querySelector('.transition-loading').classList.add('active');

        // 执行过渡动画
        this.startTransition(() => {
            // 动画完成后跳转
            window.location.href = url;
        });
    }

    /* ==================== 开始过渡动画 ==================== */
    startTransition(callback) {
        const layer = document.getElementById('page-transition-layer');
        const body = document.body;
        const content = document.querySelector('.page-content') || document.body;

        // 隐藏当前内容
        content.classList.add('transitioning-out');
        
        // 显示过渡层
        setTimeout(() => {
            layer.classList.add('active');
            
            // 等待动画完成
            setTimeout(() => {
                if (callback) callback();
            }, this.options.duration);
        }, 100);
    }

    /* ==================== 重新加载带过渡效果 ==================== */
    reloadWithTransition() {
        const layer = document.getElementById('page-transition-layer');
        
        // 立即显示过渡层（反向动画）
        layer.classList.add('active');
        
        // 隐藏过渡层（反向动画）
        setTimeout(() => {
            layer.classList.remove('active');
            
            // 显示内容
            setTimeout(() => {
                const content = document.querySelector('.page-content') || document.body;
                content.classList.remove('transitioning-out');
                this.isTransitioning = false;
            }, 100);
        }, this.options.duration);
    }

    /* ==================== 手动触发过渡 ==================== */
    transitionTo(url, type = null) {
        if (type) {
            this.setTransitionType(type);
        }
        this.navigate(url);
    }

    /* ==================== 设置过渡类型 ==================== */
    setTransitionType(type) {
        this.options.type = type;
        
        const layer = document.getElementById('page-transition-layer');
        // 移除所有过渡类
        layer.className = layer.className.replace(/transition-\w+/g, '');
        layer.classList.add(`transition-${type}`);
        
        // 重新创建内容
        this.createTransitionLayer();
    }

    /* ==================== 显示加载状态 ==================== */
    showLoading() {
        document.querySelector('.transition-loading').classList.add('active');
    }

    /* ==================== 隐藏加载状态 ==================== */
    hideLoading() {
        document.querySelector('.transition-loading').classList.remove('active');
    }

    /* ==================== 销毁 ==================== */
    destroy() {
        const layer = document.getElementById('page-transition-layer');
        const styles = document.getElementById('page-transition-styles');
        
        if (layer) layer.remove();
        if (styles) styles.remove();
        
        this.isTransitioning = false;
    }
}

/* ==================== 快捷方法 ==================== */

// 全局实例
let pageTransitionSystem = null;

// 初始化函数
function initPageTransitions(options = {}) {
    if (pageTransitionSystem) {
        pageTransitionSystem.destroy();
    }
    pageTransitionSystem = new PageTransitionSystem(options);
    return pageTransitionSystem;
}

// 导航到指定页面
function transitionTo(url, type = null) {
    if (!pageTransitionSystem) {
        initPageTransitions();
    }
    pageTransitionSystem.transitionTo(url, type);
}

// 设置过渡类型
function setTransitionType(type) {
    if (!pageTransitionSystem) {
        initPageTransitions({ type });
    } else {
        pageTransitionSystem.setTransitionType(type);
    }
}

// 显示/隐藏加载
function showPageLoading() {
    if (pageTransitionSystem) {
        pageTransitionSystem.showLoading();
    }
}

function hidePageLoading() {
    if (pageTransitionSystem) {
        pageTransitionSystem.hideLoading();
    }
}

/* ==================== 默认初始化 ==================== */

// 页面加载完成后自动初始化
document.addEventListener('DOMContentLoaded', () => {
    // 检查是否有自定义配置
    const script = document.querySelector('script[data-page-transition]');
    const options = script ? JSON.parse(script.dataset.pageTransition || '{}') : {};
    
    // 延迟初始化，确保其他脚本加载完成
    setTimeout(() => {
        initPageTransitions(options);
    }, 100);
});

/* ==================== 导出 ==================== */

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        PageTransitionSystem,
        initPageTransitions,
        transitionTo,
        setTransitionType,
        showPageLoading,
        hidePageLoading
    };
}

/* ==========================================================================
   使用示例
   ========================================================================== 

   1. 基础使用（自动初始化）
   
      在HTML中引入脚本：
      <script src="page_transitions.js"></script>
      
      所有内部链接将自动使用卷轴效果


   2. 自定义配置
   
      <script>
        initPageTransitions({
          type: 'flip',        // 翻页效果
          duration: 800,       // 0.8秒
          background: 'linear-gradient(135deg, #8B4513 0%, #C41E3A 100%)'
        });
      </script>


   3. 手动导航
   
      <button onclick="transitionTo('explore.html', 'scroll')">
        卷轴切换到探索页
      </button>
      
      <button onclick="transitionTo('timeline.html', 'flip')">
        翻页切换到时间轴
      </button>


   4. 在现有项目中集成
   
      修改导航链接：
      <a href="explore.html" onclick="transitionTo('explore.html'); return false;">
        建筑探索
      </a>


   5. 动态切换效果
   
      <select onchange="setTransitionType(this.value)">
        <option value="scroll">卷轴效果</option>
        <option value="flip">翻页效果</option>
        <option value="fade">淡入淡出</option>
        <option value="slide">滑动效果</option>
      </select>


   6. 显示加载状态
   
      showPageLoading();
      
      // 执行异步操作
      fetchData().then(() => {
        hidePageLoading();
        transitionTo('next.html');
      });


   7. 在React/Vue中使用
   
      import { initPageTransitions, transitionTo } from './page_transitions.js';
      
      // 组件挂载时初始化
      useEffect(() => {
        initPageTransitions({ type: 'scroll' });
      }, []);
      
      // 导航函数
      const handleNavigate = (url) => {
        transitionTo(url);
      };
*/
