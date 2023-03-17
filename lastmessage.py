import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = "xoxb-744485817254-4961788514196-pwTgLJg4bwl2P1gBgTt79vVD"
SLACK_CHANNEL_ID = "C04U7E4JRV0"

client = WebClient(token=SLACK_BOT_TOKEN)
last_message_ts = None

while True:
    try:
        if last_message_ts:
            response = client.conversations_history(channel=SLACK_CHANNEL_ID, latest=last_message_ts)
        else:
            response = client.conversations_history(channel=SLACK_CHANNEL_ID)
        messages = response["messages"]
        for message in messages:
            # do something with each new message
            print(message)
        if messages:
            last_message_ts = messages[-1]["ts"]
    except SlackApiError as e:
        print(f"Error: {e}")
    time.sleep(1) # wait for 1 second before checking for new messages again
