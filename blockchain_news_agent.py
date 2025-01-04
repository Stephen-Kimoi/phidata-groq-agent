from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include the source URL in your response",
        "Focus exclusively on Kenyan blockchain and crypto news",
        "Only include news from the last 30 days",
        "Prioritize local Kenyan news sources", 
        "Include relevant tweets from Kenyan financial experts and institutions",
        "Search for news about KRA, CMA, and other regulatory bodies", 
        "Check local financial news outlets and Twitter accounts"
    ]
)

# Simplified search prompt to reduce complexity
search_prompt = """
Find the most recent (within last 10 days) blockchain and cryptocurrency news specifically from Kenya, including:
- KRA updates on crypto taxation
- CMA regulations and licenses
- Crypto adoption trends in Kenya
- Local blockchain projects and tokenization

Sort results by date (newest first) and include the publication date for each item.
"""

agent.print_response(search_prompt, stream=True)