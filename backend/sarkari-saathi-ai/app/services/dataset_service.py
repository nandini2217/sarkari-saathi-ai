import json
from pathlib import Path

DATA_PATH = Path("app/data/agriculture_schemes.json")

def load_schemes():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)