from django.urls import re_path
from ..cats import consumers

websocket_urlpatterns = [
    re_path(r'ws/messages/$', consumers.MessageConsumer.as_asgi()),
]
