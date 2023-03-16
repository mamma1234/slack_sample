from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError

webhook_url = 'https://hooks.slack.com/services/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'

slack_webhook = WebhookClient(url=webhook_url)


msg = '''
This is test message using slack webhook
line 1
line 2
'''


try:
    response = slack_webhook.send(text=msg)
except SlackApiError as e:
    print(e)