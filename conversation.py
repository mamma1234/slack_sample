import os
# import openai
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
from slack_bolt import App
import re

SLACK_BOT_TOKEN = "xoxb-744485817254-4961788514196-pwTgLJg4bwl2P1gBgTt79vVD"
SLACK_APP_TOKEN = "xapp-1-A04U9NWNQF6-4960366029779-b570d5c2f8099a2a347ddea4d3cc75ca68e60b3deae24ab05ce215730cebb08e"
SLACK_CHANNEL_ID = "C04U7E4JRV0"

# Event API & Web API
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(SLACK_BOT_TOKEN)

@app.event("app_mention") # 앱을 언급했을 때
def handle_mention(event, client, message, say):
    text = event["text"]
    print(text)

    if "안녕하세요" in text:
        say(f'hello! <@{event["user"]}>')
        client.chat_postMessage(channel=event['user'], text='that is dm')  # DM으로 응답을 줄 수도 있다

    when_september_ends = 1645163580 # 시간이 되었을 때 메세지를 보내준다.
    client.chat_scheduleMessage(
        channel=event['user'],
        post_at=when_september_ends,
        text="Summer has come and passed"
    )
        
# @app.message(re.compile("12345")) # 특정 단어만 포함한 메세지를 잡고 싶다면
@app.event("message")  # 앱이 설치된 채널에 메세지가 올라올 때
def handle_message_events(event, message, say):
    print('event :', event)
    print('message:', message)

    if "12345" in message['text']:
        say("코드입력")
        

if __name__ == '__main__':
    SocketModeHandler(app, SLACK_APP_TOKEN).start()