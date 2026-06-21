import requests

BASE = "http://127.0.0.1:8000"

print("Getting Voices...")

response = requests.get(BASE + "/voices")

print(response.json())
