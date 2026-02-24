import json
import os
from datetime import datetime

LOG_FILE = "audit_log.json"


def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)


def log_attempt(data: dict):
    init_log()

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "raw_query": data["raw_query"],
        "structured_output": data["structured_output"],
        "needs_clarification": data["needs_clarification"]
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)