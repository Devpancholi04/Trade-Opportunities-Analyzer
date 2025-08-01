from uuid import uuid4
import time
from typing import Dict

class SessionManager:
    def __init__(self, session_timeout:int = 3600):
        self.session_timeout = session_timeout
        self.sessions: Dict[str, Dict] = {}

    def Create_session(self, session_id, data = None):
        expire_ts = time.time() + self.session_timeout
        self.sessions[session_id] = {
            "data" : data or {},
            "expires_at" : expire_ts
        }

    def get_session(self, session_id):
        session = self.sessions.get(session_id)
        if not session:
            return None

        if session["expires_at"] < time.time():
            self.sessions.pop(session_id)
            return None
        
        return session['data']
    
    def update_session(self, session_id, new_data):
        if session_id in self.sessions:
            self.sessions[session_id]["data"].update(new_data)
            self.sessions[session_id]["expires_at"] = time.time() + self.session_timeout
        else:
            self.Create_session(session_id, new_data)
    
    def delete_session(self, session_id):
        if session_id in self.sessions:
            self.sessions.pop(session_id)
        
