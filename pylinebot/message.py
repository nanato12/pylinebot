# local
from linebot.models import (
    TextSendMessage,
    ImageSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    LocationSendMessage,
    StickerSendMessage,
    FlexSendMessage,
    FlexContainer,
    QuickReply,
    QuickReplyButton,
    RichMenu
)
from .exception import SetQuickReplyError

class Message:

    """
        Message Object
    """

    quick_reply = None

    def create_text_message(self, text):
        return TextSendMessage(
            text=text,
            quick_reply=self.quick_reply
        )

    def create_image_message(self, image_url):
        return ImageSendMessage(
            original_content_url=image_url,
            preview_image_url=image_url,
            quick_reply=self.quick_reply
        )

    def create_video_message(self, video_data):
        return VideoSendMessage(
            original_content_url=video_data['content_url'],
            preview_image_url=video_data['preview_url'],
            quick_reply=self.quick_reply
        )

    def create_audio_message(self, audio_data):
        return AudioSendMessage(
            original_content_url=audio_data['content_url'],
            duration=audio_data['duration'],
            quick_reply=self.quick_reply
        )

    def create_location_message(self, location_data):
        return LocationSendMessage(
            title=location_data['title'],
            address=location_data['address'],
            latitude=location_data['latitude'],
            longitude=location_data['longitude'],
            quick_reply=self.quick_reply
        )

    def create_sticker_message(self, sticker_data):
        return StickerSendMessage(
            package_id=sticker_data['package_id'],
            sticker_id=sticker_data['sticker_id'],
            quick_reply=self.quick_reply
        )

    def create_flex_message(self, flex_data):
        return FlexSendMessage(
            alt_text=flex_data['alt_text'],
            contents=flex_data['content'],
            quick_reply=self.quick_reply
        )

    """
        Other
    """
    def set_quick_reply(self, action_list, img_url_list=[]):
        if not img_url_list:
            img_url_list = [None] * len(action_list)
        elif len(action_list) != len(img_url_list):
            raise SetQuickReplyError(
                'action and img_url list length is different.'
            )
        item_list = [
            QuickReplyButton(
                image_url=img_url, action=action
            ) for action, img_url in zip(action_list, img_url_list)
        ]
        self.quick_reply = QuickReply(items=item_list)

    def create_rich_menu_object(self, rich_content):
        return RichMenu(
            size=rich_content['size'],
            selected=rich_content['selected'],
            name=rich_content['name'],
            chat_bar_text=rich_content['chatBarText'],
            areas=rich_content['areas']
        )
