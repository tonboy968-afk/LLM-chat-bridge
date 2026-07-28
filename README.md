<div align="center">

<img src="https://img.shields.io/badge/version-v1.1.0-blue.svg" alt="Version">
<img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
<img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform">

# LLM Chat Bridge

**轻量级局域网 LLM 聊天网关**

*一个 HTML 文件，连接本地 LLM，支持多设备共享访问*

[快速开始](#-快速开始) · [功能特性](#-功能特性) · [配置说明](#-配置)

</div>

---

## 📖 项目简介

LLM Chat Bridge 是一款**零依赖、单文件**的 LLM 聊天网关，专为本地 LLM 服务（LM Studio、Ollama 等）设计。通过内置 Python HTTP 服务器，实现局域网内多设备共享访问，让家人朋友也能使用你的本地 AI。

**设计理念：**
- 📄 **单文件架构** - 核心 `index.html` 仅 35KB，无需构建、无需依赖
- 🌐 **局域网优先** - 内置服务器自动获取本机 IP，一键共享
- 🔒 **本地优先** - 数据不离开局域网，对话历史保存在浏览器本地存储
- 🎨 **开箱即用** - 7 个预设角色 + 自定义角色，深色模式，流式响应

**适用场景：**
- 家庭共享本地 LLM 服务
- 小型团队内部 AI 助手
- 本地 LLM 开发测试
- 离线环境下的 AI 对话

---

## ✨ 功能特性

| 特性 | 描述 |
|------|------|
| 💬 **多轮对话** | 上下文记忆，流式响应，对话历史本地存储 |
| 🌙 **深色模式** | 工具栏一键切换，自动保存偏好 |
| 🌐 **局域网共享** | 设置页显示访问地址 + 一键复制 |
| 🎭 **预设角色** | 7 个内置角色（助手、翻译、程序员等）+ 自定义角色 |
| 📱 **响应式设计** | 手机、平板、电脑自适应布局 |
| 🔌 **多 LLM 支持** | LM Studio、Ollama、vLLM 等标准 OpenAI API 兼容服务 |

---

## 🚀 快速开始

### 环境要求

- Python 3.6+（用于启动 HTTP 服务器）
- LM Studio / Ollama / 其他本地 LLM 服务

### 1. 启动 LLM 服务

确保 LM Studio 或 Ollama 已启动并开放 API：

```bash
# LM Studio: 启动服务器并开启 CORS
# Server → Enable CORS ✓

# Ollama: 默认监听 localhost:11434
ollama serve
```

### 2. 启动聊天服务

```bash
python start-chat-server.py
```

终端输出：
```
==================================================
LM Studio Chat 服务器已启动
本机访问: http://localhost:8765/lmstudio-chat.html
网络访问: http://192.168.10.80:8765/lmstudio-chat.html
==================================================
其他设备请访问上面的'网络访问'地址
按 Ctrl+C 停止服务器
==================================================
```

### 3. 访问界面

| 设备 | 访问地址 |
|------|----------|
| 本机 | http://localhost:8765/lmstudio-chat.html |
| 局域网设备 | http://`{本机IP}`:8765/lmstudio-chat.html |

---

## ⚙️ 配置说明

点击右上角「设置」按钮进行配置：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| API 地址 | LLM 服务地址 | `http://192.168.10.8:1234` |
| 模型 | 指定模型名称（可选） | 空（自动选择） |

### 防火墙配置

Windows 防火墙需放行 8765 端口：

```powershell
# 添加防火墙规则
netsh advfirewall firewall add rule name="LLM Chat Bridge" dir=in action=allow protocol=tcp localport=8765
```

---

## 📁 文件说明

```
├── index.html              # 聊天界面（GitHub Pages 部署用）
├── lmstudio-chat.html      # 聊天界面（本地使用）
├── start-chat-server.py    # Python HTTP 服务器
└── README.md
```

---

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| 前端 | 原生 HTML + CSS + JavaScript |
| 服务器 | Python http.server |
| API | OpenAI API 兼容格式 |
| 存储 | localStorage |

---

## 📋 使用注意事项

1. **CORS 配置** - LM Studio 需开启 CORS（Server → Enable CORS）
2. **端口占用** - 默认端口 8765，可修改 `start-chat-server.py` 中的 `PORT` 变量
3. **本地模式** - 直接双击 HTML 文件仅支持本机使用，无法局域网访问
4. **数据安全** - 对话历史保存在浏览器本地存储，清除浏览器数据会丢失

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 协议

[MIT License](./LICENSE) - Copyright © 2026

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐ Star！**

</div>
