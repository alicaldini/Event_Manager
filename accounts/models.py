from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('attendee', 'Attendee'),
        ('organizer', 'Organizer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username