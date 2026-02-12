from fastapi import APIRouter
from app.config import GITHUB_TOKEN



router = APIRouter()

@router.get("/webhook/github")
def get_github_token():
    return {"github_token": GITHUB_TOKEN}