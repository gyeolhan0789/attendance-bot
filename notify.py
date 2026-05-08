import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


WEBHOOK_URL = os.environ["MM_WEBHOOK_URL"]

now = datetime.now(ZoneInfo("Asia/Seoul"))

if now.hour < 12:
    message = "\u2600\ufe0f \ucd9c\uc11d \uccb4\ud06c \uc2dc\uac04\uc785\ub2c8\ub2e4!"
else:
    message = "\U0001f319 \ud1f4\uc2e4 \uccb4\ud06c\ud558\uc138\uc694!"

payload = {
    "username": "Attendance Bot",
    "icon_emoji": ":robot_face:",
    "text": message,
}

response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
response.raise_for_status()
