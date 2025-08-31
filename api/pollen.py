import logging
from typing import Dict

from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import StreamingResponse
import requests

from app.core.third_party_integrations.weather_air_quality.client import (
    GoogleWeatherAirQualityClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/weather-air-quality/pollen", tags=["weather_air_quality-pollen"])


# Utility functions

def fetch_pollen_forecast(params: Dict) -> Dict:
    client = GoogleWeatherAirQualityClient()
    return client.pollen_forecast(params=params)


def fetch_pollen_tile(map_type: str, z: int, x: int, y: int, params: Dict) -> bytes:
    client = GoogleWeatherAirQualityClient()
    return client.pollen_heatmap_tiles(map_type=map_type, z=z, x=x, y=y, params=params)


# Routes
@router.get("/forecast")
async def pollen_forecast(request: Request) -> Dict:
    try:
        return fetch_pollen_forecast(dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Pollen forecast failed")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/tiles/{map_type}/{z}/{x}/{y}")
async def pollen_heatmap_tile(map_type: str, z: int, x: int, y: int, request: Request) -> Response:
    try:
        content = fetch_pollen_tile(map_type, z, x, y, dict(request.query_params))
        return StreamingResponse(iter([content]), media_type="image/png")
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Pollen heatmap tile fetch failed")
        raise HTTPException(status_code=500, detail="Internal server error")
