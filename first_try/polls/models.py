from django.db import models

# Create your models here.
class Polls(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summery     = models.TextField(default='this is nice')