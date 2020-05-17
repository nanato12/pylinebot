import json
from io import BytesIO
from PIL import Image

def file_to_dict(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data

def get_flex(flex_title):
    return file_to_dict('flex.json')[flex_title]

def get_rich(rich_title):
    return file_to_dict('rich.json')[rich_title]

def receive_message(bot, event):
    reply_token = event.reply_token

    message = event.message
    message_id = message.id
    message_type = message.type

    source_type = event.source.type
    user_id = event.source.user_id

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
    quick_reply = bot.create_quick_reply(action_list)

    if message_type == 'sticker':
        bot.send_text_message(reply_token, 'それすたんぷ')

    elif message_type == 'image':
        bot.save_content_from_message_id(message_id, f'{message_id}.jpg')
        bot.send_text_message(reply_token, 'それがぞう', 'ほぞんさせてもらったわ', quick_reply=quick_reply)

    elif message_type == 'video':
        bot.save_content_from_message_id(message_id, f'{message_id}.mp4')
        bot.send_text_message(reply_token, 'それどうが', 'ほっぞーん', 'したよ')

    elif message_type == 'location':
        bot.send_text_message(reply_token, 'それいち')

    elif message_type == 'file':
        bot.send_text_message(reply_token, 'それふぁいる')

    elif message_type == 'text':
        message_text = message.text

        if source_type == 'group':
            group_id = event.source.group_id
            print(bot.get_group_member_ids(group_id))
        elif source_type == 'room':
            room_id = event.source.room_id
            print(bot.get_room_member_ids(room_id))

        if message_text == 'てきすと':
            bot.send_text_message(reply_token, 'テキスト')

        elif message_text == 'りっち':
            rich_menu = bot.create_rich_menu_object(get_rich('test'))
            rich_menu_id = bot.create_rich_menu(rich_menu, 'test.png', 'png')

            bot.link_rich_menu_to_user(user_id, rich_menu_id)
            bot.send_text_message(reply_token, rich_menu_id)

        elif message_text == 'いべんと':
            bot.send_text_message(reply_token, str(event), quick_reply=quick_reply)

        elif message_text == 'ふくすう':
            bot.send_text_message(reply_token, 'ふ', 'く', 'す', 'う', quick_reply=quick_reply)

        elif message_text == 'がぞう':
            bot.send_image_message(
                reply_token,
                'https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png',
                quick_reply=quick_reply
            )

        elif message_text == 'びでお':
            video_data = {
                'content_url': 'https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4',
                'preview_url': 'https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png'
            }
            bot.send_video_message(reply_token, video_data, quick_reply=quick_reply)

        elif message_text == 'おんせい':
            audio_data = {
                'content_url': 'https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3',
                'duration': 1000
            }
            bot.send_audio_message(reply_token, audio_data, quick_reply=quick_reply)

        elif message_text == 'いち':
            location_data = {
                'title': 'たいとる',
                'address': 'あどれす',
                'latitude': 0,
                'longitude': 0
            }
            bot.send_location_message(reply_token, location_data, quick_reply=quick_reply)

        elif message_text == 'すたんぷ':
            sticker_data = {
                'package_id': 1,
                'sticker_id': 1
            }
            bot.send_sticker_message(reply_token, sticker_data, quick_reply=quick_reply)

        elif message_text == 'ふれっくすひとつ':
            flex_content = {
                'flex': get_flex('test'),
                'alt_text': 'Flex Message'
            }
            bot.send_flex_message(reply_token, flex_content, quick_reply=quick_reply)

        elif message_text == 'ふれっくすいつつ':
            flex_content = {
                'flex': get_flex('test'),
                'alt_text': 'Flex Message'
            }
            bot.send_flex_message(reply_token, flex_content, flex_content, flex_content, flex_content, flex_content, quick_reply=quick_reply)

        elif message_text == 'くいっく':
            bot.send_text_message(reply_token, 'くいっく', 'くいっく', quick_reply=quick_reply)
