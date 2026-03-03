import re
import pandas as pd
from datetime import datetime

MSG_PATTERN = re.compile(
    r"^(\d{1,2}/\d{1,2}/\d{2}),\s(\d{1,2}:\d{2})\s?(am|pm)\s-\s([^:]+?):\s(.*)",
    re.IGNORECASE
)

NOISE_KEYWORDS = [
    "end-to-end encrypted",
    "was added",
    "created group",
    "you were added",
    "this message was deleted"
]


def parse_whatsapp_chat(file_path: str) -> pd.DataFrame:
    records = []
    current_msg = None

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            match = MSG_PATTERN.match(line)

            if match:
                if current_msg:
                    records.append(current_msg)

                date_str, time_str, ampm, sender, message = match.groups()

                if any(k in message.lower() for k in NOISE_KEYWORDS):
                    current_msg = None
                    continue

                dt = datetime.strptime(
                    f"{date_str} {time_str} {ampm}",
                    "%d/%m/%y %I:%M %p"
                )

                current_msg = {
                    "DateTime": dt,
                    "Sender": sender.strip(),
                    "Message": message.strip()
                }

            elif current_msg and line:
                current_msg["Message"] += "\n" + line

    if current_msg:
        records.append(current_msg)

    df = pd.DataFrame(records)
    return df.sort_values("DateTime").reset_index(drop=True)