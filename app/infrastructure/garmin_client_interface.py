from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

class GarminClientInterface(ABC):
    @abstractmethod
    def get_activities_since(self, start_date: datetime) -> List[Dict]:
        pass
