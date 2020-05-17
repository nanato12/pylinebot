from linebot import LineBotApi, WebhookParser

from .service import Service

class LINE(Service):

    def __init__(self, channel_access_token, channel_secret):
        self.client = LineBotApi(channel_access_token)
        self.parser = WebhookParser(channel_secret)
        self.initialize()

    def initialize(self):
        Service.__init__(self)
