FROM python:3

COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code
RUN python3 manage.py collectstatic --no-input