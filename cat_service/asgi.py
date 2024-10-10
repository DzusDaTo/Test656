import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cat_service.settings')


def get_application():
    from cat_service.routing import websocket_urlpatterns  # Перемещаем импорт сюда
    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns  # Для WebSocket-соединений
            )
        ),
    })
    return application


application = get_application()

