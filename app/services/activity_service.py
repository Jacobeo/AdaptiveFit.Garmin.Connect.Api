from datetime import datetime
from typing import List, Dict
from app.infrastructure.garmin_client_interface import GarminClientInterface

class ActivityService:
    def __init__(self, garmin_client: GarminClientInterface):
        self.garmin_client = garmin_client

    def get_activities_since(self, start_date_str: str) -> List[Dict]:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        activities = self.garmin_client.get_activities_since(start_date)
        return activities
