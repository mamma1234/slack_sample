from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

slack_webhook = WebhookClient(url=WEBHOOK_URL)

msg = '''
This is test message using slack webhook
line 1
line 2
'''

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
    response = slack_webhook.send(text=msg)
    print(response.status_code)
    print(response.body)
    
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