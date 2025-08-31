
# Weather & Air Quality

Integration for localized weather metrics and AQI (air quality index), including pollen when available.

## Overview
- Weather, air, and pollen endpoints with typed requests/responses
- FastAPI-ready routes and proxy helpers
- Consistent SDK interface with other integrations

## Environment Variables
- WAQ_BASE_URL (required)
- WAQ_API_KEY (required by provider)
- WAQ_TIMEOUT (default: 15)

Example .env:
WAQ_BASE_URL=https://api.example.com/weather
WAQ_API_KEY=your_api_key
WAQ_TIMEOUT=15

## Endpoints (examples)
- GET /weather-air-quality/health
- GET /weather-air-quality/weather?lat=...&lng=...
- GET /weather-air-quality/air?lat=...&lng=...
- GET /weather-air-quality/pollen?lat=...&lng=...

## Project Structure
- api/: base, requests, responses, exceptions, routes
- client.py: high-level client wrapper
- config.py: configuration and environment variables
- pyproject.toml: package metadata
