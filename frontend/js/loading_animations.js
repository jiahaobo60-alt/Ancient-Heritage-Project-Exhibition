/**
 * 古建筑主题Loading动画系统 - Loading Animation System
 * 提供多种中国传统古建筑主题的加载动画
 * 
 * 动画类型：
 * 1. dougong - 斗拱搭建动画
 * 2. taiji - 太极旋转动画
 * 3. pagoda - 宝塔逐层动画
 * 4. scroll - 卷轴展开动画
 * 5. lantern - 宫灯摆动动画
 * 
 * @version 1.0
 * @date 2026-03-25
 */

class LoadingAnimationSystem {
    constructor(container, options = {}) {
        this.container = typeof container === 'string' ? document.querySelector(container) : container;
        this.options = {
            type: 'dougong',        // 动画类型
            size: 80,              // 动画尺寸(px)
            duration: 2000,        // 动画周期(ms)
            text: '加载中...',     // 加载文本
            showText: true,        // 显示文本
            bgColor: 'rgba(139, 69, 19, 0.9)', // 背景色
            primaryColor: '#D4A574',  // 主色
            secondaryColor: '#8B4513', // 辅色
            accentColor: '#C41E3A',    // 强调色
            ...options
        };
        
        this.isVisible = false;
        this.animationTimer = null;
        this.init();
    }

    /* ==================== 初始化 ==================== */
    init() {
        if (!this.container) {
            console.error('Loading动画容器未找到');
            return;
        }

        this.injectStyles();
        this.createLoader();
    }

    /* ==================== 注入CSS样式 ==================== */
    injectStyles() {
        if (document.getElementById('loading-animation-styles')) return;

        const styles = `
            /* 基础Loading容器 */
            .loading-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: var(--loading-bg);
                z-index: 9999;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
            }

            .loading-container.active {
                opacity: 1;
                visibility: visible;
            }

            .loading-container.hidden {
                opacity: 0;
                visibility: hidden;
            }

            /* 动画区域 */
            .loading-animation {
                position: relative;
                width: var(--loading-size);
                height: var(--loading-size);
                margin-bottom: 24px;
            }

            .loading-text {
                color: #F5F5DC;
                font-size: 1.1em;
                letter-spacing: 0.2em;
                text-align: center;
                opacity: 0.8;
                animation: loadingTextPulse 2s ease-in-out infinite;
            }

            @keyframes loadingTextPulse {
                0%, 100% { opacity: 0.6; }
                50% { opacity: 1; }
            }

            /* 1. 斗拱搭建动画 */
            .loading-dougong {
                width: 100%;
                height: 100%;
                position: relative;
            }

            .dougong-layer {
                position: absolute;
                width: 100%;
                height: 100%;
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                opacity: 0;
            }

            .dougong-layer.layer-1 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M20,80 L30,60 L70,60 L80,80 L80,85 L20,85 Z' fill='%23D4A574' stroke='%238B4513' stroke-width='1'/%3E%3C/svg%3E");
                animation: dougongBuild 0.5s ease forwards;
            }

            .dougong-layer.layer-2 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M25,60 L35,40 L65,40 L75,60 L25,60 Z' fill='%238B4513' stroke='%236B3410' stroke-width='1'/%3E%3C/svg%3E");
                animation: dougongBuild 0.5s ease 0.3s forwards;
            }

            .dougong-layer.layer-3 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M30,40 L40,30 L60,30 L70,40 L30,40 Z' fill='%23D4A574' stroke='%238B4513' stroke-width='1'/%3E%3C/svg%3E");
                animation: dougongBuild 0.5s ease 0.6s forwards;
            }

            @keyframes dougongBuild {
                0% {
                    opacity: 0;
                    transform: translateY(30px) scale(0.8);
                }
                50% {
                    opacity: 0.7;
                    transform: translateY(-5px) scale(1.05);
                }
                100% {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }
            }

            /* 斗拱整体动画 */
            .loading-dougong::after {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                animation: dougongFloat 1.5s ease-in-out infinite;
            }

            @keyframes dougongFloat {
                0%, 100% { transform: translateY(0) rotateX(0); }
                50% { transform: translateY(-8px) rotateX(5deg); }
            }

            /* 2. 太极旋转动画 */
            .loading-taiji {
                width: 100%;
                height: 100%;
                position: relative;
            }

            .taiji-circle {
                width: 100%;
                height: 100%;
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='M50,0 A50,50 0 0,1 50,100 A25,25 0 0,0 50,50 A25,25 0 0,1 50,0' fill='%23F5F5DC'/%3E%3Cpath d='M50,0 A50,50 0 0,0 50,100 A25,25 0 0,1 50,50 A25,25 0 0,0 50,0' fill='%238B4513'/%3E%3Ccircle cx='50' cy='25' r='12' fill='%238B4513'/%3E%3Ccircle cx='50' cy='75' r='12' fill='%23F5F5DC'/%3E%3C/svg%3E") center/contain no-repeat;
                animation: taijiRotate 3s linear infinite;
            }

            @keyframes taijiRotate {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            /* 3. 宝塔逐层动画 */
            .loading-pagoda {
                width: 100%;
                height: 100%;
                position: relative;
            }

            .pagoda-layer {
                position: absolute;
                width: 100%;
                height: 100%;
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center bottom;
                opacity: 0;
            }

            .pagoda-layer.layer-1 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect x='40' y='80' width='20' height='20' fill='%238B4513' stroke='%23D4A574' stroke-width='1'/%3E%3C/svg%3E");
                animation: pagodaBuild 0.4s ease forwards;
            }

            .pagoda-layer.layer-2 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect x='35' y='65' width='30' height='15' fill='%23A0522D' stroke='%23D4A574' stroke-width='1'/%3E%3C/svg%3E");
                animation: pagodaBuild 0.4s ease 0.2s forwards;
            }

            .pagoda-layer.layer-3 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect x='30' y='50' width='40' height='15' fill='%238B4513' stroke='%23D4A574' stroke-width='1'/%3E%3C/svg%3E");
                animation: pagodaBuild 0.4s ease 0.4s forwards;
            }

            .pagoda-layer.layer-4 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect x='25' y='35' width='50' height='15' fill='%23A0522D' stroke='%23D4A574' stroke-width='1'/%3E%3C/svg%3E");
                animation: pagodaBuild 0.4s ease 0.6s forwards;
            }

            .pagoda-layer.layer-5 {
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpolygon points='50,10 70,35 30,35' fill='%23D4A574' stroke='%238B4513' stroke-width='1'/%3E%3C/svg%3E");
                animation: pagodaBuild 0.4s ease 0.8s forwards;
            }

            @keyframes pagodaBuild {
                0% {
                    opacity: 0;
                    transform: translateY(20px) scale(0.9);
                }
                100% {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }
            }

            /* 4. 卷轴展开动画 */
            .loading-scroll {
                width: 100%;
                height: 100%;
                position: relative;
                perspective: 1000px;
            }

            .scroll-roll {
                position: absolute;
                top: 50%;
                left: 50%;
                width: 80%;
                height: 60%;
                background: linear-gradient(135deg, #FFFDF5 0%, #EDE3CC 100%);
                border: 2px solid #8B4513;
                border-radius: 4px;
                transform: translate(-50%, -50%) rotateX(60deg) scaleY(0.3);
                opacity: 0;
                animation: scrollUnroll 2s ease-in-out infinite;
            }

            .scroll-roll::before,
            .scroll-roll::after {
                content: '';
                position: absolute;
                top: 0;
                width: 15px;
                height: 100%;
                background: linear-gradient(to bottom, #8B4513, #6B3410);
                border-radius: 0 4px 4px 0;
            }

            .scroll-roll::before {
                left: -15px;
            }

            .scroll-roll::after {
                right: -15px;
                border-radius: 4px 0 0 4px;
            }

            @keyframes scrollUnroll {
                0% {
                    opacity: 0;
                    transform: translate(-50%, -50%) rotateX(60deg) scaleY(0.3);
                }
                30% {
                    opacity: 1;
                    transform: translate(-50%, -50%) rotateX(0deg) scaleY(1);
                }
                70% {
                    opacity: 1;
                    transform: translate(-50%, -50%) rotateX(0deg) scaleY(1);
                }
                100% {
                    opacity: 0;
                    transform: translate(-50%, -50%) rotateX(-60deg) scaleY(0.3);
                }
            }

            /* 5. 宫灯摆动动画 */
            .loading-lantern {
                width: 100%;
                height: 100%;
                position: relative;
            }

            .lantern-body {
                position: absolute;
                top: 50%;
                left: 50%;
                width: 60%;
                height: 70%;
                background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 70'%3E%3Crect x='5' y='5' width='50' height='60' fill='%23C41E3A' stroke='%23F5F5DC' stroke-width='2' rx='8'/%3E%3Crect x='15' y='15' width='30' height='40' fill='none' stroke='%23F5F5DC' stroke-width='1'/%3E%3C/svg%3E") center/contain no-repeat;
                transform: translate(-50%, -50%);
                transform-origin: top center;
                animation: lanternSwing 2s ease-in-out infinite;
            }

            .lantern-light {
                position: absolute;
                top: 50%;
                left: 50%;
                width: 30%;
                height: 30%;
                background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 70%);
                border-radius: 50%;
                transform: translate(-50%, -50%);
                animation: lanternGlow 1.5s ease-in-out infinite;
            }

            @keyframes lanternSwing {
                0%, 100% { transform: translate(-50%, -50%) rotate(0deg); }
                25% { transform: translate(-50%, -50%) rotate(3deg); }
                75% { transform: translate(-50%, -50%) rotate(-3deg); }
            }

            @keyframes lanternGlow {
                0%, 100% { opacity: 0.6; transform: translate(-50%, -50%) scale(1); }
                50% { opacity: 1; transform: translate(-50%, -50%) scale(1.2); }
            }

            /* 自定义动画速度 */
            .loading-fast {
                --animation-duration: 1s;
            }

            .loading-normal {
                --animation-duration: 2s;
            }

            .loading-slow {
                --animation-duration: 3s;
            }

            /* 响应式 */
            @media (max-width: 768px) {
                .loading-animation {
                    width: calc(var(--loading-size) * 0.8);
                    height: calc(var(--loading-size) * 0.8);
                }
                
                .loading-text {
                    font-size: 0.9em;
                    letter-spacing: 0.1em;
                }
            }
        `;

        const styleElement = document.createElement('style');
        styleElement.id = 'loading-animation-styles';
        styleElement.textContent = styles;
        document.head.appendChild(styleElement);
    }

    /* ==================== 创建加载器 ==================== */
    createLoader() {
        this.container.className = 'loading-container';
        
        // 设置CSS变量
        this.container.style.setProperty('--loading-size', `${this.options.size}px`);
        this.container.style.setProperty('--loading-bg', this.options.bgColor);
        this.container.style.setProperty('--animation-duration', `${this.options.duration}ms`);

        // 创建动画区域
        const animation = document.createElement('div');
        animation.className = `loading-animation loading-${this.options.type}`;
        animation.innerHTML = this.getAnimationHTML();
        this.container.appendChild(animation);

        // 创建文本
        if (this.options.showText) {
            const text = document.createElement('div');
            text.className = 'loading-text';
            text.textContent = this.options.text;
            this.container.appendChild(text);
        }
    }

    /* ==================== 获取动画HTML ==================== */
    getAnimationHTML() {
        switch (this.options.type) {
            case 'dougong':
                return `
                    <div class="loading-dougong">
                        <div class="dougong-layer layer-1"></div>
                        <div class="dougong-layer layer-2"></div>
                        <div class="dougong-layer layer-3"></div>
                    </div>
                `;
            
            case 'taiji':
                return `
                    <div class="loading-taiji">
                        <div class="taiji-circle"></div>
                    </div>
                `;
            
            case 'pagoda':
                return `
                    <div class="loading-pagoda">
                        <div class="pagoda-layer layer-5"></div>
                        <div class="pagoda-layer layer-4"></div>
                        <div class="pagoda-layer layer-3"></div>
                        <div class="pagoda-layer layer-2"></div>
                        <div class="pagoda-layer layer-1"></div>
                    </div>
                `;
            
            case 'scroll':
                return `
                    <div class="loading-scroll">
                        <div class="scroll-roll"></div>
                    </div>
                `;
            
            case 'lantern':
                return `
                    <div class="loading-lantern">
                        <div class="lantern-body"></div>
                        <div class="lantern-light"></div>
                    </div>
                `;
            
            default:
                return `
                    <div class="loading-dougong">
                        <div class="dougong-layer layer-1"></div>
                        <div class="dougong-layer layer-2"></div>
                        <div class="dougong-layer layer-3"></div>
                    </div>
                `;
        }
    }

    /* ==================== 显示加载器 ==================== */
    show() {
        if (this.isVisible) return;
        
        this.isVisible = true;
        this.container.classList.add('active');
        
        // 开始动画循环
        this.startAnimationLoop();
    }

    /* ==================== 隐藏加载器 ==================== */
    hide() {
        if (!this.isVisible) return;
        
        this.isVisible = false;
        this.container.classList.remove('active');
        
        // 停止动画
        this.stopAnimationLoop();
    }

    /* ==================== 开始动画循环 ==================== */
    startAnimationLoop() {
        // 根据动画类型设置循环
        switch (this.options.type) {
            case 'dougong':
                this.animationTimer = setInterval(() => {
                    this.restartAnimation();
                }, this.options.duration);
                break;
            
            case 'pagoda':
                this.animationTimer = setInterval(() => {
                    this.restartAnimation();
                }, this.options.duration + 500);
                break;
            
            // 其他动画使用CSS循环，无需JS定时器
        }
    }

    /* ==================== 停止动画循环 ==================== */
    stopAnimationLoop() {
        if (this.animationTimer) {
            clearInterval(this.animationTimer);
            this.animationTimer = null;
        }
    }

    /* ==================== 重新开始动画 ==================== */
    restartAnimation() {
        const animation = this.container.querySelector('.loading-animation');
        const newAnimation = animation.cloneNode(true);
        animation.parentNode.replaceChild(newAnimation, animation);
    }

    /* ==================== 设置文本 ==================== */
    setText(text) {
        this.options.text = text;
        const textElement = this.container.querySelector('.loading-text');
        if (textElement) {
            textElement.textContent = text;
        }
    }

    /* ==================== 设置类型 ==================== */
    setType(type) {
        this.options.type = type;
        
        const animation = this.container.querySelector('.loading-animation');
        animation.className = `loading-animation loading-${type}`;
        animation.innerHTML = this.getAnimationHTML();
    }

    /* ==================== 销毁 ==================== */
    destroy() {
        this.hide();
        
        // 移除样式
        const styles = document.getElementById('loading-animation-styles');
        if (styles) {
            styles.remove();
        }
    }
}

/* ==================== 快捷方法 ==================== */

// 全局实例
let loadingSystem = null;

// 初始化函数
function initLoadingAnimation(container, options = {}) {
    if (loadingSystem) {
        loadingSystem.destroy();
    }
    loadingSystem = new LoadingAnimationSystem(container, options);
    return loadingSystem;
}

// 显示加载
function showLoading(options = {}) {
    if (!loadingSystem) {
        // 创建默认容器
        const container = document.createElement('div');
        container.id = 'global-loading-container';
        document.body.appendChild(container);
        
        initLoadingAnimation(container, options);
    }
    loadingSystem.show();
}

// 隐藏加载
function hideLoading() {
    if (loadingSystem) {
        loadingSystem.hide();
    }
}

// 设置文本
function setLoadingText(text) {
    if (loadingSystem) {
        loadingSystem.setText(text);
    }
}

// 设置类型
function setLoadingType(type) {
    if (loadingSystem) {
        loadingSystem.setType(type);
    }
}

/* ==================== 默认初始化 ==================== */

// 页面加载完成后自动初始化（如果需要）
document.addEventListener('DOMContentLoaded', () => {
    // 可以在这里自动初始化全局加载动画
});

/* ==================== 导出 ==================== */

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        LoadingAnimationSystem,
        initLoadingAnimation,
        showLoading,
        hideLoading,
        setLoadingText,
        setLoadingType
    };
}

/* ==========================================================================
   使用示例
   ========================================================================== 

   1. 基础使用
   
      HTML:
      <div id="loading-container"></div>
      
      JavaScript:
      const loading = new LoadingAnimationSystem('#loading-container', {
        type: 'dougong',
        size: 80,
        text: '正在加载...'
      });
      
      loading.show();
      
      // 数据加载完成后
      loading.hide();


   2. 全局加载动画
   
      // 显示
      showLoading({
        type: 'pagoda',
        text: '正在加载古建筑数据...'
      });
      
      // 隐藏
      hideLoading();


   3. 动态修改
   
      // 修改文本
      setLoadingText('正在处理...');
      
      // 修改类型
      setLoadingType('taiji');


   4. 在API请求中使用
   
      async function loadData() {
        showLoading({ text: '加载中...' });
        
        try {
          const response = await fetch('/api/buildings');
          const data = await response.json();
          
          hideLoading();
          return data;
        } catch (error) {
          setLoadingText('加载失败');
          setTimeout(hideLoading, 1000);
          throw error;
        }
      }


   5. 页面加载动画
   
      window.addEventListener('load', () => {
        const loading = new LoadingAnimationSystem('#page-loader', {
          type: 'scroll',
          duration: 1500,
          text: '营造中华'
        });
        
        loading.show();
        
        setTimeout(() => {
          loading.hide();
        }, 2000);
      });
*/
