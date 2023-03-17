import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = "xoxb-744485817254-4961788514196-pwTgLJg4bwl2P1gBgTt79vVD"
# SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_CHANNEL_ID = "C04U7E4JRV0"

client = WebClient(token=SLACK_BOT_TOKEN)

while True:
    try:
        response = client.conversations_history(channel=SLACK_CHANNEL_ID)
        messages = response["messages"]
        for message in messages:
            # do something with each message
            print(message)
            
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text="Hello world!"
        )
        print(response)
    except SlackApiError as e:
        print(f"Error: {e}")
    time.sleep(1) # wait for 1 second before checking for new messages again
