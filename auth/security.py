from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException
from dotenv import load_dotenv
import os
import secrets

load_dotenv()

security = HTTPBasic()

def auth(credentials: HTTPBasicCredentials = Depends(security)):
    username_env = os.getenv("myusername", "admin")
    password_env = os.getenv("mypassword", "123")
    
    username_match = secrets.compare_digest(credentials.username, username_env)
    password_match = secrets.compare_digest(credentials.password, password_env)

    if not (username_match and password_match):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return credentials.username 
