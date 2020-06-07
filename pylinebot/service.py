# standard
import os

# local
from .message import Message
from .function import Func
from .exception import (
    MessageLimitError,
    DifferentTypeError
)

def check(func):
    def message_count(*args):
        messages = args[1]
        if len(messages) > 5:
            raise MessageLimitError(
                'You can send up to 5 messages at once.'
            )
    return message_count

class Service(Message, Func):

    """
        Bot Service
    """

    def set_reply_token(self, reply_token):
        self.reply_token = reply_token

    def save_content_from_message_id(self, message_id, file_name=None):
        """
            save content (image, video, auido) from message_id
        """
        message_content = self.get_message_content(message_id)
        if file_name is None:
            type_list = message_content.content_type.split('/')
            file_type = type_list[0]
            file_extension = type_list[1]
            os.makedirs(f'content/{file_type}')
            file_name = f'content/{file_type}/{message_id}.{file_extension}'
        content = self.get_message_content(message_id).content
        with open(file_name, 'wb') as content_file:
            content_file.write(content)

    def save_image_from_rich_id(self, rich_id, file_name=None):
        """
            save rich image from rich_id
        """
        rich_content = self.get_rich_menu_image(rich_id)
        if file_name is None:
            type_list = rich_content.content_type.split('/')
            file_type = type_list[0]
            file_extension = type_list[1]
            os.makedirs(f'rich_menu/{file_type}')
            file_name = f'rich_menu/{file_type}/{rich_id}.{file_extension}'
        content = self.get_rich_menu_image(rich_id).content
        with open(file_name, 'wb') as content_file:
            content_file.write(content)

    """
        Send Message
    """
    @check
    def reply_message(self, messages):
        self.client.reply_message(
            reply_token=self.reply_token,
            messages=messages
        )

    def reply_text_message(self, *args):
        messages = [
            self.create_text_message(text) for text in args
        ]
        self.reply_message(messages)

    def reply_image_message(self, *args):
        messages = [
            self.create_image_message(img_url) for img_url in args
        ]
        self.reply_message(messages)

    def reply_video_message(self, *args):
        messages = [
            self.create_video_message(video_data) for video_data in args
        ]
        self.reply_message(messages)

    def reply_audio_message(self, *args):
        messages = [
            self.create_audio_message(audio_data) for audio_data in args
        ]
        self.reply_message(messages)

    def reply_location_message(self, *args):
        messages = [
            self.create_location_message(lct_data) for lct_data in args
        ]
        self.reply_message(messages)

    def reply_sticker_message(self, *args):
        messages = [
            self.create_sticker_message(stk_data) for stk_data in args
        ]
        self.reply_message(messages)

    def reply_flex_message(self, *args):
        messages = [
            self.create_flex_message(flex_data) for flex_data in args
        ]
        self.reply_message(messages)

    @check
    def push_message(self, to, messages):
        self.client.push_message(to, messages)

    @check
    def broadcast(self, messages):
        self.client.broadcast(messages)

    @check
    def narrowcast(self, messages):
        self.client.narrowcast(messages)

    @check
    def multicast(self, to, messages):
        self.client.multicast(to, messages)

    """
        Get function
    """
    def get_profile(self, user_id):
        return self.client.get_profile(user_id)

    def get_profile_from_group(self, group_id, user_id):
        return self.client.get_group_member_profile(group_id, user_id)

    def get_profile_from_room(self, room_id, user_id):
        return self.client.get_room_member_profile(room_id, user_id)

    def get_group_member_ids(self, group_id, start=None):
        """
            Verified account only
        """
        return self.client.get_group_member_ids(group_id, start=start)

    def get_room_member_ids(self, room_id, start=None):
        """
            Verified account only
        """
        return self.client.get_room_member_ids(room_id, start=start)

    def get_message_content(self, message_id):
        return self.client.get_message_content(message_id)

    """
        Action function
    """
    def leave_group(self, group_id):
        return self.client.leave_group(group_id)

    def leave_room(self, room_id):
        return self.client.leave_room(room_id)

    """
        Get message status
    """
    def get_progress_status_narrowcast(self, request_id):
        return self.client.get_progress_status_narrowcast(request_id)

    def get_message_delivery_broadcast(self, date):
        return self.client.get_message_delivery_broadcast(date)

    def get_message_delivery_reply(self, date):
        return self.client.get_message_delivery_reply(date)

    def get_message_delivery_push(self, date):
        return self.client.get_message_delivery_push(date)

    def get_message_delivery_multicast(self, date):
        return self.client.get_message_delivery_multicast(date)

    """
        Rich menu
    """
    def get_rich_menu(self, rich_menu_id):
        return self.client.get_rich_menu(rich_menu_id)

    def get_rich_menu_id_from_user(self, user_id):
        return self.client.get_rich_menu_id_of_user(user_id)

    def create_rich_menu(self, rich_menu, file_name, file_format='jpeg'):
        if file_format not in ['jpeg', 'png']:
            raise DifferentTypeError(
                'image file format is jpeg or png.'
            )
        rich_menu_id = self.client.create_rich_menu(rich_menu)
        content = self.img_file_to_bytes(
            file_name, format=file_format, rich=True
        )
        self.client.set_rich_menu_image(
            rich_menu_id,
            f'image/{file_format}',
            content
        )
        return rich_menu_id

    def delete_rich_menu(self, rich_menu_id):
        return self.client.delete_rich_menu(rich_menu_id)

    def link_rich_menu_to_user(self, user_id, rich_menu_id):
        return self.client.link_rich_menu_to_user(user_id, rich_menu_id)

    def link_rich_menu_to_multi_user(self, user_id_list, rich_menu_id):
        return self.client.link_rich_menu_to_users(
            user_id_list, rich_menu_id
        )

    def unlink_rich_menu_from_user(self, user_id):
        return self.client.unlink_rich_menu_from_user(user_id)

    def unlink_rich_menu_from_multi_user(self, user_id_list):
        return self.client.unlink_rich_menu_from_users(user_id_list)

    def get_rich_menu_image(self, rich_menu_id):
        return self.client.get_rich_menu_image(rich_menu_id)

    def get_rich_menu_list(self):
        return self.client.get_rich_menu_list()

    def set_default_rich_menu(self, rich_menu_id):
        return self.client.set_default_rich_menu(rich_menu_id)

    def get_default_rich_menu(self):
        return self.client.get_default_rich_menu()

    def cancel_default_rich_menu(self):
        return self.client.cancel_default_rich_menu()

    """
        Other
    """
    def get_message_quota(self):
        return self.client.get_message_quota()

    def get_message_quota_consumption(self):
        return self.client.get_message_quota_consumption()

    def issue_link_token(self, user_id):
        return self.client.issue_link_token(user_id)

    def issue_channel_token(self, client_id, client_secret):
        return self.client.issue_channel_token(client_id, client_secret)

    def revoke_channel_token(self, access_token):
        return self.client.revoke_channel_token(access_token)

    def get_insight_message_delivery(self, date):
        return self.client.get_insight_message_delivery(date)

    def get_insight_followers(self, date):
        return self.client.get_insight_followers(date)

    def get_insight_demographic(self):
        return self.client.get_insight_demographic()

    def get_insight_message_event(self, request_id):
        return self.client.get_insight_message_event(request_id)
