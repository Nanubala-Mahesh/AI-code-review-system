from fastapi import FastAPI
from app.config import GITHUB_TOKEN

app=FastAPI(title="AI Code Review System", description="An AI-powered code review system that provides feedback and suggestions for improving code quality.", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Welcome to the AI Code Review System!", "github_token": GITHUB_TOKEN}


