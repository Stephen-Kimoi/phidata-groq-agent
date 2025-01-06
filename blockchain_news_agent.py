from urllib import response
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Always include complete source URLs for every news item, project, and claim",
        "Focus exclusively on Kenyan blockchain and crypto news",
        "Only include news from the last 30 days",
        "Prioritize local Kenyan news sources",
        "Include relevant tweets from Kenyan financial experts and institutions",
        "Search for news about KRA, CMA, and other regulatory bodies",
        "Check local financial news outlets and Twitter accounts",
        "Format each news item with: Title - Date - Description - Source URL"
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

# Optionally still print to terminal
agent.print_response(search_prompt, stream=True)

# Get response using print_response instead of run
response = ""
for chunk in agent.print_response(search_prompt, stream=True):
    response += chunk

print("Adding news to report...")

current_date = datetime.today().strftime('%Y-%m-%d')
news_file = f'articles/kenya-blockchain-news-{current_date}.md'

# Create articles directory if it doesn't exist
if not os.path.exists('articles'):
    os.makedirs('articles')

# Save to file with datetime
with open(news_file, 'w', encoding='utf-8') as f:
    f.write("# Kenya Blockchain and Crypto News Report\n\n")
    f.write(f"Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write(response)

print(f"News report generated and saved to {news_file}")