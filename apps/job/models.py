from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    changed_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
