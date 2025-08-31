import json
from types import SimpleNamespace

import pytest

from backend.app.core.third_party_integrations.weather_air_quality.client import (
    GoogleWeatherAirQualityClient,
)


class _Resp:
    def __init__(self, status=200, json_data=None, content=b"tile"):
        self.status_code = status
        self._json = json_data if json_data is not None else {"ok": True}
        self.content = content

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def _patch_requests(monkeypatch, expected_url_prefix, expected_params_key=True, payload=None, content=None):
    def fake_get(url, params=None, timeout=None):
        assert url.startswith(expected_url_prefix)
        if expected_params_key:
            assert params and "key" in params
        return _Resp(json_data=payload, content=content or b"tile")

    monkeypatch.setattr("backend.app.core.third_party_integrations.weather_air_quality.client.requests.get", fake_get)


def test_weather_current_conditions(monkeypatch):
    client = GoogleWeatherAirQualityClient(api_key="k")
    _patch_requests(monkeypatch, "https://weather.googleapis.com/v1/currentConditions:lookup")
    out = client.weather_current_conditions(params={"location": {"latitude": 1, "longitude": 2}})
    assert isinstance(out, dict)


def test_air_quality_forecast(monkeypatch):
    client = GoogleWeatherAirQualityClient(api_key="k")
    _patch_requests(monkeypatch, "https://airquality.googleapis.com/v1/forecast:lookup")
    out = client.air_quality_forecast(params={"location": {"latitude": 1, "longitude": 2}, "hours": 24})
    assert isinstance(out, dict)


def test_pollen_heatmap_tiles(monkeypatch):
    client = GoogleWeatherAirQualityClient(api_key="k")
    _patch_requests(monkeypatch, "https://pollen.googleapis.com/v1/mapTypes/grass/heatmapTiles/3/1/2")
    content = client.pollen_heatmap_tiles(map_type="grass", z=3, x=1, y=2, params={})
    assert isinstance(content, (bytes, bytearray))
