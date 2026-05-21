/**
 * 增强型导航栏组件 - Enhanced Navigation Bar
 * 提供中国传统古建筑主题的导航栏样式和交互
 * 
 * 特性：
 * 1. 传统纹样边框（云纹、回纹、波浪纹）
 * 2. 流动光效
 * 3. 悬停3D效果
 * 4. 滚动时自动隐藏/显示
 * 5. 移动端汉堡菜单
 * 6. 动态活动状态
 * 
 * @version 1.0
 * @date 2026-03-25
 */

class EnhancedNavbar {
    constructor(selector, options = {}) {
        this.navbar = typeof selector === 'string' ? document.querySelector(selector) : selector;
        this.options = {
            pattern: 'cloud',      // 纹样类型: cloud, huiwen, wave, geometric
            flowEffect: true,      // 流动光效
            scrollHide: true,      // 滚动时隐藏
            mobileMenu: true,      // 移动端菜单
            3dEffect: true,        // 3D悬停效果
            animationDuration: 300, // 动画时长
            ...options
        };
        
        this.isHidden = false;
        this.lastScrollY = 0;
        this.init();
    }

    /* ==================== 初始化 ==================== */
    init() {
        if (!this.navbar) {
            console.error('导航栏元素未找到');
            return;
        }

        this.injectStyles();
        this.createPattern();
        this.bindEvents();
        this.highlightCurrentPage();
    }

    /* ==================== 注入CSS样式 ==================== */
    injectStyles() {
        if (document.getElementById('enhanced-navbar-styles')) return;

        const styles = `
            /* 基础导航栏样式 */
            .nav-bar-enhanced {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: 64px;
                background: linear-gradient(135deg, #8B4513 0%, #6B3410 50%, #8B4513 100%);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                padding: 0 48px;
                z-index: 1000;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 16px rgba(0,0,0,0.25);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }

            .nav-bar-enhanced.hidden {
                transform: translateY(-100%);
            }

            .nav-bar-enhanced.scrolled {
                height: 56px;
                background: linear-gradient(135deg, rgba(107, 52, 16, 0.95) 0%, rgba(107, 52, 16, 0.95) 100%);
            }

            /* Logo样式 */
            .nav-logo-enhanced {
                color: #F5F5DC;
                font-size: 1.4em;
                font-weight: bold;
                text-decoration: none;
                display: flex;
                align-items: center;
                gap: 10px;
                position: relative;
                z-index: 10;
            }

            .nav-logo-enhanced svg {
                transition: transform 0.3s ease;
            }

            .nav-logo-enhanced:hover svg {
                transform: rotate(15deg) scale(1.1);
            }

            /* 导航链接容器 */
            .nav-links-enhanced {
                display: flex;
                gap: 4px;
                align-items: center;
            }

            /* 导航链接样式 */
            .nav-link-enhanced {
                color: rgba(245,245,220,0.85);
                text-decoration: none;
                padding: 8px 14px;
                border-radius: 6px;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                font-size: 0.95em;
                letter-spacing: 0.03em;
                position: relative;
                overflow: hidden;
            }

            .nav-link-enhanced::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(212, 165, 116, 0.3), transparent);
                transition: left 0.5s ease;
            }

            .nav-link-enhanced:hover::before {
                left: 100%;
            }

            .nav-link-enhanced:hover {
                color: #F5F5DC;
                background: rgba(212, 165, 116, 0.25);
                transform: translateY(-2px);
            }

            .nav-link-enhanced.active {
                color: #F5F5DC;
                background: rgba(212, 165, 116, 0.4);
            }

            .nav-link-enhanced.active::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 50%;
                width: 70%;
                height: 2px;
                background: #C9A84C;
                transform: translateX(-50%);
                transition: width 0.3s ease;
            }

            /* 3D效果 */
            .nav-link-3d {
                transform-style: preserve-3d;
                perspective: 1000px;
            }

            .nav-link-3d:hover {
                transform: translateY(-2px) rotateX(5deg);
            }

            /* 纹样边框 */
            .navbar-pattern-border {
                position: relative;
            }

            .navbar-pattern-border::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(to right, #C9A84C, #D4A574, #C9A84C);
                z-index: 10;
            }

            .navbar-pattern-border::after {
                content: '';
                position: absolute;
                bottom: -6px;
                left: 0;
                right: 0;
                height: 6px;
                z-index: 10;
            }

            /* 云纹底部边框 */
            .navbar-pattern-cloud::after {
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 10' preserveAspectRatio='none'%3E%3Cpath d='M0,0 Q25,8 50,0 T100,0 L100,10 L0,10 Z' fill='%23D4A574'/%3E%3C/svg%3E") top left/50px 6px repeat-x;
            }

            /* 回纹底部边框 */
            .navbar-pattern-huiwen::after {
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 10' preserveAspectRatio='none'%3E%3Cpath d='M0,5 L10,0 L20,5 L30,0 L40,5 L50,0 L60,5 L70,0 L80,5 L90,0 L100,5 L100,10 L0,10 Z' fill='%23C9A84C'/%3E%3C/svg%3E") top left/50px 6px repeat-x;
            }

            /* 波浪纹底部边框 */
            .navbar-pattern-wave::after {
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 10' preserveAspectRatio='none'%3E%3Cpath d='M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z' fill='%23D4A574'/%3E%3C/svg%3E") top left/50px 6px repeat-x;
            }

            /* 几何纹底部边框 */
            .navbar-pattern-geometric::after {
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 10' preserveAspectRatio='none'%3E%3Cpath d='M0,0 L20,10 L40,0 L60,10 L80,0 L100,0 L100,10 L0,10 Z' fill='%238B4513'/%3E%3C/svg%3E") top left/50px 6px repeat-x;
            }

            /* 流动光效 */
            .nav-flow-effect {
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, 
                    transparent, 
                    rgba(201, 168, 76, 0.3), 
                    transparent
                );
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.5s ease;
            }

            .nav-flow-effect.active {
                opacity: 1;
                animation: flowAnimation 2s ease-in-out;
            }

            @keyframes flowAnimation {
                0% { left: -100%; }
                100% { left: 100%; }
            }

            /* 移动端菜单 */
            .mobile-menu-toggle {
                display: none;
                flex-direction: column;
                justify-content: space-between;
                width: 24px;
                height: 20px;
                background: none;
                border: none;
                cursor: pointer;
                padding: 0;
            }

            .mobile-menu-toggle span {
                width: 100%;
                height: 2px;
                background: #F5F5DC;
                transition: all 0.3s ease;
            }

            .mobile-menu-toggle.active span:nth-child(1) {
                transform: rotate(45deg) translate(5px, 5px);
            }

            .mobile-menu-toggle.active span:nth-child(2) {
                opacity: 0;
            }

            .mobile-menu-toggle.active span:nth-child(3) {
                transform: rotate(-45deg) translate(7px, -6px);
            }

            .mobile-menu-overlay {
                display: none;
                position: fixed;
                top: 64px;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0,0,0,0.5);
                z-index: 999;
            }

            .mobile-menu-overlay.active {
                display: block;
            }

            .mobile-menu-panel {
                position: absolute;
                top: 0;
                right: -80%;
                width: 80%;
                max-width: 300px;
                height: 100%;
                background: linear-gradient(135deg, #8B4513 0%, #6B3410 100%);
                backdrop-filter: blur(10px);
                transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                padding: 20px;
                overflow-y: auto;
            }

            .mobile-menu-panel.active {
                right: 0;
            }

            .mobile-nav-links {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }

            .mobile-nav-links .nav-link-enhanced {
                padding: 12px 16px;
                border-bottom: 1px solid rgba(212, 165, 116, 0.3);
                border-radius: 0;
            }

            /* 响应式设计 */
            @media (max-width: 768px) {
                .nav-bar-enhanced {
                    padding: 0 20px;
                }

                .nav-links-enhanced {
                    display: none;
                }

                .mobile-menu-toggle {
                    display: flex;
                }

                .nav-logo-enhanced {
                    font-size: 1.2em;
                }
            }

            @media (max-width: 480px) {
                .nav-bar-enhanced {
                    height: 56px;
                }

                .mobile-menu-panel {
                    width: 90%;
                    max-width: 280px;
                }
            }
        `;

        const styleElement = document.createElement('style');
        styleElement.id = 'enhanced-navbar-styles';
        styleElement.textContent = styles;
        document.head.appendChild(styleElement);
    }

    /* ==================== 创建纹样装饰 ==================== */
    createPattern() {
        if (!this.options.pattern || this.options.pattern === 'none') return;
        
        this.navbar.classList.add('navbar-pattern-border');
        this.navbar.classList.add(`navbar-pattern-${this.options.pattern}`);
    }

    /* ==================== 绑定事件 ==================== */
    bindEvents() {
        // 滚动事件
        if (this.options.scrollHide) {
            window.addEventListener('scroll', this.handleScroll.bind(this));
        }

        // 导航链接点击
        const links = this.navbar.querySelectorAll('.nav-link-enhanced');
        links.forEach(link => {
            link.addEventListener('click', this.handleLinkClick.bind(this));
            
            // 3D效果
            if (this.options['3dEffect']) {
                link.classList.add('nav-link-3d');
            }
        });

        // 流动光效
        if (this.options.flowEffect) {
            this.createFlowEffect();
        }

        // 移动端菜单
        if (this.options.mobileMenu) {
            this.createMobileMenu();
        }
    }

    /* ==================== 处理滚动 ==================== */
    handleScroll() {
        const currentScrollY = window.pageYOffset;
        const scrollDelta = currentScrollY - this.lastScrollY;

        // 向下滚动隐藏，向上滚动显示
        if (scrollDelta > 10 && currentScrollY > 100) {
            this.hide();
        } else if (scrollDelta < -10) {
            this.show();
        }

        // 添加滚动样式
        if (currentScrollY > 50) {
            this.navbar.classList.add('scrolled');
        } else {
            this.navbar.classList.remove('scrolled');
        }

        this.lastScrollY = currentScrollY;
    }

    /* ==================== 隐藏导航栏 ==================== */
    hide() {
        if (!this.isHidden) {
            this.navbar.classList.add('hidden');
            this.isHidden = true;
        }
    }

    /* ==================== 显示导航栏 ==================== */
    show() {
        if (this.isHidden) {
            this.navbar.classList.remove('hidden');
            this.isHidden = false;
        }
    }

    /* ==================== 处理链接点击 ==================== */
    handleLinkClick(e) {
        // 触发流动光效
        if (this.options.flowEffect) {
            this.triggerFlowEffect(e.currentTarget);
        }

        // 更新活动状态
        this.setActiveLink(e.currentTarget);
    }

    /* ==================== 创建流动光效 ==================== */
    createFlowEffect() {
        const flow = document.createElement('div');
        flow.className = 'nav-flow-effect';
        this.navbar.appendChild(flow);
        this.flowEffect = flow;
    }

    /* ==================== 触发流动光效 ==================== */
    triggerFlowEffect(link) {
        if (!this.flowEffect) return;

        // 计算链接位置
        const rect = link.getBoundingClientRect();
        const navbarRect = this.navbar.getBoundingClientRect();
        
        // 定位光效
        this.flowEffect.style.position = 'absolute';
        this.flowEffect.style.left = `${rect.left - navbarRect.left}px`;
        this.flowEffect.style.width = `${rect.width}px`;
        this.flowEffect.style.height = `${rect.height}px`;
        this.flowEffect.style.top = `${rect.top - navbarRect.top}px`;
        
        // 触发动画
        this.flowEffect.classList.add('active');
        
        setTimeout(() => {
            this.flowEffect.classList.remove('active');
        }, 2000);
    }

    /* ==================== 高亮当前页面 ==================== */
    highlightCurrentPage() {
        const currentPage = window.location.pathname.split('/').pop() || 'index_architecture.html';
        const links = this.navbar.querySelectorAll('.nav-link-enhanced');
        
        links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && (href === currentPage || href.includes(currentPage))) {
                link.classList.add('active');
            }
        });
    }

    /* ==================== 设置活动链接 ==================== */
    setActiveLink(activeLink) {
        const links = this.navbar.querySelectorAll('.nav-link-enhanced');
        links.forEach(link => link.classList.remove('active'));
        activeLink.classList.add('active');
    }

    /* ==================== 创建移动端菜单 ==================== */
    createMobileMenu() {
        // 创建汉堡按钮
        const toggle = document.createElement('button');
        toggle.className = 'mobile-menu-toggle';
        toggle.innerHTML = '<span></span><span></span><span></span>';
        toggle.onclick = () => this.toggleMobileMenu();
        
        this.navbar.appendChild(toggle);

        // 创建遮罩层
        const overlay = document.createElement('div');
        overlay.className = 'mobile-menu-overlay';
        overlay.onclick = () => this.closeMobileMenu();
        document.body.appendChild(overlay);

        // 创建菜单面板
        const panel = document.createElement('div');
        panel.className = 'mobile-menu-panel';
        
        // 克隆导航链接
        const mobileLinks = this.navbar.querySelector('.nav-links-enhanced').cloneNode(true);
        mobileLinks.className = 'mobile-nav-links';
        panel.appendChild(mobileLinks);
        
        overlay.appendChild(panel);

        this.mobileToggle = toggle;
        this.mobileOverlay = overlay;
        this.mobilePanel = panel;
    }

    /* ==================== 切换移动端菜单 ==================== */
    toggleMobileMenu() {
        const isActive = this.mobileToggle.classList.contains('active');
        
        if (isActive) {
            this.closeMobileMenu();
        } else {
            this.openMobileMenu();
        }
    }

    /* ==================== 打开移动端菜单 ==================== */
    openMobileMenu() {
        this.mobileToggle.classList.add('active');
        this.mobileOverlay.classList.add('active');
        this.mobilePanel.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    /* ==================== 关闭移动端菜单 ==================== */
    closeMobileMenu() {
        this.mobileToggle.classList.remove('active');
        this.mobileOverlay.classList.remove('active');
        this.mobilePanel.classList.remove('active');
        document.body.style.overflow = '';
    }

    /* ==================== 更新纹样 ==================== */
    setPattern(pattern) {
        this.navbar.className = this.navbar.className.replace(/navbar-pattern-\w+/g, '');
        this.options.pattern = pattern;
        
        if (pattern && pattern !== 'none') {
            this.navbar.classList.add('navbar-pattern-border');
            this.navbar.classList.add(`navbar-pattern-${pattern}`);
        }
    }

    /* ==================== 销毁 ==================== */
    destroy() {
        // 移除事件监听器
        window.removeEventListener('scroll', this.handleScroll);
        
        // 移除创建的DOM元素
        if (this.flowEffect) {
            this.flowEffect.remove();
        }
        
        if (this.mobileOverlay) {
            this.mobileOverlay.remove();
        }

        // 移除样式
        const styles = document.getElementById('enhanced-navbar-styles');
        if (styles) {
            styles.remove();
        }
    }
}

/* ==================== 快捷方法 ==================== */

// 全局实例
let enhancedNavbar = null;

// 初始化函数
function initEnhancedNavbar(selector, options = {}) {
    if (enhancedNavbar) {
        enhancedNavbar.destroy();
    }
    enhancedNavbar = new EnhancedNavbar(selector, options);
    return enhancedNavbar;
}

// 设置纹样
function setNavbarPattern(pattern) {
    if (enhancedNavbar) {
        enhancedNavbar.setPattern(pattern);
    }
}

// 触发流动光效
function triggerNavbarFlow(link) {
    if (enhancedNavbar && enhancedNavbar.flowEffect) {
        enhancedNavbar.triggerFlowEffect(link);
    }
}

/* ==================== 默认初始化 ==================== */

// 页面加载完成后自动初始化
document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.nav-bar');
    if (navbar) {
        initEnhancedNavbar(navbar, {
            pattern: 'cloud',
            flowEffect: true,
            scrollHide: true,
            mobileMenu: true,
            '3dEffect': true
        });
    }
});

/* ==================== 导出 ==================== */

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        EnhancedNavbar,
        initEnhancedNavbar,
        setNavbarPattern,
        triggerNavbarFlow
    };
}

/* ==========================================================================
   使用示例
   ========================================================================== 

   1. 基础使用（自动初始化）
   
      HTML结构：
      <nav class="nav-bar">
        <a href="index.html" class="nav-logo">营造中华</a>
        <div class="nav-links">
          <a href="index.html" class="nav-link">首页</a>
          <a href="explore.html" class="nav-link">建筑探索</a>
          <a href="timeline.html" class="nav-link">历史长河</a>
        </div>
      </nav>
      
      自动转换为增强版导航栏


   2. 自定义初始化
   
      <script>
        initEnhancedNavbar('.nav-bar', {
          pattern: 'huiwen',      // 回纹边框
          flowEffect: true,       // 流动光效
          scrollHide: true,       // 滚动隐藏
          mobileMenu: true,       // 移动端菜单
          3dEffect: true          // 3D悬停效果
        });
      </script>


   3. 动态切换纹样
   
      <select onchange="setNavbarPattern(this.value)">
        <option value="cloud">云纹边框</option>
        <option value="huiwen">回纹边框</option>
        <option value="wave">波浪纹边框</option>
        <option value="geometric">几何纹边框</option>
      </select>


   4. 手动触发流动光效
   
      <a href="explore.html" class="nav-link" 
         onclick="triggerNavbarFlow(this)">
        建筑探索
      </a>


   5. 在React中使用
   
      import { initEnhancedNavbar } from './navbar_enhanced.js';
      
      useEffect(() => {
        initEnhancedNavbar('.nav-bar', {
          pattern: 'cloud',
          flowEffect: true
        });
      }, []);
*/
