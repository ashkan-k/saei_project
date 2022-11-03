from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.views.generic import TemplateView

from ACL.mixins import VerifiedUserMixin
from Class.models import Class
from Gateway.models import PaymentTransaction
from Student.models import Student
from Teacher.models import Teacher

User = get_user_model()


class Dashboard(VerifiedUserMixin, TemplateView):
    template_name = "admin_app/admin/admin-dashboard.html"

    def get_context_data(self, **kwargs):
        context = {
            'total_transaction_amount': PaymentTransaction.objects.filter(status='success').aggregate(total_amount=Sum('amount'))['total_amount'],
            'users_count': User.objects.count(),
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'classes_count': Class.objects.count(),
        }

        return context
