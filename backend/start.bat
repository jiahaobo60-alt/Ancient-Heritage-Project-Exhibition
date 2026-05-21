@echo off
chcp 65001 >nul
echo ========================================
echo   启动 Django 服务器 (端口 80)
echo ========================================
echo.
echo 注意: 如果启动失败，请以管理员身份运行此脚本
echo.
python manage.py runserver 80
pause
