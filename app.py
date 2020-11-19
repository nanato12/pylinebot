import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, request

from op import receive_message
from pylinebot import LINE, TRACER_EVENT_TYPE, Tracer

load_dotenv(verbose=True)
load_dotenv(".env")

CHANNEL_ACCESS_TOKEN: str = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET: str = os.environ["CHANNEL_SECRET"]

app = Flask(__name__)

bot = LINE(channel_access_token=CHANNEL_ACCESS_TOKEN, channel_secret=CHANNEL_SECRET)

tracer = Tracer(bot, debug=True)
tracer.add_event(TRACER_EVENT_TYPE.MESSAGE, receive_message)


@app.route("/", methods=["POST"])
def hello() -> Any:
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    tracer.trace(body, signature)
    return "OK"


@app.route("/twitter", methods=["POST"])
def twitter() -> Any:
    print("\n\nget_data\n")
    print(request.get_data())
    print("\n\njson\n")
    print(request.get_json())
    print("\n\njson\n")
    print(request.json)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
