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

"""pylinebot.structs module."""

from typing import Optional, Any, Dict
from dataclasses import dataclass

from linebot.models import (
    TextSendMessage,
    ImageSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    LocationSendMessage,
    StickerSendMessage,
    FlexSendMessage,
    QuickReply,
    Sender,
    RichMenu,
)


@dataclass
class TextMessage:

    text: str

    def __init__(self, text: str) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.text = text

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> TextSendMessage:
        return TextSendMessage(text=self.text, quick_reply=quick_reply, sender=sender)


@dataclass
class StickerMessage:

    package_id: str
    sticker_id: str

    def __init__(self, package_id: str, sticker_id: str) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.package_id = package_id
        self.sticker_id = sticker_id

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> StickerSendMessage:
        return StickerSendMessage(
            package_id=self.package_id,
            sticker_id=self.sticker_id,
            quick_reply=quick_reply,
            sender=sender,
        )


@dataclass
class ImageMessage:

    content_url: str
    preview_url: str

    def __init__(self, content_url: str, preview_url: str) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.content_url = content_url
        self.preview_url = preview_url

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> ImageSendMessage:
        return ImageSendMessage(
            original_content_url=self.content_url,
            preview_image_url=self.preview_url,
            quick_reply=quick_reply,
            sender=sender,
        )


@dataclass
class VideoMessage:

    content_url: str
    preview_url: str

    def __init__(self, content_url: str, preview_url: str) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.content_url = content_url
        self.preview_url = preview_url

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> VideoSendMessage:
        return VideoSendMessage(
            original_content_url=self.content_url,
            preview_image_url=self.preview_url,
            quick_reply=quick_reply,
            sender=sender,
        )


@dataclass
class AudioMessage:

    content_url: str
    duration: int

    def __init__(self, content_url: str, duration: int) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.content_url = content_url
        self.duration = duration

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> AudioSendMessage:
        return AudioSendMessage(
            original_content_url=self.content_url,
            duration=self.duration,
            quick_reply=quick_reply,
            sender=sender,
        )


@dataclass
class LocationMessage:

    title: str
    address: str
    latitude: float
    longitude: float

    def __init__(
        self, title: str, address: str, latitude: float, longitude: float
    ) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> LocationSendMessage:
        return LocationSendMessage(
            title=self.title,
            address=self.address,
            latitude=self.latitude,
            longitude=self.longitude,
            quick_reply=quick_reply,
            sender=sender,
        )


@dataclass
class FlexMessage:

    alt_text: str
    content: dict

    def __init__(self, alt_text: str, content: Dict[str, Any]) -> None:
        """
        インテリセンスで表示されないため。
        """
        self.alt_text = alt_text
        self.content = content

    def create(
        self, quick_reply: Optional[QuickReply] = None, sender: Optional[Sender] = None
    ) -> FlexSendMessage:
        return FlexSendMessage(
            alt_text=self.alt_text,
            contents=self.content,
            quick_reply=quick_reply,
            sender=sender,
        )


class RichMenu(RichMenu):
    pass
