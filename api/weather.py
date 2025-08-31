import logging
from typing import Dict

from fastapi import APIRouter, HTTPException, Request
import requests

from app.core.third_party_integrations.weather_air_quality.client import (
    GoogleWeatherAirQualityClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/weather-air-quality/weather", tags=["weather_air_quality-weather"])


# Utility functions

def fetch_current(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.weather_current_conditions(params=params)


def fetch_forecast_hours(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.weather_forecast_hours(params=params)


def fetch_forecast_days(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.weather_forecast_days(params=params)


def fetch_history_hours(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.weather_history_hours(params=params)


# Routes
@router.get("/current")
async def weather_current(request: Request) -> Dict:
    try:
        return fetch_current(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Weather current conditions failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/forecast/hours")
async def weather_forecast_hours(request: Request) -> Dict:
    try:
        return fetch_forecast_hours(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Weather forecast hours failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/forecast/days")
async def weather_forecast_days(request: Request) -> Dict:
    try:
        return fetch_forecast_days(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Weather forecast days failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/history/hours")
async def weather_history_hours(request: Request) -> Dict:
    try:
        return fetch_history_hours(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Weather history hours failed")
        raise HTTPException(status_code=500, detail="Internal server error")
