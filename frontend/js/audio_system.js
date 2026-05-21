/**
 * 古建筑主题音效系统 - Audio System
 * 提供中国传统古建筑主题的音效交互
 * 
 * 音效类型：
 * 1. guzheng - 古筝音效
 * 2. bell - 钟声
 * 3. guqin - 古琴
 * 4. flute - 笛声
 * 5. chime - 磬声
 * 
 * @version 1.0
 * @date 2026-03-25
 */

class AudioSystem {
    constructor(options = {}) {
        this.options = {
            enabled: true,              // 启用音效
            volume: 0.3,                // 默认音量 (0-1)
            preload: true,              // 预加载
            autoPlay: false,            // 自动播放
            ...options
        };
        
        this.sounds = {};
        this.isEnabled = this.options.enabled;
        this.volume = this.options.volume;
        this.init();
    }

    /* ==================== 初始化 ==================== */
    init() {
        // 检查浏览器支持
        if (!this.checkAudioSupport()) {
            console.warn('浏览器不支持音频播放');
            this.isEnabled = false;
            return;
        }

        // 预加载音效
        if (this.options.preload) {
            this.preloadSounds();
        }
    }

    /* ==================== 检查音频支持 ==================== */
    checkAudioSupport() {
        try {
            const audio = new Audio();
            return !!audio.canPlayType;
        } catch (e) {
            return false;
        }
    }

    /* ==================== 预加载音效 ==================== */
    preloadSounds() {
        const soundList = ['guzheng', 'bell', 'guqin', 'flute', 'chime'];
        soundList.forEach(soundName => {
            this.loadSound(soundName);
        });
    }

    /* ==================== 加载音效 ==================== */
    loadSound(soundName) {
        // 使用Web Audio API创建音效或使用预录制的音频文件
        // 这里使用Web Audio API生成简单的音效
        
        if (typeof AudioContext !== 'undefined' || typeof webkitAudioContext !== 'undefined') {
            // Web Audio API方式
            this.sounds[soundName] = this.createWebAudioSound(soundName);
        } else {
            // 回退到HTML5 Audio
            this.sounds[soundName] = this.createHTMLAudioSound(soundName);
        }
    }

    /* ==================== 使用Web Audio API创建音效 ==================== */
    createWebAudioSound(soundName) {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        const sound = {
            context: audioContext,
            gainNode: audioContext.createGain(),
            play: () => this.playWebAudioSound(soundName, audioContext)
        };
        
        sound.gainNode.connect(audioContext.destination);
        sound.gainNode.gain.value = this.volume;
        
        return sound;
    }

    /* ==================== 播放Web Audio音效 ==================== */
    playWebAudioSound(soundName, audioContext) {
        if (!this.isEnabled) return;
        
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        // 根据音效类型设置参数
        switch (soundName) {
            case 'guzheng':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(440, audioContext.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(880, audioContext.currentTime + 0.5);
                gainNode.gain.setValueAtTime(this.volume * 0.5, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 1);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 1);
                break;
            
            case 'bell':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
                gainNode.gain.setValueAtTime(this.volume * 0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 2);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 2);
                break;
            
            case 'guqin':
                oscillator.type = 'triangle';
                oscillator.frequency.setValueAtTime(220, audioContext.currentTime);
                gainNode.gain.setValueAtTime(this.volume * 0.4, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 1.5);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 1.5);
                break;
            
            case 'flute':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(660, audioContext.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(880, audioContext.currentTime + 0.3);
                gainNode.gain.setValueAtTime(this.volume * 0.2, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.5);
                break;
            
            case 'chime':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(1200, audioContext.currentTime);
                gainNode.gain.setValueAtTime(this.volume * 0.2, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.8);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.8);
                break;
        }
    }

    /* ==================== 使用HTML5 Audio创建音效 ==================== */
    createHTMLAudioSound(soundName) {
        // 这里可以使用预录制的音频文件
        // 由于文件限制，这里返回模拟对象
        return {
            play: () => {
                if (!this.isEnabled) return;
                console.log(`播放${soundName}音效（模拟）`);
            }
        };
    }

    /* ==================== 播放音效 ==================== */
    play(soundName, options = {}) {
        if (!this.isEnabled || !this.sounds[soundName]) return;
        
        const sound = this.sounds[soundName];
        const volume = options.volume !== undefined ? options.volume : this.volume;
        
        // 设置音量
        if (sound.gainNode) {
            sound.gainNode.gain.value = volume;
        }
        
        // 播放
        sound.play();
        
        // 触发事件
        this.onPlay(soundName, options);
    }

    /* ==================== 播放完成回调 ==================== */
    onPlay(soundName, options) {
        if (options.onPlay) {
            options.onPlay(soundName);
        }
        
        // 触发自定义事件
        const event = new CustomEvent('audio:play', {
            detail: { soundName, options }
        });
        document.dispatchEvent(event);
    }

    /* ==================== 启用音效 ==================== */
    enable() {
        this.isEnabled = true;
    }

    /* ==================== 禁用音效 ==================== */
    disable() {
        this.isEnabled = false;
    }

    /* ==================== 设置音量 ==================== */
    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
        
        // 更新所有音效的音量
        Object.values(this.sounds).forEach(sound => {
            if (sound.gainNode) {
                sound.gainNode.gain.value = this.volume;
            }
        });
    }

    /* ==================== 静音 ==================== */
    mute() {
        this.previousVolume = this.volume;
        this.setVolume(0);
    }

    /* ==================== 取消静音 ==================== */
    unmute() {
        this.setVolume(this.previousVolume || 0.3);
    }

    /* ==================== 预加载音频文件 ==================== */
    preloadAudioFile(url, soundName) {
        const audio = new Audio(url);
        audio.preload = 'auto';
        
        this.sounds[soundName] = {
            audio: audio,
            play: () => {
                if (!this.isEnabled) return;
                audio.currentTime = 0;
                audio.volume = this.volume;
                audio.play().catch(e => console.log('音频播放失败:', e));
            }
        };
    }

    /* ==================== 绑定交互 ==================== */
    bindInteraction(selector, soundName, eventType = 'click') {
        const elements = document.querySelectorAll(selector);
        
        elements.forEach(element => {
            element.addEventListener(eventType, () => {
                this.play(soundName);
            });
        });
    }

    /* ==================== 自动绑定常见交互 ==================== */
    autoBindCommonInteractions() {
        // 按钮点击
        this.bindInteraction('button', 'guzheng', 'click');
        this.bindInteraction('.btn', 'guzheng', 'click');
        
        // 导航点击
        this.bindInteraction('.nav-link', 'flute', 'click');
        
        // 卡片悬停
        this.bindInteraction('.card', 'guqin', 'mouseenter');
        
        // 重要操作
        this.bindInteraction('.btn-primary', 'bell', 'click');
        this.bindInteraction('.btn-danger', 'chime', 'click');
    }

    /* ==================== 销毁 ==================== */
    destroy() {
        // 停止所有音频
        Object.values(this.sounds).forEach(sound => {
            if (sound.audio) {
                sound.audio.pause();
                sound.audio.currentTime = 0;
            }
        });
        
        // 清空音效
        this.sounds = {};
    }
}

/* ==================== 快捷方法 ==================== */

// 全局实例
let audioSystem = null;

// 初始化函数
function initAudioSystem(options = {}) {
    if (audioSystem) {
        audioSystem.destroy();
    }
    audioSystem = new AudioSystem(options);
    return audioSystem;
}

// 播放音效
function playSound(soundName, options = {}) {
    if (!audioSystem) {
        audioSystem = new AudioSystem();
    }
    audioSystem.play(soundName, options);
}

// 启用/禁用
function enableAudio() {
    if (audioSystem) audioSystem.enable();
}

function disableAudio() {
    if (audioSystem) audioSystem.disable();
}

// 音量控制
function setAudioVolume(volume) {
    if (audioSystem) audioSystem.setVolume(volume);
}

function muteAudio() {
    if (audioSystem) audioSystem.mute();
}

function unmuteAudio() {
    if (audioSystem) audioSystem.unmute();
}

/* ==================== 默认初始化 ==================== */

document.addEventListener('DOMContentLoaded', () => {
    // 初始化音效系统（默认禁用，需要用户交互后启用）
    audioSystem = new AudioSystem({
        enabled: false,
        volume: 0.3,
        preload: true
    });
});

/* ==================== 导出 ==================== */

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        AudioSystem,
        initAudioSystem,
        playSound,
        enableAudio,
        disableAudio,
        setAudioVolume,
        muteAudio,
        unmuteAudio
    };
}

/* ==========================================================================
   使用示例
   ========================================================================== 

   1. 基础使用
   
      // 初始化
      const audio = new AudioSystem();
      
      // 播放音效
      audio.play('guzheng');
      audio.play('bell', { volume: 0.5 });


   2. 交互绑定
   
      // 绑定按钮点击
      audio.bindInteraction('button', 'guzheng');
      
      // 绑定卡片悬停
      audio.bindInteraction('.card', 'guqin', 'mouseenter');
      
      // 自动绑定常见交互
      audio.autoBindCommonInteractions();


   3. 音量控制
   
      // 设置音量
      audio.setVolume(0.5);
      
      // 静音
      audio.mute();
      
      // 取消静音
      audio.unmute();


   4. 预加载音频文件
   
      // 使用预录制的音频
      audio.preloadAudioFile('/sounds/guzheng.mp3', 'guzheng');
      audio.preloadAudioFile('/sounds/bell.mp3', 'bell');
      
      // 播放预加载的音频
      audio.play('guzheng');


   5. 在页面事件中使用
   
      // 页面加载完成
      window.addEventListener('load', () => {
        playSound('bell', { volume: 0.2 });
      });
      
      // 点击建筑卡片
      document.querySelectorAll('.building-card').forEach(card => {
        card.addEventListener('click', () => {
          playSound('guqin');
        });
      });


   6. 切换音效开关
   
      <button onclick="toggleAudio()">
        <span id="audio-status">音效: 关</span>
      </button>
      
      <script>
        let audioEnabled = false;
        
        function toggleAudio() {
          const status = document.getElementById('audio-status');
          
          if (audioEnabled) {
            disableAudio();
            status.textContent = '音效: 关';
          } else {
            enableAudio();
            status.textContent = '音效: 开';
          }
          
          audioEnabled = !audioEnabled;
        }
      </script>


   7. 在React中使用
   
      import { initAudioSystem, playSound } from './audio_system.js';
      
      function BuildingCard({ building }) {
        const handleClick = () => {
          playSound('guqin');
          // 其他逻辑
        };
        
        return (
          <div className="building-card" onClick={handleClick}>
            {building.name}
          </div>
        );
      }
*/
