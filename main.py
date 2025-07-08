from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/health")
def health_check():
    environment = os.getenv("ENVIRONMENT", "unknown")
    return JSONResponse(content={"status": "ok", "environment": environment})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 