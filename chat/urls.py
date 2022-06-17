from django.urls import re_path

from chat.views import index, room

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'(?P<room_name>\w+)/$', room, name='room'),
]