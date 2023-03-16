import requests
import json

api_url = "https://hooks.slack.com/services/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"
headers = {"Content-type": "application/json"}
data = json.dumps({"text":"python testing"})
response = requests.post(api_url, headers=headers, data=data)
print(response)