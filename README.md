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
from flask import Flask, request
from pylinebot import LINE, Tracer

def receive_message(bot, event):
    message = event.message
    message_type = message.type

    if message_type == 'text':
        bot.reply_text_message(message.text)

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

```

## Reply Message
- text
```python
text = 'test'
bot.reply_text_message(text)
```
- image
```python
img_url = 'https://xxx.xxxx/xxxx.jpg'
bot.reply_image_message(img_url)
```

- video
```python
video_data = {
    'content_url': 'https://xxx.xxxx/xxxx.mp4',
    'preview_url': 'https://xxx.xxxx/xxxx.jpg'
}
bot.reply_video_message(video_data)
```
- audio
```python
audio_data = {
    'content_url': 'https://xxx.xxxx/xxxx.mp3',
    'duration': 1000
}
bot.reply_audio_message(audio_data)
```
- location
```python
location_data = {
    'title': 'title',
    'address': 'adress_name',
    'latitude': 0,
    'longitude': 0
}
bot.reply_location_message(location_data)
```
- sticker
```python
sticker_data = {
    'package_id': 1,
    'sticker_id': 1
}
bot.reply_sticker_message(sticker_data)
```
- flex
```python
flex_data = {
    'flex': flex_content,
    'alt_text': 'Flex Message'
}
bot.reply_flex_message(flex_data)
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
messages = [
    bot.create_text_message('いろんなめっせーじ'),
    bot.create_text_message('いちどにおくれるよ'),
    bot.create_image_message(img_data),
    bot.create_video_message(video_data)
]
bot.reply_message(messages)
```

## Save message content
Save image, video, and audio data sent by users.

```python
bot.save_content_from_message_id(message_id, file_name)
```

## Push message
```python
bot.push_message(to, messages)
```

## Broadcast
```python
bot.broadcast(messages)
```

## Narrowcast
```python
bot.narrowcast(messages)
```

## Multicast

```python
bot.multicast(to, messages)
```
