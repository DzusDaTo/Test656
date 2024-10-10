import pytest
from channels.testing import WebsocketCommunicator
from cat_service.asgi import application


@pytest.mark.asyncio
async def test_send_message():
    communicator = WebsocketCommunicator(application, "/ws/messages/")
    connected, _ = await communicator.connect()
    assert connected, "WebSocket connection was not established."

    # Отправляем сообщение через WebSocket
    message = {'type': 'chat_message', 'text': 'Hello, World!'}
    await communicator.send_json_to(message)

    # Получаем ответное сообщение
    response = await communicator.receive_json_from()

    # Проверяем корректность сообщения
    assert response['message'] == 'Hello, World!'
