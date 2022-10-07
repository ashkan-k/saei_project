from django.views.generic import TemplateView

from Blog.models import Blog
from Class.models import Class
from Help.models import Help
from Slider.models import Slider
from Student.models import Student
from Teacher.models import Teacher


class Index(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = {
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'sliders': Slider.objects.all(),
            'helps': Help.objects.all(),
            'classes': Class.objects.all(),
            'last_class': Class.objects.filter(status='active').last(),
            'upcomming_classes': Class.objects.filter(status='pending')[:10],
            'new_blogs': Blog.objects.order_by('-created_at')[:4],
        }
        return context


# ==================== About Us ====================

class AboutUs(TemplateView):
    template_name = "about/about_us.html"

    def get_context_data(self, **kwargs):
        context = {
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'teachers': Teacher.objects.all(),
            'sliders': Slider.objects.all(),
            'helps': Help.objects.all(),
            'classes': Class.objects.all(),
            'last_class': Class.objects.filter(status='active').last(),
            'upcomming_classes': Class.objects.filter(status='pending')[:10],
        }
        return context
