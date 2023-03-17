
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
# ID of the channel you want to send the message to

client = WebClient(token=SLACK_BOT_TOKEN)
try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=SLACK_CHANNEL_ID,
        text="Hello world"
    )
 
except SlackApiError as e:
    print(f"Error posting message: {e}")