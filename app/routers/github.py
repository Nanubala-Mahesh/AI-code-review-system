from fastapi import APIRouter, Request, HTTPException
import os, hmac, hashlib, json


router = APIRouter()

SECRET = os.getenv("WEBHOOK_SECRET")


def verify_signature(body: bytes, signature: str):
    mac = hmac.new(
        SECRET.encode(),
        msg=body,
        digestmod=hashlib.sha256
    )
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)


@router.post("/webhook/github")
async def github_webhook(request: Request):

    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")

    if not verify_signature(body, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    payload = json.loads(body)

    event = request.headers.get("X-GitHub-Event")

    if event != "pull_request":
        return {"status": "ignored"}

    action = payload["action"]

    if action not in ["opened", "synchronize", "reopened"]:
        return {"status": "ignored"}

    pr_number = payload["pull_request"]["number"]
    repo = payload["repository"]["full_name"]

    return {"status": "processing", "pr_number": pr_number, "repo": repo}

