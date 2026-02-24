import json
from datetime import datetime

LOG_FILE = "audit_log.json"

def log_attempt(user_input, classification):
    record = {
        "timestamp": str(datetime.now()),
        "input": user_input,
        "classification": classification
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

