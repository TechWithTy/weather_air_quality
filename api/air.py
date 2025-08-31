import logging
from typing import Dict

from fastapi import APIRouter, HTTPException, Request
import requests

from app.core.third_party_integrations.weather_air_quality.client import (
    GoogleWeatherAirQualityClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/weather-air-quality/air", tags=["weather_air_quality-air"])


# Utility functions

def fetch_air_current(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.air_quality_current_conditions(params=params)


def fetch_air_forecast(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.air_quality_forecast(params=params)


def fetch_air_history(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.air_quality_history(params=params)


# Routes
@router.get("/current")
async def air_quality_current(request: Request) -> Dict:
    try:
        return fetch_air_current(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Air quality current conditions failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/forecast")
async def air_quality_forecast(request: Request) -> Dict:
    try:
        return fetch_air_forecast(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Air quality forecast failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/history")
async def air_quality_history(request: Request) -> Dict:
    try:
        return fetch_air_history(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Air quality history failed")
        raise HTTPException(status_code=500, detail="Internal server error")
