from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    STATUS_CHOICES =[
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected")
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "applications")
    company = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = "applied")
    date_applied = models.DateField()
    notes = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["-date_applied"]

    def __str__(self):
        return f"{self.role} at {self.company}"