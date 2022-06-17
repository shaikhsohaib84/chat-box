from django.urls import re_path
# from . import consumers
from chat.consumers import ChatRoomConsumer
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi())
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]