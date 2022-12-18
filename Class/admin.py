from django.contrib import admin
from .models import *

admin.site.register(Class)
admin.site.register(ClassAttendance)

class ClassUserAdmin(admin.ModelAdmin):
    list_filter = [
         "user",
         "class_item",
         "status"
    ]

class ClassUserAttendanceAdmin(admin.ModelAdmin):
    list_filter = [
         "user",
         "class_attendance",
         "status"
    ]

admin.site.register(ClassUser, ClassUserAdmin)
admin.site.register(ClassUserAttendance, ClassUserAttendanceAdmin)
