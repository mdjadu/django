from django.db import models

# Create your models here.
# for better understanding use uppercase(1st) for class and lower case for functions
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True) #blank means the field cant be ketp empty and null means the filed can have null value
    price       = models.DecimalField(decimal_places=2,max_digits=100)
    summary     = models.TextField()
    features    = models.BooleanField(default=False)