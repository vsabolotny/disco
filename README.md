# Discovery Health Check App

This is a minimal FastAPI application with a single `/health` endpoint for environment testing in production (e.g., AWS Runner).

## Requirements
- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Docker

To build and run with Docker:

```bash
docker build -t disco .
docker run --env-file .env -p 8000:8000 disco
```

## Endpoint
- `GET /health` → `{ status: "ok", environment: "production" }` 