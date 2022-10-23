import requests
from django.conf import settings
from config.celery import app


@app.task()
def send_sms(receiver, msg):
    response = requests.get(
        f'{settings.SMS_WEB_SERVICE_URL}username={settings.SMS_USERNAME}&password={settings.SMS_PASSWORD}&from={settings.SMS_FROM_NUMBER}&to={receiver}&text=سلاام'
    )
    response = response.json()

    from django.core.mail import send_mail
    subject = 'Thank you for registering to our site'
    message = response
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['karimiashkan8181@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

    if response == 0:
        return False
    return True
