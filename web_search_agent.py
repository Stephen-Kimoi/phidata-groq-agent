from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

# web_agent = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=OpenAIChat(id="gpt-4o"), 
#     tools=[DuckDuckGo()],
#     show_tool_calls=True,
#     markdown=True,
#     instructions=["Always include the source URL in your response", "Always use the most recent data available"]
# )

# finance_agent = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=OpenAIChat(id="gpt-4o"), 
#     tools=[YFinanceTools()], 
#     show_tool_calls=True,
#     markdown=True, 
#     instructions=["Use tables to display the data"]
# )

# agent_team = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=OpenAIChat(id="gpt-4o"), 
#     tools=[web_agent, finance_agent],
#     show_tool_calls=True,
#     markdown=True,
#     instructions=[
#         "Always include the source URL in your response", 
#         "Always use the most recent data available", 
#         "Use tables to display the data"
#     ]
# )

# Create a single agent with both DuckDuckGo and YFinanceTools
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), YFinanceTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include the source URL in your response",
        "Always use the most recent data available",
    ]
)

agent.print_response("Share the latest news for BTC-USD and ETH-USD.", stream=True)