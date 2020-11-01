import os
import json
from dotenv import load_dotenv

from flask import Flask, request
from pylinebot import LINE, Tracer

from op import receive_message

load_dotenv(verbose=True)
load_dotenv('.env')

CHANNELACCESS_TOKEN = os.environ.get("CHANNELACCESS_TOKEN")
CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET")

app = Flask(__name__)

bot = LINE(
    channel_access_token=CHANNELACCESS_TOKEN,
    channel_secret=CHANNEL_SECRET
)

tracer = Tracer(bot, debug=True)
tracer.add_event('message', receive_message)

@app.route("/", methods=['POST'])
def hello():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    tracer.trace(body, signature)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
