## 问题说明

在使用 Qwen (千问) 模型时遇到了 401 认证错误。

## 根本原因

`langchain-openai` 的 `ChatOpenAI` 类默认会读取 `OPENAI_API_KEY` 环境变量，即使我们指定了自定义的 `base_url`。但是对于 Qwen，我们应该使用 `DASHSCOPE_API_KEY`。

## 解决方案

在 `trading_graph.py` 中，为 Qwen provider 单独处理，显式地：

1. 读取 `DASHSCOPE_API_KEY` 环境变量
2. 验证 API key 是否存在
3. 将 API key 传递给 `ChatOpenAI` 构造函数

## 使用方法

确保在 `.env` 文件中设置了 `DASHSCOPE_API_KEY`：

```bash
DASHSCOPE_API_KEY=your_actual_dashscope_api_key_here
```

然后重新运行程序即可。
