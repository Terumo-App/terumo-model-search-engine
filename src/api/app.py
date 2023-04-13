from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import base64
import io

from api.schema.schemas import HealthCheckResult
import logging
import json

with open('search-result.json') as file:
    json_data = json.load(file)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Creating an app object
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="api/images/"), name="images")

class BodyResquest(BaseModel):
    data: int

# Default route
@app.post("/attribute-query")
async def search(body: BodyResquest):
    


    return json_data


@app.get("/health", response_model=HealthCheckResult)
async def health_check() -> HealthCheckResult:
    return HealthCheckResult(success=True)