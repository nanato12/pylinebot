# pylinebot
linebot-sdk-python wrapper.

## Install
```bash
pip install pylinebot
```

## Import
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
    reply_token = event.reply_token

    message = event.message
    message_type = message.type

    if message_type == 'text':
        message_text = message.text
        bot.send_text_message(reply_token, message_text)


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

## Send Message
- text
```python
bot.send_text_message(reply_token, text)
```
- image
```python
bot.send_image_message(reply_token, 'https://xxx.xxxx/xxxx.jpg')
```

- video
```python
video_data = {
    'content_url': 'https://xxx.xxxx/xxxx.mp4',
    'preview_url': 'https://xxx.xxxx/xxxx.jpg'
}
bot.send_video_message(reply_token, video_data)
```
- audio
```python
audio_data = {
    'content_url': 'https://xxx.xxxx/xxxx.mp3',
    'duration': 1000
}
bot.send_audio_message(reply_token, audio_data)
```
- location
```python
location_data = {
    'title': 'title',
    'address': 'adress_name',
    'latitude': 0,
    'longitude': 0
}
bot.send_location_message(reply_token, location_data)
```
- sticker
```python
sticker_data = {
    'package_id': 1,
    'sticker_id': 1
}
bot.send_sticker_message(reply_token, sticker_data)
```
- flex
```python
flex_data = {
    'flex': flex_content,
    'alt_text': 'Flex Message'
}
bot.send_flex_message(reply_token, flex_data)
```

## replay, push, other
Default `send_type='reply'`

send_type
- reply
- push
- broadcast
- narrowcast
- multicast

```python
bot.send_text_message(to, text, send_type='push')
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
bot.send_text_message(reply_token, 'text', quick_reply=quick_reply)
```

## Send multiple messages
The max count of messages that can be sent at one time is 5.
```python
# 2 text message
bot.send_text_message(reply_token, 'text', 'text')
# 5 text message
bot.send_text_message(reply_token, 'text', 'text', 'text', 'text', 'text')
# Error
bot.send_text_message(reply_token, 'text', 'text', 'text', 'text', 'text', 'text')
```

## Send various messages at once.
```python
message_list = [
    bot.create_text_message('いろんなめっせーじ'),
    bot.create_text_message('いちどにおくれるよ'),
    bot.create_image_message('https://xxx.xxxx/xxxx.jpg'),
    bot.create_video_message('https://xxx.xxxx/xxxx.mp4', 'https://xxx.xxxx/xxxx.jpg')
]
bot.send_message(reply_token, message_list)
```

## Save message content
Save image, video, and audio data sent by users.

```python
bot.save_content_from_message_id(message_id, file_name)
```
