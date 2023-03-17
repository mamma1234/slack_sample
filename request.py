import requests
import json

api_url = "https://hooks.slack.com/services/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"
headers = {"Content-type": "application/json"}
data = json.dumps({"text":"python testing"})
response = requests.post(api_url, headers=headers, data=data)
print(response)