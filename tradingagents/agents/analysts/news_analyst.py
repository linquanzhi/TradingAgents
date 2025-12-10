from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
from tradingagents.agents.utils.agent_utils import get_news, get_global_news
from tradingagents.dataflows.config import get_config


def create_news_analyst(llm):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]

        tools = [
            get_news,
            get_global_news,
        ]

        system_message = (
            "你是一位新闻研究员，负责分析过去一周的最新新闻和趋势。请撰写一份全面的报告，说明与交易和宏观经济相关的当前世界状况。使用可用的工具：get_news(query, start_date, end_date) 用于公司特定或目标新闻搜索，get_global_news(curr_date, look_back_days, limit) 用于更广泛的宏观经济新闻。不要简单地说趋势混合，要提供详细和细致的分析和见解，以帮助交易者做出决策。"
            + """ 请确保在报告末尾附加一个Markdown表格，以整理报告中的要点，使其有组织且易于阅读。"""
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一个有用的AI助手，与其他助手协作。"
                    " 使用提供的工具来推进回答问题。"
                    " 如果你无法完全回答，没关系；另一个拥有不同工具的助手"
                    " 将在你停止的地方继续帮助。执行你能做的来取得进展。"
                    " 如果你或其他助手有最终交易提案：**买入/持有/卖出**或可交付成果，"
                    " 请在你的回复前加上最终交易提案：**买入/持有/卖出**，以便团队知道停止。"
                    " 你可以访问以下工具：{tool_names}。\n{system_message}"
                    "供您参考，当前日期是{current_date}。我们正在关注公司{ticker}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)

        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "news_report": report,
        }

    return news_analyst_node
