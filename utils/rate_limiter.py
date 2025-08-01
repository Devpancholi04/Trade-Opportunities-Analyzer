import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, session_manager, max_requests_per_hours = 10):
        self.session_manager = session_manager
        self.max_requests_per_hour = max_requests_per_hours

    def allow(self, user_id:str) -> bool:
        session_data = self.session_manager.get_session(user_id)
        now = time.time()

        if not session_data:
            self.session_manager.create_session(user_id, {"requests_made" : 1, "start_time" : now})
            return True

        start_time = session_data.get("start_time", now)
        requests_made = session_data.get("requests_made", 0)

        if now - start_time > 3600:
            self.session_manager.update_session(user_id, {"requests_made" : 1, "start_time": now})
            return True
        
        if requests_made < self.max_requests_per_hour:
            self.session_manager.update_session(user_id, {"requests_made" : requests_made + 1})
            return True
        
        return False