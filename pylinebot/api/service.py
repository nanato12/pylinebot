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

"""pylinebot.api.service module."""

from typing import Any, List, Optional

from linebot import LineBotApi
from linebot.models import QuickReply, QuickReplyButton, Sender
from linebot.models.responses import BroadcastResponse, Content, NarrowcastResponse

from ..structs.message import ImageMessage, TextMessage
from ..types.exception import SetQuickReplyError
from ..utils.annotation import SEND_MESSAGE
from ..utils.decorator import check


class Service(LineBotApi):
    """
    LineBotApi wrapper class
    """

    reply_token: Optional[str] = None
    sender: Optional[Sender] = None
    quick_reply: Optional[QuickReply] = None

    def __init__(self, channel_access_token: str) -> None:
        """
        LineBotApiの継承
        """
        LineBotApi.__init__(self, channel_access_token)

    def refresh(self) -> None:
        """
        各種リセット
        """
        self.reply_token = None
        self.sender = None
        self.quick_reply = None

    def set_reply_token(self, reply_token: str) -> None:
        """
        一々、reply_tokenをセットしなくていいようにするため。(Tracerのみ)
        """
        self.reply_token = reply_token

    def set_sender(
        self, name: Optional[str] = None, icon_url: Optional[str] = None
    ) -> None:
        """
        送信時、アイコンと名前を変更することができる。
        """
        self.sender = Sender(name=name, icon_url=icon_url)

    def set_quick_reply(self, action_list: list, img_url_list: list = []) -> None:
        """
        QuickReplyがつく。
        """
        if not img_url_list:
            img_url_list = [None] * len(action_list)
        elif len(action_list) != len(img_url_list):
            raise SetQuickReplyError("action and img_url list length is different.")
        item_list: List[QuickReplyButton] = [
            QuickReplyButton(image_url=img_url, action=action)
            for action, img_url in zip(action_list, img_url_list)
        ]
        self.quick_reply = QuickReply(items=item_list)

    @check
    def reply_message(self, messages: List[SEND_MESSAGE]) -> None:
        """
        LineBotApi reply_messageのオーバーライド
        """
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        super().reply_message(reply_token=self.reply_token, messages=messages)

    @check
    def push_message(self, to: str, messages: List[SEND_MESSAGE]) -> None:
        """
        LineBotApi push_messageのオーバーライド
        """
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        super().push_message(to, messages=messages)

    @check
    def broadcast(self, messages: List[SEND_MESSAGE]) -> BroadcastResponse:
        """
        LineBotApi broadcastのオーバーライド
        """
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        return super().broadcast(messages)

    @check
    def narrowcast(self, messages: List[SEND_MESSAGE]) -> NarrowcastResponse:
        """
        LineBotApi narrowcastのオーバーライド
        """
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        return super().narrowcast(messages)

    @check
    def multicast(self, to: List[str], messages: List[SEND_MESSAGE]) -> None:
        """
        LineBotApi multicastのオーバーライド
        """
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        super().multicast(to, messages)

    def reply_text_message(self, *args: str) -> None:
        """
        簡易的にテキストメッセージが送れる関数
        例: reply_text_message("a", "i", "u")
        """
        text: str
        messages: List[TextMessage] = [TextMessage(text) for text in args]
        self.reply_message(messages)

    def reply_image_message(self, *args: str) -> None:
        """
        簡易的に画像メッセージが送れる関数
        例: reply_image_message("https://xxxx.png", "https://yyyy.png", "https://zzzz.png")
        """
        image_url: str
        messages: List[ImageMessage] = [
            ImageMessage(content_url=image_url, preview_url=image_url)
            for image_url in args
        ]
        self.reply_message(messages)

    def save_content_from_message_id(self, message_id: str, file_name: str) -> None:
        """
        save content (image, video, auido) from message_id
        """
        message_content: Content = self.get_message_content(message_id)
        with open(file_name, "wb") as content_file:
            content_file.write(message_content.content)
