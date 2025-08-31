import os


GOOGLE_MAPS_API_KEY: str | None = os.getenv("GOOGLE_MAPS_API_KEY")

# Base URLs per service
WEATHER_BASE_URL = os.getenv("WEATHER_BASE_URL", "https://weather.googleapis.com")
AIR_QUALITY_BASE_URL = os.getenv("AIR_QUALITY_BASE_URL", "https://airquality.googleapis.com")
POLLEN_BASE_URL = os.getenv("POLLEN_BASE_URL", "https://pollen.googleapis.com")

# HTTP settings
DEFAULT_TIMEOUT = float(os.getenv("WEATHER_API_TIMEOUT", "15"))