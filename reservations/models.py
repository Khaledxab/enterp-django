from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"