FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apt update -y && apt install gcc -y
RUN pip install -r requirements.txt
COPY . /app/
RUN python3 /app/manage.py collectstatic --noinput
