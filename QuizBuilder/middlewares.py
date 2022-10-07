import jdatetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from QuizBuilder.models import Quiz


class CheckQuizzesExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        Quiz.objects.filter(expire_time__lte=jdatetime.datetime.now()).update(status='close')
        return response
