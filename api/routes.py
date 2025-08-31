import logging
from typing import Dict

from fastapi import APIRouter

from app.core.third_party_integrations.weather_air_quality.api.weather import router as weather_router
from app.core.third_party_integrations.weather_air_quality.api.air import router as air_router
from app.core.third_party_integrations.weather_air_quality.api.pollen import router as pollen_router


logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(weather_router)
router.include_router(air_router)
router.include_router(pollen_router)

