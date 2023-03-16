import slack_api

token = "xoxb-744485817254-4961788514196-6PIRV4HMx8FsYqPG0z7E4r1o"
slack = slack_api.SlackAPI(token)

channel_name = "mamma" #webhook
query = "슬랙 봇 테스트"
text = "자동 생성 문구 테스트"

# 채널ID 파싱
channel_id = slack.get_channel_id(channel_name)
# 메세지ts 파싱
message_ts = slack.get_message_ts(channel_id, query)
# 댓글 달기
slack.post_thread_message(channel_id, message_ts, text)