from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ai.gemini_client import analyze_sector
from data.market_scraper import get_data
from utils import rate_limiter, session_manager, save_md
from dotenv import load_dotenv
from auth.security import auth
from uuid import uuid4


app = FastAPI(
    title="Trade Opportunities Analyzer",
    description="API for sector-wise Indian trade opportunity reports.",
    version='1.0'
)

session_manager = session_manager.SessionManager(session_timeout=3600)
rate_limiter = rate_limiter.RateLimiter(session_manager, max_requests_per_hours=10)

security = HTTPBasic()

@app.get("/analyze/{sector}")
async def AnalyzeSector(
    sector,
    credentails = Depends(security),
):
    
    if credentails is None:
        raise HTTPException(status_code=401, detail="Authentication Required.")
    
    user_id = auth(credentails)

    session_id = user_id

    session_data = session_manager.get_session(session_id)
    if not session_data:
        session_manager.Create_session(session_id, {"requests_made": 1})
    else:
        session_manager.update_session(session_id, {"requests_made": session_data.get("requests_made", 0) + 1})

    
    if not (sector.isalpha() and 3 <= len(sector) <= 32):
        raise HTTPException(status_code=400, detail="Sector name must be alphabetic and 3-32 characters.")
    
    if not rate_limiter.allow(session_id):
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")
    
    try:
        market_data = await get_data(sector)
        if not market_data:
            raise HTTPException(status_code=404, detail=f"No Data Found for {sector} Sector.")
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Data fetch Failed : {e}")

    try:
        markdown_report = await analyze_sector(sector, market_data)
        file_path = save_md.save_md_file(sector, markdown_report)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI analysis failed : {e}")
    

    return markdown_report