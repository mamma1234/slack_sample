from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
class SlackAPI:
    """
    슬랙 API 핸들러
    """
    def __init__(self, token):
        # 슬랙 클라이언트 인스턴스 생성
        self.client = WebClient(token)
        # print(self.client)
        
    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        # conversations_list() 메서드 호출
        result = self.client.conversations_list()
        # print(result)
        # 채널 정보 딕셔너리 리스트
        channels = result.data['channels']
        # print(channels)
        # 채널 명이 'test'인 채널 딕셔너리 쿼리
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        # 채널ID 파싱
        channel_id = channel["id"]
        print(channel_id)
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        # conversations_history() 메서드 호출
        result = self.client.conversations_history(channel=channel_id)
        # print(result)
        # 채널 내 메세지 정보 딕셔너리 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m["text"]==query, messages))[0]
        # print(message)
        # 해당 메세지ts 파싱
        message_ts = message["ts"]
        # print(message_ts)
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result

    def post_message(self, channel_id, text):
        """
        슬랙 채널에 메세지 보내기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text
        )
        return result



# token = "xoxb-744485817254-4961788514196-6PIRV4HMx8FsYqPG0z7E4r1o"
# slack = SlackAPI(token)

# channel_name = "webhook"
# query = "슬랙 봇 테스트"
# text = "자동 생성 문구 테스트"

# # 채널ID 파싱
# channel_id = slack.get_channel_id(channel_name)
# # print(channel_name, '==>', channel_id)

# # 메세지ts 파싱
# message_ts = slack.get_message_ts(channel_id, query)
# # # 댓글 달기
# slack.post_thread_message(channel_id, message_ts, text)
slack = SlackAPI(SLACK_BOT_TOKEN)

channel_name = "bot" #webhook
query = "슬랙 봇 테스트"
text = "자동 생성 문구 테스트"

# 채널ID 파싱
channel_id = slack.get_channel_id(channel_name)
# query(슬랙 봇 테스트) 메세지ts 파싱
message_ts = slack.get_message_ts(channel_id, query)
# 댓글 달기
slack.post_thread_message(channel_id, message_ts, text)

text1 = "메세지 전송"
slack.post_message(channel_id, text1)
