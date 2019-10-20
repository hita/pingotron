from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Target(models.Model):
    path = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_ping = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    date_last_online = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('ON', 'online'),
        ('OFF', 'offline'),
    )
    status_choices = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )