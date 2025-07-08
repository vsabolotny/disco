from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/health")
def health_check():
    environment = os.getenv("ENVIRONMENT")
    return JSONResponse(content={"status": "ok", "environment": environment})
