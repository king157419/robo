@echo off
REM Robo-Desktop 启动脚本 (Startup Script for Windows)
chcp 65001 >nul

echo ========================================
echo 🤖 Robo-Desktop Starting...
echo ========================================

REM 获取脚本所在目录
cd /d "%~dp0"

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: Python 未安装 ^(Error: Python is not installed^)
    echo 请先安装 Python: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查 .env 文件是否存在
if not exist ".env" (
    echo ⚠️  警告: .env 文件不存在 ^(Warning: .env file not found^)
    echo 请创建 .env 文件并配置 API_KEY
    echo Example: echo API_KEY=your_deepseek_api_key ^> .env
)

REM 检查依赖是否安装
echo 📦 检查依赖 ^(Checking dependencies^)...
python -c "import speech_recognition, whisper, pygame, openai" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  警告: 依赖未完全安装 ^(Warning: Dependencies not fully installed^)
    echo 正在安装依赖... ^(Installing dependencies...^)
    pip install -r requirements.txt
)

REM 启动应用
echo 🚀 启动 Robo-Desktop...
cd chat
python main.py

REM 等待用户按键
echo.
echo 👋 Robo-Desktop 已退出 ^(Robo-Desktop exited^)
pause
