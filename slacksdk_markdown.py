from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError

webhook_url = 'https://hooks.slack.com/services/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'

slack_webhook = WebhookClient(url=webhook_url)


mrkdwn_text = '''
This is test message.
> Block quote

*Bold text*

```
code block - line 1
code block - line 2\ncode block - line 3
```

`highlight`

_italicize_

~Strikethrough~

<https://www.google.com|This is link to google.com>
'''


try:
    response = slack_webhook.send(
        blocks=[
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': mrkdwn_text
                }
            }
        ]
    )
    
    print(response.status_code)
    print(response.body)
    
except SlackApiError as e:
    print(e)