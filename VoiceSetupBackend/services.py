import json
import os

FILE = "storage/settings.json"

os.makedirs("storage", exist_ok=True)


def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_settings():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)
