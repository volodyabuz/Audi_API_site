FROM python:3.8-slim

RUN mkdir app
WORKDIR app

ADD . /app/

ENV APP_NAME=DOCKER_DEMO
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]