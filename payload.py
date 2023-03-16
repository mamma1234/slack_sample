import requests
import json

url = "https://hooks.slack.com/services/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"
headers = {"Content-type": "application/json"}

payload = {
	"blocks": [
		{
			# "type": "section",
			"text": {
				# "type": "plain_text1111",
				"text": "This is a plain text section block.",
				"emoji": "true"
			}
		}
	]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response)