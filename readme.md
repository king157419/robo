# Robo-Desktop (桌面机器人桌宠) 🤖

> 一个基于 RTX 4070 本地算力的实体机器人/桌宠项目。
> 具备听觉、视觉（表情）、语音合成（情感克隆）与大模型思考能力。

## ✨ 功能特性 (Features)
- 👂 **听觉**: 本地部署 OpenAI Whisper (Small)，无需联网即可精准识别。
- 🧠 **大脑**: 接入 DeepSeek 大模型，支持情感识别与多轮对话。
- 🗣️ **嘴巴**: 集成 GPT-SoVITS V2，支持**情感语音合成**与**音色克隆**（告别机械音！）。
- 👀 **表情**: 基于 Pygame 的实时表情反馈，随对话情绪自动切换。

## 🛠️ 技术栈 (Tech Stack)
- **Language**: Python 3.10
- **AI Models**: GPT-SoVITS (TTS), OpenAI Whisper (STT), DeepSeek (LLM)
- **Libraries**: Pygame, Requests, Threading, SpeechRecognition

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
确保你拥有一张 6G 显存以上的 N 卡（推荐 RTX 3060/4070 及以上）。

```bash
# 克隆仓库
git clone https://github.com/king157419/robo.git
cd robo

# 安装依赖
pip install -r requirements.txt

# 配置 API Key
echo "API_KEY=your_deepseek_api_key" > .env
```

### 2. 运行方式 (How to Run)

#### 方式一：使用启动脚本（推荐，无需每次手动授权）

**Windows 用户:**
```bash
# 双击运行 run.bat 文件，或在命令行中执行：
run.bat
```

**Linux/Mac 用户:**
```bash
# 添加执行权限（首次运行需要）
chmod +x run.sh

# 运行启动脚本
./run.sh

# 或直接执行 main.py
chmod +x chat/main.py
./chat/main.py
```

#### 方式二：手动运行（传统方式）
```bash
cd chat
python main.py
```

#### 方式三：开机自启动（Linux 系统）

如需让 Robo-Desktop 开机自动启动，可以配置 systemd 服务：

```bash
# 1. 修改 robo-desktop.service 文件中的路径
# 将 /path/to/robo 替换为实际的项目路径

# 2. 复制服务文件到 systemd 目录
sudo cp robo-desktop.service /etc/systemd/system/

# 3. 重载 systemd 配置
sudo systemctl daemon-reload

# 4. 启用开机自启动
sudo systemctl enable robo-desktop.service

# 5. 立即启动服务
sudo systemctl start robo-desktop.service

# 查看服务状态
sudo systemctl status robo-desktop.service
```

### 3. 前置条件 (Prerequisites)

在运行之前，请确保：
1. ✅ 已安装 Python 3.10 及以上版本
2. ✅ 已配置 `.env` 文件并填入有效的 DeepSeek API Key
3. ✅ 已启动 GPT-SoVITS 服务（默认运行在 `http://127.0.0.1:9880`）
4. ✅ 准备好参考音频文件（用于音色克隆）
5. ✅ 麦克风正常工作

## 📝 注意事项 (Notes)

- **权限问题**: 如果遇到 "Permission Denied" 错误，请使用 `chmod +x` 为脚本添加执行权限。
- **路径配置**: `mouth.py` 中的参考音频路径需根据实际情况修改。
- **GPU 要求**: 推荐使用 NVIDIA GPU（6GB+ 显存），CPU 模式下推理速度较慢。

## 🐛 故障排除 (Troubleshooting)

1. **找不到模块错误**: 确保所有依赖已正确安装 `pip install -r requirements.txt`
2. **麦克风无法使用**: 检查系统麦克风权限设置
3. **TTS 生成失败**: 确认 GPT-SoVITS 服务正常运行
4. **API 调用失败**: 检查 `.env` 文件中的 API_KEY 是否正确