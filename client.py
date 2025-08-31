import os
from typing import Any, Dict, Optional

import requests


class GoogleWeatherAirQualityClient:
    """
    Google Maps Weather and Air Quality APIs.
    Docs:
      - Weather: https://developers.google.com/maps/documentation/weather
        - Service endpoint: https://weather.googleapis.com
      - Air Quality: https://developers.google.com/maps/documentation/air-quality
        - Service endpoint: https://airquality.googleapis.com

    Methods expose exact REST paths and pass through query params per docs.
    """

    def __init__(self, api_key: Optional[str] = None, timeout: int = 30):
        self.api_key = api_key or os.getenv("GOOGLE_MAPS_API_KEY")
        self.weather_base = "https://weather.googleapis.com"
        self.air_base = "https://airquality.googleapis.com"
        self.pollen_base = "https://pollen.googleapis.com"
        self.timeout = timeout

    def _inject_key(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        q: Dict[str, Any] = dict(params or {})
        if self.api_key and "key" not in q:
            q["key"] = self.api_key
        return q

    # Weather API endpoints
    def weather_current_conditions(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.weather_base}/v1/currentConditions:lookup"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    # Pollen API endpoints
    def pollen_forecast(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.pollen_base}/v1/forecast:lookup"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def pollen_heatmap_tiles(self, *, map_type: str, z: int, x: int, y: int, params: Optional[Dict[str, Any]] = None) -> bytes:
        """
        Returns raw tile bytes for pollen heatmap tiles.
        Path shape: /v1/mapTypes/{mapType}/heatmapTiles/{z}/{x}/{y}
        """
        url = f"{self.pollen_base}/v1/mapTypes/{map_type}/heatmapTiles/{z}/{x}/{y}"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.content

    def weather_forecast_hours(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.weather_base}/v1/forecast:hours"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def weather_forecast_days(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.weather_base}/v1/forecast:days"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def weather_history_hours(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.weather_base}/v1/history:hours"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    # Air Quality API endpoints
    def air_quality_current_conditions(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.air_base}/v1/currentConditions:lookup"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def air_quality_forecast(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.air_base}/v1/forecast:lookup"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def air_quality_history(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.air_base}/v1/history:lookup"
        resp = requests.get(url, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()