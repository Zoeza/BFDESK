from django.db import models


class Appointment(models.Model):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
