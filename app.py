import os
from datetime import datetime

from flask import Flask, abort, request
from dotenv import load_dotenv
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from binance_process import get_sybol_price
app = Flask(__name__)

load_dotenv()
line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))
def prepare_record(msg):
    text_list = msg.split('\n')
    record_list = []
    print(text_list)
    for item in text_list[1:]:
        record_list.append(item)
        
    return record_list
@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    reply_text = get_message
    if "!get_price" in get_message:
        record_list=prepare_record(get_message)
        data = get_sybol_price(record_list)
        reply_text = data
    reply = TextSendMessage(text=reply_text)
    line_bot_api.reply_message(event.reply_token, reply)
if __name__ == "__main__":
    app.run(debug=True)