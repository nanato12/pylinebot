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

class Message:

    """
        Message Object
    """
    def create_text_message(self, text, quick_reply=None, sender=None):
        return TextSendMessage(
            text=text,
            quick_reply=quick_reply
        )

    def create_image_message(self, image_url, quick_reply=None, sender=None):
        return ImageSendMessage(
            original_content_url=image_url,
            preview_image_url=image_url,
            quick_reply=quick_reply
        )

    def create_video_message(self, content_url, preview_url, quick_reply=None, sender=None):
        return VideoSendMessage(
            original_content_url=content_url,
            preview_image_url=preview_url,
            quick_reply=quick_reply
        )

    def create_audio_message(self, content_url, duration, quick_reply=None, sender=None):
        return AudioSendMessage(
            original_content_url=content_url,
            duration=duration,
            quick_reply=quick_reply
        )

    def create_location_message(self, title, address, latitude, longitude, quick_reply=None, sender=None):
        return LocationSendMessage(
            title=title,
            address=address,
            latitude=latitude,
            longitude=longitude,
            quick_reply=quick_reply
        )

    def create_sticker_message(self, package_id, sticker_id, quick_reply=None, sender=None):
        return StickerSendMessage(
            package_id=package_id,
            sticker_id=sticker_id,
            quick_reply=quick_reply
        )

    def create_flex_message(self, content, alt_text, quick_reply=None, sender=None):
        return FlexSendMessage(
            alt_text=alt_text,
            contents=content,
            quick_reply=quick_reply
        )

    """
        Other
    """
    def create_quick_reply(self, action_list, img_url_list=[]):
        if not img_url_list:
            img_url_list = [None] * len(action_list)
        elif len(action_list) != len(img_url_list):
            raise Exception('[pylinebot: create_quick_reply] action, img_url list length is different.')
        item_list = [
            QuickReplyButton(
                image_url=img_url,
                action=action
            ) for action, img_url in zip(action_list, img_url_list)
        ]
        return QuickReply(items=item_list)

    def create_rich_menu_object(self, content):
        return RichMenu(
            size=content['size'],
            selected=content['selected'],
            name=content['name'],
            chat_bar_text=content['chatBarText'],
            areas=content['areas']
        )
