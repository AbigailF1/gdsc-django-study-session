from django.db import models
from django.utils import timezone

class Comment(models.Model):
    content = models.TextField()
    created_time= models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(auto_now=True)


