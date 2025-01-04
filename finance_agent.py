from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create a finance agent with YFinance capabilities
finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()], 
    show_tool_calls=True,
    markdown=True, 
    instructions=["Use tables to display the data"]
)

# Define the crypto analysis prompt
analysis_prompt = """
Analyze BTC-USD and ETH-USD. For each:
1. Get current price and trading volume
2. Compare key metrics and market indicators
3. Provide a summary of their current market position
4. Highlight notable differences between these two cryptocurrencies

Use actual data from Yahoo Finance tools to support your analysis.
"""

# Get the analysis
finance_agent.print_response(analysis_prompt)