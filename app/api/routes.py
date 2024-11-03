from fastapi import APIRouter, Depends, HTTPException
from app.services.activity_service import ActivityService
from app.infrastructure.garmin_client import GarminClient
from app.infrastructure.garmin_client_interface import GarminClientInterface

router = APIRouter()

def get_garmin_client() -> GarminClientInterface:
    # You can switch between GarminClient and MockGarminClient here
    return GarminClient()

def get_activity_service(
    garmin_client: GarminClientInterface = Depends(get_garmin_client),
) -> ActivityService:
    return ActivityService(garmin_client)

@router.get("/activities", tags=["Activities"])
def get_activities_since(
    date: str,
    activity_service: ActivityService = Depends(get_activity_service),
):
    """
    Get all activities since the given date (YYYY-MM-DD).
    """
    try:
        activities = activity_service.get_activities_since(date)
        return activities
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error.")
