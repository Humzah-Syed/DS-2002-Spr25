#!C:\Users\hum2a\AppData\Local\Programs\Python\Python313\python.exe
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')

print(f"GitHub User: {GHUSER}")

url = f"https://api.github.com/users/{GHUSER}/events"


r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)
