from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView
from django.contrib import messages
from ACL.mixins import VerifiedUserMixin, PermissionMixin
from Admin.forms import DashboardImageForm
from Admin.models import DashboardImage
from Class.models import Class
from Gateway.models import PaymentTransaction
from Student.models import Student
from Teacher.models import Teacher
from django.conf import settings

User = get_user_model()


class DashboardImagesList(PermissionMixin, ListView):
    permissions = ['dashboard_images_delete']
    model = DashboardImage
    context_object_name = 'settings'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'admin_app/admin/images/list.html'


class DashboardImagesCreate(PermissionMixin, CreateView):
    permissions = ['dashboard_images_delete']
    model = DashboardImage
    form_class = DashboardImageForm
    template_name = 'admin_app/admin/images/form.html'
    success_url = reverse_lazy('images-list')


class DashboardImagesUpdate(PermissionMixin, UpdateView):
    permissions = ['dashboard_images_delete']
    model = DashboardImage
    form_class = DashboardImageForm
    template_name = 'admin_app/admin/images/form.html'
    success_url = reverse_lazy('images-list')


class DashboardImagesDelete(PermissionMixin, DeleteView):
    permissions = ['dashboard_images_delete']
    model = DashboardImage
    template_name = 'admin_app/admin/images/form.html'
    success_url = reverse_lazy('images-list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


###############################################

class Dashboard(VerifiedUserMixin, TemplateView):
    template_name = "admin_app/admin/admin-dashboard.html"

    def get_context_data(self, **kwargs):
        context = {
            'total_transaction_amount':
                PaymentTransaction.objects.filter(status='success').aggregate(total_amount=Sum('amount'))[
                    'total_amount'],
            'users_count': User.objects.count(),
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'classes_count': Class.objects.count(),
            'dashboard_image': DashboardImage.objects.last(),
        }

        return context
