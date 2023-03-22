from django.db import models

# Create your models here.
class MailIntegration(models.Model):
    email = models.EmailField(max_length=30)
    profileName = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class BulkMessaging(models.Model):
    email = models.EmailField(max_length=30)
    profileName = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    selected = models.BooleanField(default=True)

    def __str__(self):
        return self.email

