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

"""pylinebot.types.event module."""

from linebot.models import (
    AccountLinkEvent,
    BeaconEvent,
    FollowEvent,
    JoinEvent,
    LeaveEvent,
    MemberJoinedEvent,
    MemberLeftEvent,
    MessageEvent,
    PostbackEvent,
    ThingsEvent,
    UnfollowEvent,
)


class Event:
    ACCOUNT_LINK = AccountLinkEvent
    BEACON = BeaconEvent
    FOLLOW = FollowEvent
    UNFOLLOW = UnfollowEvent
    JOIN = JoinEvent
    LEAVE = LeaveEvent
    MEMBER_JOIN = MemberJoinedEvent
    MEMBER_LEFT = MemberLeftEvent
    POSTBACK = PostbackEvent
    THINGS = ThingsEvent
    MESSAGE = MessageEvent


class TRACER_EVENT:
    ACCOUNT_LINK = "accountLink"
    BEACON = "beacon"
    FOLLOW = "follow"
    UNFOLLOW = "unfollow"
    JOIN = "join"
    LEAVE = "leave"
    MEMBER_JOIN = "memberJoined"
    MEMBER_LEFT = "memberLeft"
    POSTBACK = "postback"
    THINGS = "things"
    MESSAGE = "message"
