import requests
from django.conf import settings
from config.celery import app


@app.task()
def send_sms(receiver, msg):
    # response = requests.get(
    #     f'{settings.SMS_WEB_SERVICE_URL}username={settings.SMS_USERNAME}&password={settings.SMS_PASSWORD}&from={settings.SMS_FROM_NUMBER}&to={receiver}&text={msg}'
    # )
    # response = response.json()
    #
    # if response == 0:
    #     return False
    return True
