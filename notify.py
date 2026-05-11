import os
from datetime import datetime
from zoneinfo import ZoneInfo

import holidays
import requests


WEBHOOK_URL = os.environ["MM_WEBHOOK_URL"]
CHECKIN_TIME = (8, 55)
CHECKOUT_TIME = (18, 0)
ALLOWED_DELAY_MINUTES = 5

now = datetime.now(ZoneInfo("Asia/Seoul"))
kr_holidays = holidays.KR()

if now.date() in kr_holidays:
    print(f"Holiday: {kr_holidays.get(now.date())}. Skip notification.")
    raise SystemExit(0)

if now.weekday() >= 5:
    print("Weekend. Skip notification.")
    raise SystemExit(0)

minutes = now.hour * 60 + now.minute
checkin_minutes = CHECKIN_TIME[0] * 60 + CHECKIN_TIME[1]
checkout_minutes = CHECKOUT_TIME[0] * 60 + CHECKOUT_TIME[1]

if checkin_minutes <= minutes < checkin_minutes + ALLOWED_DELAY_MINUTES:
    message = "\u2600\ufe0f \ucd9c\uc11d \uccb4\ud06c \uc2dc\uac04\uc785\ub2c8\ub2e4!"
elif checkout_minutes <= minutes < checkout_minutes + ALLOWED_DELAY_MINUTES:
    message = "\U0001f319 \ud1f4\uc2e4 \uccb4\ud06c\ud558\uc138\uc694!"
else:
    print(f"Outside notification window: {now.isoformat()}. Skip notification.")
    raise SystemExit(0)

payload = {
    "username": "Attendance Bot",
    "icon_emoji": ":robot_face:",
    "text": message,
}

response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
response.raise_for_status()
