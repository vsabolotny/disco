# Discovery Health Check App

This is a minimal FastAPI application with a single `/health` endpoint for environment testing in production (e.g., AWS Runner).

## Requirements
- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for local environment variable loading)
- [AWS CLI](https://aws.amazon.com/cli/) (for deployment)
- Docker

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables (create a `.env` file or export them in your shell):
   ```
   ENVIRONMENT=environment
   REPO=your_ecr_repo_url
   REGION=your_aws_region
   ```
3. Start the app:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080
   ```

## Docker

To build and run with Docker:

```bash
docker build --platform linux/amd64 -t disco .
docker run --env-file .env -p 8080:8080 disco
```

## Deployment to AWS ECR

The `deploy.py` script automates building, tagging, and pushing the Docker image to AWS ECR.

**Required environment variables:**
- `ECR_REPO` (e.g., `123456789012.dkr.ecr.us-east-1.amazonaws.com/disco`)
- `REGION` (e.g., `us-east-1`)

**Deploy with:**
```bash
python deploy.py
```

## Endpoint
- `GET /health` → `{ "status": "ok", "environment": "<value of ENVIRONMENT>" }` 