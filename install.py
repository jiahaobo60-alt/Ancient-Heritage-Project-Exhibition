"""
飞檐翚影 / 营造中华  环境检测与安装脚本  v1.0 (Python 备用方案)
=============================================================
功能与 install.bat 完全一致，作为 bat 脚本闪退时的备用方案。
使用方法: 双击运行 或 命令行执行 python install.py
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# ============================================================
#  全局配置
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = SCRIPT_DIR / "backend"
ADMIN_DIR = SCRIPT_DIR / "admin-frontend"
VENV_DIR = BACKEND_DIR / ".venv"
REQ_FILE = BACKEND_DIR / "requirements.txt"

PIP_MIRRORS = [
    "https://mirrors.aliyun.com/pypi/simple/",
    "https://pypi.tuna.tsinghua.edu.cn/simple/",
]
PIP_TRUSTED_HOSTS = {
    "https://mirrors.aliyun.com/pypi/simple/": "mirrors.aliyun.com",
    "https://pypi.tuna.tsinghua.edu.cn/simple/": "pypi.tuna.tsinghua.edu.cn",
}

NPM_MIRRORS = [
    "https://registry.npmmirror.com",
    None,  # 官方源
]

# 统计
ERR_COUNT = 0
WARN_COUNT = 0


# ============================================================
#  工具函数
# ============================================================
def run(cmd, capture=False, check=False, cwd=None, env=None):
    """运行外部命令并返回 CompletedProcess。"""
    kwargs = dict(shell=True, cwd=cwd)
    if capture:
        kwargs.update(stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      text=True, encoding="utf-8", errors="replace")
    if env:
        merged = os.environ.copy()
        merged.update(env)
        kwargs["env"] = merged
    result = subprocess.run(cmd, **kwargs)
    if check and result.returncode != 0:
        out = result.stdout.strip() if capture else ""
        err = result.stderr.strip() if capture else ""
        raise RuntimeError(f"命令执行失败: {cmd}\n  stdout: {out}\n  stderr: {err}")
    return result


def print_step(step, total, title):
    print()
    print("=" * 58)
    print(f"  STEP {step}/{total}  {title}")
    print("=" * 58)
    print()


def ok(msg):
    print(f"  [OK] {msg}")


def fail(msg):
    global ERR_COUNT
    ERR_COUNT += 1
    print(f"  [X] {msg}")


def warn(msg):
    global WARN_COUNT
    WARN_COUNT += 1
    print(f"  [!] {msg}")


def info(msg):
    print(f"  [>> {msg}]")


def ask_yes_no(prompt, default=True):
    """交互式是/否提问。"""
    hint = "Y/n" if default else "y/N"
    try:
        answer = input(f"  {prompt} [{hint}]: ").strip().upper()
    except (EOFError, KeyboardInterrupt):
        print()
        return default
    if not answer:
        return default
    return answer == "Y"


def find_python():
    """
    按优先级查找可用的 Python 解释器。
    返回 (python_exe_path_or_name, version_string) 或 (None, None)。
    """
    # 候选命令
    candidates = ["python", "python3"]
    # 候选路径 (Windows 常见安装位置)
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    candidate_paths = [
        Path("C:/Python312/python.exe"),
        Path("C:/Python311/python.exe"),
        Path(local_app_data) / "Programs/Python/Python312/python.exe" if local_app_data else None,
        Path(local_app_data) / "Programs/Python/Python311/python.exe" if local_app_data else None,
    ]
    candidate_paths = [p for p in candidate_paths if p is not None]

    for cmd in candidates:
        r = run(f'"{cmd}" --version', capture=True)
        if r.returncode == 0 and r.stdout.strip():
            ver = r.stdout.strip().split()[-1] if r.stdout.strip() else "unknown"
            return cmd, ver

    for p in candidate_paths:
        if p.exists():
            r = run(f'"{p}" --version', capture=True)
            if r.returncode == 0 and r.stdout.strip():
                ver = r.stdout.strip().split()[-1] if r.stdout.strip() else "unknown"
                return str(p), ver

    return None, None


def get_venv_python():
    """获取虚拟环境中的 python 路径。"""
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"


def get_venv_pip():
    """获取虚拟环境中的 pip 路径。"""
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "pip.exe"
    else:
        return VENV_DIR / "bin" / "pip"


def pip_install_requirements():
    """使用多源回退安装 requirements.txt。"""
    pip_exe = str(get_venv_pip())
    for mirror in PIP_MIRRORS:
        cmd = f'"{pip_exe}" install -r "{REQ_FILE}"'
        if mirror:
            host = PIP_TRUSTED_HOSTS[mirror]
            cmd += f' -i {mirror} --trusted-host {host}'
            info(f"使用镜像源: {mirror}")
        else:
            info("使用官方源")
        r = run(cmd)
        if r.returncode == 0:
            return True
        if mirror:
            warn(f"当前源安装失败, 尝试下一个源...")
    return False


def npm_install():
    """使用多源回退执行 npm install。"""
    for mirror in NPM_MIRRORS:
        cmd = "npm install"
        if mirror:
            cmd += f" --registry {mirror}"
            info(f"使用镜像源: {mirror}")
        else:
            info("使用官方源")
        r = run(cmd, cwd=str(ADMIN_DIR))
        if r.returncode == 0:
            return True
        if mirror:
            warn(f"当前源安装失败, 尝试下一个源...")
    return False


# ============================================================
#  主流程
# ============================================================
def main():
    global ERR_COUNT, WARN_COUNT

    os.system("chcp 65001 >nul 2>&1" if sys.platform == "win32" else "clear")
    if sys.platform == "win32":
        try:
            os.system("title 飞檐翚影 - 环境检测与安装")
        except Exception:
            pass

    # ===================== 欢迎界面 =====================
    print()
    print("=" * 58)
    print("    飞檐翚影 / 营造中华  环境检测与安装  v1.0")
    print("              (Python 备用方案)")
    print("=" * 58)
    print()
    print("  本脚本将自动检测并安装以下环境:")
    print("    - Python 3.12  (后端运行环境)")
    print("    - Python 虚拟环境 + 后端依赖 (requirements.txt)")
    print("    - Node.js 20 LTS (Vue 管理后台构建环境)")
    print("    - npm 依赖 (admin-frontend/package.json)")
    print("    - 数据库初始化迁移 (Django migrate)")
    print()
    print("  建议以管理员身份运行本脚本以避免权限问题")
    print()
    input("  按回车键开始, Ctrl+C 可随时取消...")
    print()

    # ===================== STEP 1: 项目目录检查 =====================
    print_step(1, 6, "项目目录完整性检查")

    required_files = [
        (BACKEND_DIR / "manage.py", "backend/manage.py"),
        (REQ_FILE, "backend/requirements.txt"),
        (ADMIN_DIR / "package.json", "admin-frontend/package.json"),
    ]

    dir_ok = True
    for filepath, display_name in required_files:
        if filepath.exists():
            ok(display_name)
        else:
            fail(f"缺少 {display_name}")
            dir_ok = False

    if not dir_ok:
        print()
        print("  [错误] 项目目录结构不完整!")
        print("  请确认脚本放置在项目根目录!")
        print()
        input("  按回车键退出...")
        return

    print()
    ok("项目目录验证通过")

    # ===================== STEP 2: Python 检测 =====================
    print_step(2, 6, "Python 3.12 检测")

    python_cmd, py_ver = find_python()
    python_ok = False

    if python_cmd:
        ok(f"检测到 Python {py_ver}")
        python_ok = True
    else:
        fail("未检测到 Python!")
        print()
        print("  需要安装 Python 3.12 (推荐):")
        print("    方式一: 通过 winget 自动安装")
        print("    方式二: 手动下载 https://www.python.org/downloads/")
        print()

        if ask_yes_no("是否通过 winget 自动安装 Python 3.12?"):
            info("winget install Python.Python.3.12 ...")
            r = run(
                "winget install --id Python.Python.3.12 --source winget "
                "--accept-source-agreements --accept-package-agreements"
            )
            if r.returncode == 0:
                ok("Python 3.12 安装完成!")
                print("  请关闭本窗口后重新运行脚本")
                print()
                input("  按回车键退出...")
                return
            else:
                fail("winget 安装失败, 请手动安装 Python 3.12")
        else:
            warn("请手动安装后重新运行本脚本")

    print()
    if python_ok:
        ok("Python 已就绪")

    # ===================== STEP 3: 虚拟环境 =====================
    print_step(3, 6, "Python 虚拟环境 + 后端依赖")

    venv_created = False

    if not python_ok:
        warn("Python 未就绪, 跳过虚拟环境配置")
    else:
        venv_python = get_venv_python()
        if venv_python.exists():
            ok("虚拟环境已存在")
            venv_created = True
        else:
            info("创建虚拟环境...")
            r = run(f'"{python_cmd}" -m venv "{VENV_DIR}"')
            if r.returncode == 0:
                ok("虚拟环境创建成功")
                venv_created = True
            else:
                fail("虚拟环境创建失败!")

        if venv_created:
            # 升级 pip
            info("升级 pip...")
            r = run(f'"{get_venv_pip()}" install --upgrade pip -q')
            if r.returncode == 0:
                ok("pip 已升级")
            else:
                warn("pip 升级失败, 使用当前版本")

            # 检查 Django 是否已安装
            r = run(f'"{get_venv_python()}" -c "import django; print(django.__version__)"',
                    capture=True)
            if r.returncode == 0:
                ver = r.stdout.strip()
                ok(f"Django {ver} 已安装")
                ok("依赖已就绪")
            else:
                info("安装 backend 依赖 (requirements.txt), 请耐心等待...")
                print()
                if pip_install_requirements():
                    ok("后端依赖安装完成")
                else:
                    fail("依赖安装失败! 请检查网络连接!")

    # ===================== STEP 4: Node.js =====================
    print_step(4, 6, "Node.js 20 LTS 检测")

    node_ok = False
    r = run("node --version", capture=True)
    if r.returncode == 0 and r.stdout.strip():
        ok(f"检测到 Node.js {r.stdout.strip()}")
        node_ok = True
    else:
        fail("未检测到 Node.js!")
        print()

        if ask_yes_no("是否通过 winget 自动安装 Node.js 20 LTS?"):
            info("winget install OpenJS.NodeJS.LTS ...")
            r = run(
                "winget install --id OpenJS.NodeJS.LTS --source winget "
                "--accept-source-agreements --accept-package-agreements"
            )
            if r.returncode == 0:
                ok("Node.js 安装完成! 请关闭本窗口后重新运行脚本")
                print()
                input("  按回车键退出...")
                return
            else:
                fail("winget 安装失败, 请手动安装 Node.js")
        else:
            warn("请手动安装 Node.js 后重新运行本脚本")

    # ===================== STEP 5: npm =====================
    print_step(5, 6, "npm 依赖安装 (admin-frontend)")

    if not node_ok:
        warn("Node.js 未就绪, 跳过 npm 安装")
    elif (ADMIN_DIR / "node_modules" / "vite").exists():
        ok("node_modules 已安装")
    else:
        info("安装 npm 依赖, 请耐心等待...")
        print()
        if npm_install():
            ok("npm 依赖安装完成")
        else:
            fail("npm install 失败!")

    # ===================== STEP 6: 数据库 =====================
    print_step(6, 6, "数据库初始化 (Django migrate)")

    db_file = BACKEND_DIR / "db.sqlite3"

    if not python_ok:
        warn("Python 未就绪, 跳过数据库迁移")
    elif db_file.exists():
        ok("db.sqlite3 已存在 (包含现有数据, 跳过 migrate)")
    else:
        info("首次运行, 执行数据库迁移...")
        venv_python = get_venv_python()
        cmd = f'"{venv_python}" manage.py migrate'
        r = run(cmd, cwd=str(BACKEND_DIR))
        if r.returncode == 0:
            ok("数据库迁移完成")
        else:
            fail("数据库迁移失败!")

    # ===================== 最终报告 =====================
    print()
    print("=" * 58)
    print("  环境状态报告 + 项目可运行性判断")
    print("=" * 58)
    print()

    runnable = True

    # Python
    r = run("python --version", capture=True)
    if r.returncode == 0:
        ok("Python: 已安装")
    else:
        fail("Python: 未安装")
        runnable = False

    # 虚拟环境
    venv_python = get_venv_python()
    if venv_python.exists():
        ok("虚拟环境: 已创建")
    else:
        warn("虚拟环境: 未创建")

    # Django
    if venv_python.exists():
        r = run(f'"{venv_python}" -c "import django"', capture=True)
        if r.returncode == 0:
            ok("Django: 已安装")
        else:
            fail("Django: 未安装")
            runnable = False
    else:
        fail("Django: 未安装 (虚拟环境不存在)")
        runnable = False

    # Node.js
    r = run("node --version", capture=True)
    if r.returncode == 0:
        ok("Node.js: 已安装")
    else:
        fail("Node.js: 未安装")
        runnable = False

    # node_modules
    if (ADMIN_DIR / "node_modules" / "vite").exists():
        ok("node_modules: 已安装")
    else:
        fail("node_modules: 未安装")
        runnable = False

    print()
    print("-" * 58)
    print("  项目可运行性判断")
    print("-" * 58)
    print()

    if runnable:
        ok("项目可以运行! 所有关键环境均已就绪")
        print()
        print(f"  错误: {ERR_COUNT}   警告: {WARN_COUNT}")
        print()
        print("  下一步: 双击 [启动项目.bat] 即可一键启动所有服务")
    else:
        print(f"  [X] 项目暂时无法运行, 存在 {ERR_COUNT} 个关键错误")
        print()
        print("  请根据上方 [X] 标记的项目进行修复:")
        print("    1. 若 Python 缺失      - 重新运行本脚本并选择安装")
        print("    2. 若 Django 缺失      - 删除 backend/.venv 后重新运行本脚本")
        print("    3. 若 Node.js 缺失     - 重新运行本脚本并选择安装")
        print("    4. 若 node_modules 缺失 - 重新运行本脚本")

    print()
    print("  服务访问地址 (启动后):")
    print("       http://localhost:8000        后端 API + 前端主页")
    print("       http://localhost:9527        Vue 管理后台")
    print()
    input("  按回车键退出...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  用户中断, 脚本退出。")
    except Exception as e:
        print(f"\n  [严重错误] 未预期的异常: {e}")
        import traceback
        traceback.print_exc()
        input("\n  按回车键退出...")
