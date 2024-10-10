FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt /app/


RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

RUN mkdir -p /app/db

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=cat_service.settings


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]