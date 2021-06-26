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

"""pylinebot.client module."""

from linebot import WebhookHandler, WebhookParser

from .api.service import Service


class LINE(Service):

    parser: WebhookParser
    handler: WebhookHandler

    def __init__(self, channel_access_token: str, channel_secret: str) -> None:
        Service.__init__(self, channel_access_token)
        self.parser = WebhookParser(channel_secret)
        self.handler = WebhookHandler(channel_secret)
