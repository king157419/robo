# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-12-07
### 🚀 Major Features (重大特性)
- **GPT-SoVITS Integration**: 实现了本地 TTS 模型的接入，替换了原有的 Edge-TTS，支持声音克隆。
- **Emotion System**: 新增情感映射逻辑，实现了 `Brain` (文本情绪识别) -> `Face` (表情变化) -> `Mouth` (情感语音) 的多模态联动。
- **Face Module**: 基于 Pygame 实现了基础的 GUI 界面，根据不同情感（开心/难过/生气等）改变眼睛颜色和大小。

### 🔄 Changed (变更)
- **Architecture**: 重构了 `main.py`，采用多线程 (`threading`) 分离 UI 渲染与 AI 逻辑，解决了画面卡顿问题。
- **API Handling**: 重写了 `mouth.py`，改为通过 HTTP 请求直接调用 GPT-SoVITS 的 API 接口。

### ⚠️ Known Issues (已知问题)
- **Latency**: 本地 TTS 推理速度较慢，对话延迟较高。
- **Audio Quality**: 偶尔存在电音/白噪音问题（疑似 FP16 精度问题）。
- **STT Hallucination**: Whisper 在安静环境下偶尔会出现幻觉（输出无意义文本）。
- **Code Structure**: 部分文件路径硬编码，尚未抽离为配置文件。

---

## [0.0.1] - 2025-12-02 (Initial Proof of Concept)
### Added
- 完成了基础架构：`Ear` (Whisper Small) + `Brain` (DeepSeek API) + `Mouth` (Edge-TTS)。
- 实现了基础的语音转文字与文字转语音流程。

### 🐛 Fixed (修复)
- 修复了 `api_key` 硬编码导致的安全隐患，引入 `python-dotenv` 管理环境变量。
- 修复了 Git 缓存未清除导致 `.gitignore` 失效的问题。