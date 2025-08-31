class WeatherAirQualityError(Exception):
    """Base exception for Weather/Air Quality/Pollen SDK."""


class RequestValidationError(WeatherAirQualityError):
    pass


class ApiHTTPError(WeatherAirQualityError):
    def __init__(self, status_code: int, message: str | None = None):
        super().__init__(message or f"HTTP {status_code}")
        self.status_code = status_code