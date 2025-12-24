#!/bin/bash
# Robo-Desktop 启动脚本 (Startup Script for Linux/Mac)

echo "========================================"
echo "🤖 Robo-Desktop Starting..."
echo "========================================"

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 检查 Python3 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: Python3 未安装 (Error: Python3 is not installed)"
    echo "请先安装 Python3: https://www.python.org/downloads/"
    exit 1
fi

# 检查 .env 文件是否存在
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "⚠️  警告: .env 文件不存在 (Warning: .env file not found)"
    echo "请创建 .env 文件并配置 API_KEY"
    echo "Example: echo 'API_KEY=your_deepseek_api_key' > .env"
fi

# 检查依赖是否安装
echo "📦 检查依赖 (Checking dependencies)..."
python3 -c "import speech_recognition, whisper, pygame, openai" 2>/dev/null || {
    echo "⚠️  警告: 依赖未完全安装 (Warning: Dependencies not fully installed)"
    echo "正在安装依赖... (Installing dependencies...)"
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
}

# 启动应用
echo "🚀 启动 Robo-Desktop..."
cd "$SCRIPT_DIR/chat"
python3 main.py

# 捕获退出信号
echo ""
echo "👋 Robo-Desktop 已退出 (Robo-Desktop exited)"
