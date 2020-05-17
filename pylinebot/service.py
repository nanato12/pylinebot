from .message import Message
from .function import Func

class Service(Message, Func):

    def __init__(self):
        Func.__init__(self)

    """
        Send Message
    """
    def reply_message(self, reply_token, message_list):
        self.client.reply_message(
            reply_token=reply_token,
            messages=message_list
        )

    def push_message(self, to, message_list):
        self.client.push_message(
            to=to,
            messages=message_list
        )

    def broadcast(self, message_list):
        self.client.broadcast(message_list)

    def narrowcast(self, message_list):
        self.client.narrowcast(message_list)

    def multicast(self, to, message_list):
        self.client.multicast(to, message_list)

    def send_message(self, reply_token_or_to=None, message_list=[], send_type='reply'):
        if not message_list:
            raise Exception('[pylinebot: send_message] message count 0 is invalid.')
        elif len(message_list) > 5:
            raise Exception('[pylinebot: send_message] message count over 5 is invalid.')
        elif send_type == 'reply':
            self.reply_message(reply_token_or_to, message_list)
        elif send_type == 'push':
            self.push_message(reply_token_or_to, message_list)
        elif send_type == 'broadcast':
            self.broadcast(message_list)
        elif send_type == 'narrowcast':
            self.narrowcast(message_list)
        elif send_type == 'multicast':
            self.multicast(reply_token_or_to, message_list)

    def send_text_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [self.create_text_message(text, quick_reply) for text in args]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_image_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [self.create_image_message(url, quick_reply) for url in args]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_video_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [
            self.create_video_message(
                video_data['content_url'],
                video_data['preview_url'],
                quick_reply
            ) for video_data in args
        ]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_audio_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [
            self.create_audio_message(
                audio_data['content_url'],
                audio_data['duration'],
                quick_reply
            ) for audio_data in args
        ]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_location_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [
            self.create_location_message(
                location_data['title'],
                location_data['address'],
                location_data['latitude'],
                location_data['longitude'],
                quick_reply
            ) for location_data in args
        ]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_sticker_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [
            self.create_sticker_message(
                sticker_data['package_id'],
                sticker_data['sticker_id'],
                quick_reply
            ) for sticker_data in args
        ]
        self.send_message(reply_token_or_to, message_list, send_type)

    def send_flex_message(self, reply_token_or_to, *args, quick_reply=None, sender=None, send_type='reply'):
        message_list = [
            self.create_flex_message(
                content['flex'],
                content['alt_text'],
                quick_reply=quick_reply
            ) for content in args
        ]
        self.send_message(reply_token_or_to, message_list, send_type)

    """
        Get message or status
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
        Get function
    """
    def get_profile(self, user_id):
        return self.client.get_profile(user_id)

    def get_profile_from_group(self, group_id, user_id):
        return self.client.get_group_member_profile(group_id, user_id)

    def get_profile_from_room(self, room_id, user_id):
        return self.client.get_room_member_profile(room_id, user_id)

    def get_group_member_ids(self, group_id, start=None):
        # Verified account only
        return self.client.get_group_member_ids(group_id, start=start)

    def get_room_member_ids(self, room_id, start=None):
        # Verified account only
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
        Rich menu
    """
    def get_rich_menu(self, rich_menu_id):
        return self.client.get_rich_menu(rich_menu_id)

    def get_rich_menu_id_from_user(self, user_id):
        return self.client.get_rich_menu_id_of_user(user_id)

    def create_rich_menu(self, rich_menu, file_name, file_format='jpeg'):
        if file_format not in ['jpeg', 'png']:
            raise Exception('[pylinebot: create_rich_menu] image file format is jpeg or png.')
        rich_menu_id = self.client.create_rich_menu(rich_menu)
        content = self.img_file_to_bytes(file_name, format=file_format, rich=True)
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
        return self.client.link_rich_menu_to_users(user_id_list, rich_menu_id)

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
