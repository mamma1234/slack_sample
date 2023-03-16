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