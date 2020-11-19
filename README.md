# pylinebot
linebot-sdk-python wrapper.

## Install
```bash
pip install pylinebot
```

## Import, Instance
```python
from pylinebot import LINE, Tracer

bot = LINE(
    channel_access_token='XXXXXXXXXXXXXXXXXXX',
    channel_secret='XXXXXXXXX'
)
```

## Example (Echo-bot)
```python
import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, request

from pylinebot import LINE, Tracer
from pylinebot.types.event import Event, TracerEvent
from pylinebot.types.message import ContentType, Message


def receive_message(bot: LINE, event: Event.MESSAGE) -> None:
    message: Message = event.message
    message_type = message.type

    if message_type == ContentType.TEXT:
        bot.reply_text_message(message.text)


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

```

## Reply Message
Refer to this: [sample_op.py](./sample_op.py)
- text
```python
text = 'test'
bot.reply_text_message(text)
# > test
bot.reply_text_message(text, text, text)
# > test
# > test
# > test

```
- image
```python
img_url = 'https://xxx.xxxx/xxxx.jpg'
bot.reply_image_message(img_url)
# > img
```

- video
```python
video_message = VideoMessage(
    content_url='https://xxx.xxxx/xxxx.mp4',
    preview_url='https://xxx.xxxx/xxxx.jpg'
)
bot.reply_message([video_message])
```
- audio
```python
audio_message = AudioMessage(
    content_url="https://xxx.xxxx/xxxx.mp3",
    duration=1000,
)
bot.reply_message([audio_message])

```

## Quick reply
```python
action_list = [
    {
        'type': 'message',
        'label': 'aaaa',
        'text': 'これ送信'
    },
    {
        'type': 'camera',
        'label': 'かめら',
    },
    {
        'type': 'cameraRoll',
        'label': 'かめらろーる',
    },
    {
        'type': 'location',
        'label': 'ろけーしょん',
    },
    {
        'type': 'postback',
        'label': 'ぽすとばっく',
        'data': 'test_postback'
    },
    {
        'type': 'datetimepicker',
        'label': 'でーとぴっく',
        'data': 'test_datepick',
        'mode': 'date',
        'initial': '2020-05-15',
        'max': '2020-05-31',
        'min': '2020-05-01'
    }
]
bot.set_quick_reply(action_list)
bot.reply_text_message('quick_reply')
```

## Send multiple messages
The max count of messages that can be sent at one time is 5.
```python
# 2 text message
bot.reply_text_message('text', 'text')
# 5 text message
bot.reply_text_message('text', 'text', 'text', 'text', 'text')
# Error
bot.reply_text_message('text', 'text', 'text', 'text', 'text', 'text')
```

## Send various messages at once.
```python
video_message = VideoMessage(
    content_url="https://xxx.xxxx/xxxx.mp4",
    preview_url="https://xxx.xxxx/xxxx.png",
)
audio_message = AudioMessage(
    content_url="https://xxx.xxxx/xxxx.mp3",
    duration=1000,
)
image_message = ImageMessage(
    preview_url="https://xxx.xxxx/xxxx.png",
    content_url="https://xxx.xxxx/xxxx.png",
)
text_message = TextMessage("test")
# メッセージを詰める
messages: List[SEND_MESSAGE] = []
messages.append(video_message)
messages.append(audio_message)
messages.append(image_message)
messages.append(text_message)
bot.reply_message(messages)
```

## Save message content
Save image, video, and audio data sent by users.

```python
bot.save_content_from_message_id(message_id, file_name)
```

### How to use
```python
from pylinebot.types.event import Event
from pylinebot.types.message import ContentType

def receive_message(bot: LINE, event: Event.MESSAGE) -> None:
    message = event.message
    message_type = message.type

    if message_type == ContentType.IMAGE:
        bot.save_content_from_message_id(message_id, f"{message_id}.jpg")
        bot.reply_text_message("その画像", "保存したよ。")
```
