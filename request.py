import requests
import json

api_url = "https://hooks.slack.com/services/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"
headers = {"Content-type": "application/json"}
data = json.dumps({"text":"python testing"})
response = requests.post(api_url, headers=headers, data=data)
print(response)