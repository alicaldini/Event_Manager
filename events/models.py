from django.db import models
from accounts.models import CustomUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    attendee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'attendee')

    def __str__(self):
        return f"{self.attendee.username} - {self.event.title}"