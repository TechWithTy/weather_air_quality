from typing import Optional

from pydantic import Field

from ._base import ApiModel, Location


# Weather API responses
class WeatherCondition(ApiModel):
    description: Optional[str] = None
    iconUri: Optional[str] = None


class WeatherCurrentConditions(ApiModel):
    location: Optional[Location] = None
    currentTime: Optional[str] = None
    isDaytime: Optional[bool] = None
    temperature: Optional[float] = None
    temperatureUnit: Optional[str] = None
    weatherCondition: Optional[WeatherCondition] = None


class HourlyForecast(ApiModel):
    startTime: Optional[str] = None
    temperature: Optional[float] = None
    temperatureUnit: Optional[str] = None


class DailyForecast(ApiModel):
    date: Optional[str] = None
    minTemperature: Optional[float] = None
    maxTemperature: Optional[float] = None
    temperatureUnit: Optional[str] = None


class WeatherForecastHours(ApiModel):
    hours: list[HourlyForecast] = Field(default_factory=list)


class WeatherForecastDays(ApiModel):
    days: list[DailyForecast] = Field(default_factory=list)


class WeatherHistoryHours(ApiModel):
    hours: list[HourlyForecast] = Field(default_factory=list)


# Air Quality API responses
class AirQualityIndex(ApiModel):
    code: Optional[str] = None
    category: Optional[str] = None
    value: Optional[int] = None


class AirQualityCurrent(ApiModel):
    location: Optional[Location] = None
    indexes: list[AirQualityIndex] = Field(default_factory=list)


class AirQualityForecast(ApiModel):
    hours: list[AirQualityIndex] = Field(default_factory=list)


class AirQualityHistory(ApiModel):
    hours: list[AirQualityIndex] = Field(default_factory=list)


# Pollen API responses
class PollenIndex(ApiModel):
    type: Optional[str] = None
    value: Optional[int] = None
    category: Optional[str] = None


class PollenForecast(ApiModel):
    days: list[PollenIndex] = Field(default_factory=list)