import requests
from django.conf import settings
from config.celery import app


@app.task()
def send_sms(receiver, msg):
    response = requests.get(
        f'{settings.SMS_WEB_SERVICE_URL}username={settings.SMS_USERNAME}&password={settings.SMS_PASSWORD}&from={settings.SMS_FROM_NUMBER}&to={receiver}&text={msg}'
    )

    print('dddddddddddddddddddddddddd')
    print(response.status_code)
    print(response.text)
    print(settings.SMS_USERNAME)
    print(settings.SMS_PASSWORD)

    if response.status_code == 200 and response.text == 'SendWasSuccessful':
        return False
    return True
