import os
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from garminconnect import Garmin
from app.infrastructure.garmin_client_interface import GarminClientInterface

load_dotenv()  # Load environment variables from .env file

class GarminClient(GarminClientInterface):
    def __init__(self):
        self.email = os.environ.get('GARMIN_EMAIL')
        self.password = os.environ.get('GARMIN_PASSWORD')
        if not self.email or not self.password:
            raise ValueError("GARMIN_EMAIL and GARMIN_PASSWORD environment variables not set.")
        self.client = Garmin(self.email, self.password)
        self.client.login()

    def get_activities_since(self, start_date: datetime) -> List[Dict]:
        activities = []
        start = 0
        limit = 100  # Adjust as needed
        while True:
            batch = self.client.get_activities(start, limit)
            for activity in batch:
                activity_date = datetime.strptime(activity['startTimeLocal'], '%Y-%m-%d %H:%M:%S')
                if activity_date >= start_date:
                    activities.append(activity)
                else:
                    return activities  # No more activities since start_date
            if len(batch) < limit:
                break  # No more activities to fetch
            start += limit
        return activities
