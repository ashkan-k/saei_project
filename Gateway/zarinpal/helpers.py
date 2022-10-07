from django.conf import settings
from zeep import Client

MERCHANT = settings.MERCHANT_CODE
client = Client('https://sandbox.zarinpal.com/pg/services/WebGate/wsdl')
# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 0  # Toman / Required
description = "پرداخت آموزشگاه ساعی"  # Required
email = settings.EMAIL_ADDRESS  # Optional
mobile = settings.MOBILE_NUMBER  # Optional
CallbackURL = settings.URL + '/zarinpal/callback/'  # Important: need to edit for realy server.
