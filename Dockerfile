FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt
COPY . /app/
RUN python3 /app/manage.py collectstatic --noinput
