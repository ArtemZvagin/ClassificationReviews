FROM python:3.9-slim

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD gunicorn my_project.wsgi:application -b 0.0.0.0:8000