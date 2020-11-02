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

"""pylinebot.tracer module."""

import traceback
from typing import List, Callable

from linebot.models.events import MessageEvent
from linebot.exceptions import InvalidSignatureError

from .client import LINE
from .types import TRACER_EVENT


class Tracer:

    client: LINE
    debug: bool
    exec_events: dict = {}

    def __init__(self, client: LINE, debug: bool = False) -> None:
        self.client = client
        self.debug = debug

    def trace(self, body: str, signature: str) -> None:
        try:
            events: List[MessageEvent] = self.client.parser.parse(body, signature)
        except InvalidSignatureError:
            traceback.print_exc()

        event: MessageEvent
        for event in events:
            if self.debug:
                print(event)
            self.__execute(event)

    def __execute(self, event: MessageEvent) -> None:
        if event.type in self.exec_events:
            self.client.refresh()
            self.client.set_reply_token(event.reply_token)
            self.exec_events[event.type](self.client, event)

    def add_event(self, event_type: TRACER_EVENT, func: Callable) -> None:
        self.exec_events[event_type] = func
