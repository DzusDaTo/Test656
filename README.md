# Cat Service

Cat Service — это веб-приложение на Django, разработанное для заводчиков кошек. Оно включает регистрацию пользователей, операции CRUD для управления кошками, секцию сообщений с использованием WebSocket и полностью контейнизировано с помощью Docker.

## Особенности

- Регистрация пользователей для заводчиков кошек
- Операции CRUD для управления кошками
- Мгновенные сообщения с использованием WebSocket
- Административная панель для управления пользователями и кошками
- Контейнеризация с помощью Docker для простоты развертывания

## Используемые технологии

- **Django**: веб-фреймворк для разработки приложения
- **Django REST Framework**: фреймворк для создания RESTful API
- **Django Channels**: для обработки WebSocket соединений
- **SQLite**: легковесная база данных для разработки
- **Docker**: контейнеризация для обеспечения согласованности в средах разработки и продакшена

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваше_имя_пользователя/cat_service.git
   cd cat_service
   python -m venv venv
   source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   pytest cats/tests.py
   ```
2. Запустите репозиторий:

   ```bash
   python manage.py migrate
   python manage.py runserver
   pytest cats/tests.py
   ```
