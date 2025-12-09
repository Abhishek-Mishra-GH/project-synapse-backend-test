from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal, List
from model_loader import get_model

app = FastAPI()

Domain = Literal["finance", "healthcare", "ecommerce", "insurance"]

class GenerateRequest(BaseModel):
    domain: Domain
    rows: int = 100

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in Docker"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/domains")
def domains():
    return {"domains": ["finance", "healthcare", "ecommerce", "insurance"]}

@app.post("/generate")
def generate(req: GenerateRequest):
    model = get_model(req.domain)
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    data = model.sample(req.rows)
    
    return {
        "domain": req.domain,
        "rows": req.rows,
        "data": data.to_dict(orient="records")
    }
