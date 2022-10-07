import requests
from django.conf import settings
from config.celery import app


@app.task()
def send_sms(receiver, msg):
    # response = requests.get(
    #     f'{settings.SMS_WEBSERVICE_URL}&From={settings.SMS_SENDER_NUMBER}&Text={msg}&To={receiver}'
    # )
    # response = response.json()
    #
    # if response.get('ResultStatusCode') != 1 and not response.get('Data'):
    #     return False
    print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    print(receiver)
    print(msg)
    return True
