from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    
    class RoleChoises(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        CREATOR = 'creator', _('Creator')
        DONOR = 'donor', _('Donor')

    role = models.CharField(
        max_length=10,
        choices=RoleChoises.choices,
        default=RoleChoises.DONOR
    )