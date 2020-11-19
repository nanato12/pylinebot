import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, request

from pylinebot import LINE, Tracer
from pylinebot.types.event import TracerEvent
from sample_op import receive_message

load_dotenv(verbose=True)
load_dotenv(".env")

CHANNEL_ACCESS_TOKEN: str = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET: str = os.environ["CHANNEL_SECRET"]

app = Flask(__name__)

bot = LINE(channel_access_token=CHANNEL_ACCESS_TOKEN, channel_secret=CHANNEL_SECRET)

tracer = Tracer(bot, debug=True)
tracer.add_event(TracerEvent.MESSAGE, receive_message)


@app.route("/", methods=["POST"])
def hello() -> Any:
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    tracer.trace(body, signature)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
