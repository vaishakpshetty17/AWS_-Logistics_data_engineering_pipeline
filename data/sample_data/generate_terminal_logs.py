import json
import random
from datetime import datetime
import time

events = ["ARRIVED", "DEPARTED", "SCANNED"]

while True:
    log = {
        "shipment_id": f"S{random.randint(100, 999)}",
        "terminal": random.choice(["Bangalore Hub", "Mumbai Hub"]),
        "event": random.choice(events),
        "timestamp": datetime.now().isoformat()
    }

    with open("terminal_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    print("New log generated:", log)

    time.sleep(2)
