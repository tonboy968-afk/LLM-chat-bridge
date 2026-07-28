# LLM Chat Bridge

轻量级局域网聊天界面，连接本地 LLM 服务（LM Studio / Ollama 等），支持多设备共享访问。

## 功能

- **多轮对话** - 上下文记忆，流式响应
- **深色模式** - 工具栏一键切换，自动保存偏好
- **局域网共享** - 设置页面显示访问地址，一键复制
- **响应式设计** - 手机、平板、电脑自适应
- **本地存储** - 对话历史保存在浏览器

## 快速开始

### 1. 启动 LLM 服务

确保 LM Studio 或 Ollama 已启动并开放 API：

```
LM Studio:  http://192.168.10.8:1234
Ollama:     http://localhost:11434
```

### 2. 启动聊天服务

```bash
python start-chat-server.py
```

输出示例：
```
==================================================
本机访问: http://localhost:8765/lmstudio-chat.html
网络访问: http://192.168.10.80:8765/lmstudio-chat.html
==================================================
```

### 3. 访问界面

- **本机**: http://localhost:8765/lmstudio-chat.html
- **局域网设备**: http://192.168.10.80:8765/lmstudio-chat.html

## 配置

点击右上角「设置」按钮：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| API 地址 | LLM 服务地址 | http://192.168.10.8:1234 |
| 模型 | 指定模型名称（可选） | 空（自动选择） |

## 文件说明

```
├── index.html              # 聊天界面（GitHub Pages 用）
├── lmstudio-chat.html      # 聊天界面（本地用）
├── start-chat-server.py    # Python HTTP 服务器（端口 8765）
└── README.md
```

## 注意事项

1. LM Studio 需开启 CORS（Server → Enable CORS）
2. 防火墙需放行 8765 端口
3. 直接双击 HTML 文件只能本机使用，局域网访问需启动服务器

## License

MIT
