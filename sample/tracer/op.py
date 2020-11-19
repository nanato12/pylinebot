import json
from typing import Any, List

from pylinebot import LINE, ImageMessage, TextMessage
from pylinebot.types.message import ContentType, ToType


def file_to_dict(file_name: str) -> dict:
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def get_flex(flex_title: str) -> dict:
    return file_to_dict("flex.json")[flex_title]


def get_rich(rich_title: str) -> dict:
    return file_to_dict("rich.json")[rich_title]


def get_quick(quick_title: str) -> List[Any]:
    return file_to_dict("quick.json")[quick_title]


def receive_message(bot: LINE, event: Any) -> None:
    reply_token = event.reply_token

    message = event.message
    message_id = message.id
    message_type = message.type

    source_type = event.source.type
    user_id = event.source.user_id

    if message_type == ContentType.STICKER:
        bot.reply_message([TextMessage("a")])

    elif message_type == ContentType.IMAGE:
        bot.save_content_from_message_id(message_id)
        bot.reply_text_message("その画像", "保存したよ。")

    elif message_type == ContentType.VIDEO:
        bot.save_content_from_message_id(message_id, f"{message_id}.mp4")
        bot.reply_text_message("その動画", "保存", "したよ")

    elif message_type == ContentType.LOCATION:
        bot.reply_text_message("それいち")

    elif message_type == ContentType.FILE:
        bot.reply_text_message("それふぁいる")

    elif message_type == ContentType.TEXT:
        message_text = message.text

        if source_type == ToType.GROUP:
            pass
            # group_id = event.source.group_id
            # print(bot.get_group_member_ids(group_id))
        elif source_type == ToType.ROOM:
            pass
            # room_id = event.source.room_id
            # print(bot.get_room_member_ids(room_id))

        if message_text == "てきすと":
            bot.set_quick_reply(get_quick("test"))
            bot.reply_text_message("テキスト")
            bot.push_message(user_id, [TextMessage("a")])
            bot.broadcast([TextMessage("ぶろーど")])

        elif message_text == "ふくすうてきすと":
            bot.reply_text_message("ふ", "く", "す", "う")

        elif message_text == "がぞう":
            url = "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png"
            message = ImageMessage(url, url)
            bot.reply_message([message])

        elif message_text == "ふくすうがぞう":
            bot.reply_image_message(
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )

        elif message_text == "どうが":
            video_data = {
                "content_url": "https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                "preview_url": "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            }
            bot.reply_video_message(video_data)

        elif message_text == "ふくすうどうが":
            video_data = {
                "content_url": "https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                "preview_url": "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            }
            bot.reply_video_message(video_data, video_data, video_data)

        elif message_text == "おんせい":
            audio_data = {
                "content_url": "https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                "duration": 1000,
            }
            bot.reply_audio_message(audio_data)

        elif message_text == "ふくすうおんせい":
            audio_data = {
                "content_url": "https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                "duration": 1000,
            }
            bot.reply_audio_message(audio_data, audio_data, audio_data, audio_data)

        elif message_text == "いち":
            location_data = {
                "title": "たいとる",
                "address": "あどれす",
                "latitude": 0,
                "longitude": 0,
            }
            bot.reply_location_message(location_data)

        elif message_text == "ふくすういち":
            location_data = {
                "title": "たいとる",
                "address": "あどれす",
                "latitude": 0,
                "longitude": 0,
            }
            bot.reply_location_message(location_data, location_data)

        elif message_text == "すたんぷ":
            sticker_data = {"package_id": 1, "sticker_id": 1}
            bot.reply_sticker_message(sticker_data)

        elif message_text == "ふくすうすたんぷ":
            sticker_data = {"package_id": 1, "sticker_id": 1}
            bot.reply_sticker_message(
                sticker_data, sticker_data, sticker_data, sticker_data, sticker_data
            )

        elif message_text == "ふれっくす":
            flex_data = {"content": get_flex("test"), "alt_text": "Flex Message"}
            bot.reply_flex_message(flex_data)

        elif message_text == "ふくすうふれっくす":
            flex_data = {"content": get_flex("test"), "alt_text": "Flex Message"}
            bot.reply_flex_message(
                flex_data, flex_data, flex_data, flex_data, flex_data
            )

        elif message_text == "いろんな":
            video_data = {
                "content_url": "https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                "preview_url": "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            }
            audio_data = {
                "content_url": "https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                "duration": 1000,
            }
            flex_data = {"content": get_flex("test"), "alt_text": "Flex Message"}
            message_list = [
                bot.create_text_message("いろんなメッセージを送るよ！"),
                bot.create_image_message(
                    "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png"
                ),
                bot.create_video_message(video_data),
                bot.create_audio_message(audio_data),
                bot.create_flex_message(flex_data),
            ]
            bot.reply_message(message_list)

        elif message_text == "りっち":
            rich_menu = bot.create_rich_menu_object(get_rich("test"))
            rich_menu_id = bot.create_rich_menu(rich_menu, "test.png", "png")

            bot.link_rich_menu_to_user(user_id, rich_menu_id)
            bot.send_text_message(reply_token, rich_menu_id)

        elif message_text == "いべんと":
            bot.reply_text_message(str(event))

        elif message_text == "くいっく":
            bot.set_quick_reply(get_quick("test"))
            bot.reply_text_message("くいっくりぷらいだよ")
