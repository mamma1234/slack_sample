import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

api_url = WEBHOOK_URL
headers = {"Content-type": "application/json"}
data = json.dumps({"text":"python testing"})
response = requests.post(api_url, headers=headers, data=data)
print(response)