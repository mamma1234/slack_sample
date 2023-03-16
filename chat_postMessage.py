
# xoxb-744485817254-4961788514196-6PIRV4HMx8FsYqPG0z7E4r1o
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
 
# ID of the channel you want to send the message to
channel_id = "C04U0LZ9HUN" #C04U7E4JRV0
slack_token = "xoxb-744485817254-4961788514196-6PIRV4HMx8FsYqPG0z7E4r1o"
client = WebClient(token=slack_token)
try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world"
    )
 
except SlackApiError as e:
    print(f"Error posting message: {e}")