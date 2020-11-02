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

"""pylinebot.service module."""

from typing import Any, Callable, Optional, Tuple

from linebot import LineBotApi
from linebot.models import Sender, QuickReply, QuickReplyButton

from .structs import TextMessage
from .exception import MessageLimitError, SetQuickReplyError


class Service(LineBotApi):

    reply_token: str
    sender: Sender = None
    quick_reply: QuickReply = None

    def __init__(self, channel_access_token: str) -> None:
        LineBotApi.__init__(self, channel_access_token)

    def check(func: Callable) -> Callable:
        def message_count(self, *args: Tuple[Any]) -> None:
            if len(args) > 5:
                raise MessageLimitError("You can send up to 5 messages at once.")
            else:
                func(self, *args)

        return message_count

    def refresh(self) -> None:
        self.reply_token = None
        self.sender = None
        self.quick_reply = None

    def set_reply_token(self, reply_token: str) -> None:
        """
        一々、reply_tokenをセットしなくていいようにするため。
        """
        self.reply_token = reply_token

    def set_sender(self, name: Optional[str], icon_url: Optional[str]) -> None:
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
        item_list = [
            QuickReplyButton(image_url=img_url, action=action)
            for action, img_url in zip(action_list, img_url_list)
        ]
        self.quick_reply = QuickReply(items=item_list)

    @check
    def reply_message(self, *messages: Tuple[Any]) -> None:
        message: Any
        messages = [
            message.create(self.quick_reply, self.sender) for message in messages
        ]
        super().reply_message(reply_token=self.reply_token, messages=messages)

    def reply_text_message(self, *args: Tuple[str]) -> None:
        text: str
        messages = [TextMessage(text) for text in args]
        self.reply_message(*messages)
