import traceback

from linebot.exceptions import InvalidSignatureError

class Tracer:

    exec_event_list = {}

    def __init__(self, client, debug=False):
        self.client = client
        self.debug = debug

    def trace(self, app, request):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)

        try:
            events = self.client.parser.parse(body, signature)
        except InvalidSignatureError:
            traceback.print_exc()

        for event in events:
            if self.debug:
                app.logger.debug(event)
            self.__execute(event)

    def __execute(self, event):
        if event.type in self.exec_event_list:
            try:
                self.exec_event_list[event.type](self.client, event)
            except:
                traceback.print_exc()

    def add_event(self, event_type, func):
        self.exec_event_list[event_type] = func

