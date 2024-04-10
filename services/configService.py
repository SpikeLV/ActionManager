import json

with open("config.json", mode="r", encoding="utf-8") as f:
    config = json.load(f)
    f.close()