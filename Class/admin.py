from django.contrib import admin
from .models import *

admin.site.register(Class)
admin.site.register(ClassUser)
admin.site.register(ClassAttendance)
admin.site.register(ClassUserAttendance)
