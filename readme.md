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
git clone https://github.com/你的用户名/你的仓库名.git

pip install -r requirements.txt