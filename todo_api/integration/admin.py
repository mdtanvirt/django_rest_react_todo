from django.contrib import admin
from .models import MailIntegration, BulkMessaging

# Register your models here.
admin.site.register(MailIntegration)
admin.site.register(BulkMessaging)