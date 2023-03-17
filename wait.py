import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
# SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
# SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]

SLACK_BOT_TOKEN = "xoxb-744485817254-4961788514196-pwTgLJg4bwl2P1gBgTt79vVD"
SLACK_APP_TOKEN = "xapp-1-A04U9NWNQF6-4960366029779-b570d5c2f8099a2a347ddea4d3cc75ca68e60b3deae24ab05ce215730cebb08e"
SLACK_CHANNEL_ID = "C04U7E4JRV0"

app = App(token=SLACK_BOT_TOKEN)

@app.event("message")
def handle_message(event, client, logger):
    if event["channel"] == SLACK_CHANNEL_ID:
        message = event["text"]
        # do something with the message
        print(message)

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN)
    handler.start()
