FROM python:3.8-slim

WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic -c --skip-checks --no-input

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

CMD gunicorn config.wsgi:application --bind :8000