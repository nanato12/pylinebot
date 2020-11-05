import os
import json
from dotenv import load_dotenv
from typing import Any

from flask import Flask, request, abort
from pylinebot import LINE, Tracer, HANDLER_EVENT_TYPE, TRACER_EVENT_TYPE, MESSAGE_TYPE
from linebot.exceptions import InvalidSignatureError

from op import receive_message

load_dotenv(verbose=True)
load_dotenv(".env")

CHANNEL_ACCESS_TOKEN: str = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET: str = os.environ["CHANNEL_SECRET"]

app = Flask(__name__)

bot = LINE(channel_access_token=CHANNEL_ACCESS_TOKEN, channel_secret=CHANNEL_SECRET)

tracer = Tracer(bot, debug=True)
tracer.add_event(TRACER_EVENT_TYPE.MESSAGE, receive_message)

handler = bot.handler


@handler.add(HANDLER_EVENT_TYPE.MESSAGE, message=MESSAGE_TYPE.TEXT)
def test(event: Any) -> None:
    print(event)


@app.route("/", methods=["POST"])
def hello() -> Any:
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    tracer.trace(body, signature)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
