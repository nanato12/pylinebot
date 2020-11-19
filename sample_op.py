import json
from typing import Any, List

from pylinebot import LINE
from pylinebot.structs.message import (
    AudioMessage,
    FlexMessage,
    ImageMessage,
    LocationMessage,
    StickerMessage,
    TextMessage,
    VideoMessage,
)
from pylinebot.types.event import Event
from pylinebot.types.message import ContentType, ToType
from pylinebot.utils.annotation import SEND_MESSAGE


def file_to_dict(file_name: str) -> dict:
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def get_flex(flex_title: str) -> dict:
    return file_to_dict("./resources/flex.json")[flex_title]


def get_rich(rich_title: str) -> dict:
    return file_to_dict("./resources/rich.json")[rich_title]


def get_quick(quick_title: str) -> List[Any]:
    return file_to_dict("./resources/quick.json")[quick_title]


def receive_message(bot: LINE, event: Event.MESSAGE) -> None:
    message = event.message
    message_id = message.id
    message_type = message.type

    source_type = event.source.type
    user_id = event.source.user_id

    if message_type == ContentType.STICKER:
        bot.reply_message([TextMessage("a")])

    elif message_type == ContentType.IMAGE:
        bot.save_content_from_message_id(message_id, f"{message_id}.jpg")
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
            message = ImageMessage(preview_url=url, content_url=url)
            bot.reply_message([message])

        elif message_text == "ふくすうがぞう":
            bot.reply_image_message(
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
                "https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )

        elif message_text == "どうが":
            video_message = VideoMessage(
                content_url="https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                preview_url="https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )
            bot.reply_message([video_message])

        elif message_text == "ふくすうどうが":
            video_message = VideoMessage(
                content_url="https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                preview_url="https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )
            bot.reply_message([video_message, video_message, video_message])

        elif message_text == "おんせい":
            audio_message = AudioMessage(
                content_url="https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                duration=1000,
            )
            bot.reply_message([audio_message])

        elif message_text == "ふくすうおんせい":
            audio_message = AudioMessage(
                content_url="https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                duration=1000,
            )
            bot.reply_message([audio_message, audio_message])

        elif message_text == "いち":
            location_message = LocationMessage(
                title="たいとる",
                address="あどれす",
                latitude=0,
                longitude=0,
            )
            bot.reply_message([location_message])

        elif message_text == "ふくすういち":
            location_message = LocationMessage(
                title="たいとる",
                address="あどれす",
                latitude=0,
                longitude=0,
            )
            bot.reply_message(
                [location_message, location_message, location_message, location_message]
            )

        elif message_text == "すたんぷ":
            sticker_message = StickerMessage(package_id=1, sticker_id=1)
            bot.reply_message([sticker_message])

        elif message_text == "ふくすうすたんぷ":
            sticker_message = StickerMessage(package_id=1, sticker_id=1)
            bot.reply_message([sticker_message, sticker_message])

        elif message_text == "ふれっくす":
            flex_message = FlexMessage(
                alt_text="Flex Message", content=get_flex("test")
            )
            bot.reply_message([flex_message])

        elif message_text == "ふくすうふれっくす":
            flex_message = FlexMessage(
                alt_text="Flex Message", content=get_flex("test")
            )
            bot.reply_message([flex_message, flex_message, flex_message])

        elif message_text == "いろんな":
            video_message = VideoMessage(
                content_url="https://file3-d.kuku.lu/files/20200514-0225_b5468a4effd6228a4c454c6b0d477f08.mp4",
                preview_url="https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )
            audio_message = AudioMessage(
                content_url="https://www.ne.jp/asahi/music/myuu/wave/springsonate.mp3",
                duration=1000,
            )
            image_message = ImageMessage(
                preview_url="https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
                content_url="https://linebot.m3e.xyz/public_self_bot/img/dev_img_nanato12.png",
            )
            text_message = TextMessage("test")
            # メッセージを詰める
            messages: List[SEND_MESSAGE] = []
            messages.append(video_message)
            messages.append(audio_message)
            messages.append(image_message)
            messages.append(text_message)
            bot.reply_message(messages)

        elif message_text == "いべんと":
            bot.reply_text_message(str(event))

        elif message_text == "くいっく":
            bot.set_quick_reply(get_quick("test"))
            bot.reply_text_message("くいっくりぷらいだよ")
