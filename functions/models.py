from django.db import models


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    role = models.TextField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
