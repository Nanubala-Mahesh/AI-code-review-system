import requests
import os

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}


def get_diff(repo, pr_number):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    r = requests.get(url, headers=HEADERS)
    return r.text


def post_comment(repo, pr_number, comment):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    requests.post(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/json"
        },
        json={"body": comment}
    )
