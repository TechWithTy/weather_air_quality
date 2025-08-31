from typing import Optional

from ._base import ApiModel, Location, TimeRange
from ._enums import Language, UnitSystem, PollenMapType


# Weather API
class WeatherCurrentConditionsRequest(ApiModel):
    location: Location
    unitSystem: Optional[UnitSystem] = None
    language: Optional[Language] = None


class WeatherForecastHoursRequest(ApiModel):
    location: Location
    hours: Optional[int] = None  # up to 240 per docs
    unitSystem: Optional[UnitSystem] = None
    language: Optional[Language] = None


class WeatherForecastDaysRequest(ApiModel):
    location: Location
    days: Optional[int] = None  # up to 10 per docs
    unitSystem: Optional[UnitSystem] = None
    language: Optional[Language] = None


class WeatherHistoryHoursRequest(ApiModel):
    location: Location
    timeRange: TimeRange
    unitSystem: Optional[UnitSystem] = None
    language: Optional[Language] = None


# Air Quality API
class AirQualityCurrentConditionsRequest(ApiModel):
    location: Location
    language: Optional[Language] = None


class AirQualityForecastRequest(ApiModel):
    location: Location
    hours: Optional[int] = None  # up to 96 per docs
    language: Optional[Language] = None


class AirQualityHistoryRequest(ApiModel):
    location: Location
    timeRange: TimeRange
    language: Optional[Language] = None


# Pollen API
class PollenForecastRequest(ApiModel):
    location: Location
    days: Optional[int] = None  # up to 5 per docs


class PollenHeatmapTileRequest(ApiModel):
    map_type: PollenMapType
    z: int
    x: int
    y: int