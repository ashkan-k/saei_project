FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apk add -u gcc musl-dev
RUN pip install -r requirements.txt
COPY . /app/
RUN python3 /app/manage.py collectstatic --noinput
