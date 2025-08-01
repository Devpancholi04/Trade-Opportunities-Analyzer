import asyncio
from ddgs import DDGS

async def get_data(sector: str) -> list[str]:   

    with DDGS() as ddgs:
        result = [r["body"] for r in ddgs.text(f"Latest {sector} sector India's market")]
    
    return result

if __name__ == "__main__":
    result = asyncio.run(get_data("IT"))
    print(result)