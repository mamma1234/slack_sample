import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

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


# last_message_ts = None

# while True:
#     try:
#         if last_message_ts:
#             response = client.conversations_history(channel=SLACK_CHANNEL_ID, latest=last_message_ts)
#         else:
#             response = client.conversations_history(channel=SLACK_CHANNEL_ID)
#         messages = response["messages"]
#         for message in messages:
#             # do something with each new message
#             print("==============================")
#             print(message)
#         if messages:
#             last_message_ts = messages[-1]["ts"]
#     except SlackApiError as e:
#         print(f"Error: {e}")
#     time.sleep(1) # wait for 1 second before checking for new messages again
