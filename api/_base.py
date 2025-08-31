from typing import Optional

from pydantic import BaseModel, Field


class ApiModel(BaseModel):
    class Config:
        extra = "allow"
        arbitrary_types_allowed = True


class Location(ApiModel):
    latitude: float = Field(..., description="Latitude in decimal degrees")
    longitude: float = Field(..., description="Longitude in decimal degrees")


class TimeRange(ApiModel):
    start_time: Optional[str] = Field(None, description="ISO-8601 start timestamp, e.g., 2025-08-30T00:00:00Z")
    end_time: Optional[str] = Field(None, description="ISO-8601 end timestamp, optional depending on API")