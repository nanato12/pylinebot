#  Copyright 2020 nanato12

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""pylinebot.types.message module."""

from linebot.models import (
    AudioMessage,
    FileMessage,
    ImageMessage,
    LocationMessage,
    StickerMessage,
    TextMessage,
    VideoMessage,
)


class MESSAGE:
    TEXT = TextMessage
    STICKER = StickerMessage
    IMAGE = ImageMessage
    VIDEO = VideoMessage
    AUDIO = AudioMessage
    FILE = FileMessage
    LOCATION = LocationMessage


class ToType:
    USER = "user"
    GROUP = "group"
    ROOM = "room"


class ContentType:
    TEXT = "text"
    STICKER = "sticker"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    LOCATION = "location"
