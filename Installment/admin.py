from django.contrib import admin
from .models import *

class UserInstallmentAdmin(admin.ModelAdmin):
    list_filter = [
         "user",
         "class_item",
         "is_complete"
    ]

admin.site.register(UserInstallment, UserInstallmentAdmin)
admin.site.register(UserInstallmentPayments)