import time
import json


def create_risky_debator(llm):
    def risky_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        risky_history = risk_debate_state.get("risky_history", "")

        current_safe_response = risk_debate_state.get("current_safe_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        trader_decision = state["trader_investment_plan"]

        prompt = f"""作为激进风险分析师，你的角色是积极倡导高回报、高风险的机会，强调大胆的策略和竞争优势。在评估交易员的决定或计划时，重点关注潜在的上行空间、增长潜力和创新效益——即使这些伴随着更高的风险。使用提供的市场数据和情绪分析来加强你的论点并挑战相反的观点。具体来说，直接回应保守和中性分析师提出的每个观点，用数据驱动的反驳和有说服力的推理进行回应。强调他们的谨慎可能会错过关键机会，或者他们的假设可能过于保守。这是交易员的决定：

{trader_decision}

你的任务是通过质疑和批评保守和中性立场来为交易员的决定创建一个引人入胜的案例，以证明为什么你的高回报观点提供了最佳前进道路。将以下来源的见解融入到你的论点中：

市场研究报告：{market_research_report}
社交媒体情绪报告：{sentiment_report}
最新世界事务报告：{news_report}
公司基本面报告：{fundamentals_report}
这是当前的对话历史：{history} 这是保守分析师的最新论点：{current_safe_response} 这是中性分析师的最新论点：{current_neutral_response}。如果没有来自其他观点的回应，请不要虚构，只需提出你的观点。

通过解决提出的任何具体关切、反驳他们逻辑中的弱点并断言承担风险的好处来积极参与，以超越市场常态。专注于辩论和说服，而不仅仅是呈现数据。挑战每个反论点以强调高风险方法为何是最佳选择。以对话的方式输出，就像你在说话一样，不使用任何特殊格式。"""

        response = llm.invoke(prompt)

        argument = f"Risky Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "risky_history": risky_history + "\n" + argument,
            "safe_history": risk_debate_state.get("safe_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Risky",
            "current_risky_response": argument,
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response": risk_debate_state.get(
                "current_neutral_response", ""
            ),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return risky_node
