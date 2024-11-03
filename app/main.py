# app/main.py

from fastapi import FastAPI
from app.api import routes

app = FastAPI(
    title="Garmin Connect Proxy API",
    description="An API to interact with Garmin Connect data.",
    version="1.0.0",
)

app.include_router(routes.router)
