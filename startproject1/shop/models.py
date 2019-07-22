from django.db import models
<<<<<<< HEAD
from django.conf import settings
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======

# Create your models here.
>>>>>>> fe8d6ea25fc383f1a07a7c976b9cfc98ea13a39a
