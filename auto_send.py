import os
import time
from datetime import datetime
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage
from binance_process import get_sybol_price
load_dotenv()
line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
while True:
    now=datetime.now()
    if now.hour == 9 or now.hour == 21:
        reply_text =get_sybol_price(['btc','eth','sol'])
        reply = TextSendMessage(text=reply_text)
        line_bot_api.push_message('U5346e9fc320875e972ccf7f1cd2181ff',reply)
    time.sleep(60*60)