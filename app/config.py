from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(env_path)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

