from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)