# TradingAgents 项目概览

TradingAgents 是一个多智能体交易框架，模拟了现实世界交易公司的动态。该项目通过部署专门的LLM驱动智能体，从基本面分析师、情绪专家和技术分析师到交易员、风险管理团队，共同评估市场状况并指导交易决策。此外，这些智能体还会进行动态讨论以确定最佳策略。

## 项目结构

```
TradingAgents/
├── .env.example                # 环境变量示例文件
├── .gitignore
├── LICENSE
├── README.md
├── main.py                     # 主程序入口
├── requirements.txt            # 依赖包列表
├── cli/                        # 命令行界面模块
│   ├── main.py                 # CLI 主程序
│   ├── models.py
│   ├── utils.py
│   └── static/
├── tradingagents/              # 核心交易智能体模块
│   ├── default_config.py       # 默认配置文件
│   ├── agents/                 # 智能体实现
│   │   ├── analysts/           # 分析师团队
│   │   ├── researchers/        # 研究员团队
│   │   ├── trader/             # 交易员智能体
│   │   ├── risk_mgmt/          # 风险管理团队
│   │   └── utils/              # 工具函数
│   ├── dataflows/              # 数据流处理
│   └── graph/                  # 智能体图结构
├── assets/                     # 项目资源文件
└── results/                    # 结果输出目录
```

## 核心组件

### 智能体团队
- **分析师团队**:
  - 基本面分析师: 评估公司财务和业绩指标，识别内在价值和潜在风险
  - 情绪分析师: 分析社交媒体和公众情绪，使用情绪评分算法
  - 新闻分析师: 监控全球新闻和宏观经济指标
  - 技术分析师: 使用技术指标（如MACD和RSI）检测交易模式

- **研究员团队**:
  - 包括看涨和看跌研究员，对分析师团队提供的见解进行批判性评估

- **交易员智能体**:
  - 综合分析师和研究员的报告做出交易决策

- **风险管理和投资组合经理**:
  - 评估投资组合风险并调整交易策略

### 框架依赖
- LangGraph: 用于构建和运行智能体图
- LLM提供商: OpenAI、Anthropic、Google等
- 数据提供商: Alpha Vantage、yfinance、Google News等

## 配置与使用

### 环境配置
需要设置OpenAI API密钥和Alpha Vantage API密钥：

```bash
export OPENAI_API_KEY=your_openai_api_key
export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

或者创建`.env`文件:

```
OPENAI_API_KEY=your_openai_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

### CLI 使用
```bash
python -m cli.main
```

### 代码集成使用

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# 前向传播
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

## 默认配置

```python
DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_cache_dir": os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")), "dataflows/data_cache"),
    # LLM 设置
    "llm_provider": "openai",
    "deep_think_llm": "o4-mini",
    "quick_think_llm": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    # 语言设置
    "language": "en",
    # 辩论和讨论设置
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # 数据提供商配置
    "data_vendors": {
        "core_stock_apis": "yfinance",
        "technical_indicators": "yfinance",
        "fundamental_data": "alpha_vantage",
        "news_data": "alpha_vantage",
    },
}
```

## 安装与运行

### 安装步骤

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
conda create -n tradingagents python=3.13
conda activate tradingagents
pip install -r requirements.txt
```

### 依赖包
主要依赖包括：
- langchain-openai
- langgraph
- yfinance
- pandas
- chainlit
- rich

## 开发约定

- 项目使用LangGraph确保灵活性和模块化
- 推荐使用`o4-mini`和`gpt-4o-mini`进行测试，以节省成本
- 遵循模块化设计，各智能体职责明确
- 支持多种LLM提供商和数据源配置
- 具有反思和记忆功能，能够从过去的交易中学习