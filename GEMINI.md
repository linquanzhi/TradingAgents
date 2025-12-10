# Project Overview

This project is a multi-agent LLM financial trading framework called "TradingAgents". It uses a team of specialized AI agents to analyze market conditions and make trading decisions. The framework is built with Python, LangChain, and LangGraph.

The key components of the framework are:

*   **Analyst Team:** A team of specialized agents that analyze different aspects of the market, including:
    *   **Fundamentals Analyst:** Evaluates company financials and performance metrics.
    *   **Sentiment Analyst:** Analyzes social media and public sentiment.
    *   **News Analyst:** Monitors global news and macroeconomic indicators.
    *   **Technical Analyst:** Utilizes technical indicators to detect trading patterns.
*   **Researcher Team:** A team of agents that debate the findings of the Analyst Team to balance potential gains against inherent risks. This team includes a "bull" and a "bear" researcher.
*   **Trader Agent:** Makes the final trading decision based on the reports from the analysts and researchers.
*   **Risk Management and Portfolio Manager:** Evaluates portfolio risk and approves or rejects transaction proposals.

The framework is designed to be modular and extensible. The data sources, LLMs, and other parameters can be configured in the `tradingagents/default_config.py` file.

# Building and Running

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/TauricResearch/TradingAgents.git
    cd TradingAgents
    ```

2.  Create a virtual environment:
    ```bash
    conda create -n tradingagents python=3.13
    conda activate tradingagents
    ```

3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Required APIs

The project requires API keys for OpenAI and Alpha Vantage. You can set them as environment variables or create a `.env` file.

```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
export ALPHA_VANTAGE_API_KEY=$YOUR_ALPHA_VANTAGE_API_KEY
```

Alternatively, create a `.env` file:
```bash
cp .env.example .env
# Edit .env with your actual API keys
```

## Running the CLI

You can run the command-line interface (CLI) to interact with the TradingAgents framework:

```bash
python -m cli.main
```

The CLI allows you to select tickers, dates, LLMs, and other parameters.

## Running the Python Package

You can also use the `tradingagents` package in your own Python code. Here's an example:

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

# Development Conventions

*   **Configuration:** The project uses a centralized configuration file at `tradingagents/default_config.py`. You can override the default configuration by creating a new config dictionary and passing it to the `TradingAgentsGraph` constructor.
*   **Prompts:** The system prompts for each agent are located in `tradingagents/agents/utils/prompts.py`. This file supports both English and Chinese languages.
*   **Tools:** The tools available to the agents are defined in `tradingagents/agents/utils/`.
*   **Dataflows:** The dataflow modules in `tradingagents/dataflows/` are responsible for fetching data from various sources like Alpha Vantage, yfinance, and Google News.
*   **Graph:** The agent graph is constructed and managed by the `TradingAgentsGraph` class in `tradingagents/graph/trading_graph.py`. The graph logic is defined using LangGraph.
