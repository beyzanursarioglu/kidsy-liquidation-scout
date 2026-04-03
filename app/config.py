import os
from dotenv import load_dotenv

load_dotenv()

SOURCE_URL = "https://example.com"
SNAPSHOT_FILE = "snapshots/source_page.html"

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")