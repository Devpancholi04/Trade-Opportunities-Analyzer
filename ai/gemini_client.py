import sys
import os
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.market_scraper import get_data 

genai.configure(api_key=os.getenv('api_key'))

async def analyze_sector(sector: str, data: list[str]) -> str:
    joined_data = "\n\n".join(data)

#     prompt = f"""
# Analyze the following news data for the {sector} sector in India and provide a structured markdown report:

# {joined_data}

# Format:
# # {sector.capitalize()} Sector Market Analysis
# ## Summary
# ...
# ## Trade Opportunities
# ...
# ## Risks & Outlook
# ...
# """
    prompt = f"""
    Analyze the current Indian {sector} sector based on the following news and data:
    {joined_data}
    Highlight key trends, risks, and concrete trade opportunities in markdown format.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    sector = "IT"
    result = asyncio.run(get_data(sector))
    print("Fetched Data:\n", result)

    report = asyncio.run(analyze_sector(sector, result))
    print("\nGenerated Report:\n", report)
