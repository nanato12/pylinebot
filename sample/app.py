import json

from flask import Flask, request
from pylinebot import LINE, Tracer

from op import receive_message

DEBUG = True

app = Flask(__name__)

bot = LINE(
    channel_access_token='XXXXXXXXXXXXXXXXXXX',
    channel_secret='XXXXXXXXX'
)

tracer = Tracer(bot, debug=DEBUG)
tracer.add_event('message', receive_message)

@app.route("/", methods=['POST'])
def hello():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    tracer.trace(body, signature)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=DEBUG)
