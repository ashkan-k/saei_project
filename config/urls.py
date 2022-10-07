"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django_admin/', admin.site.urls),

    path('', include('Admin.urls')),
    path('', include('User.urls')),
    path('', include('ACL.urls')),
    path('', include('Auth.urls')),
    path('', include('Student.urls')),
    path('', include('Teacher.urls')),
    path('', include('Course.urls')),
    path('', include('Class.urls')),
    path('', include('Setting.urls')),
    path('', include('Slider.urls')),
    path('', include('Chat.urls')),
    path('', include('ReportCard.urls')),
    path('', include('Blog.urls')),
    path('', include('Shop.urls')),
    path('', include('Ticket.urls')),
    path('', include('ContactUs.urls')),
    path('', include('QuizBuilder.urls')),
    path('', include('Gateway.urls')),
    path('', include('Installment.urls')),
    path('', include('Sms.urls')),
    path('', include('Help.urls')),


    path('', include('Index.urls')),
]

urlpatterns += [
    path('api/auth/', include('Auth.api.urls')),
    path('api/student/', include('Student.api.urls')),
    path('api/teacher/', include('Teacher.api.urls')),
    path('api/course/', include('Course.api.urls')),
    path('api/class/', include('Class.api.urls')),
    path('api/blog/', include('Blog.api.urls')),
    path('api/chat/', include('Chat.api.urls')),
    path('api/quiz/', include('QuizBuilder.api.urls')),
    path('api/installment/', include('Installment.api.urls')),
    path('api/sms/', include('Sms.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
