import asyncio
import os
# requires: pip install aiohttp
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError

client = AsyncWebClient("xoxb-744485817254-4961788514196-pwTgLJg4bwl2P1gBgTt79vVD")

# This must be an async method
async def main() -> None:
    try:
        # Don't forget `await` keyword here
        response = await client.chat_postMessage(
            channel='#webhook',
            text="Hello world!"
        )
        print(response)
        # assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        # assert e.response["ok"] is False
        # assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

# This is the simplest way to run the async method
# but you can go with any ways to run it
if __name__ == "__main__":
    asyncio.run(main()) 
# asyncio.run(post_message())

